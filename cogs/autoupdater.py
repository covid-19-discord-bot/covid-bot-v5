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
from typing import Optional
from utils.models import get_from_db
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.human_time import ShortTime, human_timedelta, FutureTime


class AutoUpdaterCog(Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.push_auto_updates.start()

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
            await ctx.send(_("❌ Did you really try to set the autoupdater delay to more than a year? Oi. "
                             "Anyways, that isn't allowed. Try again with a more reasonable delay."))

        db_user = await get_from_db(ctx.author)  # Put it here that way it can be checked quickly if needed

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)
        is_premium = db_guild.is_premium or db_user.is_premium
        if db_channel.autoupdater.already_set:
            await ctx.send(_("❌ You already have a autoupdater set in this channel! Remove it with "
                             "`/disable_updates` and try again!"))
            return
        if delta_seconds > 86400 and not db_guild.overtime_confirmed:
            def pred(c):
                return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and \
                       c.message.content.lower() == "ok"

            await ctx.send(_("⚠ You're setting a delay longer than 1 day! Are you sure you want to do this? To "
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
                await ctx.send(_("You're setting the autoupdater to less than 10 minutes delay. I'll skip the check "
                                 "because you are a premium guild/user. <3 from 0/0#0001"))
            else:
                await ctx.send(_("❌ You can't set the autoupdater delay to less than 10 minutes unless you are a "
                                 "premium guild.\n"
                                 "Hint: there's no point in setting it to less than 10 minutes due to the fact the "
                                 "stats updater only fires once every 10 minutes. If you really want to get a "
                                 "shorter delay (no point in doing so), check out the `/donate` command."))
                return

        if country != "world":
            country_list = await self.bot.worldometers_api.get_all_iso_codes()
            _id = covid19api.get_iso2_code(country, country_list)
            if not _id:
                country_data = await self.bot.worldometers_api.get_continent_stats(country)
                if country_data is not None:
                    friendly_country_name = iso2_code = country.title()
                else:
                    await ctx.send(_("Failed to get a ISO2 code for the country! `/list` will show you a list of "
                                     "countries and their IDs."))
                    return
            else:
                friendly_country_name = covid19api.get_country_name(_id, country_list)
        else:
            _id = "OT"
            friendly_country_name = "World"

        update_delay = delta_seconds

        db_channel.autoupdater.already_set = True
        db_channel.autoupdater.country_name = iso2_code
        db_channel.autoupdater.delay = update_delay
        await db_channel.autoupdater.save()
        await db_channel.save()

        await ctx.send(_("✅ Posting stats for {0} in this "
                         "channel every {1} minutes.".format(friendly_country_name, human_update_time)))

    @commands.command(name="disable_updates", aliases=["disableUpdates"])
    @commands.has_permissions(manage_messages=True)
    async def disable_updates(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        if db_channel.autoupdater.already_set:
            db_channel.autoupdater.already_set = False
            await db_channel.autoupdater.save()
            await db_channel.save()
            await ctx.send(_("Disabled autoupdates in this channel."))
        else:
            await ctx.send(_("You don't have a autoupdater set here!"))

    @commands.command(name="force_update")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 150, type=commands.BucketType.channel)
    async def force_updates(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        if not db_channel.autoupdater.already_set:
            await ctx.send(_("You don't have a autoupdater set here!"))
            return
        db_channel.autoupdater.force_update = True
        await db_channel.autoupdater.save()
        await db_channel.save()
        await ctx.send(_("Forcing a update sometime in the next minute."))

    @commands.command(name="update_at")
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 600, type=commands.BucketType.channel)
    async def update_at(self, ctx: MyContext, at: FutureTime):
        # need to calculate the timedelta and set the last update to be at minus timedelta to keep the code in
        # push_auto_updates the same
        time_to_update_at: datetime.datetime = at.dt
        if time_to_update_at < datetime.date.today() + datetime.timedelta(days=30):
            await ctx.send("You can't force a update further than 30 days away!")
            return
        db_channel = await get_from_db(ctx.channel)
        delta = time_to_update_at - datetime.timedelta(seconds=db_channel.autoupdater.delay - 15)  # get rid of 15 seconds to make it better
        db_channel.autoupdater.last_updated = delta
        await ctx.send("Next update {0}.".format(human_timedelta(delta)))

    @tasks.loop(minutes=1.0)
    async def push_auto_updates(self):
        self.bot.logger.info("Running autoupdater...")
        for channel in self.bot.get_all_channels():  # Holy hell is this a lot simpler...
            if not isinstance(channel, discord.TextChannel):  # shouldn't be triggered, but who knows...
                continue
            channel: discord.TextChannel
            db_channel = await get_from_db(channel)
            perms_for = channel.permissions_for(channel.guild.me)
            if not perms_for.send_messages and perms_for.embed_links:
                self.bot.logger.info("Idiots can have fun trying to figure out why this isn't working",
                                     channel=channel, guild=channel.guild)
                db_channel.autoupdater.already_set = False  # no perms? heh: have fun
                await db_channel.autoupdater.save()
                await db_channel.save()
                # big brains will figure out it's missing perms
                # small brains will complain wHy BoT nO wOrK?
                continue
            if db_channel.autoupdater.already_set or db_channel.autoupdater.force_update:
                db_channel.autoupdater.force_update = False
                now = datetime.datetime.utcnow()
                delta: datetime.timedelta = now - db_channel.autoupdater.last_updated
                if not delta.total_seconds() >= db_channel.autoupdater.delay:
                    continue
                db_channel.autoupdater.last_updated = now
                country = db_channel.autoupdater.country_name
                country = 'world' if country == 'OT' else country
                try:
                    embed = await embeds.stats_embed(f"{country}", self.bot)
                    await channel.send(embed=embed)
                except discord.DiscordException as e:
                    if isinstance(e, discord.Forbidden):
                        # how da hell did that happen? should've been caught on L162
                        await self.bot.logger.info("No permissions to send messages here!",
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
        self.bot.logger.info("Done autoupdater!")

    @push_auto_updates.before_loop
    async def before_updates_pushed(self):
        await self.bot.wait_until_ready()

    def cog_unload(self):
        self.push_auto_updates.cancel()


setup = AutoUpdaterCog.setup
