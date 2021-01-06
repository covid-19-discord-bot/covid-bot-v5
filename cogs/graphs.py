# coding=utf-8
import asyncio
import io
from copy import deepcopy, copy
from os import unlink

import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils import graphs
from utils.caching import TTLCache
from utils.async_helpers import wrap_in_async
import time

graphs.BASE_IMAGE_PATH = "/home/pi/covid_bot_beta/temp_data/plots"

graph_cache = TTLCache(82800)  # items expire after 23 hours


class GraphsCog(Cog):
    @commands.command()
    async def graphs(self, ctx: MyContext, *name: str):
        name = " ".join(name)
        _ = await ctx.get_translate_function()
        name = self.bot.jhucsse_api.try_to_get_name(name)
        if not name:
            await ctx.reply(_("Couldn't find that name. Try again, or use `{0}list` for help.",
                              ctx.prefix))
            return
        elif name[0] == "world":
            data = self.bot.jhucsse_api.global_historical_stats
        elif name[0] == "country":
            data = await self.bot.jhucsse_api.get_country_stats(name[1])
        elif name[0] == "province":
            data = await self.bot.jhucsse_api.get_province_stats(name[1])
        elif name[0] == "state":
            data = await self.bot.jhucsse_api.get_state_stats(name[1])["timeline"]
        elif name[0] == "continent":
            await ctx.reply(_("Continents are not supported, as historical data is not available."))
            return

        msg: discord.Message = await ctx.send(_("React with 📈 for a logarithmic graph.\n"
                                                "React with 📉 for a linear graph.\n"
                                                "This message expires after 30 seconds."))

        def predicate(r: discord.RawReactionActionEvent):
            return r.message_id == msg.id and r.user_id == ctx.author.id and (
                    r.emoji.name == "📈" or r.emoji.name == "📉")

        await msg.add_reaction("📈")
        await msg.add_reaction("📉")
        try:
            event: discord.RawReactionActionEvent = await self.bot.wait_for("raw_reaction_add",
                                                                            check=predicate, timeout=30)
        except asyncio.TimeoutError:
            await msg.edit(content=_("Timed out. Request a new message with `{0}graphs`", ctx.prefix))
            return
        else:
            await msg.edit(content=_("Please wait, this could take a few seconds..."))
            buffer_name = f"{name[1].title() if name[1] else 'world'}_{'log' if event.emoji.name == '📈' else 'lin'}"
        st = time.perf_counter_ns()
        graph_buffer = graph_cache.get(buffer_name)
        if not graph_buffer:
            cache_hit = False
            fp = await wrap_in_async(graphs.generate_line_plot, data,
                                     name[1].title() if name[1] else "world",
                                     logarithmic=event.emoji.name == "📈")
            with open(fp, "rb") as f:
                graph_buffer = io.BytesIO(f.read())
            unlink(fp)
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
        await msg.delete()
        await ctx.send(file=f, embed=e)

    @commands.has_role(686939763927678986)
    @commands.command()
    async def clear_cache(self, ctx: MyContext):
        global graph_cache
        graph_cache = TTLCache(82800)
        await ctx.reply("Cleared cache.")


setup = GraphsCog.setup
