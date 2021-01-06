# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands
import discord
import utils.api as covid19api
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class Template(Cog):
    @commands.command()
    async def top(self, ctx: MyContext, _type: str):
        """
        <_type> can be one of "cases", "recovered", "deaths", "critical" or "tests"
        """
        _ = await ctx.get_translate_function()
        try:
            _list = await self.bot.worldometers_api.get_sorted_list(_type.lower())
        except covid19api.IncorrectSortType:
            not_correct_type_embed = discord.Embed(title=_("Incorrect Top List Type"),
                                                   description=_("Try sorting with one of the following:"))
            for _type in ["cases", "recovered", "deaths", "critical", "tests"]:
                not_correct_type_embed.add_field(name="\u200b", value=_type)
            await ctx.send(embed=not_correct_type_embed)
            return
        if _list is None:
            not_correct_type_embed = discord.Embed(title=_("Incorrect Top List Type"),
                                                   description=_("Try sorting with one of the following:"))
            for _type in ["cases", "recovered", "deaths", "critical", "tests"]:
                not_correct_type_embed.add_field(name="\u200b", value=_type)
            await ctx.send(embed=not_correct_type_embed)
            return
        top_embed = discord.Embed(title=_("Top List"),
                                  description=_("Run `{0}help top` for a list of all possible sorts!", ctx.prefix))
        for country, i in zip(_list, range(1, len(_list))):
            top_embed.add_field(name=_("{0}: {1}", i, country["country"]),
                                value=format(int(country[_type.lower()]), ","))
        await ctx.send(embed=top_embed)


setup = Template.setup
