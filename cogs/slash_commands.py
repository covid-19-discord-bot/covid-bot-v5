# coding=utf-8
import datetime
from datetime import date
import discord
from discord.ext import commands
from cogs.error_handling import submit_error_message
from utils import embeds, api
from utils.cog_class import Cog
from utils.ctx_class import MyContext

slash_commands = {
    "covid":
        {
            "name": "covid",
            "description": "COVID-19 stats for anything you want!",
            "options": [
                {
                    "name": "world",
                    "description": "COVID-19 stats for the world",
                    "type": 1,
                    "options": []
                },
                {
                    "name": "country",
                    "description": "COVID-19 stats for a country",
                    "type": 1,
                    "options": [
                        {
                            "name": "country_name",
                            "description": "the name of the country you want stats for",
                            "type": 3,
                            "required": True,
                            "choices": []
                        }
                    ]
                },
                {
                    "name": "province",
                    "description": "COVID-19 stats for a province",
                    "type": 1,
                    "options": [
                        {
                            "name": "province_name",
                            "description": "the name of the province you want stats for",
                            "type": 3,
                            "required": True,
                            "choices": []
                        }
                    ]
                },
                {
                    "name": "state",
                    "description": "COVID-19 stats for a US state",
                    "type": 1,
                    "options": [
                        {
                            "name": "state_name",
                            "description": "the name of the province you want stats for",
                            "type": 3,
                            "required": True,
                            "choices": []
                        }
                    ]
                },
                {
                    "name": "continent",
                    "description": "COVID-19 stats for a continent",
                    "type": 1,
                    "options": [
                        {
                            "name": "continent_name",
                            "description": "the name of the continent you want stats for",
                            "type": 3,
                            "required": True,
                            "choices": [
                                {'name': 'North America', 'value': 'North America'},
                                {'name': 'Asia', 'value': 'Asia'},
                                {'name': 'South America', 'value': 'South America'},
                                {'name': 'Europe', 'value': 'Europe'},
                                {'name': 'Africa', 'value': 'Africa'},
                                {'name': 'Australia/Oceania', 'value': 'Australia/Oceania'}
                            ]
                        }
                    ]
                }
            ]
        }
}


class SlashCommands(Cog):
    @commands.command()
    async def submit_slash_commands(self, ctx: MyContext):
        guild: discord.Guild = ctx.guild
        self.bot.remove_command("covid")
        await guild.create_application_command(slash_commands["covid"])
        await self.bot.create_slash_command(slash_commands["covid"])
        await ctx.reply("Submitted commands.")

    # noinspection PyTypeChecker
    @commands.Cog.listener()
    async def on_interaction(self, data: discord.Interaction):
        print("fired slash command")
        """
        # trying to trick statcord... will this work?
        ctx = commands.Context()
        ctx.author.id = data.member.id
        ctx.command.name = data.name
        self.bot.statcord.command_run(ctx)
        """
        try:
            if data.name == "covid":
                for option in data.options:
                    if option.name == "world":
                        await data.send(embeds=[await embeds.advanced_stats_embed(("world", None),
                                                                                  bot=self.bot)],
                                        type=discord.InteractionResponseType.channel_message_with_source)
                    elif option.name == "continent":
                        continent_name = [i for i in option.options if i.name == "continent_name"][0]
                        try:
                            await data.send(
                                embeds=[await embeds.advanced_stats_embed(("continent", continent_name.value),
                                                                          bot=self.bot)],
                                type=discord.InteractionResponseType.channel_message_with_source)
                        except TypeError:
                            await data.send("Not a valid continent name!",
                                            type=discord.InteractionResponseType.channel_message_with_source)
                    elif option.name == "country":
                        country_name = [i for i in option.options if i.name == "country_name"][0]
                        try:
                            await data.send(embeds=[await embeds.advanced_stats_embed(("country", country_name.value),
                                                                                      bot=self.bot)],
                                            type=discord.InteractionResponseType.channel_message_with_source)
                        except TypeError:
                            await data.send("Not a valid country name!",
                                            type=discord.InteractionResponseType.channel_message_with_source)
                    elif option.name == "province":
                        country_name = [i for i in option.options if i.name == "province_name"][0]
                        today = datetime.date.today()
                        today = today - datetime.timedelta(days=1)
                        try:
                            await data.send(embeds=[await embeds.basic_stats_embed(("province", country_name.value),
                                                                                   today=today, bot=self.bot)],
                                            type=discord.InteractionResponseType.channel_message_with_source)
                        except api.BaseAPIException:
                            await data.send("Not a valid province name!",
                                            type=discord.InteractionResponseType.channel_message_with_source)
                        except AttributeError:
                            await data.send(f"I can't find stats for today! I'm currently trying to find stats for "
                                            f"{today!s}.",
                                            type=discord.InteractionResponseType.channel_message_with_source)
                    elif option.name == "state":
                        state_name = [i for i in option.options if i.name == "state_name"][0]
                        try:
                            await data.send(embeds=[await embeds.advanced_stats_embed(("state", state_name.value),
                                                                                      bot=self.bot)],
                                            type=discord.InteractionResponseType.channel_message_with_source)
                        except TypeError:
                            await data.send("Not a valid country name!",
                                            type=discord.InteractionResponseType.channel_message_with_source)
        except Exception as e:
            if isinstance(e, RuntimeError) and e.args[0] == \
                    "The bot hasn't been set up yet! Ensure bot.async_setup is called ASAP!":
                message = "The bot's still setting up, please wait a few minutes and try again!"
            else:
                await submit_error_message(e, "running slash command", self.bot, None)
                message = "There was an error running the specified command‽ This error has been logged."
            # be sure to make the command not appear if a error happened!
            await data.send(message, type=discord.InteractionResponseType.channel_message_with_source)


setup = SlashCommands.setup
