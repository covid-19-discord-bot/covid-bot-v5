# coding=utf-8
# Licenced under the CC BY-NC-SA 4.0 licence: by modifying any code you agree to be bound by the terms of the licence:
# https://creativecommons.org/licenses/by-nc-sa/4.0/

# Accept/Yes: ✅
# Warning: ⚠
# Error/No: ❌

import asyncio
import discord
import datetime
import utils.api as covid19api
import utils.embeds as embeds
from discord.ext import tasks, commands
from typing import Optional, List
from utils.models import get_from_db, DiscordChannel
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.human_time import ShortTime, human_timedelta, FutureTime

utc_zero = datetime.datetime.utcfromtimestamp(-1)


class AutoUpdaterCog(Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.push_auto_updates.start()

    @staticmethod
    def split_seq(seq, size):
        newseq = []
        splitsize = 1.0 / size * len(seq)
        for i in range(size):
            newseq.append(seq[int(round(i * splitsize)):int(round((i + 1) * splitsize))])
        return newseq

    @commands.command(name="autoupdate", aliases=["autoupdate_country", "autoupdateCountry"])
    @commands.has_permissions(manage_messages=True)
    async def autoupdate(self, ctx: MyContext, delay: ShortTime, country: Optional[str] = "OT"):
        """
        /autoupdate <country> <delay> updates stats for <country> (if not set, defaults to world),
        every <delay> time units
        1d updates daily, while 4m updates every 4 minutes
        Only Premium members/guilds can set the delay to less than 10 minutes.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = abs((datetime.datetime.utcnow() - delay.dt).total_seconds())
        human_update_time = human_timedelta(delay.dt, brief=True)

        if delta_seconds > 31536000:
            await ctx.reply(_("❌ Did you really try to set the autoupdater delay to more than a year? Oi. "
                              "Anyways, that isn't allowed. Try again with a more reasonable delay."))

        db_user = await get_from_db(ctx.author)  # Put it here that way it can be checked quickly if needed

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)
        is_premium = db_guild.is_premium or db_user.is_premium
        if db_channel.autoupdater.already_set:
            await ctx.reply(_("❌ You already have a autoupdater set in this channel! Remove it with "
                              "`/disable_updates` and try again!"))
            return
        if delta_seconds > 86400 and not db_guild.overtime_confirmed:
            def pred(c):
                return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and \
                       c.message.content.lower() == "ok"

            await ctx.reply(_("⚠ You're setting a delay longer than 1 day! Are you sure you want to do this? To "
                              "confirm, type `ok` within 15 seconds."))
            try:
                await self.bot.wait_for("message", check=pred, timeout=15)
            except asyncio.TimeoutError:
                await ctx.send(_("Action cancelled. Set up a new autoupdater with `/autoupdate <delay>`."))
                return
            else:
                await ctx.send(_("Continuing setup..."))
                db_guild.overtime_confirmed = True
                await db_guild.save()
        elif delta_seconds < 600:
            if is_premium:
                await ctx.reply(_("You're setting the autoupdater to less than 10 minutes delay. I'll skip the check "
                                  "because you are a premium guild/user. <3 from 0/0#0001"))
            else:
                await ctx.reply(_("❌ You can't set the autoupdater delay to less than 10 minutes unless you are a "
                                  "premium guild.\n"
                                  "Hint: there's no point in setting it to less than 10 minutes due to the fact the "
                                  "stats updater only fires once every 10 minutes. If you really want to get a "
                                  "shorter delay (no point in doing so), check out the `/donate` command."))
                return

        info = await self.bot.worldometers_api.try_to_get_name(country)
        if info is None:
            await ctx.reply(_("❌ Failed to get a ISO2 code for the country! `/list` will show you a list of countries "
                              "and their IDs."))
        elif info[0] == "world":
            iso2_code = "OT"
            friendly_country_name = "World"
        elif info[0] == "country":
            country_list = await self.bot.worldometers_api.get_all_iso_codes()
            iso2_code = covid19api.get_iso2_code(country, country_list)
            friendly_country_name = covid19api.get_country_name(country, country_list)
        elif info[0] == "continent":
            iso2_code = info[1]
            friendly_country_name = info[1]

        update_delay = delta_seconds

        db_channel.autoupdater.already_set = True
        db_channel.autoupdater.country_name = iso2_code
        db_channel.autoupdater.delay = update_delay
        await db_channel.autoupdater.save()
        await db_channel.save()

        await ctx.reply(_("✅ Posting stats for {0} in this "
                          "channel every {1}.".format(friendly_country_name, human_update_time)))

    @commands.command(name="disable_updates", aliases=["disableUpdates"])
    @commands.has_permissions(manage_messages=True)
    async def disable_updates(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        if db_channel.autoupdater.already_set:
            db_channel.autoupdater.already_set = False
            await db_channel.autoupdater.save()
            await db_channel.save()
            await ctx.reply(_("✅ Disabled autoupdates in this channel."))
        else:
            await ctx.reply(_("❌ You don't have a autoupdater set here!"))

    @commands.command(name="force_update")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 150, type=commands.BucketType.channel)
    async def force_updates(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        if not db_channel.autoupdater.already_set:
            await ctx.reply(_("❌ You don't have a autoupdater set here!"))
            return
        db_channel.autoupdater.force_update = True
        await db_channel.autoupdater.save()
        await db_channel.save()
        await ctx.reply(_("✅ Forcing a update sometime in the next minute."))

    @commands.command(name="update_at")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 600, type=commands.BucketType.channel)
    async def update_at(self, ctx: MyContext, at: FutureTime):
        # need to calculate the timedelta and set the last update to be at minus timedelta to keep the code in
        # push_auto_updates the same
        _ = await ctx.get_translate_function()
        time_to_update_at: datetime.datetime = at.dt
        db_channel = await get_from_db(ctx.channel)
        db_channel.autoupdater.do_update_at = time_to_update_at
        await db_channel.autoupdater.save()
        await db_channel.save()
        await ctx.reply(_("✅ Next update: {0}", human_timedelta(time_to_update_at)))

    @tasks.loop(minutes=1.0)
    async def push_auto_updates(self):
        """"""
        self.bot.logger.info("Starting autoupdater...")
        db_channels = await DiscordChannel.filter(autoupdater__already_set=True).prefetch_related("autoupdater")
        channels_to_parse = []
        for db_channel in db_channels:
            channel: discord.TextChannel = self.bot.get_channel(db_channel.discord_id)
            if channel is None:
                continue
            channels_to_parse.append([db_channel, channel])
        self.bot.logger.info(f"Updating in {len(channels_to_parse)} channels.")
        sized_list = self.split_seq(channels_to_parse, 100)  # split into chunks of 100: as of this writing there's
        # only 137 heh
        loop = asyncio.get_event_loop()
        futures = []
        for sublist in sized_list:
            futures.append(loop.create_task(self.run_updates_in_channels(sublist)))
        for future in futures:
            await future
        self.bot.logger.info("Done autoupdater!")

    @push_auto_updates.before_loop
    async def before_updates_pushed(self):
        await self.bot.wait_until_ready()

    def cog_unload(self):
        self.push_auto_updates.cancel()

    async def run_updates_in_channels(self, channels: List[list]):
        """"""
        for channel_data in channels:
            db_channel = channel_data[0]
            channel: discord.TextChannel = channel_data[1]
            if db_channel.autoupdater.delay == -1:
                await channel.send("The autoupdater delay in this channel is -1 seconds, or default. **I have "
                                   "disabled the updater**, and I recommend you make a new one. The stats on this "
                                   "updater are as follows:\nCountry: {0}\nDelay between updates: {1} seconds\n\nIf "
                                   "you're confused as to why this happened, it was most likely a bug in the bot that "
                                   "unfortunately hit you. If you'd like to know even more, join the bot's support "
                                   "server and ask 0/0#0001. Thanks for using this bot!".format(
                    db_channel.autoupdater.country_name, db_channel.autoupdater.delay))
                db_channel.autoupdater.already_set = False
                await db_channel.autoupdater.save()
                await db_channel.save()
                continue
            now = datetime.datetime.utcnow()
            if db_channel.autoupdater.force_update:
                db_channel.autoupdater.force_update = False
            elif db_channel.autoupdater.do_update_at != utc_zero:
                delta: datetime.timedelta = now - db_channel.autoupdater.do_update_at
                if delta.total_seconds() > 120:
                    continue
                db_channel.autoupdater.do_update_at = utc_zero
                db_channel.autoupdater.last_updated = now
            else:
                delta: datetime.timedelta = now - db_channel.autoupdater.last_updated
                if not delta.total_seconds() >= db_channel.autoupdater.delay:
                    continue
                db_channel.autoupdater.last_updated = now
            country = db_channel.autoupdater.country_name
            try:
                for msg in channel.history(limit=1):
                    ctx = await self.bot.get_context(msg, cls=MyContext)
                    msg1 = None
                    break
                else:
                    msg1 = await ctx.send("0x00000000")
                    ctx = await self.bot.get_context(msg1, cls=MyContext)
                _ = await ctx.get_translate_function()
                embed = await embeds.advanced_stats_embed(await self.bot.worldometers_api.try_to_get_name(country),
                                                          ctx=ctx)
                if embed is None:
                    await channel.send(_("I'm having a issue with finding the country name here! Here's what I'm "
                                         "showing: {trying}",
                                         trying=await self.bot.worldometers_api.try_to_get_name(country)))
                await channel.send(embed=embed)
                if msg1:
                    await msg1.delete()
            except TypeError:
                continue
            except (discord.DiscordException, discord.errors.Forbidden) as e:
                if isinstance(e, discord.Forbidden):
                    # how da hell did that happen? should've been caught on L162
                    self.bot.logger.info("No permissions to send messages here!",
                                         channel=channel, guild=channel.guild)
                    db_channel.autoupdater.already_set = False  # no perms? heh: have fun
                    await db_channel.autoupdater.save()
                    await db_channel.save()
                else:
                    self.bot.logger.exception("Exception in autoupdater!",
                                              exception_instance=e,
                                              channel=channel, guild=channel.guild)
                    # Since it failed this time, don't save it and force a update at next loop.
                continue
            await db_channel.autoupdater.save()
            await db_channel.save()


setup = AutoUpdaterCog.setup
