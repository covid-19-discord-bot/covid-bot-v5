# coding=utf-8
# noinspection PyUnresolvedReferences
import datetime
from typing import Any, Optional, List

import discord

from utils.bot_class import MyBot
from utils.ctx_class import MyContext


# designed to be overridden in functions, used as a fallback
def _(msg, *args, **kwargs):
    return msg.format(*args, **kwargs)


def add_zero_space(embed: discord.Embed, count: int):
    for _ in range(1, count):
        embed.add_field(name="\u200b", value="\u200b")


async def basic_stats_embed(location: tuple, today: datetime.date, *, ctx: MyContext = None,
                            bot: MyBot = None) -> Optional[discord.Embed]:
    if ctx:
        _ = await ctx.get_translate_function()
        bot = ctx.bot
    else:
        if not bot:
            raise ValueError("bot must be passed if ctx is not!")

        def _(msg, *args, **kwargs):
            return msg.format(*args, **kwargs)
    stats = await bot.jhucsse_api.get_province_stats_for_day(location[1], today)
    if stats is None:
        return None
    data_points = ((_("<:infected:775877435320565801> Total Cases"), "cases"),
                   (_("<:deaths:775877434687488030> Total Deaths"), "deaths"),
                   (_("<:recovered:775877435089748008> Total Recoveries"), "recovered"))
    stats_embed = discord.Embed(title=_("Province Stats for {province} on {today}",
                                        province=location[1].title(), today=str(today)),
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


async def owid_embed(name: str, *, ctx: Optional[MyContext] = None, bot: Optional[MyBot] = None)\
        -> Optional[List[discord.Embed]]:
    if not ctx and not bot:
        raise ValueError("Must pass either bot or ctx!")
    elif not bot:
        bot = ctx.bot
        _ = await ctx.get_translate_function()
    elif not ctx:
        def _(msg: str, *args, **kwargs) -> str:
            return msg.format(*args, **kwargs)

    if name.lower() in ("ot", "world", "global"):
        data = await bot.owid_api.get_world_stats()
    else:
        data = await bot.owid_api.get_country_stats(name)
    if data is None:
        return None

    def format_num(x):
        return format(int(x), ",")

    embed0_data_points = (
        (_("Total Cases"), "total_cases", format_num),
        (_("New Cases"), "new_cases", format_num),
        (_("New Cases (7d avg)"), "new_cases_smoothed", format_num),
        (_("Total Deaths"), "total_deaths", format_num),
        (_("New Deaths"), "new_deaths", format_num),
        (_("New Deaths (7d avg)"), "total_deaths_smoothed", format_num),
        (_("Total Cases per 1m"), "total_cases_per_million", format_num),
        (_("New Cases per 1m"), "new_cases_per_million", format_num),
        (_("New Cases per 1m (7d avg)"), "new_cases_smoothed_per_million", format_num),
        (_("Total Deaths per 1m"), "total_deaths_per_million"),
        (_("New Deaths per 1m"), "new_deaths_per_million"),
        (_("New Deaths per 1m (7d avg)"), "new_deaths_smoothed_per_million"),
        (_("R-Value"), "reproduction_rate"),
        (_("Stringency Index"), "stringency_index"),
    )

    embed1_data_points = (
        (_("ICU Patients"), "icu_patients"),
        (_("ICU Patients per 1m"), "icu_patients_per_million"),
        (_("Hospitalized Patients"), "hosp_patients"),
        (_("Hospitalized Patients per 1m"), "hosp_patients_per_million"),
        (_("Weekly ICU Admissions"), "weekly_icu_admissions"),
        (_("Weekly ICU Admissions per 1m"), "weekly_icu_admissions_per_million"),
        (_("Weekly Hospital Admissions"), "weekly_hosp_admissions"),
        (_("Weekly Hospital Admissions per 1m"), "weekly_hosp_admissions_per_million"),
    )

    embed2_data_points = (
        (_("Total Tests"), "total_tests"),
        (_("New Tests"), "new_tests"),
        (_("New Tests (7d avg)"), "total_tests_smoothed"),
        (_("Total Tests per 1k"), "total_tests_per_thousand"),
        (_("New Tests per 1k"), "new_tests_per_thousand"),
        (_("New Tests per 1k (7d avg)"), "new_tests_smoothed_per_thousand"),
        (_("Tests Per Case"), "tests_per_case"),
        (_("Test Positivity Rate"), "positivity_rate"),
    )

    embed3_data_points = (
        (_("Total Vaccinations"), "total_vaccinations"),
        (_("Total Vaccinations per 100"), "total_vaccinations_per_hundred"),
        (_("New Vaccinations"), "new_vaccinations"),
        (_("New Vaccinations per 1m"), "new_vaccinations_per_million"),
    )

    embed4_data_points = (
        (_("Population"), "population"),
        (_("Population Density (km^2)"), "population_density"),
        (_("Median Age"), "median_age"),
        (_("% of population 65+"), "aged_65_older"),
        (_("% of population 70+"), "aged_70_older"),
        (_("GDP per person (USD$)"), "gdp_per_capita"),
        (_("% in extreme poverty"), "extreme_poverty"),
        (_("Cardiovascular Event Death Rate"), "cardiovasc_death_rate"),
        (_("% of population with diabetes"), "diabetes_prevalence"),
        (_("% of women that smoke"), "female_smokers"),
        (_("% of men that smoke"), "male_smokers"),
        (_("% of the population with access to handwashing facilities"), "handwashing_facilities"),
        (_("Hospital beds per 1,000 people"), "hospital_beds_per_thousand"),
        (_("Life expectancy"), "life_expectancy"),
        (_("Human Development Index"), "human_development_index")
    )

    embeds = []
    d = {}
    i = -1
    while not d.get("total_cases", None):
        d = data["data"][i]
        i -= 1

    r_value = d.get("reproduction_rate")
    if r_value:
        if r_value < 0.95:
            color = discord.Color.green()
        elif 0.95 <= r_value < 1.05:
            color = discord.Color.orange()
        elif 1.05 <= r_value:
            color = discord.Color.red()
    else:
        color = discord.Color.from_rgb(47, 49, 54)

    e0 = discord.Embed(title=_("COVID-19 Stats for {0}", name), color=color)
    e0.set_footer(text="Source: Our World in Data | See /credits for a link")
    for i in embed0_data_points:
        value = d.get(i[1], None)
        if value is None:
            continue  # skip the field if no data
        if isinstance(value, (float, int)):
            value = format(int(value), ",")
        e0.add_field(name=i[0], value=value)
    embeds.append(e0)

    e1 = discord.Embed(title=_("COVID-19 Hospital Stats for {0}", name), color=color)
    for i in embed1_data_points:
        value = d.get(i[1], None)
        if value is None:
            continue  # skip the field if no data
        if isinstance(value, (float, int)):
            value = format(int(value), ",")
        e1.add_field(name=i[0], value=value)
    if not len(e1.fields) == 0:
        embeds.append(e1)

    e2 = discord.Embed(title=_("COVID-19 Test Stats for {0}", name), color=color)
    for i in embed2_data_points:
        value = d.get(i[1], None)
        if value is None:
            continue  # skip the field if no data
        if isinstance(value, (float, int)):
            value = format(int(value), ",")
        e2.add_field(name=i[0], value=value)
    if not len(e2.fields) == 0:
        embeds.append(e2)

    e3 = discord.Embed(title=_("COVID-19 Vaccination Stats for {0}", name), color=color)
    for i in embed3_data_points:
        value = d.get(i[1], None)
        if value is None:
            continue  # skip the field if no data
        if isinstance(value, (float, int)):
            value = format(int(value), ",")
        e3.add_field(name=i[0], value=value)
    if not len(e3.fields) == 0:
        embeds.append(e3)

    e4 = discord.Embed(title=_("General Stats for {0}", name), color=color)
    for i in embed4_data_points:
        value = data.get(i[1], None)
        if value is None:
            continue  # skip the field if no data
        if isinstance(value, (float, int)):
            value = format(int(value), ",")
        e4.add_field(name=i[0], value=value)
    if not len(e4.fields) == 0:
        embeds.append(e4)

    return embeds


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
