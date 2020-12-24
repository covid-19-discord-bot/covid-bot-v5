# coding=utf-8
import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils import embeds
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
        if data.name == "covid":
            for option in data.options:
                if option.name == "world":
                    await data.send(embeds=[await embeds.advanced_stats_embed(("world", None),
                                                                              bot=self.bot)],
                                    type=discord.InteractionResponseType.channel_message_with_source)
                elif option.name == "continent":
                    continent_name = [i for i in option.options if i.name == "continent_name"][0]
                    try:
                        await data.send(embeds=[await embeds.advanced_stats_embed(("continent", continent_name.value),
                                                                                  bot=self.bot)],
                                        type=discord.InteractionResponseType.channel_message_with_source)
                    except TypeError:
                        await data.send("Not a valid continent name!",
                                        type=discord.InteractionResponseType.channel_message_with_source)
                elif option.name == "country":
                    continent_name = [i for i in option.options if i.name == "country_name"][0]
                    try:
                        await data.send(embeds=[await embeds.advanced_stats_embed(("country", continent_name.value),
                                                                                  bot=self.bot)],
                                        type=discord.InteractionResponseType.channel_message_with_source)
                    except TypeError:
                        await data.send("Not a valid country name!",
                                        type=discord.InteractionResponseType.channel_message_with_source)
                elif option.name == "province":
                    await data.send("not implemented",
                                    type=discord.InteractionResponseType.channel_message_with_source)


setup = SlashCommands.setup
