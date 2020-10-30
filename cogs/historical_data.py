# coding=utf-8
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class HistoricalData(Cog):
    @commands.command()
    async def ping(self, ctx: MyContext):
        pass

    @commands.Cog.listener()
    async def on_error(self, ctx: MyContext):
        pass


setup = Template.setup
