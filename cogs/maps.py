# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands
from discord.ext import tasks
import discord
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.maps import map_identifiers
from utils.async_helpers import wrap_in_async


class MapsCommands(Cog):
    @commands.group()
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
        map_buffer = await wrap_in_async(self.bot.maps_api.get_map, map_type, thread_pool=True)
        img_file = discord.File(map_buffer, filename="map.png")
        map_embed.set_image(url="attachment://map.png")
        await ctx.send(embed=map_embed, file=img_file)


setup = MapsCommands.setup
