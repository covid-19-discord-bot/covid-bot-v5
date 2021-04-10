# coding=utf-8
import asyncio
import concurrent.futures
import datetime
from functools import partial
from typing import Optional

import arrow
import comodels
import discord
from discord.ext import commands, tasks
from numpy import ndarray

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db, DiscordUser

basic_queue = asyncio.Queue()
premium_queue = asyncio.Queue()
kill_pools = asyncio.Queue()

# why dicts? one reason: speed: they're a lot faster
text_commands = {"first": 1, "prev": 1, "next": 1, "last": 1, "exit": 1}
numerical_commands = {i: 1 for i in range(0, 32768)}
all_commands = {**text_commands, **numerical_commands}


class SimulationsDisabled(commands.CommandError):
    pass


# designed to be shadowed
def _(msg, *args, **kwargs):
    return msg.format(*args, **kwargs)


def check_if_enabled():
    async def pred(ctx):
        db_guild = await get_from_db(ctx.guild)
        if db_guild.disable_simulations:
            raise SimulationsDisabled()
        return True

    return commands.check(pred)


class FutureSimulations(Cog):
    @staticmethod
    async def parse_simulation_data_for_date(data: dict, date_to_parse: int, ctx: MyContext) -> Optional[discord.Embed]:
        _ = await ctx.get_translate_function()
        infected: ndarray = data['infected']
        if len(infected) < date_to_parse:
            return None
        recovered: ndarray = data['recovered']
        deaths: ndarray = data['deaths']
        data_embed = discord.Embed(color=discord.Color.dark_red(), title=_("Data for Day {0}", date_to_parse)). \
            add_field(name="Infected", value=str(round(infected[date_to_parse - 1]))). \
            add_field(name="Recovered", value=str(round(recovered[date_to_parse - 1]))). \
            add_field(name="Deaths", value=str(round(deaths[date_to_parse - 1])))
        return data_embed

    @commands.group(hidden=True, disabled=True)
    @commands.guild_only()
    @check_if_enabled()
    async def simulate(self, ctx: MyContext):
        """
        What's the trend going to be like?

        Basic members can only use existing data from a certain country.
        Premium members/guilds can set any data values they want, even if they're not based off a country.
        Expect weird things if you set the data values to something other than default.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help("simulate")

    # noinspection PyArgumentList
    @simulate.command()
    async def run(self, ctx: MyContext, ping_when_done: Optional[bool] = True):
        """
        Run the simulation you have set up. Will ping you when your simulation is complete.
        If ping_when_done is set to false, the bot will not ping you when the sim is complete.
        """
        _ = await ctx.get_translate_function()

        def agree(c):
            return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and c.message.content.lower() == "ok"

        terms_of_service = await ctx.send(_("**WARNING**\n"
                                            "This is not a scientific modeling system by any means, this purely exists "
                                            "for entertainment purposes. For actual advice, refer to your medical "
                                            "specialist. By agreeing to these terms, you agree not to hold 0/0#0001 "
                                            "liable for anything stemming from the use of this modeling system. Type "
                                            "`ok` within 15 seconds to agree to these terms."))
        try:
            await self.bot.wait_for("message", check=agree, timeout=15)
        except asyncio.TimeoutError:
            await terms_of_service.edit(content=_("Didn't get a response. To try again, do "
                                                  "`{0}{1}`.",
                                                  ctx.prefix, ctx.command.qualified_name))
            return
        if ping_when_done:
            await ctx.reply(_("I'll ping you when this is done, you can go do other stuff."))
        msg = await ctx.reply(_("Please wait, initializing..."))
        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        if ctx.guild is not None:
            db_guild = await get_from_db(ctx.guild)
        else:
            db_guild = None
        queue = premium_queue
        model_data = db_user.future_simulation
        if not model_data.is_set_up:
            await ctx.send(_("You haven't set up your simulation! Run `{0}simulate setup` to set your sim up!",
                             ctx.prefix))
            return
        sim_data = {"sim_class": comodels.PennDeath(N=model_data.population_size,
                                                    I=model_data.infected,
                                                    R=model_data.recoveries,
                                                    D=model_data.dead,
                                                    D_today=model_data.dead_today,
                                                    hosp_rate=model_data.hosp_rate,
                                                    icu_rate=model_data.icu_rate,
                                                    vent_rate=model_data.vent_rate,
                                                    death_rate=model_data.death_rate,
                                                    contact_reduction=model_data.contact_reduction,
                                                    t_death=model_data.t_death,
                                                    t_double=model_data.t_double,
                                                    beta_decay=model_data.beta_decay,
                                                    vent_los=model_data.vent_los,
                                                    hos_los=model_data.hosp_los,
                                                    icu_los=model_data.icu_los,
                                                    recover_time=model_data.recover_time,
                                                    birth_rate=0),
                    "time_to_simulate": model_data.time_to_simulate}
        data = {"id": msg.id,  # why spend CPU cycles on generating a random number when Discord makes a perfectly
                # fine one?
                "simulation": sim_data,
                "queue": asyncio.Queue(maxsize=1)}
        await msg.edit(content=_("Submitting your item to be processed..."))
        await queue.put(data)
        next_iter = (self.run_premium_simulations if is_premium else self.run_basic_simulations) \
                        .next_iteration or datetime.datetime.now()
        next_iter = arrow.get(next_iter)
        now = arrow.now()
        locale = await ctx.get_language_code()
        await msg.edit(content=_("Waiting for next run of simulation processor, which will happen {0}.",
                                 now.humanize(other=next_iter, locale=locale)))
        result = await data['queue'].get()  # this asynchronously blocks until the item is put on the queue
        if isinstance(result, Exception):
            if isinstance(result, MemoryError):
                message = _("Simulation failed: ran out of memory: retry with smaller values.")
            elif isinstance(result, ValueError):
                message = _("Simulation failed: had incorrect values passed to it: try with more reasonable values.")
            elif isinstance(result, concurrent.futures.BrokenExecutor):
                message = _("Simulation failed: process running the simulation has failed: ask a mod in the bot's "
                            "support server (find it via {0}) to run {1}.",
                            "`/invite`", "`/simulate restart_process_pool`")
            else:
                message = _("Simulation failed: had a unknown error: report ID ({0}) to 0/0#0001 to be fixed.",
                            msg.id)
            await msg.edit(content=message)
            await ctx.reply(message)
            return
        result: tuple
        infected: ndarray = result[0]['infected']
        recovered: ndarray = result[0]['recovered']
        deaths: ndarray = result[0]['dead']

        await msg.edit(content=_("Processed simulation!"))
        sim_details_embed = discord.Embed(title=_("Simulation Results"),
                                          description=_("Navigate using `next` to view the next day's stats, `prev` to "
                                                        "view the previous day's stats, `first` to jump to the first day "
                                                        "(tomorrow), and `last` to jump to the last day in your "
                                                        "simulation. Type a number to jump straight to that day. Type "
                                                        "`exit` to exit the paginator (for example, if you want to "
                                                        "modify sim data)."), color=discord.Color.dark_red())
        sim_details_embed.add_field(name=_("Total infections by end of simulation"), value=infected.max(axis=0))
        sim_details_embed.add_field(name=_("Total recoveries by end of simulation"), value=recovered.max(axis=0))
        sim_details_embed.add_field(name=_("Total deaths by end of simulation"), value=deaths.max(axis=0))
        stats_msg = await ctx.reply(_("Your simulation is ready: it will be available for 15 minutes."),
                                    embed=sim_details_embed)
        sim_results_msg = await ctx.send("\u0000")  # who knows if discord will take it, so
        # TODO: check if discord takes this ^
        current_page = 1
        first_iter = True
        while True:
            def pred(c: MyContext):
                return c.author.id == ctx.author.id and c.channel.id == ctx.channel.id and \
                       ctx.message.content.lower().strip() in all_commands

            try:
                msg_2: discord.Message = await self.bot.wait_for("message",
                                                                 check=pred,
                                                                 timeout=900 if first_iter else 120)
            except asyncio.TimeoutError:
                await stats_msg.edit(content=_("Your simulation has timed out. Request a new one with "
                                               "`{0}{1}`.", ctx.prefix, ctx.command.qualified_name))
                await sim_results_msg.delete()
                return
            cmd: str = msg_2.content.lower().strip()
            try:
                await msg_2.delete()
            except discord.Forbidden:
                await ctx.send(_("I now require the MANAGE MESSAGES permission. I've disabled this command until you "
                                 "give me this permission. If you'd prefer not to give me such a permission, the bot "
                                 "will still function, just with the simulation module disabled. Thanks in advance!"))
                db_guild.disable_simulations = True
                await db_guild.save()
                return
            old_page = current_page
            if cmd == "first":
                current_page = 1
            elif cmd == "last":
                current_page = model_data.time_to_simulate - 1
            elif cmd == "next":
                current_page += 1
            elif cmd == "prev":
                current_page -= 1
            elif cmd == "exit":
                return
            elif cmd.isdigit():
                cmd: int = int(cmd)
                current_page = cmd
            else:
                await ctx.send(_("Internal bot error. Try again."), delete_after=15)
                continue
            if not 0 < current_page <= model_data.time_to_simulate:
                await ctx.send(_("Out of bounds."), delete_after=5)
                current_page = old_page
                continue
            await stats_msg.edit(embed=await self.parse_simulation_data_for_date(result[0], current_page, ctx))

    @simulate.command()
    async def restart_process_pool(self, ctx: MyContext):
        _ = await ctx.get_translate_function()
        author: discord.Member = ctx.author
        for role in author.roles:
            if role.id == 686939763927678986:
                break
        else:
            await ctx.send(_("You aren't a mod in the bot's support server! You can't run this command. If simulations "
                             "are actually broken, ask a mod in the bot's support server (find it via {0}) to run this "
                             "command.", "`/invite`"))
            return
        await ctx.send(_("This could take up to 60 seconds, please wait..."))
        stats_msg = await ctx.send(_("Stopping simulation runners..."))
        self.run_basic_simulations.stop()
        self.run_premium_simulations.stop()
        for _ in range(2):
            await kill_pools.put("kill")
        await asyncio.sleep(5)  # wait for the processes to stop: shouldn't take longer than 5 seconds due to the
        # process pool being broken (presumably)
        self.run_basic_simulations.cancel()
        self.run_premium_simulations.cancel()  # if they still haven't stopped, cancel them
        await stats_msg.edit(content=_("Stopping broken process pools..."))
        self.bot.basic_process_pool.shutdown(wait=False)
        self.bot.premium_process_pool.shutdown(wait=False)
        await stats_msg.edit(content=_("Waiting 20 seconds for the final tasks to stop..."))
        await asyncio.sleep(20)
        await stats_msg.edit(content=_("Destroying pools..."))
        self.bot.basic_process_pool = None
        self.bot.premium_process_pool = None
        await stats_msg.edit(content=_("Creating new pools..."))
        self.bot.basic_process_pool = concurrent.futures.ProcessPoolExecutor(2)
        self.bot.premium_process_pool = concurrent.futures.ProcessPoolExecutor(4)
        await stats_msg.edit(content=_("Starting up simulation runners..."))
        self.run_basic_simulations.start()
        self.run_premium_simulations.start()
        await stats_msg.edit(content=_("Restarted pool sucessfully!"))

    @simulate.command()
    async def set_length(self, ctx: MyContext, days_to_simulate: int):
        _ = await ctx.get_translate_function()
        db_user = await get_from_db(ctx.author, as_user=True)
        if days_to_simulate > 157:
            await ctx.send(_("Simulation results are very inaccurate after 157 days. I have set the simulation length "
                             "to 157 days."))
            days_to_simulate = 157
        db_user.future_simulation.time_to_simulate = days_to_simulate
        await db_user.save()
        await ctx.send(_("Set simulation length to {0} days.", days_to_simulate))

    @simulate.command()
    async def set_country(self, ctx: MyContext, country: str):
        stats = self.bot.worldometers_api.get_country_stats(country)
        db_user = await get_from_db(ctx.author, as_user=True)  # TODO: add country setter
        db_user.future_simulation.is_set_up = True
        db_user.future_simulation.population_size = stats['population']

    @commands.Cog.listener()
    async def on_roles_update(self):
        pass  # TODO: figure out how this will work

    # Simulation processors here

    @tasks.loop(minutes=15)
    async def run_basic_simulations(self):
        self.bot.logger.info(f"Running simulations for basic members... {basic_queue.qsize()} simulations "
                             f"need to be processed.")
        loop = asyncio.get_running_loop()
        async with self.bot.basic_process_pool as pp:
            while True:
                try:
                    kill_pools.get_nowait()
                except asyncio.QueueEmpty:
                    pass
                else:
                    self.bot.logger.warning("Got a request to end the basic simulation runner early, shutting down!")
                    return
                try:
                    sim = basic_queue.get_nowait()
                except asyncio.QueueEmpty:
                    self.bot.logger.info("All simulations for basic members are done!")
                    break

                self.bot.logger.debug(f"Processing simulation ID {sim['id']}")
                try:
                    result = await loop.run_in_executor(pp, partial(sim['simulation']['sim_class'].sir(),
                                                                    sim['simulation']['time_to_simulate']))
                except Exception as e:
                    await sim['queue'].put(e)
                    self.bot.logger.exception(f"Simulation ID {sim['id']} failed to process.", exc_info=e)
                    continue
                await sim['queue'].put(result)
                self.bot.logger.debug(f"Processed simulation ID {sim['id']} sucessfully.")

    @tasks.loop(minutes=5)
    async def run_premium_simulations(self):
        self.bot.logger.info(f"Running simulations for premium members... {premium_queue.qsize()} simulations "
                             f"need to be processed.")
        loop = asyncio.get_running_loop()
        async with self.bot.premium_process_pool as pp:
            while True:
                try:
                    kill_pools.get_nowait()
                except asyncio.QueueEmpty:
                    pass
                else:
                    self.bot.logger.warning("Got a request to end the premium simulation runner early, shutting down!")
                    return
                try:
                    sim = premium_queue.get_nowait()
                except asyncio.QueueEmpty:
                    self.bot.logger.info("All simulations for premium members are done!")
                    break

                self.bot.logger.debug(f"Processing simulation ID {sim['id']}")
                try:
                    result = await loop.run_in_executor(pp, partial(sim['simulation']['sim_class'].sir(),
                                                                    sim['simulation']['time_to_simulate']))
                except Exception as e:
                    await sim['queue'].put(e)
                    self.bot.logger.exception(f"Simulation ID {sim['id']} failed to process.", exc_info=e)
                    continue
                await sim['queue'].put(result)
                self.bot.logger.debug(f"Processed simulation ID {sim['id']} sucessfully.")


setup = FutureSimulations.setup
