# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext


class FutureSimulationsCog(Cog):
    @commands.command()
    async def simulate(self, ctx: MyContext):
        pass


setup = FutureSimulationsCog.setup
