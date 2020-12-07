# coding=utf-8
# noinspection PyUnresolvedReferences
import datetime
from typing import Any, Optional

import discord

from utils.bot_class import MyBot
from utils.ctx_class import MyContext


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


async def basic_stats_embed(country: str, province: str, today: datetime.date, ctx: MyContext
                            ) -> Optional[discord.Embed]:
    stats = await ctx.bot.jhucsse_api.get_province_stats_for_day(country, province, today)
    if stats is None:
        return None
    data_points = (("<:infected:775877435320565801> Total Cases", "cases"),
                   ("<:deaths:775877434687488030> Total Deaths", "deaths"),
                   ("<:recovered:775877435089748008> Total Recoveries", "recovered"))
    stats_embed = discord.Embed(title=f"Province Stats for {province.title()} on {today!s}",
                                description="Why such a small amount of data compared to country stats?\n"
                                            "Some provinces may report the same amount of data, but these provinces "
                                            "make up such a small amount of all provinces, meaning it's not worth it "
                                            "to try to show it for all of them.")
    for name, value in data_points:
        if stats[value] == 0:
            stats_embed.add_field(name=name, value=f"{format(stats[value], ',')} (could also have no data)")
        else:
            stats_embed.add_field(name=name, value=format(stats[value], ','))
    stats_embed.set_footer(text="Last updated at")
    stats_embed.timestamp = ctx.bot.jhucsse_api.last_updated_utc
    return stats_embed


async def advanced_stats_embed(country: str, ctx: MyContext):
    data_points = (("<:infected:775877435320565801> Total Cases", "cases"),
                   ("New Cases", "todayCases"),
                   ("Cases per 1m People", "casesPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("<:active:775877437056614491> Active Cases", "active"),
                   ("Active Case Change", "activeCaseChange"),
                   ("Active Cases per 1m People", "activePerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("<:deaths:775877434687488030> Total Deaths", "deaths"),
                   ("New Deaths", "todayDeaths"),
                   ("Deaths per 1m People", "deathsPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("<:recovered:775877435089748008> Total Recoveries", "recovered"),
                   ("New Recoveries", "todayRecovered"),
                   ("Recovered per 1m People", "recoveredPerOneMillion"),
                   ("zero_space", "zero_space"),
                   ("<:tests:775877436075802676> Tests", "tests"),
                   ("Tests per 1m People", "testsPerOneMillion"),
                   ("zero_space", "zero_space") * 2,
                   ("Critical Cases", "critical"),
                   ("Population", "population"))
    if country is None:
        return None
    elif country[0] == "world":
        country_data = await ctx.bot.worldometers_api.get_global_stats()
        name = "World"
    elif country[0] == "country":
        country_data = await ctx.bot.worldometers_api.get_country_stats(country[1])
        name = country_data["country"]
    elif country[0] == "state":
        country_data = await ctx.bot.worldometers_api.get_state_stats(country[1])
        name = country_data["state"]
    elif country[0] == "continent":
        country_data = await ctx.bot.worldometers_api.get_continent_stats(country[1])
        name = country_data["continent"]
    else:
        return None
    _ = await ctx.get_translate_function()
    embed = discord.Embed(title=_("COVID-19 Stats for {name}", name=name),
                          color=discord.Color.dark_red(),
                          timestamp=ctx.bot.worldometers_api.last_updated_utc)
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
                ctx.bot.logger.warning(f"Key {dp[1]} is missing from {name}!")
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
