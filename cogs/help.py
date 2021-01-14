# coding=utf-8
"""
Help command for the bot.
Credit for the framework goes to https://gist.github.com/InterStella0/b78488fb28cadf279dfd3164b9f0cf96
"""
from typing import Union

import discord
from discord.ext.commands import HelpCommand, Cooldown, BucketType, Command, Group, Context
from utils import MyBot, MyContext
from utils.cog_class import Cog


class BoatHelp(HelpCommand):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.command_attrs = {
            "cooldown": Cooldown(3, 5.0, BucketType.user),
            "name": "help"
        }

    def get_command_signature(self, command):
        return '{0}{1} {2}'.format(self.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        _ = await self.context.get_translate_function()
        embed = discord.Embed(title=_("Help"))
        if self.context.bot.description:
            embed.description = self.context.bot.description
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) + " - " + c.help for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_cog_help(self, cog: Cog):
        _ = await self.context.get_translate_function()
        embed = discord.Embed(title=cog.qualified_name,
                              description=cog.description)
        for command in cog.walk_commands():
            if isinstance(command, Command) and not command.hidden:
                embed.add_field(name=self.get_command_signature(command), value=command.help)
            elif isinstance(command, Group) and not command.hidden:
                embed.add_field(name=command.qualified_name, value=command.help)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_group_help(self, group: Group):
        _ = await self.context.get_translate_function()
        embed = discord.Embed(title=group.qualified_name,
                              description=group.description)
        for command in group.walk_commands():
            if isinstance(command, Command) and not command.hidden and command.parent == group:
                embed.add_field(name=self.get_command_signature(command), value=command.short_doc)
            elif isinstance(command, Group) and not command.hidden:
                embed.add_field(name=command.qualified_name, value=command.help)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        _ = await self.context.get_translate_function()
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name=_("Help"), value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name=_("Aliases"), value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def command_not_found(self, string):
        _ = await self.context.get_translate_function()
        return _("No command called {0} found.", string)

    async def subcommand_not_found(self, command: Union[Command, Group], string: str):
        _ = await self.context.get_translate_function()
        if isinstance(command, Group) and len(command.all_commands) > 0:
            return _("Command \"{0.qualified_name}\" has no subcommand named {1}", command, string)
        return _("Command \"{0.qualified_name}\" has no subcommands.", command)

    async def send_error_message(self, error):
        _ = await self.context.get_translate_function()
        embed = discord.Embed(title=_("Error"), description=error)
        channel = self.get_destination()
        await channel.send(embed=embed)

    # Required to make ctx.get_translate_function() work
    async def prepare_help_command(self, ctx: Union[Context, MyContext], command=None):
        if not isinstance(ctx, MyContext):
            self.context = await self.context.bot.get_context(ctx.message, cls=MyContext)
        else:
            self.context = ctx


class HelpCommand(Cog):
    @classmethod
    def setup(cls, bot: MyBot):
        bot.help_command = BoatHelp()
        return super().setup(bot)


setup = HelpCommand.setup
