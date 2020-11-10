# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands
from discord.ext import tasks

from utils.cog_class import Cog
from utils.ctx_class import MyContext

map_types = ["infected", "recovered", "deaths", "tests"]

class Template(Cog):
    @commands.command()
    async def maps(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("maps")

    @maps.command()
    async def types(self, ctx: MyContext):



setup = Template.setup
