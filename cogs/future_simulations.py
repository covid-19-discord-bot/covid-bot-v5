# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
import asyncio
import time
import discord
from discord.ext import commands
from covid_machine_learning.ml_models.async_generators import AsyncModelGenerator
from utils.models import DiscordUser, get_from_db, FutureSimulations
from utils.bot_class import MyBot
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class FutureSimulationsCog(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.ml_model_gen = AsyncModelGenerator()

    @commands.group()
    async def simulate(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("simulate")

    @simulate.command(name="setup")
    async def _setup(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        db_user.future_simulation.is_set_up = True
        await db_user.future_simulation.save()
        await db_user.save()
        cmd_usage = f"{ctx.prefix}simulate settings"
        await ctx.reply(_("Set up your simulation to default values. Edit them with the {0} commands.", cmd_usage))

    @simulate.group()
    async def settings(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("simulate settings")

    @settings.command()
    async def country_name(self, ctx: MyContext, country_name: str):
        _ = await ctx.get_translate_function()
        if len(country_name) != 3:
            await ctx.reply(_("ISO3 codes are always 3 characters long! If you're trying to get the world, try {0}.",
                              "`WRL`"))
            return

        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        db_user.future_simulation.country_name = country_name
        await db_user.future_simulation.save()
        await db_user.save()
        await ctx.reply(_("Country name for simulation set to {0}.", country_name))

    @settings.command()
    async def time(self, ctx: MyContext, delay: int):
        _ = await ctx.get_translate_function()
        if delay > 1095:  # TODO: actually implement vote credit bypass
            await ctx.reply(_("3 years is the upper limit on simulation length."))
            return

        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        db_user.future_simulation.time_to_simulate = delay
        await db_user.future_simulation.save()
        await db_user.save()
        await ctx.reply(_("Simulation time set to {0} days.", delay))

    @simulate.group()
    async def templates(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("simulate templates")

    @simulate.command()
    async def run(self, ctx: MyContext):
        """
        Run your set up simulation.
        """
        _ = await ctx.get_translate_function()

        def agree(c):
            return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and c.content.lower() == "ok"

        terms_of_service = await ctx.send(_("**WARNING**\n"
                                            "This is not a scientific modeling system by any means, this purely exists "
                                            "for entertainment purposes. For actual advice, refer to your medical "
                                            "specialist. By agreeing to these terms, you agree not to hold 0/0#0001 "
                                            "liable for anything stemming from the use of this modeling system. Type "
                                            "`ok` within 15 seconds to agree to these terms."))
        try:
            m1 = await self.bot.wait_for("message", check=agree, timeout=15)
        except asyncio.TimeoutError:
            cmd_usage = f"`{ctx.prefix}{ctx.command.qualified_name}`"
            await terms_of_service.edit(content=_("Didn't get a response. To try again, do {0}.", cmd_usage))
            return
        else:
            await terms_of_service.delete()
            try:
                await m1.delete()
            except (discord.Forbidden, discord.NotFound):
                pass

        msg = await ctx.reply(_("Please wait, initializing..."))
        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        if not db_user.future_simulation.is_set_up:
            cmd_usage = f"`{ctx.prefix}simulate setup`"
            await ctx.send(_("You haven't set up your simulation! Run {0} to set your simulation up!",
                             cmd_usage))
            return
        await msg.edit(content=_("Running simulation..."))
        st = time.perf_counter_ns()
        ret_data = {}
        for i in ["total_cases", "total_deaths"]:
            j = await self.ml_model_gen.async_predict_model(db_user.future_simulation.country_name, i,
                                                            db_user.future_simulation.time_to_simulate,
                                                            just_last=True)
            if j is None:
                await msg.edit(content=_("Invalid country name! Try again, making sure the ISO3 code you passed is "
                                         "correct! For the world, the code is {0}.", "`WRL`"))
                return
            ret_data[i] = j
        et = time.perf_counter_ns()
        tt = et - st

        e = discord.Embed(title=_("Results after {0} days", db_user.future_simulation.time_to_simulate),
                          description=_("More features will be available later: join the support server for updates "
                                        "when new features are released!"), color=discord.Color.dark_red())
        e.add_field(name=_("Total Cases"), value=format(ret_data["total_cases"], ","))
        e.add_field(name=_("Total Deaths"), value=format(ret_data["total_deaths"], ","))
        await msg.edit(embed=e, content=_("Took {0} seconds ({1}ns) to run.",
                                          format(round(tt/1000000000, 2), ","), format(tt, ",")))


setup = FutureSimulationsCog.setup
