# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import tasks
from discord.ext import commands
from utils.ctx_class import MyContext
from utils.cog_class import Cog
from utils.bot_class import MyBot
from asyncio import sleep


class BackgroundUpdates(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.update_all_stats.start()

    @commands.command(name="restart_autoupdaters")
    @commands.has_any_role(686939763927678986)
    async def you_ve_got_to_be_kidding(self, ctx: MyContext):
        stats_msg = await ctx.send("Stopping task...")
        await self.update_all_stats.stop()
        await stats_msg.edit(content="Task has been sent a stop signal.")
        await sleep(10)
        await stats_msg.edit(content="Sending terminate signal...")
        self.update_all_stats.cancel()
        await stats_msg.edit(content="Task has been killed. Starting now...")
        self.update_all_stats.start()
        await stats_msg.edit(content="Task has been sent a start signal.")
        await sleep(10)
        await stats_msg.edit(content="Task restarted!")

    @tasks.loop(minutes=10)
    async def update_all_stats(self):
        await self.bot.wait_until_ready()
        self.bot.logger.info("Starting autoupdates...")
        if self.index == 0:
            await self.bot.async_setup()  # just to be 100% certain this is called
        await self.bot.worldometers_api.update_covid_19_virus_stats()
        await self.bot.jhucsse_api.update_covid_19_virus_stats()
        await self.bot.vaccine_api.update_covid_19_vaccine_stats()
        self.index += 1


setup = BackgroundUpdates.setup
