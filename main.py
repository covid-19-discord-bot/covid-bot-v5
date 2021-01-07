# coding=utf-8
import asyncio
import uvloop
import discord
import statcord
from utils.config import load_config
from utils.bot_class import MyBot
from utils.models import init_db_connection
from pretty_help import PrettyHelp
import sentry_sdk
try:
    from blackfire import probe
except (ImportError, ModuleNotFoundError):
    blackfire = False
else:
    blackfire = True

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

config = load_config()

if blackfire:
    bf_config = config["auth"]["blackfire"]
    probe.initialize(**bf_config)
    probe.enable()

sentry_sdk.init(
    config["auth"]["sentry"]["sentry_url"],
    traces_sample_rate=1.0,

)

if config['database']['enable']:
    asyncio.ensure_future(init_db_connection(config['database']))

basic_intents = discord.Intents(guilds=True, messages=True, reactions=True)
bot = MyBot(description=config["bot"]["description"], intents=basic_intents,
            member_cache_flags=discord.MemberCacheFlags.from_intents(basic_intents),
            help_command=PrettyHelp())

bot.blackfire = blackfire

stcd = statcord.Client(bot, config["auth"]["statcord"]["token"])
stcd.start_loop()
bot.statcord = stcd  # best way i know of to make a global system

for cog_name in config["cogs"]["cog_reloader"]["cogs_to_load"]:
    try:
        bot.load_extension(cog_name)
        bot.logger.debug(f"{cog_name} loaded!")
    except Exception as e:
        bot.logger.exception(f'Failed to load extension {cog_name}\n{type(e).__name__}: {e}')

try:
    bot.run(config['auth']['discord']['token'])
finally:
    if blackfire:
        probe.disable()
        probe.end()


