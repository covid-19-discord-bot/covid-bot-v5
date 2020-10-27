# coding=utf-8
import discord
from discord.ext import commands, tasks
from utils.api import VaccineStats
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.bot_class import MyBot


# TODO: fix vaccine stats system
class Vaccine(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.vaccine_data = VaccineStats()

    @commands.group()
    async def vaccine(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            vaccine_phases = ""
            for phase in self.vaccine_data.phases:
                vaccine_phases += f"{phase['phase']}: {phase['candidates']} candidates\n"
            vaccine_embed = discord.Embed(name="Vaccine Updates",
                                          description=f"(For more details, run `{ctx.prefix}help vaccine`)\n"
                                                      f"There are a total of **{self.vaccine_data.total_candidates} "
                                                      f"vaccine candidates**."
                                                      f"\n__**Phases**__\n{vaccine_phases}")
            await ctx.send(embed=vaccine_embed)

    @vaccine.group()
    async def list_all_candidates(self, ctx: MyContext):
        vaccine_embed = discord.Embed()

    @tasks.loop(minutes=10)
    async def do_vaccine_update(self):
        await self.vaccine_data.update_covid_19_vaccine_stats()  # easy as pie


setup = Vaccine.setup
