# coding=utf-8
# noinspection PyUnresolvedReferences
from typing import Any
import datetime
import discord
import utils.api as covid19api


def add_zero_space(embed: discord.Embed, count: int):
    for _ in range(1, count):
        embed.add_field(name="\u200b", value="\u200b")


def error_embed(bot: discord.Client, reason: Any = None):
    _error_embed = discord.Embed(title="Error!",
                                 description="",
                                 color=discord.Color.red())
    zeroslashzero = bot.get_user(661660243033456652)
    _error_embed.add_field(name="An error happened!",
                           value="Report this to {0} on the official Discord server, available via `/invite`".format(
                              zeroslashzero.mention))
    if reason:
        if isinstance(reason, BaseException):
            _error_embed.add_field(name="Add this when you're reporting this message",
                                   value=f"`{str(reason)}`\n"
                                         f"```py\n{reason.__traceback__}```")
        else:
            _error_embed.add_field(name="Add this when you're reporting this message", value=str(reason))
    _error_embed.set_thumbnail(url="https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/sign-error-icon.png")
    return _error_embed


async def stats_embed(country_name: str, bot: discord.Client, covid_api: covid19api.Covid19StatsWorldometers):
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
    try:
        if country_name != "world":
            country_list = await covid_api.get_all_iso_codes()
            _id = covid19api.get_iso2_code(country_name, country_list)
            name = covid19api.get_country_name(_id, country_list)
            if not _id:
                return None
        else:
            _id = "OT"
            name = "World"
        country_data = await covid_api.get_country_stats(_id)
        updated_time = datetime.datetime.utcfromtimestamp(country_data["updated"] / 1000)
        embed = discord.Embed(title="COVID-19 Stats for {0}".format(name),
                              color=discord.Color.dark_red(),
                              timestamp=updated_time)
        embed.set_footer(text="Stats last updated at (UTC)")
        if name != "world":
            embed.set_thumbnail(url=country_data["countryInfo"]["flag"])
        for name, key in data_points:
            if name == "zero_space":
                add_zero_space(embed, 1)
            else:
                if country_data[key] is not None:
                    embed.add_field(name=name,
                                    value=format(int(country_data[key]), ","))
                else:
                    embed.add_field(name=name,
                                    value="no data")
        if country_name == "world":
            embed.add_field(name="Affected Countries",
                            value=format(int(country_data["affectedCountries"]), ","))
        return embed
    except Exception as e:
        _error_embed = error_embed(bot,
                                   reason=e)
        return _error_embed


async def list_embed(bot: discord.Client, letter: str,
                     covid_api: covid19api.Covid19StatsWorldometers) -> [discord.Embed, None]:
    try:
        _list = await covid_api.get_all_iso_codes()
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
