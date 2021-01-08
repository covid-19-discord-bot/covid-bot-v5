# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from asyncio import sleep

from discord.ext import commands
from discord.ext import tasks

from utils import wrap_in_async
from utils.bot_class import MyBot
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class BackgroundUpdates(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.update_all_stats.start()

    @commands.command(name="restart_autoupdaters")
    @commands.has_any_role(686939763927678986)
    async def you_ve_got_to_be_kidding(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        stats_msg = await ctx.send(_("Stopping task..."))
        self.update_all_stats.stop()
        await stats_msg.edit(content=_("Task has been sent a stop signal. Waiting 10 seconds..."))
        await sleep(10)
        await stats_msg.edit(content=_("Sending terminate signal..."))
        self.update_all_stats.cancel()
        await stats_msg.edit(content=_("Task has been killed. Starting now..."))
        await sleep(10)
        self.update_all_stats.start()
        await stats_msg.edit(content=_("Task has been sent a start signal."))
        await sleep(10)
        await stats_msg.edit(content=_("Task restarted!"))

    def cog_unload(self):
        self.update_all_stats.stop()

    @tasks.loop(minutes=10)
    async def update_all_stats(self):
        await self.bot.wait_until_ready()
        self.bot.logger.info("Starting autoupdates...")
        if self.index == 0:
            await self.bot.async_setup()  # just to be 100% certain this is called
        await self.bot.worldometers_api.update_covid_19_virus_stats()
        await self.bot.jhucsse_api.update_covid_19_virus_stats()
        await self.bot.vaccine_api.update_covid_19_vaccine_stats()
        # selenium hates being run in another process
        await wrap_in_async(self.bot.maps_api.download_maps, thread_pool=True)
        self.index += 1


setup = BackgroundUpdates.setup
