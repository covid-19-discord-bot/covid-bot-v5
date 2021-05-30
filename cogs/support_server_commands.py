"""
Some example of commands that can be used only in the bot support server.
"""

import datetime
import time
import random
import discord
import pytz
from babel import dates
from discord.ext import commands, tasks

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.interaction import purge_channel_messages


statuses = [discord.Status.online, discord.Status.idle, discord.Status.dnd]


class SupportServerCommands(Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.background_loop.start()
        self.update_status.start()

    def cog_unload(self):
        self.background_loop.cancel()
        self.update_status.cancel()

    async def cog_check(self, ctx):
        ret = await super().cog_check(ctx)
        ret = ret and ctx.guild.id == self.config()["support_server_id"]
        return ret

    @tasks.loop(seconds=75)
    async def update_status(self):
        self.bot.logger.info("Updating status...")
        for shard in self.bot.latencies:
            await self.bot.change_presence(
                activity=discord.Game(f"Shard {shard[0]} | "
                                      f"{round(shard[1] * 1000, 2)}ms latency | "
                                      f"{len(self.bot.guilds)} servers | "
                                      f"Mention for help"),
                status=random.choice(statuses),
                shard_id=shard[0])
        self.bot.logger.info("Updated status!")

    @tasks.loop(minutes=15)
    async def background_loop(self):
        status_channel = self.bot.get_channel(self.config()["status_channel_id"])
        if not status_channel or not isinstance(status_channel, discord.TextChannel):
            self.bot.logger.warning("The status channel for the support server command is misconfigured.")
            return

        self.bot.logger.debug("Updating status message", guild=status_channel.guild, channel=status_channel)

        await purge_channel_messages(status_channel)
        embed = discord.Embed(colour=discord.Color.dark_red(),
                              title=f"{self.bot.user.name}'s status")
        try:
            user_count = 0
            for guild in self.bot.guilds:
                user_count += guild.member_count
        except AttributeError:
            user_count = "unknown"

        embed.add_field(name="Guilds Count", value=str(len(self.bot.guilds)), inline=True)
        embed.add_field(name="Users Count", value=str(user_count), inline=True)
        embed.add_field(name="Messages in cache", value=str(len(self.bot.cached_messages)), inline=True)

        ping_f = status_channel.trigger_typing()
        t_1 = time.perf_counter()
        await ping_f  # tell Discord that the bot is "typing", which is a very simple request
        t_2 = time.perf_counter()
        ping = round(t_2 - t_1)  # calculate the time needed to trigger typing

        embed.add_field(name="Average Latency", value=f"{round(self.bot.latency*1000, 2)}ms", inline=True)
        embed.add_field(name="Current ping", value=f"{round(ping*1000, 2)}ms", inline=True)
        embed.add_field(name="Shards Count", value=f"{self.bot.shard_count}", inline=True)

        def get_bot_uptime():
            return dates.format_timedelta(self.bot.uptime - datetime.datetime.utcnow(), locale='en')

        embed.add_field(name="Cogs loaded", value=f"{len(self.bot.cogs)}", inline=True)
        embed.add_field(name="Commands loaded", value=f"{len(self.bot.commands)}", inline=True)
        embed.add_field(name="Uptime", value=f"{get_bot_uptime()}", inline=True)

        embed.timestamp = datetime.datetime.utcnow()

        next_it = self.background_loop.next_iteration
        now = pytz.utc.localize(datetime.datetime.utcnow())

        delta = dates.format_timedelta(next_it - now, locale='en')
        embed.set_footer(text=f"This should update every {delta} - Last update")

        await status_channel.send(embed=embed)

    @background_loop.before_loop
    async def before(self):
        await self.bot.wait_until_ready()

    @commands.command(aliases=["shard_status"])
    async def shards(self, ctx: MyContext):
        """
        Check the status of every shard the bot is hosting.
        """
        _ = await ctx.get_translate_function()
        if self.bot.shard_count == 1:
            await ctx.send(_("The bot is not yet sharded."))
            return

        latencies = sorted(self.bot.latencies, key=lambda l: l[0])
        message = ""

        for shard, latency in latencies:
            if shard == ctx.guild.shard_id:
                message += ""
            message += _("•\t Shard ID {0}: {1}ms", shard, round(latency*1000, 2))
            if shard in self.bot.shards_ready:
                message += _(" (ready)")
            if shard == ctx.guild.shard_id:
                message += _(" (current shard)")
            message += "\n"

        message += _("\n\nAvg latency: {0}ms", round(self.bot.latency*1000, 2))
        if self.bot.is_ready():  # should always be true
            message += _(" (bot ready)")

        await ctx.send(message)


setup = SupportServerCommands.setup
