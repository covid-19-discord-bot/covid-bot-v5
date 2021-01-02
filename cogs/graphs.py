# coding=utf-8
import asyncio
import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils import graphs
from utils.async_helpers import wrap_in_async
import time

graphs.BASE_IMAGE_PATH = "/home/pi/covid_bot_beta/temp_data/plots"


class GraphsCog(Cog):
    @commands.command()
    async def graphs(self, ctx: MyContext, name: str):
        _ = await ctx.get_translate_function()
        name = self.bot.jhucsse_api.try_to_get_name(name)
        if not name:
            await ctx.reply(_("Couldn't find that name. Try again, or use `{0}list` for help.",
                              ctx.prefix))
            return
        if name[0] == "world":
            data = self.bot.jhucsse_api.global_historical_stats
        elif name[0] == "country":
            data = await self.bot.jhucsse_api.get_country_stats(name[1])
        elif name[0] == "province":
            data = await self.bot.jhucsse_api.get_province_stats(name[1])
        elif name[0] == "state":
            data = await self.bot.jhucsse_api.get_state_stats(name[1])
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
        st = time.perf_counter_ns()
        fp = await wrap_in_async(graphs.generate_line_plot, data["timeline"], name[1].title(),
                                 logarithmic=event.emoji.name == "📈")
        et = time.perf_counter_ns()
        f = discord.File(fp, filename="image.png")
        tt = et - st
        e = discord.Embed(title=_("Graph for {0}", name[1].title()))
        e.set_footer(text=_("Took {0} seconds ({1}ns) to generate.", format(round(tt / 1000000000, 1), ","),
                            format(tt, ",")))
        e.set_image(url="attachment://image.png")
        await msg.delete()
        await ctx.send(file=f, embed=e)


setup = GraphsCog.setup
