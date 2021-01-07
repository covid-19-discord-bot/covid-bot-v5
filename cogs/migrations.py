# coding=utf-8
"""
Export data from v5.2.x and import it into v5.3.0
"""
import json

from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import *


class Template(Cog):
    @commands.command()
    @commands.is_owner()
    async def export_old_data(self, ctx: MyContext):
        updaters = []
        async for db_channel in DiscordChannel.filter(autoupdater__already_set=True):
            updaters.append({"country": db_channel.autoupdater.country_name,
                             "delay": db_channel.autoupdater.delay,
                             "discord_id": db_channel.discord_id})
        with open("v5.2.0_data.json", "w") as f:
            json.dump(updaters, f)
        await ctx.reply("Dumped data to `v5.2.0_data.json`. Run `/import_old_data` to load it.")

    @commands.command()
    @commands.is_owner()
    async def import_old_data(self, ctx: MyContext):
        with open("v5.2.0_data.json", "r") as f:
            data = json.load(f)
        try:
            await ctx.send("Loading {0} total updaters...".format(len(data)))
        except discord.DiscordException:  # discord exceptions should NOT crash the bot
            pass
        for channel in data:
            try:
                discord_channel = self.bot.get_channel(channel["discord_id"]) or \
                                  self.bot.fetch_channel(channel["discord_id"])
            except discord.DiscordException:
                try:
                    await ctx.send("Skipping channel with Discord ID {0}...".format(channel["discord_id"]))
                except discord.DiscordException:
                    self.bot.logger.info("Skipping channel with Discord ID {0}...".format(channel["discord_id"]))
                continue
            else:
                if discord_channel is None:
                    try:
                        await ctx.send("Skipping channel with Discord ID {0}...".format(channel["discord_id"]))
                    except discord.DiscordException:
                        self.bot.logger.info("Skipping channel with Discord ID {0}...".format(channel["discord_id"]))
                    continue
            db_channel = await get_from_db(discord_channel)
            if db_channel["country"] == "OT":
                updater_type = AutoupdateTypes.world
            elif len(db_channel["country"]) == 2:
                updater_type = AutoupdateTypes.country
            else:
                updater_type = AutoupdateTypes.continent
            autoupdater_data = AutoupdaterData(discord_id=channel["discord_id"], delay=channel["delay"],
                                               already_set=True, country_name=channel["country"], type=updater_type)
            await autoupdater_data.save()
            await db_channel.autoupdater.add(autoupdater_data)
            await db_channel.save()
            try:
                await ctx.send("Done channel with Discord ID {0}.".format(channel["discord_id"]))
            except discord.DiscordException:
                self.bot.logger.info("Done channel with Discord ID {0}.".format(channel["discord_id"]))
        try:
            await ctx.send("Done all channels.")
        except discord.DiscordException:
            self.bot.logger.info("Done all channels.")


setup = Template.setup
