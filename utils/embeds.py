# coding=utf-8
# noinspection PyUnresolvedReferences
import datetime
from typing import Any, Optional

import discord

from utils.bot_class import MyBot
from utils.ctx_class import MyContext


# designed to be overridden in functions, used as a fallback
def _(msg, *args, **kwargs):
    return msg.format(*args, **kwargs)


def add_zero_space(embed: discord.Embed, count: int):
    for _ in range(1, count):
        embed.add_field(name="\u200b", value="\u200b")


async def basic_stats_embed(country: str, province: str, today: datetime.date, *, ctx: MyContext = None,
                            bot: MyBot = None) -> Optional[discord.Embed]:
    if ctx:
        _ = await ctx.get_translate_function()
        bot = ctx.bot
    stats = await bot.jhucsse_api.get_province_stats_for_day(country, province, today)
    if stats is None:
        return None
    data_points = ((_("<:infected:775877435320565801> Total Cases"), "cases"),
                   (_("<:deaths:775877434687488030> Total Deaths"), "deaths"),
                   (_("<:recovered:775877435089748008> Total Recoveries"), "recovered"))
    stats_embed = discord.Embed(title=_("Province Stats for {province} on {today}",
                                        province=province.title(), today=str(today)),
                                description=_("Why such a small amount of data compared to country stats?\n"
                                              "Some provinces may report the same amount of data, but these provinces "
                                              "make up such a small amount of all provinces, meaning it's not worth it "
                                              "to try to show it for all of them."))
    for name, value in data_points:
        if stats[value] == 0:
            stats_embed.add_field(name=name, value=_("{0} (could also have no data)", format(stats[value], ',')))
        else:
            stats_embed.add_field(name=name, value=format(stats[value], ','))
    stats_embed.set_footer(text=_("Last updated at"))
    stats_embed.timestamp = bot.jhucsse_api.last_updated_utc
    return stats_embed


async def advanced_stats_embed(country: str, *, ctx: Optional[MyContext] = None, bot: MyBot = None):
    if ctx:
        _ = await ctx.get_translate_function()
        bot = ctx.bot
    else:
        def _(msg, *args, **kwargs):
            return msg.format(*args, **kwargs)
    data_points = ((_("<:infected:775877435320565801> Total Cases"), "cases"),
                   (_("New Cases"), "todayCases"),
                   (_("Cases per 1m People"), "casesPerOneMillion"),
                   ("zero_space", "zero_space"),
                   (_("<:active:775877437056614491> Active Cases"), "active"),
                   (_("Active Case Change"), "activeCaseChange"),
                   (_("Active Cases per 1m People"), "activePerOneMillion"),
                   ("zero_space", "zero_space"),
                   (_("<:deaths:775877434687488030> Total Deaths"), "deaths"),
                   (_("New Deaths"), "todayDeaths"),
                   (_("Deaths per 1m People"), "deathsPerOneMillion"),
                   ("zero_space", "zero_space"),
                   (_("<:recovered:775877435089748008> Total Recoveries"), "recovered"),
                   (_("New Recoveries"), "todayRecovered"),
                   (_("Recovered per 1m People"), "recoveredPerOneMillion"),
                   ("zero_space", "zero_space"),
                   (_("<:tests:775877436075802676> Tests"), "tests"),
                   (_("Tests per 1m People"), "testsPerOneMillion"),
                   ("zero_space", "zero_space") * 2,
                   (_("Critical Cases"), "critical"),
                   (_("Population"), "population"))
    print(*country)
    if country is None:
        return None
    elif country[0] == "world":
        country_data = await bot.worldometers_api.get_global_stats()
        name = "World"
    elif country[0] == "country":
        country_data = await bot.worldometers_api.get_country_stats(country[1])
        name = country_data["country"]
    elif country[0] == "state":
        country_data = await bot.worldometers_api.get_state_stats(country[1])
        name = country_data["state"]
    elif country[0] == "continent":
        country_data = await bot.worldometers_api.get_continent_stats(country[1])
        name = country_data["continent"]
    else:
        return None
    embed = discord.Embed(title=_("COVID-19 Stats for {name}", name=name),
                          color=discord.Color.dark_red(),
                          timestamp=bot.worldometers_api.last_updated_utc)
    embed.set_footer(text=_("Stats last updated at (UTC)"))
    if "countryInfo" in country_data and "flag" in country_data["countryInfo"]:
        embed.set_thumbnail(url=country_data["countryInfo"]["flag"])
    for dp in data_points:
        if dp[0] == "zero_space":
            add_zero_space(embed, 1)
        else:
            try:
                if country_data[dp[1]] is not None:
                    embed.add_field(name=_(dp[0]),
                                    value=format(int(country_data[dp[1]]), ","))
                else:
                    embed.add_field(name=_(dp[0]),
                                    value=_("no data"))
            except KeyError:
                bot.logger.warning(f"Key {dp[1]} is missing from {name}!")
                embed.add_field(name=_(dp[0]),
                                value=_("no data"))
    if name == "World":
        embed.add_field(name=_("Affected Countries"),
                        value=format(int(country_data["affectedCountries"]), ","))
    return embed


async def list_embed(ctx: MyContext, letter: str) -> [discord.Embed, None]:
    _ = await ctx.get_translate_function()
    _list = await ctx.bot.worldometers_api.get_all_iso_codes()
    embed = discord.Embed(color=discord.Color.blue(),
                          title=_("Country List"),
                          description=_("Use either the country name, or the ISO2/ISO3 code when getting stats with "
                                        "`/covid <name>`!"))
    countries = []
    letter = str(letter).lower()
    for field in _list:
        country_name = field["country"].lower()
        if country_name.startswith(letter):
            countries.append(field)
    if len(countries) != 0:
        for country in countries:
            embed.add_field(name=country["country"],
                            value=country["iso2"])
        return embed
