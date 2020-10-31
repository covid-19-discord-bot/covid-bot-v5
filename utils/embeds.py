# coding=utf-8
# noinspection PyUnresolvedReferences
from utils.bot_class import MyBot
from typing import Any
import datetime
import discord
import utils.api as covid19api


def add_zero_space(embed: discord.Embed, count: int):
    for _ in range(1, count):
        embed.add_field(name="\u200b", value="\u200b")


def error_embed(bot: MyBot, reason: Any = None):
    _error_embed = discord.Embed(title="Error!",
                                 description="",
                                 color=discord.Color.red())
    zeroslashzero = bot.get_user(661660243033456652)
    _error_embed.add_field(name="An error happened!",
                           value="Report this to {0} on the official Discord server, available via `/invite`".format(
                              zeroslashzero.mention))
    if reason:
        bot.logger.exception("Exception while creating embed!", exception_instance=reason)
        if isinstance(reason, BaseException):
            _error_embed.add_field(name="Add this when you're reporting this message",
                                   value=f"`{str(reason)}`\n"
                                         f"```py\n{reason.__traceback__}```")
        else:
            _error_embed.add_field(name="Add this when you're reporting this message", value=str(reason))
    _error_embed.set_thumbnail(url="https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-error-icon.png")
    return _error_embed


async def stats_embed(country_name: str, bot: MyBot):
    data_points = (("Total Cases", "cases"),
                   ("New Cases", "todayCases"),
                   ("Cases per 1m People", "casesPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("Active Cases", "active"),
                   ("Active Case Change", "activeCaseChange"),
                   ("Active Cases per 1m People", "activePerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("Total Deaths", "deaths"),
                   ("New Deaths", "todayDeaths"),
                   ("Deaths per 1m People", "deathsPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("Total Recoveries", "recovered"),
                   ("New Recoveries", "todayRecovered"),
                   ("Recovered per 1m People", "recoveredPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("Tests", "tests"),
                   ("Tests per 1m People", "testsPerOneMillion"),
                   ("zero_space", "zero_space")*2,
                   ("Critical Cases", "critical"),
                   ("Population", "population"))
    if country_name != "world":
        country_list = await bot.worldometers_api.get_all_iso_codes()
        _id = covid19api.get_iso2_code(country_name, country_list)
        if not _id:
            country_data = await bot.worldometers_api.get_continent_stats(country_name)
            if country_data is not None:
                name = country_name.title()
        else:
            name = covid19api.get_country_name(_id, country_list)
            country_data = await bot.worldometers_api.get_country_stats(_id)
    else:
        _id = "OT"
        name = "World"
        country_data = bot.worldometers_api.global_stats
    embed = discord.Embed(title="COVID-19 Stats for {0}".format(name),
                          color=discord.Color.dark_red(),
                          timestamp=bot.worldometers_api.last_updated_utc)
    embed.set_footer(text="Stats last updated at (UTC)")
    if name in bot.worldometers_api.country_stats:
        embed.set_thumbnail(url=country_data["countryInfo"]["flag"])
    for dp in data_points:
        if dp[0] == "zero_space":
            add_zero_space(embed, 1)
        else:
            try:
                if country_data[dp[1]] is not None:
                    embed.add_field(name=dp[0],
                                    value=format(int(country_data[dp[1]]), ","))
                else:
                    embed.add_field(name=dp[0],
                                    value="no data")
            except KeyError:
                bot.logger.warning(f"Key {dp[1]} is missing from {name}!")
    if country_name == "world":
        embed.add_field(name="Affected Countries",
                        value=format(int(country_data["affectedCountries"]), ","))
    return embed


async def list_embed(bot: MyBot, letter: str) -> [discord.Embed, None]:
    try:
        _list = await bot.worldometers_api.get_all_iso_codes()
        embed = discord.Embed(color=discord.Color.blue(),
                              title="Country List",
                              description="Use either the country name, or the ISO2/ISO3 code when getting stats with "
                                          "`/covid <name>`!")
        countries = []
        letter = str(letter).lower()
        for field in _list:
            country_name = field["country"].lower()
            if country_name.startswith(letter):
                countries.append(field)
        if len(countries) != 0:
            for country in countries:
                embed.add_field(name="Country Name",
                                value=country["country"])
                embed.add_field(name="Country ISO2 ID",
                                value=country["iso2"])
                embed.add_field(name="Country ISO3 ID",
                                value=country["iso3"])
                add_zero_space(embed, 1)
            return embed
        else:
            return None
    except Exception as e:
        _error_embed = error_embed(bot, reason=e)
        return _error_embed
