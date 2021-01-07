# coding=utf-8
import asyncio
import io
import time
from copy import deepcopy, copy
from os import unlink
from typing import Tuple, Optional, Callable

import discord
from discord.ext import commands

from utils import graphs
from utils.async_helpers import wrap_in_async
from utils.caching import TTLCache
from utils.cog_class import Cog
from utils.ctx_class import MyContext

graphs.BASE_IMAGE_PATH = "/home/pi/covid_bot_beta/temp_data/plots"

graph_cache = TTLCache(82800)  # items expire after 23 hours


class GraphsCog(Cog):
    @commands.group()
    @commands.cooldown(1, 10, type=commands.BucketType.member)
    @commands.max_concurrency(10, commands.BucketType.default)  # 10 is a good balance between CPU and
    # concurrency/frustration
    async def graphs(self, ctx: MyContext):
        """
        Fancy, dark mode graphs for any province or state or country, and the world!
        If a name contains spaces, it must be wrapped in quotes.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help("graphs")

    async def process_graphs(self, ctx: MyContext, name: Tuple[Optional[str]], data, _: Callable,
                             log: Optional[bool] = None):
        if log is None:
            msg: discord.Message = await ctx.reply(_("React with 📈 for a logarithmic graph.\n"
                                                     "React with 📉 for a linear graph.\n"
                                                     "This message expires after 10 seconds."))

            def predicate(r: discord.RawReactionActionEvent):
                return r.message_id == msg.id and r.user_id == ctx.author.id and (
                        r.emoji.name == "📈" or r.emoji.name == "📉")

            await msg.add_reaction("📈")
            await msg.add_reaction("📉")
            try:
                event: discord.RawReactionActionEvent = await self.bot.wait_for("raw_reaction_add",
                                                                                check=predicate, timeout=10)
            except asyncio.TimeoutError:
                await msg.edit(content=_("Timed out. Request a new message with `{0}graphs`", ctx.prefix))
                return
            log = event.emoji.name == '📈'
            await msg.edit(content=_("Please wait, this could take a few seconds..."))
        else:
            msg = await ctx.reply(_("Please wait, this could take a few seconds..."))
        buffer_name = f"{name[1].title() if name[1] else 'world'}_{'log' if log else 'lin'}"
        st = time.perf_counter_ns()
        graph_buffer = graph_cache.get(buffer_name)
        if not graph_buffer:
            cache_hit = False
            fp = await wrap_in_async(graphs.generate_line_plot, data,
                                     name[1].title() if name[1] else "world",
                                     logarithmic=log)
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
        await ctx.send(file=f, embed=e)
        if msg:
            await msg.delete()

    @graphs.command()
    async def world(self, ctx: MyContext, log: Optional[bool] = None):
        """
        Graphs for the world.
        Pass True as the second argument to skip the reaction menu and go straight to graph creation, and generate a
        logarithmic graph. If the 2nd argument is False, it will instead generate a linear graph.
        """
        _ = await ctx.get_translate_function()
        name = await self.bot.jhucsse_api.try_to_get_name("world")
        data = self.bot.jhucsse_api.global_historical_stats
        await self.process_graphs(ctx, name, data, _, log)

    @graphs.command()
    async def country(self, ctx: MyContext, name: str, log: Optional[bool] = None):
        """
        Graphs for any given country.
        If the country name contains a space, wrap it in quotes.
        Pass True as the second argument to skip the reaction menu and go straight to graph creation, and generate a
        logarithmic graph. If the 2nd argument is False, it will instead generate a linear graph.
        """
        _ = await ctx.get_translate_function()
        name = await self.bot.jhucsse_api.try_to_get_name(name)
        if name is None:
            cmd_usage = f"`{ctx.prefix}list`"
            await ctx.reply(_("That isn't a valid name! Check out {0} for a list of all names I can get data for!",
                              cmd_usage))
        elif name[0] != "country":
            await ctx.reply(_("I found a {0} instead of a country!", name[0]))
        else:
            data = await self.bot.jhucsse_api.get_country_stats(name[1])
            await self.process_graphs(ctx, name, data["timeline"], _, log)

    @graphs.command()
    async def province(self, ctx: MyContext, name: str, log: Optional[bool] = None):
        """
        Graphs for any given province. US states are not supported here, see the states subcommand.
        If the province name contains a space, wrap it in quotes.
        Pass True as the second argument to skip the reaction menu and go straight to graph creation, and generate a
        logarithmic graph. If the 2nd argument is False, it will instead generate a linear graph.
        """
        _ = await ctx.get_translate_function()
        name = await self.bot.jhucsse_api.try_to_get_name(name)
        if name is None:
            cmd_usage = f"`{ctx.prefix}list`"
            await ctx.reply(_("That isn't a valid name! Check out {0} for a list of all names I can get data for!",
                              cmd_usage))
        elif name[0] != "province":
            cmd_usage = f"`{ctx.prefix}graphs {name[0]}`"
            await ctx.reply(_("I found a {0} instead of a province! Try {1} instead.", name[0], cmd_usage))
        else:
            data = await self.bot.jhucsse_api.get_province_stats(name[1])
            await self.process_graphs(ctx, name, data["timeline"], _, log)

    @graphs.command()
    async def state(self, ctx: MyContext, name: str, log: Optional[bool] = None):
        """
        Graphs for any given US state.
        If the state name contains a space, wrap it in quotes.
        Pass True as the second argument to skip the reaction menu and go straight to graph creation, and generate a
        logarithmic graph. If the 2nd argument is False, it will instead generate a linear graph.
        """
        _ = await ctx.get_translate_function()
        name = await self.bot.jhucsse_api.try_to_get_name(name)
        if name is None:
            cmd_usage = f"`{ctx.prefix}list`"
            await ctx.reply(_("That isn't a valid name! Check out {0} for a list of all names I can get data for!",
                              cmd_usage))
        elif name[0] != "state":
            cmd_usage = f"`{ctx.prefix}graphs {name[0]}`"
            await ctx.reply(_("I found a {0} instead of a state! Try {1} instead.", name[0], cmd_usage))
        else:
            data = await self.bot.jhucsse_api.get_state_stats(name[1])
            await self.process_graphs(ctx, name, data["timeline"], _, log)

    @graphs.command()
    async def continent(self, ctx: MyContext):
        """
        Will not send anything. Only exists to let users know graphs are not available for continents.
        """
        await ctx.reply("Graphs are not supported with continents as the data is simply not available!")

    @commands.has_role(686939763927678986)
    @commands.command()
    async def clear_cache(self, ctx: MyContext):
        global graph_cache
        graph_cache = TTLCache(82800)
        await ctx.reply("Cleared cache.")


setup = GraphsCog.setup
