# coding=utf-8
import asyncio
from math import ceil
from typing import Optional

import discord
from discord.ext import commands, tasks
import datetime
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils import api as covid19api
from utils import embeds


async def list_file(ctx: MyContext, letter: str) -> Optional[str]:
    iso_codes = await ctx.bot.worldometers_api.get_all_iso_codes()
    countries = []
    letter = str(letter).lower()
    for field in iso_codes:
        country_name = field["country"].lower()
        if country_name.startswith(letter):
            countries.append(field)
    longest_name = 0
    if len(countries) != 0:
        for country in countries:
            if len(country["country"]) > longest_name:
                longest_name = len(country["country"])

        msg_str = "{0:<{1}} | ISO2 Code | ISO3 Code".format(country_name, longest_name)
        msgs = [msg_str, "-" * len(msg_str)]
        for country in countries:
            msgs.append("{0:<{1}} | {2}        | {3}      ".format(country["country"],
                                                                   longest_name,
                                                                   country["iso2"],
                                                                   country["iso3"]))
        return "\n".join(msgs)
    return None


class CovidCog(Cog):
    @commands.group()
    async def covid(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("covid")

    @covid.command(aliases=["global"])
    async def world(self, ctx: MyContext):
        """
        Stats for the entire world.
        """
        emb = await embeds.advanced_stats_embed(await self.bot.worldometers_api.try_to_get_name("world"), ctx)
        if emb is None:
            _ = await ctx.get_translate_function()
            await ctx.reply(_("A fatal error has happened! The world data seems to have gone missing. Please let a "
                              "mod in the bot's support server know."))
        else:
            await ctx.reply(embed=emb)

    @covid.command()
    async def continent(self, ctx: MyContext, continent_name: str):
        """
        Stats for any given continent.
        """
        real_name = await self.bot.worldometers_api.try_to_get_name(continent_name)
        if real_name is None or real_name[0] != "continent":
            _ = await ctx.get_translate_function()
            await ctx.reply(_("Didn't find any continents with that name!"))
        else:
            emb = await embeds.advanced_stats_embed(real_name, ctx)
            await ctx.reply(embed=emb)

    @covid.command()
    async def country(self, ctx: MyContext, *args):
        """
        Get stats on COVID-19 for any country!
        """
        _ = await ctx.get_translate_function()
        country = " ".join(args).lower().strip()
        if country == "global":
            country = "world"
        if country == "world" or country in ("", " "):
            await ctx.reply(_("Use the `{prefix}covid world` command instead.", prefix=ctx.prefix))
        country_test = await self.bot.worldometers_api.try_to_get_name(country)
        if country_test is None:
            if "korea" in country:
                msg = _("Didn't find a country with that name, or the country has no cases! Try searching for the name "
                        "with `{prefix}list country`.\n"
                        "Hint: if you're looking for North or South Korea, try "
                        "`{prefix}covid KP` or `{prefix}covid KR` for North and South Korea, "
                        "respectively!", prefix=ctx.prefix)
            else:
                msg = _("Didn't find a country with that name, or the country has no cases! Try searching for the name " \
                        "with `{prefix}list country`.", prefix=ctx.prefix)
            await ctx.reply(msg)
        elif country_test[0] != "country":
            await ctx.reply(_("You've used a incorrect command: try `{ctx.prefix}covid {country_test[0]}`"))
        else:
            stats_embed = await embeds.advanced_stats_embed(country_test, self.bot)
            await ctx.reply(embed=stats_embed)

    @covid.command()
    async def province(self, ctx: MyContext, *args):
        """
        Get stats on COVID-19 for any given province!

        You MUST split the country and province names with a semicolon followed by a space (; ), like so:
        /covid province canada; alberta
        """
        args = " ".join(args)
        if len(args.split("; ")) < 2:
            await ctx.send("You haven't split the country name and province with a `; `!")
            return
        elif len(args.split("; ")) > 2:
            await ctx.send("You've placed too many `; ` in your message! You can use only one to split the country "
                           "and province names! For help, run `{ctx.prefix}help covid province`!")
            return
        else:
            country, province = args.split("; ")
        today = datetime.date.today()
        today = today - datetime.timedelta(days=1)
        try:
            embed = await embeds.basic_stats_embed(country, province, today, ctx)
        except covid19api.CountryNotFound:
            await ctx.reply("Couldn't find a country with that ID (`/list` for a list of IDs) or the country has no "
                            "cases!")
            return
        except covid19api.ProvinceNotFound:
            await ctx.reply("Couldn't find a province with that name! If you're looking for US states, see the "
                            "`{ctx.prefix}covid states` command.")
            return
        else:
            if embed is None:
                await ctx.reply("Something went wrong, I can't find today's stats! I'm currently trying to find stats "
                                "for {today!s}!")
            else:
                await ctx.reply(embed=embed)

    @covid.command()
    async def states(self, ctx: MyContext, *state):
        """
        Get stats for US states!
        """
        if len(state) == 0:
            await ctx.reply("You need to specify a US state! For a list, run `{ctx.prefix}list states`.")
            return
        state = " ".join(state)
        state_test = await self.bot.worldometers_api.try_to_get_name(state)
        if state_test is None:
            await ctx.reply("Didn't find a state with that name! For a list, run `{ctx.prefix}list states`.")
        if state_test[0] != "state":
            await ctx.reply("That isn't a state! Try the `{ctx.prefix}covid {state_test[0]}` command.")
        else:
            await ctx.reply(embed=await embeds.advanced_stats_embed(state_test, self.bot))

    @commands.group(name="list")
    async def _list(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("list")

    @_list.command(name="countries", aliases=["country"])
    async def _countries(self, ctx: MyContext, *first_letter):
        """
        List countries that can be used in /covid country.
        """
        if len(first_letter) == 0:
            await ctx.reply("I can't send the entire country list: it's over Discord's 6,000 character limit! Try "
                            "`{ctx.prefix}{ctx.command.qualified_name} <letter>` to get only "
                            "countries starting with `<letter>`.")
            return
        first_letter = " ".join(first_letter)
        embed = await embeds.list_embed(self.bot, " ".join(first_letter))
        if embed is not None:
            try:
                await ctx.author.send(embed=embed)
            except discord.HTTPException:
                def file(reaction: discord.Reaction, user: discord.Member):
                    return reaction.message.id == ctx.message.id and ctx.author.id == user.id and reaction.emoji == "📔"

                msg = await ctx.reply("Whatever you have requested, it is over 6,000 characters. I can send a text "
                                      "file, however. React with 📔 any time in the next 15 seconds to be DMed a text "
                                      "file instead of a embed.")
                await msg.add_reaction("📔")
                try:
                    await self.bot.wait_for("reaction_add", check=file, timeout=15)
                except asyncio.TimeoutError:
                    await msg.edit(content="Timed out.")
                else:
                    msg = await list_file(ctx, first_letter)
                    await ctx.author.send(msg)  # the bot will convert this to a file for us, how nice
                    if ctx.guild is not None:
                        await ctx.reply("Sent you a DM!")
            if ctx.message.guild is not None:
                await ctx.reply("DMed a list to you!")
        else:
            await ctx.reply("Couldn't find any countries starting with those letters!")

    @staticmethod
    async def generate_list_embed(ctnts: list, type: tuple, ctx: MyContext):
        emb = discord.Embed(title="List of {type[1]}",
                            description="Use `{ctx.prefix}covid {type[0]} <name>` when getting stats for a {type[0]}!")
        for ctnt in ctnts:
            emb.add_field(name="Name", value=ctnt)
        return emb

    @_list.command(name="continents", aliases=["continent"])
    async def _continents(self, ctx: MyContext):
        """
        DMs you a list of all continents that can be used in the /covid continent command!
        """
        await ctx.author.send(embed=await self.generate_list_embed(self.bot.worldometers_api.continents,
                                                                   ("continent", "continents"),
                                                                   ctx))
        if ctx.guild is not None:
            await ctx.reply("DMed a list to you!")

    @_list.command(name="states", aliases=["state"])
    async def _states(self, ctx: MyContext, page: int = 1):
        """
        DMs you a list of all continents that can be used in the /covid state command!
        """
        state_list_embed = discord.Embed(title="List of American States",
                                         description="Use the `{ctx.prefix}covid states <name>` command when getting "
                                                     "stats for `<name>`!")
        max_pages = ceil(len(self.bot.worldometers_api.american_states) / 24)
        if not 0 < page <= max_pages:
            await ctx.reply("The page number you have selected is not between 1 and "
                            "{max_pages}. Please try again.")
            return
        sect = self.bot.worldometers_api.american_states[(page - 1) * 24: page * 24]
        for state_name in sect:
            state_list_embed.add_field(name="Name", value=state_name)
        if len(sect) == 24:
            state_list_embed.add_field(name="Page {page} of {max_pages}",
                                       value="To go to the next page, run "
                                             "`{ctx.prefix}{ctx.command.full_parent_name} {ctx.invoked_with} {page + 1}`")
        else:
            state_list_embed.add_field(name="Page {page} of {max_pages}", value="\u200b")
        await ctx.author.send(embed=state_list_embed)
        if ctx.guild is not None:
            await ctx.reply("DMed a list to you!")

    @commands.command()
    async def top(self, ctx: MyContext, _type: str):
        """
        <_type> can be one of "cases", "recovered", "deaths", "critical" or "tests"
        """
        try:
            _list = await self.bot.worldometers_api.get_sorted_list(_type.lower())
        except covid19api.IncorrectSortType:
            not_correct_type_embed = discord.Embed(title="Incorrect Top List Type",
                                                   description="Try sorting with one of the following:")
            for _type in ["cases", "recovered", "deaths", "critical", "tests"]:
                not_correct_type_embed.add_field(name="\u200b", value=_type)
            await ctx.send(embed=not_correct_type_embed)
            return
        if _list is None:
            not_correct_type_embed = discord.Embed(title="Incorrect Top List Type",
                                                   description="Try sorting with one of the following:")
            for _type in ["cases", "recovered", "deaths", "critical", "tests"]:
                not_correct_type_embed.add_field(name="\u200b", value=_type)
            await ctx.send(embed=not_correct_type_embed)
            return
        top_embed = discord.Embed(title="Top List",
                                  description="Run `{ctx.prefix}help top` for a list of all possible sorts")
        for country, i in zip(_list, range(1, len(_list))):
            top_embed.add_field(name="{i}: {country['country']}", value=format(int(country[_type.lower()]), ","))
        await ctx.send(embed=top_embed)

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
