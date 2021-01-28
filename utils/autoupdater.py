# coding=utf-8
"""
Utility functions to take care of most of the parsing behind the autoupdater, to make it more logically sound,
if you will
"""
from utils import embeds
from utils.ctx_class import MyContext


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


country = state = continent
