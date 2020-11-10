# coding=utf-8
import asyncio
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


class CovidCog(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.update_stats.start()

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
                if is_premium:
                    await ctx.send("Couldn't find data for that country you tried to find, please wait as I try to "
                                   "find the nearest match!")
                    nearest_match = await ai_system.find_nearest_match(country,
                                                                       await self.bot.worldometers_api.
                                                                       get_all_iso_codes())
                    if nearest_match:
                        await ctx.send(f"Found a possible match!\n"
                                       f"Please let me know if this match was a good one by sending me a yes/no "
                                       f"message in DMs within 30 seconds!\n"
                                       f"`{nearest_match}`")
                    else:
                        await ctx.send("Didn't find any possible matches. Sorry!")
                    return
                msg = "Couldn't find a country with that ID (`/list` for a list of IDs) or the country has no cases! "
                if db_guild.enable_tips and not is_premium and randint(1, 100) < 82:
                    msg += f"To get a possible AI-powered correction, level up this guild to premium: `/donate`! " \
                           f"(disable these tips with `{ctx.prefix}settings set enable_tips false`)"
                await ctx.send(msg)
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
        embed = await embeds.list_embed(self.bot, " ".join(first_letter))
        if embed is not None:
            await ctx.author.send(embed=embed)
            if ctx.message.guild is not None:
                await ctx.send("DMed a list to you!")
        else:
            await ctx.send("Couldn't find any countries starting with those letters!")

    @commands.command()
    async def top(self, ctx: MyContext, *_type):
        """
        /top <type>

        where <type> is one of "cases", "recovered", "deaths", "critical", "tests"
        """
        try:
            _list = await self.bot.worldometers_api.get_sorted_list(_type[0].lower())
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
            top_embed.add_field(name=f"{i}: {country['country']}", value=country[_type[0].lower()])
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
