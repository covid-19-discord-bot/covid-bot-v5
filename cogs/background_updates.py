# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import tasks
from utils.cog_class import Cog
from utils.bot_class import MyBot


class BackgroundUpdates(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.index = 0
        self.update_all_stats.start()

    @tasks.loop(minutes=10)
    async def update_all_stats(self):
        await self.bot.wait_until_ready()
        if self.index == 0:
            await self.bot.async_setup()  # just to be 100% certain this is called
        await self.bot.worldometers_api.update_covid_19_virus_stats()
        await self.bot.jhucsse_api.update_covid_19_virus_stats()
        await self.bot.vaccine_api.update_covid_19_vaccine_stats()
        await self.bot.maps_api.download_maps()
        self.index += 1


setup = BackgroundUpdates.setup
