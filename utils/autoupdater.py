# coding=utf-8
"""
Utility functions to take care of most of the parsing behind the autoupdater, to make it more logically sound,
if you will
"""
import datetime
import time
from copy import deepcopy, copy

import discord

from utils import embeds, graphs
from utils.async_helpers import wrap_in_async
from utils.ctx_class import MyContext
from utils.caching import TTLCache


graph_cache = TTLCache(82800)


async def continent(ctx: MyContext, name: str):
    embed = await embeds.advanced_stats_embed(await ctx.bot.worldometers_api.try_to_get_name(name),
                                              ctx=ctx)
    if embed is None:
        _ = await ctx.get_translate_function()
        await ctx.send(_("I'm having a issue with finding the country name here! Here's what I'm showing: {0}",
                         await ctx.bot.worldometers_api.try_to_get_name(name)))
        return None
    else:
        return embed


async def world(ctx: MyContext):
    return await continent(ctx, "world")


async def country(ctx: MyContext, name: str):
    return await continent(ctx, name)


async def state(ctx: MyContext, name: str):
    return await continent(ctx, name)


async def province(ctx: MyContext, name: str):
    n = await ctx.bot.jhucsse_api.try_to_get_name(name)
    today = datetime.date.today()
    today = today - datetime.timedelta(days=1)
    e = await embeds.basic_stats_embed(n, today)
    return e


async def custom(ctx: MyContext, custom_str: str):
    return NotImplemented


async def graph(ctx: MyContext, name: str):
    _ = await ctx.get_translate_function()
    name, log = name.split("_")
    log = True if log == "log" else False
    name = await ctx.bot.jhucsse_api.try_to_get_name(name)
    data = await ctx.bot.jhucsse_api.get_country_stats(name[1])
    buffer_name = f"{name[1].title() if name[1] else 'world'}_{'log' if log else 'lin'}"
    st = time.perf_counter_ns()
    graph_buffer = graph_cache.get(buffer_name)
    if not graph_buffer:
        cache_hit = False
        graph_buffer = await wrap_in_async(graphs.generate_line_plot, data, name[1].title() if name[1] else "world",
                                           logarithmic=log, thread_pool=True)
        graph_cache[buffer_name] = deepcopy(graph_buffer)
    else:
        graph_buffer = copy(graph_buffer)
        cache_hit = True
    et = time.perf_counter_ns()
    f = discord.File(graph_buffer, filename="image.png")
    tt = et - st
    e = discord.Embed(title=_("Graph for {0}", name[1].title() if name[1] else 'world'))
    e.set_footer(text=_("Took {0} seconds ({1} nanoseconds) to generate • Cache Status: {2}",
                        format(round(tt / 1000000000, 1), ","), format(tt, ","), "HIT" if cache_hit else "MISS"))
    e.set_image(url="attachment://image.png")
    await ctx.send(file=f, embed=e)