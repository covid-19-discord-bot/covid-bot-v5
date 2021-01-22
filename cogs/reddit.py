# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext


class RedditCog(Cog):
    @commands.command()
    @commands.cooldown(1, 60, type=commands.BucketType.user)
    async def reddit(self, ctx: MyContext):
        """
        Get the latest COVID-19 info from Reddit.

        Credits to
        """
        pass


setup = RedditCog.setup
