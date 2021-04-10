# coding=utf-8
"""
Top commands, like /top.
"""
from typing import Callable

import discord
from discord.ext import commands

import utils.api as covid19api
from utils.cog_class import Cog
from utils.ctx_class import MyContext


def incorrect_sort(_: Callable) -> discord.Embed:
    not_correct_type_embed = discord.Embed(title=_("Incorrect Top List Type"),
                                           description=_("Try sorting with one of the following:"),
                                           color=discord.Color.dark_red())
    for _type in ["cases", "recovered", "deaths", "critical", "tests"]:
        not_correct_type_embed.add_field(name="\u200b", value=_type)
    return not_correct_type_embed


class TopCommands(Cog):
    @commands.command()
    async def top(self, ctx: MyContext, _type: str):
        """
        Get top statistics for one of _type! Pie charts can be found in /graphs (soon™).
        <_type> can be one of "cases", "recovered", "deaths", "critical" or "tests"
        """
        _ = await ctx.get_translate_function()
        print(_type)
        try:
            _list = await self.bot.worldometers_api.get_sorted_list(_type.lower())
        except covid19api.IncorrectSortType:
            await ctx.send(embed=incorrect_sort(_))
            return
        if _list is None:
            await ctx.send(embed=incorrect_sort(_))
            return
        top_embed = discord.Embed(title=_("Top List"),
                                  description=_("Run `{0}help top` for a list of all possible sorts!", ctx.prefix),
                                  color=discord.Color.dark_red())
        for country, i in zip(_list, range(1, len(_list))):
            top_embed.add_field(name=_("{0}: {1}", i, country["country"]),
                                value=format(int(country[_type.lower()]), ","))
        await ctx.send(embed=top_embed)


setup = TopCommands.setup
