# coding=utf-8
from discord.ext import tasks

from utils.async_helpers import wrap_in_async
from utils.bot_class import MyBot
from utils.cog_class import Cog


class BackgroundUpdates(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.updaters = [
            self.update_worldometers_stats,
            self.update_jhucsse_stats,
            self.update_vaccine_stats,
            self.update_owid_stats,
            self.update_maps
        ]
        for updater in self.updaters:
            updater: tasks.Loop
            updater.start()

    def cog_unload(self):
        for updater in self.updaters:
            updater: tasks.Loop
            updater.clear_exception_types()  # just in case it throws a exception, we don't want it to keep trying.
            updater.stop()

    @tasks.loop(minutes=5)
    async def update_worldometers_stats(self):
        await self.bot.wait_until_ready()
        await self.bot.worldometers_api.update_covid_19_virus_stats()

    @tasks.loop(minutes=15)
    async def update_jhucsse_stats(self):
        await self.bot.wait_until_ready()
        await self.bot.jhucsse_api.update_covid_19_virus_stats()

    @tasks.loop(hours=12)
    async def update_vaccine_stats(self):
        await self.bot.wait_until_ready()
        await self.bot.vaccine_api.update_covid_19_vaccine_stats()

    @tasks.loop(hours=12)
    async def update_owid_stats(self):
        await self.bot.wait_until_ready()
        await self.bot.owid_api.update_covid_19_owid_data()

    @tasks.loop(hours=24)
    async def update_maps(self):
        await self.bot.wait_until_ready()
        # selenium hates being run in another process
        await wrap_in_async(self.bot.maps_api.download_maps, thread_pool=True)


setup = BackgroundUpdates.setup
