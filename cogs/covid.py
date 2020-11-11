# coding=utf-8
import asyncio
from typing import Optional

import discord
from discord.ext import commands, tasks
from discord.ext.commands import BucketType
from random import randint
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.bot_class import MyBot
from utils.models import get_from_db
from utils import ai_system
from utils import api as covid19api
from utils import embeds
from utils import graphs


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
    @commands.command()
    @commands.cooldown(1, 0.25, BucketType.user)  # No average user will be hitting this command once every 250ms
    async def covid(self, ctx: MyContext, *args):
        db_guild = await get_from_db(ctx.guild)
        db_user = await get_from_db(ctx.author, as_user=True)
        if db_user.is_premium or db_guild.is_premium:
            is_premium = True
        else:
            is_premium = False
        if len(args) == 0:
            stats_embed = await embeds.stats_embed("world", self.bot)
            if stats_embed is None:
                error_embed = embeds.error_embed(self.bot, reason="Severe error: no world data!")
                await ctx.send(embed=error_embed)
                return
            msg = await ctx.send(embed=stats_embed)
        else:
            country = " ".join(args).lower()
            if country == "global":
                country = "world"
            stats_embed = await embeds.stats_embed(country, self.bot)
            if stats_embed is None:
                await ctx.send("Couldn't find a country with that ID (`/list` for a list of IDs) or the country has "
                               "no cases!")
                return
            msg = await ctx.send(embed=stats_embed)
        return  # TODO: set up JHUCSSE API

        # noinspection PyUnreachableCode
        def reaction_add_event(reaction: discord.Reaction, user: discord.Member):
            return reaction.emoji == "📈" and user.id == ctx.author.id and reaction.message.id == msg.id
        await msg.add_reaction("📈")
        while True:
            try:
                event_return = self.bot.wait_for("reaction_add", check=reaction_add_event, timeout=600)
            except asyncio.TimeoutError:
                return
            else:
                emoji: str = event_return[0]
                await msg.remove_reaction(emoji, event_return[1])
                process_pool = self.bot.premium_process_pool if is_premium else self.bot.basic_process_pool
                loop = asyncio.get_running_loop()
                await loop.run_in_executor(process_pool, graphs.generate_line_plot())

    @commands.command(name="list")
    async def _list(self, ctx: MyContext, *first_letter):
        if len(first_letter) == 0:
            await ctx.send("I can't send the entire country list: it's over Discord's 6,000 character limit! Try "
                           "`/list <letter>` to get only countries starting with `<letter>`.")
            return
        first_letter = " ".join(first_letter)
        embed = await embeds.list_embed(self.bot, " ".join(first_letter))
        if embed is not None:
            if len(embed) >= 6000:
                def file(reaction: discord.Reaction, user: discord.Member):
                    return reaction.message.id == ctx.message.id and ctx.author.id == user.id and reaction.emoji == "📔"

                msg = await ctx.send("Whatever you have requested, it is over 6,000 characters. I can send a text "
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
                        await ctx.send("Sent you a DM!")

            await ctx.author.send(embed=embed)
            if ctx.message.guild is not None:
                await ctx.send("DMed a list to you!")
        else:
            await ctx.send("Couldn't find any countries starting with those letters!")

    @commands.command()
    async def top(self, ctx: MyContext, _type: str):
        """
        /top <type>

        where <type> is one of "cases", "recovered", "deaths", "critical", "tests"
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
        top_embed = discord.Embed(title="Top List", description="Run `/help list` for a list of all possible sorts")
        for country, i in zip(_list, range(1, len(_list))):
            top_embed.add_field(name=f"{i}: {country['country']}", value=country[_type.lower()])
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
