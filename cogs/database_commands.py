"""
Some example of commands that can be used to interact with the database.
"""
import secrets
from typing import Optional

import discord
from discord.ext import commands
from discord.utils import escape_markdown, escape_mentions

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db


class DatabaseCommands(Cog):
    @commands.group()
    @commands.has_permissions(manage_guild=True)
    async def settings(self, ctx: MyContext):
        """
        Commands to view and edit settings
        """
        if not ctx.invoked_subcommand:
            await ctx.send_help(ctx.command)

    @settings.command()
    async def prefix(self, ctx: MyContext, new_prefix: Optional[str] = None):
        """
        Change/view the server prefix.

        Note that some prefixes are global and can't be edited.
        """
        _ = await ctx.get_translate_function()
        db_guild = await get_from_db(ctx.guild)
        if new_prefix:
            db_guild.prefix = new_prefix
        await db_guild.save()
        if db_guild.prefix:
            await ctx.send(_("The server prefix is set to `{0}`.",
                             escape_mentions(escape_markdown(db_guild.prefix))))
        else:
            await ctx.send(_("There is no specific prefix set for this guild."))

    @settings.command()
    async def language(self, ctx: MyContext, language_code: Optional[str] = None):
        """
        Change/view the server language.

        Specify the server language as a 2/5 letters code. For example, if you live in France, you'd use fr or fr_FR.
        In Québec, you could use fr_QC.
        """
        db_guild = await get_from_db(ctx.guild)
        if language_code:
            db_guild.language = language_code
        await db_guild.save()

        _ = await ctx.get_translate_function()
        if db_guild.language:
            await ctx.send(_("The server language is now set to `{0}`.",
                             escape_mentions(escape_markdown(db_guild.language))))

            # Do not translate
            await ctx.send(f"If you wish to go back to the default, english language, use "
                           f"`{ctx.prefix}{ctx.command.qualified_name} en`")
        else:
            await ctx.send(_("There is no specific language set for this guild."))

    @settings.command()
    async def enable_tips(self, ctx: MyContext, enabled: Optional[bool] = True):
        db_guild = await get_from_db(ctx.guild)
        _ = await ctx.get_translate_function()
        if enabled is None:
            if db_guild.enable_tips:
                await ctx.reply(_("Tips are currently enabled for this guild."))
            else:
                await ctx.reply(_("Tips are currently disabled for this guild."))
        else:
            db_guild.enable_tips = enabled
            await db_guild.save()
            if enabled:
                await ctx.reply(_("Enabled tips for this guild."))
            else:
                await ctx.reply(_("Disabled tips for this guild."))

    @settings.command()
    async def api_key(self, ctx: MyContext, action: str):
        """
        Manage your channel's API key.
        Pass one of the following arguments to manage the key.
        "view": DMs you your API key.
        "revoke": Revokes the API key. **DOES NOT generate a new one!** Use "new" for that.
        "new": Revokes the API key, if one exists, generates a new one, and DMs it to you.
        """
        db_channel = await get_from_db(ctx.channel)
        _ = await ctx.get_translate_function()
        if db_channel.disabled_api:
            await ctx.reply(_("The API has been disabled for this channel. To restore your permissions, contact "
                              "0/0#0001 on the official support server."))
            return
        if action.lower() in ("view", "see"):
            await ctx.author.send(db_channel.api_key)
            await ctx.reply(_("DMed your API key to you."))
        elif action.lower() in ("revoke", "delete"):
            db_channel.api_key = "0"*32
            await ctx.reply(_("Revoked/deleted API key."))
        elif action.lower() in ("regenerate", "new", "generate"):
            api_key = secrets.token_urlsafe(32)
            while api_key != "0"*32:  # the chances of it actually being that is 1 in 2.135987036×10⁹⁶, but if that
                # happens... that's a first
                api_key = secrets.token_urlsafe(32)
            db_channel.api_key = api_key
            await ctx.author.send(api_key)
            await ctx.reply(_("DMed your new API key to you."))
        await db_channel.save()

    @commands.command()
    @commands.is_owner()
    async def disable_api(self, ctx: MyContext, channel: discord.TextChannel):
        _ = await ctx.get_translate_function()
        db_channel = await get_from_db(channel)
        db_channel.disabled_api = True
        await db_channel.save()
        await ctx.reply(_("Disabled the API for {0}.", channel.name))


setup = DatabaseCommands.setup
