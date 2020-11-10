# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands
from discord.ext import tasks
import aiofiles
import discord
from utils.cog_class import Cog
from utils.ctx_class import MyContext

map_identifiers = {"total_cases_per_million": ["total_covid_cases_per_million.png", "Total COVID-19 Cases Per Million"],
                   "total_cases": ["total_covid_cases.png", "Total COVID-19 Cases"],
                   "total_deaths": ["total_deaths.png", "Total COVID-19 Deaths"],
                   "total_deaths_per_million": ["total_deaths_per_million.png", "Total COVID-19 Deaths Per Million"],
                   "tests": ["tests.png", "Total COVID-19 Tests"],
                   "tests_per_thousand": ["tests_per_1k.png", "Total COVID-19 Tests per Thousand"]}


class MapsCommands(Cog):
    @commands.command()
    async def maps(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("maps")

    @maps.command()
    async def types(self, ctx: MyContext):
        map_type_embed = discord.Embed(title="Map Types",
                                       description=f"Use one of these map types when running `{ctx.prefix}maps "
                                                   f"show <name>`.")
        for item in map_identifiers:
            map_type_embed.add_field(name=map_identifiers[item][1], value=item)
        await ctx.send(embed=map_type_embed)

    @maps.command()
    async def show(self, ctx: MyContext, map_type: str):
        _ = await ctx.get_translate_function()
        map_type = map_type.lower().strip()
        if map_type not in map_identifiers:
            await ctx.send(_(f"I don't know what map you're looking for! Run `{ctx.prefix}maps types` to see all the "
                             f"maps I can show you!"))
            return
        map_embed = discord.Embed(title=f"Map for {map_identifiers[map_type][1]}")
        img_file = discord.File(f"{self.bot.maps_api.base_path}/{map_identifiers[map_type][0]}", filename="map.png")
        map_embed.set_image(url="attachment://map.png")
        await ctx.send(embed=map_embed, file=img_file)


setup = MapsCommands.setup
