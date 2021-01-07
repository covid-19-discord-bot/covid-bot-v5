# coding=utf-8
import datetime

from discord.ext import commands, tasks

from utils import api as covid19api
from utils import embeds
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class CovidCog(Cog):
    @commands.group()
    async def covid(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("covid")

    @covid.command(aliases=["global"])
    async def world(self, ctx: MyContext):
        """
        COVID-19 statistics for the world.
        """
        emb = await embeds.advanced_stats_embed(await self.bot.worldometers_api.try_to_get_name("world"), ctx=ctx)
        if emb is None:
            _ = await ctx.get_translate_function()
            await ctx.reply(_("A fatal error has happened! The world data seems to have gone missing. Please let a "
                              "mod in the bot's support server know."))
        else:
            await ctx.reply(embed=emb)

    @covid.command()
    async def continent(self, ctx: MyContext, continent_name: str):
        """
        COVID-19 stats for any continent.
        """
        real_name = await self.bot.worldometers_api.try_to_get_name(continent_name)
        if real_name is None or real_name[0] != "continent":
            _ = await ctx.get_translate_function()
            await ctx.reply(_("Didn't find any continents with that name!"))
        else:
            emb = await embeds.advanced_stats_embed(real_name, ctx=ctx)
            await ctx.reply(embed=emb)

    @covid.command()
    async def country(self, ctx: MyContext, *args):
        """
        COVID-19 stats for any country.
        """
        _ = await ctx.get_translate_function()
        country = " ".join(args).lower().strip()
        if country == "global":
            country = "world"
        if country == "world" or country in ("", " "):
            await ctx.reply(_("Use the `{0}covid world` command instead.", ctx.prefix))
        country_test = await self.bot.worldometers_api.try_to_get_name(country)
        if country_test is None:
            if "korea" in country:
                msg = _("Didn't find a country with that name, or the country has no cases! Try searching for the name "
                        "with `{0}list country`.\n"
                        "Hint: if you're looking for North or South Korea, try "
                        "`{0}covid KP` or `{0}covid KR` for North and South Korea, "
                        "respectively!", ctx.prefix)
            else:
                msg = _("Didn't find a country with that name, or the country has no cases! Try searching for the name "
                        "with `{0}list country`.", ctx.prefix)
            await ctx.reply(msg)
        elif country_test[0] != "country":
            await ctx.reply(_("You've used a incorrect command: try `{0}covid {1}`", ctx.prefix, country_test[0]))
        else:
            stats_embed = await embeds.advanced_stats_embed(country_test, ctx=ctx)
            await ctx.reply(embed=stats_embed)

    @covid.command()
    async def province(self, ctx: MyContext, *args):
        """
        COVID-19 stats for any province.
        """
        _ = await ctx.get_translate_function()
        args = " ".join(args)
        if len(args.split(";")) < 2:
            await ctx.send(_("You haven't split the country name and province with a `; `!"))
            return
        elif len(args.split(";")) > 2:
            await ctx.send(_("You've placed too many `; ` in your message! You can use only one to split the country "
                             "and province names! For help, run `{0}help covid province`!", ctx.prefix))
            return
        else:
            country, province = args.split(";")
            country = country.strip()
            province = province.strip()
        today = datetime.date.today()
        today = today - datetime.timedelta(days=1)
        try:
            embed = await embeds.basic_stats_embed(country, province, today, ctx=ctx)
        except covid19api.CountryNotFound:
            await ctx.reply(_("Couldn't find a country with that ID (`/list` for a list of IDs) or the country has no "
                              "cases!"))
            return
        except covid19api.ProvinceNotFound:
            await ctx.reply(_("Couldn't find a province with that name! If you're looking for US states, see the "
                              "`{0}covid states` command.", ctx.prefix))
            return
        else:
            if embed is None:
                await ctx.reply(_("Something went wrong, I can't find today's stats! I'm currently trying to find stats "
                                  "for {0}!", str(today)))
            else:
                await ctx.reply(embed=embed)

    @covid.command()
    async def states(self, ctx: MyContext, *state):
        """
        COVID-19 stats for any US state.
        """
        _ = await ctx.get_translate_function()
        if len(state) == 0:
            await ctx.reply(_("You need to specify a US state! For a list, run `{0}list states`.", ctx.prefix))
            return
        state = " ".join(state)
        state_test = await self.bot.worldometers_api.try_to_get_name(state)
        if state_test is None:
            await ctx.reply(_("Didn't find a state with that name! For a list, run `{0}list states`.", ctx.prefix))
        if state_test[0] != "state":
            await ctx.reply(_("That isn't a state! Try the `{0}covid {1}` command.", ctx.prefix, state_test[0]))
        else:
            await ctx.reply(embed=await embeds.advanced_stats_embed(state_test, ctx=ctx))

    @tasks.loop(minutes=10)
    async def update_stats(self):
        await self.bot.wait_until_ready()
        try:
            await self.bot.worldometers_api.update_covid_19_virus_stats()
        except Exception as e:
            await self.bot.worldometers_api.logger.exception("Fatal error while updating stats!",
                                                             exc_info=e)
        # Well that was simple :P

    # ignore it here, as it may not be in the correct state
    # noinspection PyProtectedMember
    @commands.command(name="force_stats_update", hidden=True)
    async def stats_update(self, ctx: MyContext):
        await ctx.send("Loading...")
        try:
            await self.bot._worldometers_api.update_covid_19_virus_stats()
            await self.bot._jhucsse_api.update_covid_19_virus_stats()
            await self.bot._vaccine_api.update_covid_19_vaccine_stats()
        except Exception:
            await ctx.send("Encountered error while updating. This error has been logged.")
            raise
        else:
            await ctx.send("Updated sucessfully!")


setup = CovidCog.setup
