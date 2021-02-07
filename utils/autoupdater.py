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
from utils.custom_updaters import InvalidKeyError
from utils.maps import map_identifiers

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
        return {"embed": embed}


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
    return {"embed": e}


async def custom(ctx: MyContext, custom_str: str):
    custom_updater = ctx.bot.custom_updater_helper
    try:
        custom_str = await custom_updater.parse(custom_str)
    except InvalidKeyError as e:
        _ = await ctx.get_translate_function()
        return {"content": _("Invalid key ({0}) found in the updater, requires fixing!", str(e))}
    else:
        return {"content": custom_str}


async def graph(ctx: MyContext, name: str):
    _ = await ctx.get_translate_function()
    name, log = name.split("_")
    log = True if log == "log" else False
    name = await ctx.bot.jhucsse_api.try_to_get_name(name)
    if name[0] == "world":
        data = ctx.bot.jhucsse_api.global_historical_stats
    elif name[0] == "country":
        data = await ctx.bot.jhucsse_api.get_country_stats(name[1])
    elif name[0] == "province":
        data = await ctx.bot.jhucsse_api.get_province_stats(name[1])
    elif name[0] == "state":
        data = await ctx.bot.jhucsse_api.get_state_stats(name[1])
    else:
        return {"content": "internal bot error"}
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
    return {"embed": e, "file": f}


async def maps(ctx: MyContext, name: str):
    _ = await ctx.get_translate_function()
    map_embed = discord.Embed(title=_("Map for {0}", map_identifiers[name][1]))
    try:
        map_buffer = await wrap_in_async(ctx.bot.maps_api.get_map, name, thread_pool=True)
    except KeyError:
        return {"content": _("Bot still setting up...")}
    img_file = discord.File(map_buffer, filename="map.png")
    map_embed.set_image(url="attachment://map.png")
    return {"embed": map_embed, "file": img_file}
