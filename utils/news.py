# coding=utf-8
import datetime
import logging
import time
from typing import Optional, Dict
from discord import Embed
from discord.ext import menus
import aiohttp


def from_time_to_datetime(in_time: time.struct_time) -> datetime.datetime:
    return datetime.datetime(year=in_time.tm_year,
                             month=in_time.tm_mon,
                             day=in_time.tm_mday,
                             hour=in_time.tm_hour,
                             minute=in_time.tm_min,
                             second=in_time.tm_sec)


class NewsAPI:
    # Supported NewsAPI countries: get all
    country_codes = ["ae", "ar", "at", "au", "be", "bg", "br", "ca", "ch", "cn", "co", "cu", "cz", "de", "eg", "fr",
                     "gb", "gr", "hk", "hu", "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma", "mx", "my",
                     "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro", "rs", "ru", "sa", "se", "sg", "si", "sk", "th",
                     "tr", "tw", "ua", "us", "ve", "za"]
    r"""
    ^^^
    Input regex was "(\S{2}) "
    Output regex was "$1", ""
    """

    def __init__(self, api_key: str):
        if len(api_key) != 32:
            raise ValueError("NewsAPI key is not 32 characters long!")
        self.api_key = api_key
        self.logger = logging.getLogger("news_api")
        self.world_data: Optional[dict] = None
        self.country_data: Dict[str, Optional[dict]] = {}
        self._updated: bool = False

    async def update(self, *, session: Optional[aiohttp.ClientSession] = None):
        self.logger.info("Updating News API...")
        session = session or aiohttp.ClientSession()
        self.logger.debug("Opening session...")
        async with session as s:
            self.logger.debug("Getting global stats...")
            r = await s.get(f"https://newsapi.org/v2/top-headlines?q=covid-19&apiKey={self.api_key}")
            r.raise_for_status()
            self.world_data = await r.json()

            for i in self.country_codes:
                self.logger.debug(f"Getting stats for {i}...")
                r = await s.get(f"https://newsapi.org/v2/top-headlines?q=covid-19&country={i}&apiKey={self.api_key}")
                r.raise_for_status()
                if (await r.json())["status"] != "ok":
                    raise aiohttp.ClientResponseError("Status was not ok!")
                self.country_data[i] = await r.json()
        self._updated = True
        self.logger.info("Updated News API!")

    async def _check_updated(self):
        if not self._updated:
            raise RuntimeError("NewsAPI not set up yet!")

    async def get_world_news(self) -> dict:
        await self._check_updated()
        return self.world_data

    async def get_country_news(self, iso2_code: str) -> Optional[dict]:
        await self._check_updated()
        if len(iso2_code) != 2:
            return None
        iso2_code = iso2_code.lower()
        if iso2_code in self.country_data:
            return self.country_data[iso2_code]
        else:
            return None


class NewsAPIMenu(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=1)

    async def format_page(self, menu: menus.MenuPages, page):
        offset = menu.current_page * self.per_page
        news_item = self.entries["articles"][offset]
        e = Embed(title=news_item["title"], url=news_item["url"])
        author = f"{news_item['source']['name']} | {news_item['author']}" if news_item["author"] else \
            str(news_item['source']['name'])
        e.set_author(name=author)
        e.set_image(url=news_item["urlToImage"])
        timestamp: str = news_item["publishedAt"]
        parse = "%Y-%m-%dT%H:%M:%SZ" if timestamp.endswith("Z") else "%Y-%m-%dT%H:%M:%S%z"
        try:
            e.timestamp = from_time_to_datetime(time.strptime(timestamp, parse))
        except ValueError:
            # noinspection SpellCheckingInspection
            pass  # ignore ValueErrors from the time.strptime func
        return e
