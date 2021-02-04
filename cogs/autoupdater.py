# coding=utf-8
# Licenced under the CC BY-NC-SA 4.0 licence: by modifying any code you agree to be bound by the terms of the licence:
# https://creativecommons.org/licenses/by-nc-sa/4.0/

# Accept/Yes: ✅
# Warning: ⚠
# Error/No: ❌

import asyncio
import datetime
from typing import Optional, List, Union, Callable, Dict, Any

import discord
from discord.ext import tasks, commands

import utils.api as covid19api
import utils.embeds as embeds
from utils import autoupdater
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.human_time import ShortTime, human_timedelta, FutureTime
from utils.models import get_from_db, DiscordChannel, AutoupdaterData, DiscordGuild, AutoupdateTypes

utc_zero = datetime.datetime.utcfromtimestamp(-1)

updater_types = {"1⃣": "world", "2⃣": "continent", "3⃣": "country"}


class AutoUpdaterCog(Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.push_auto_updates.start()

    def cog_unload(self):
        self.push_auto_updates.cancel()

    async def do_initial_checks(self, ctx: MyContext, db_guild: DiscordGuild, db_channel: DiscordChannel,
                                delta_seconds: int, _: Callable, *, requires_vote: bool = False):
        await db_channel.fetch_related("autoupdater")

        if len(db_channel.autoupdater) + 1 > db_guild.total_updaters:
            await ctx.reply(_("You've used too many updaters! You've used {0} of your {1} updaters. Get more by "
                              "voting on top.gg.", db_guild.used_updaters, db_guild.total_updaters))
            return False

        if requires_vote and db_guild.total_updaters - db_guild.used_updaters <= 1:
            await ctx.reply(_("You need to vote for one of these special updaters! See `/vote` for details."))
            return False

        if delta_seconds > 31536000:
            await ctx.reply(_("❌ Did you really try to set the autoupdater delay to more than a year? Oi. "
                              "Anyways, that isn't allowed. Try again with a more reasonable delay."))
            return False

        if delta_seconds > 86400 and not db_guild.overtime_confirmed:
            def pred(c):
                return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and \
                       c.content.lower() == "ok"

            await ctx.reply(_("⚠ You're setting a delay longer than 1 day! Are you sure you want to do this? To "
                              "confirm, type `ok` within 15 seconds."))
            try:
                await self.bot.wait_for("message", check=pred, timeout=15)
            except asyncio.TimeoutError:
                await ctx.send(_("Action cancelled."))
                return False
            else:
                await ctx.send(_("Continuing setup..."))
                db_guild.overtime_confirmed = True
                await db_guild.save()
        return True

    @commands.group()
    @commands.has_permissions(manage_messages=True)
    async def autoupdate(self, ctx: MyContext):
        """
        Invoking this command without subcommands starts interactive setup.
        Subcommands can be found with `/help autoupdate`.
        """
        if ctx.invoked_subcommand is None:
            _ = await ctx.get_translate_function()
            msg = await ctx.send(_("Hi there! Welcome to the COVID-19 Bot autoupdater interactive setup.\n"
                                   "Let's get started. Choose one of the following options.\n"
                                   "1⃣: Updates for the world.\n"
                                   "2⃣: Updates for a continent.\n"
                                   "3⃣: Updates for a country."))

            def reaction_event(payload: discord.RawReactionActionEvent):
                return payload.message_id == msg.id and payload.user_id == ctx.author.id and (payload.emoji.name in
                                                                                              updater_types)

            for emoji in updater_types:
                await msg.add_reaction(emoji)

            try:
                reaction = await self.bot.wait_for("raw_reaction_add", timeout=30, check=reaction_event)
            except asyncio.TimeoutError:
                await msg.edit(content=_("Timed out."))
                return

            _type = updater_types.get(reaction.emoji.name)
            await msg.clear_reactions()

            def msg_event(msg0: discord.Message):
                return msg0.channel.id == ctx.channel.id and msg0.author.id == ctx.author.id

            valid = False
            while not valid:
                await msg.edit(content=_("Next, what update delay would you like? For example, 12h would do a update "
                                         "every 12 hours. Keep in mind any delays beyond 1 year will not work."))
                try:
                    msg1 = await self.bot.wait_for("message", timeout=30, check=msg_event)
                except asyncio.TimeoutError:
                    await msg.edit(content=_("Timed out."))
                    return
                msg_ctx = await self.bot.get_context(msg1, cls=MyContext)
                try:
                    delay = await ShortTime.convert(ctx=msg_ctx, argument=msg1.content.lower().strip())
                except commands.BadArgument:
                    await ctx.send(_("Invalid time provided. Make sure it's in the correct format!"), delete_after=15)
                else:
                    valid = True
                finally:
                    await msg1.delete()

            if _type == "country":
                await msg.edit(content=_("Finally, what country would you like to do a update for? Type the country's "
                                         "ISO2 code into chat."))
                valid = False
                while not valid:
                    try:
                        msg1 = await self.bot.wait_for("message", timeout=30, check=msg_event)
                    except asyncio.TimeoutError:
                        await msg.edit(content=_("Timed out."))
                        return
                    finally:
                        await msg1.delete()
                    info = await self.bot.worldometers_api.try_to_get_name(msg1.content.lower())
                    if info is None:
                        await ctx.send(_("Didn't find a country name! Try again."), delete_after=15)
                    elif info[0] != "country":
                        await ctx.send(_("I found a {0} instead of a country! You can let this time out and try "
                                         "again.", info[0]))
                    else:
                        country = info[1]
                        valid = True
                # we're bypassing all internal checks, so this had better work... otherwise it's not gonna end well
                await self._country.__call__(ctx, delay, country)  # yes _country() would work but it's not explicit
            elif _type == "world":
                await self._world.__call__(ctx, delay)
            elif _type == "continent":
                await msg.edit(content=_("Finally, what continent would you like to do a update for? Type the "
                                         "continent name into chat."))
                valid = False
                while not valid:
                    try:
                        msg1 = await self.bot.wait_for("message", timeout=30, check=msg_event)
                    except asyncio.TimeoutError:
                        await msg.edit(content=_("Timed out."))
                        return
                    finally:
                        await msg1.delete()
                    info = await self.bot.worldometers_api.try_to_get_name(msg1.content.lower())
                    if info is None:
                        await ctx.send(_("Didn't find a continent name! Try again."), delete_after=15)
                    elif info[0] != "continent":
                        await ctx.send(_("I found a {0} instead of a continent! You can let this time out and try "
                                         "again.", info[0]), delete_after=15)
                    else:
                        continent = info[1]
                        valid = True
                await self._continent.__call__(ctx, delay, continent)
            await msg.delete()

    @autoupdate.command(name="world")
    async def _world(self, ctx: MyContext, delay: ShortTime):
        """
        Enable autoupdaters for the world.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _):
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True, country_name="OT", delay=update_delay,
                                  discord_id=ctx.channel.id, type=AutoupdateTypes.world)
        await ad_data.save()
        db_guild.used_updaters += 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting stats for {0} in this channel every {1}.", "OT", human_update_time))

    @autoupdate.command(name="continent")
    async def _continent(self, ctx: MyContext, delay: ShortTime, continent: str):
        """
        Enable autoupdaters for a continent. For a list of all continents, run /list continents.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        continent is the continent name. If it includes spaces, be sure to wrap it in quotes.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _):
            return

        info = await self.bot.worldometers_api.try_to_get_name(continent)
        if info is None:
            cmd_usage = "`{0}list continent`".format(ctx.prefix)
            await ctx.reply(_("❌ Failed to get a continent name! {0} will show you a list of continents.", cmd_usage))
        elif info[0] == "continent":
            iso2_code = friendly_country_name = continent
        else:
            cmd_usage = "{0}autoupdate {1} {2}".format(ctx.prefix, info[0], '' if info[0] != 'world' else continent)
            await ctx.reply(_("❌ I found a {0} instead of a continent! You can try `{1}` instead.", info[0],
                              cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True, country_name=iso2_code, delay=update_delay,
                                  discord_id=ctx.channel.id, type=AutoupdateTypes.continent)
        await ad_data.save()
        db_guild.used_updaters += 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting stats for {0} in this channel every {1}.",
                          friendly_country_name, human_update_time))

    @autoupdate.command(name="country")
    async def _country(self, ctx: MyContext, delay: ShortTime, country: str):
        """
        Enable autoupdaters for a continent. For a list of countries, run /list .
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        continent is the continent name. If it includes spaces, be sure to wrap it in quotes.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _):
            return

        info = await self.bot.worldometers_api.try_to_get_name(country)
        if info is None:
            await ctx.reply(_("❌ Failed to get a ISO2 code for the country! `/list` will show you a list of countries "
                              "and their IDs."))
        elif info[0] == "country":
            country_list = await self.bot.worldometers_api.get_all_iso_codes()
            iso2_code = covid19api.get_iso2_code(country, country_list)
            friendly_country_name = covid19api.get_country_name(country, country_list)
        else:
            cmd_usage = "{0}autoupdate {1} {2}".format(ctx.prefix, info[0], '' if info[0] != 'world' else country)
            await ctx.reply(_("I found a {0} instead of a country! You can try `{1}` instead.", info[0], cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True, country_name=iso2_code, delay=update_delay,
                                  discord_id=ctx.channel.id, type=AutoupdateTypes.country)
        await ad_data.save()
        db_guild.used_updaters += 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting stats for {0} in this channel every {1}.",
                          friendly_country_name, human_update_time))

    @autoupdate.command(name="state")
    async def _state(self, ctx: MyContext, delay: ShortTime, state: str):
        """
        Enable autoupdaters for a state. For a list of states, run /list .
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        state is the state name. If it includes spaces, be sure to wrap it in quotes.
        This requires at least two vote credits.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _):
            return

        info = await self.bot.worldometers_api.try_to_get_name()
        if info is None:
            await ctx.reply(_("❌ Failed to find a state with that name! `/list` will show you a list of states "
                              "and their names."))
        elif info[0] == "state":
            iso2_code = friendly_country_name = state
        else:
            cmd_usage = "{0}autoupdate {1} {2}".format(ctx.prefix, info[0], '' if info[0] != 'world' else state)
            await ctx.reply(_("I found a {0} instead of a state! You can try `{1}` instead.", info[0], cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True, country_name=iso2_code, delay=update_delay,
                                  discord_id=ctx.channel.id, type=AutoupdateTypes.state)
        await ad_data.save()
        db_guild.used_updaters += 1
        db_guild.total_updaters -= 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting stats for {0} in this channel every {1}.",
                          friendly_country_name, human_update_time))

    @autoupdate.group(name="graphs", aliases=["graph"])
    async def _graph(self, ctx: MyContext):
        """
        Enable autoupdaters for graphs. See all subcommands. This requires two vote credits to enable any of them.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help("autoupdate graphs")

    @_graph.command(name="world")
    async def __world(self, ctx: MyContext, delay: ShortTime, logarithmic: bool):
        """
        Enable graph autoupdaters for the world.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        logarithmic is whether the graph should be logarithmic.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _, requires_vote=True):
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True, country_name=f"world_{'log' if logarithmic else 'lin'}",
                                  delay=update_delay, discord_id=ctx.channel.id, type=AutoupdateTypes.graph)
        await ad_data.save()
        db_guild.used_updaters += 1
        db_guild.total_updaters -= 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting a {0} graph for {1} in this channel every {2}.",
                          _("logarithmic") if logarithmic else _("linear"), "world", human_update_time))

    @_graph.command(name="country")
    async def __country(self, ctx: MyContext, delay: ShortTime, country: str, logarithmic: bool):
        """
        Enable autoupdaters for a country.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        country is the country name. For a list of countries, run /list.
        logarithmic is whether the graph should be logarithmic.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _, requires_vote=True):
            return

        info = await self.bot.jhucsse_api.try_to_get_name(country)
        if info is None:
            await ctx.reply(_("❌ Failed to get a ISO2 code for the country! `/list` will show you a list of countries "
                              "and their IDs."))
            return
        elif info[0] == "country":
            country_list = await self.bot.worldometers_api.get_all_iso_codes()
            friendly_country_name = covid19api.get_country_name(country, country_list)
        else:
            cmd_usage = f"{ctx.prefix}autoupdate graphs {info[0]} {'' if info[0] != 'world' else country}"
            await ctx.reply(_("I found a {0} instead of a country! You can try `{1}` instead.", info[0], cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True,
                                  country_name=f"{info[1].title() if info[1] else 'world'}_"
                                               f"{'log' if logarithmic else 'lin'}",
                                  delay=update_delay, discord_id=ctx.channel.id, type=AutoupdateTypes.graph)
        await ad_data.save()
        db_guild.used_updaters += 1
        db_guild.total_updaters -= 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting a {0} graph for {1} in this channel every {2}.",
                          _("logarithmic") if logarithmic else _("linear"), friendly_country_name, human_update_time))

    @_graph.command(name="province")
    async def __province(self, ctx: MyContext, delay: ShortTime, province: str, logarithmic: bool):
        """
        Enable autoupdaters for a province.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        province is the province name.
        logarithmic is whether the graph should be logarithmic.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _, requires_vote=True):
            return

        info = await self.bot.jhucsse_api.try_to_get_name(province)
        if info is None:
            await ctx.reply(_("❌ Failed to find that province name!"))
            return
        elif info[0] == "province":
            friendly_country_name = province
        else:
            cmd_usage = f"{ctx.prefix}autoupdate graphs {info[0]} {'' if info[0] != 'world' else province}"
            await ctx.reply(_("I found a {0} instead of a province! You can try `{1}` instead.", info[0], cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True,
                                  country_name=f"{info[1].title() if info[1] else 'world'}_"
                                               f"{'log' if logarithmic else 'lin'}",
                                  delay=update_delay, discord_id=ctx.channel.id, type=AutoupdateTypes.graph)
        await ad_data.save()
        db_guild.used_updaters += 1
        db_guild.total_updaters -= 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting a {0} graph for {1} in this channel every {2}.",
                          _("logarithmic") if logarithmic else _("linear"), friendly_country_name, human_update_time))

    @_graph.command(name="state")
    async def __state(self, ctx: MyContext, delay: ShortTime, state: str, logarithmic: bool):
        """
        Enable autoupdaters for a US state.
        delay is a human-readable time, like 12h for 12 hours, or 10m for 10 minutes.
        state is the state name.
        logarithmic is whether the graph should be logarithmic.
        """
        _ = await ctx.get_translate_function()

        delta_seconds = int(abs((datetime.datetime.utcnow() - delay.dt).total_seconds()))
        human_update_time = human_timedelta(delay.dt)

        db_guild = await get_from_db(ctx.guild)
        db_channel = await get_from_db(ctx.channel)

        if not await self.do_initial_checks(ctx, db_guild, db_channel, delta_seconds, _, requires_vote=True):
            return

        info = await self.bot.jhucsse_api.try_to_get_name(state)
        if info is None:
            cmd_usage = f"`{ctx.prefix}list`"
            await ctx.reply(_("❌ Failed to find that state name! See {0} for help!", cmd_usage))
            return
        elif info[0] == "state":
            friendly_country_name = state
        else:
            cmd_usage = f"{ctx.prefix}autoupdate graphs {info[0]} {'' if info[0] != 'world' else state}"
            await ctx.reply(_("I found a {0} instead of a state! You can try `{1}` instead.", info[0], cmd_usage))
            return

        update_delay = delta_seconds
        ad_data = AutoupdaterData(already_set=True,
                                  country_name=f"{info[1].title() if info[1] else 'world'}_"
                                               f"{'log' if logarithmic else 'lin'}",
                                  delay=update_delay, discord_id=ctx.channel.id, type=AutoupdateTypes.graph)
        await ad_data.save()
        db_guild.used_updaters += 1
        db_guild.total_updaters -= 1
        await db_guild.save()
        await db_channel.autoupdater.add(ad_data)
        await db_channel.save()

        await ctx.reply(_("✅ Posting a {0} graph for {1} in this channel every {2}.",
                          _("logarithmic") if logarithmic else _("linear"), friendly_country_name, human_update_time))

    #######################
    # Manglement Commands #
    #######################
    @autoupdate.command(name="disable", aliases=["delete", "remove"])
    async def _disable(self, ctx: MyContext, _id: str):
        """
        Removes a autoupdater from this channel.
        The only argument should be either a autoupdater ID, or "all" to delete all the updaters in the channel.
        """
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        all_ad = db_channel.autoupdater
        _id = _id.lower().strip()
        total_updaters = len(all_ad)
        try:
            _id = int(_id)
        except ValueError:
            if not _id == "all":
                await ctx.reply(_("❌ Must pass either {0} or a ID as a argument.", "`all`"))
                return
        await db_channel.fetch_related("guild")
        if _id == "all":
            await db_channel.autoupdater.clear()
            async for ad in AutoupdaterData().filter(discord_id=ctx.channel.id):
                await ad.delete()
            db_channel.guild.used_updaters -= total_updaters
            await db_channel.guild.save()
            await db_channel.save()
            await ctx.reply(_("✅ Deleted all autoupdaters in this channel."))
        else:
            async for ad in AutoupdaterData().filter(discord_id=ctx.channel.id, id=_id):
                await ad.delete()
                break
            else:
                await ctx.reply(_("❌ No autoupdater with that ID found."))
                return
            db_channel.guild.used_updaters -= 1
            await db_channel.guild.save()
            await db_channel.save()
            await ctx.reply(_("✅ Deleted autoupdater with ID {0}.", _id))

    @autoupdate.command(name="list")
    @commands.cooldown(1, 30, type=commands.BucketType.channel)
    async def _list(self, ctx: MyContext):
        """
        Lists all autoupdaters in this channel.
        """
        _ = await ctx.get_translate_function()
        cmd_usage = "{0}autoupdate disable <id>".format(ctx.prefix)
        update_embed = discord.Embed(title=_("List of Updaters"),
                                     description=_("To disable one of these updaters, run {0}, replacing {1} with the "
                                                   "ID.", cmd_usage, "`<id>`"))
        async for updater in AutoupdaterData().filter(discord_id=ctx.channel.id):
            update_embed.add_field(name=updater.id, value=_("Country: {0}\n"
                                                            "Delay: {1} seconds", updater.country_name, updater.delay))
        if len(update_embed.fields) == 0:
            update_embed.add_field(name=_("None 😞"), value=_("Add one with the {0} command!", "`/autoupdate`"))
        await ctx.reply(embed=update_embed)

    @autoupdate.command(name="force_update")
    @commands.cooldown(1, 150, type=commands.BucketType.channel)
    async def force_updates(self, ctx: MyContext, _id: int):
        """
        Forces a update in this channel. A ID must be passed.
        """
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        updater = await get_updater(str(_id), ctx)
        if not updater:
            await ctx.reply(_("❌ You don't have a autoupdater set here or the ID you sent is invalid!"))
            return
        updater.force_update = True
        await updater.save()
        await db_channel.save()
        await ctx.reply(_("✅ Forcing a update sometime in the next minute."))

    @autoupdate.command(name="update_at")
    @commands.cooldown(1, 600, type=commands.BucketType.channel)
    async def update_at(self, ctx: MyContext, _id: int, at: FutureTime):
        """
        Can force a update at a specific time.
        Useful for when you want to make your updates run when your country releases data.
        """
        time_to_update_at: datetime.datetime = at.dt
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(ctx.channel)
        updater = await get_updater(str(_id), ctx)
        if not updater:
            await ctx.reply(_("❌ You don't have a autoupdater set here or the ID you sent is invalid!"))
            await self.update_at.reset_cooldown(ctx)
            return
        updater.do_update_at = time_to_update_at
        await db_channel.save()
        await ctx.reply(_("✅ Next update: {0}", human_timedelta(time_to_update_at)))

    @tasks.loop(minutes=1.0)
    async def push_auto_updates(self):
        self.bot.logger.info("Starting autoupdater...")
        db_channels = await AutoupdaterData.filter(already_set=True)
        channels_to_parse = []
        for db_channel in db_channels:
            channel: discord.TextChannel = self.bot.get_channel(db_channel.discord_id)
            if channel is None:
                continue
            db_data = await get_from_db(channel)
            channels_to_parse.append([db_channel, channel, db_data])
        self.bot.logger.info(f"Updating in {len(channels_to_parse)} channels.")
        sized_list = split_seq(channels_to_parse, 100)  # split into chunks of 100: as of this writing there's
        # only 137 heh
        # next part seems weird, but it seems to give me a 10 to 1,000 times speedup (over three minutes cut down to
        # less than 1 second)
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

    async def run_updates_in_channels(self, channels: List[list]):
        """"""
        for channel_data in channels:
            updater: AutoupdaterData = channel_data[0]
            channel: discord.TextChannel = channel_data[1]
            db_channel: DiscordChannel = channel_data[2]
            now = datetime.datetime.utcnow()
            if updater.force_update:
                updater.force_update = False
            elif updater.do_update_at != utc_zero:
                delta: datetime.timedelta = now - updater.do_update_at
                if delta.total_seconds() > 60:
                    continue
                updater.do_update_at = utc_zero
                updater.last_updated = now
            else:
                delta: datetime.timedelta = now - updater.last_updated
                if not delta.total_seconds() >= updater.delay:
                    continue
                updater.last_updated = now
            country = updater.country_name
            msg_to_send: Optional[Dict[str, Any]] = None
            try:
                async for msg in channel.history(limit=1):
                    ctx = await self.bot.get_context(msg, cls=MyContext)
                    msg1 = None
                    break
                else:
                    # discord DOES accept empty strings... until you load it up in your IDE
                    msg1 = await channel.send("​")
                    ctx = await self.bot.get_context(msg1, cls=MyContext)
                if updater.type == AutoupdateTypes.world:
                    msg_to_send = await autoupdater.world(ctx)
                elif updater.type == AutoupdateTypes.continent:
                    msg_to_send = await autoupdater.continent(ctx, country)
                elif updater.type == AutoupdateTypes.country:
                    msg_to_send = await autoupdater.country(ctx, country)
                elif updater.type == AutoupdateTypes.state:
                    msg_to_send = await autoupdater.state(ctx, country)
                elif updater.type == AutoupdateTypes.graph:
                    msg_to_send = await autoupdater.graph(ctx, country)
                await channel.send(**msg_to_send)
                if msg1:
                    await msg1.delete()
            except Exception as e:
                if isinstance(e, discord.Forbidden):
                    # how da hell did that happen? should've been caught earlier
                    self.bot.logger.info("No permissions to send messages here!",
                                         channel=channel, guild=channel.guild)
                    updater.already_set = False  # no perms? heh: have fun
                    await updater.save()
                    await db_channel.save()
                else:
                    self.bot.logger.exception("Exception in autoupdater!",
                                              exception_instance=e,
                                              channel=channel, guild=channel.guild)
                # Since it failed this time, don't save it and force a update at next loop.
                continue
            await updater.save()
            await db_channel.save()


async def get_updater(_id: Union[str, int], ctx: MyContext, *, allow_all: bool = False) -> \
        Optional[Union[List[AutoupdaterData], AutoupdaterData]]:
    _id = _id.lower().strip()
    try:
        _id = int(_id)
    except ValueError:
        if not _id == "all":
            return
        else:
            if allow_all:
                updater_list = []
                async for ad in AutoupdaterData().filter(discord_id=ctx.channel.id):
                    updater_list.append(ad)
                return updater_list
            else:
                raise commands.BadArgument("`all` is a invalid ID!")
    else:
        async for ad in AutoupdaterData().filter(discord_id=ctx.channel.id, id=_id):
            return ad


def split_seq(seq, size):
    new_seq = []
    split_size = 1.0 / size * len(seq)
    for i in range(size):
        new_seq.append(seq[int(round(i * split_size)):int(round((i + 1) * split_size))])
    return new_seq


setup = AutoUpdaterCog.setup
