# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
import discord
from discord.ext import commands

from utils.cog_class import Cog
from utils.models import get_from_db


class ChannelCleanupCog(Cog):
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
        db_channel = await get_from_db(channel)
        await db_channel.save()
        await db_channel.delete()


setup = ChannelCleanupCog.setup
