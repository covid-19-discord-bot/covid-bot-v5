# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from typing import Optional

from discord.ext import commands, tasks, menus
from utils.bot_class import MyBot
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.news import NewsAPIMenu


class NewsCog(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.do_news_update.start()

    def cog_unload(self):
        self.do_news_update.cancel()

    @commands.command()
    async def news(self, ctx: MyContext, country_name: Optional[str] = None):
        _ = await ctx.get_translate_function()
        """
        if country_name is not None and (len(country_name) != 2 or
                                         country_name.lower() not in self.bot.news_api.country_codes):
            codes = "` `".join(self.bot.news_api.country_codes)
            await ctx.send(_("That isn't a valid ISO2 code! Try one of the following: `{0}`", codes))
            return
        """

        # data = await self.bot.news_api.get_country_news(country_name) if country_name else \
        #     await self.bot.news_api.get_world_news()
        data = await self.bot.news_api.get_world_news()
        pages = menus.MenuPages(source=NewsAPIMenu(data), clear_reactions_after=True, timeout=60)
        await pages.start(ctx)

    @tasks.loop(minutes=30)
    async def do_news_update(self):
        await self.bot.news_api.update()


setup = NewsCog.setup
