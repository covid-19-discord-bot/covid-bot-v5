# coding=utf-8
import asyncio
from typing import Optional

import discord
from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext

active_suggestions = {}


class SuggestionsCommands(Cog):
    @commands.command()
    async def suggest(self, ctx: MyContext, *suggestion):
        """
        Suggest something new to be added to the bot!
        Be sure to react to your message to send it.
        """
        _ = await ctx.get_translate_function()

        msg = await ctx.reply(_("React to this message with 📥 within 10 seconds to send your reaction."))
        await msg.add_reaction("📥")
        def reaction_event(payload: discord.RawReactionActionEvent):
            return payload.message_id == msg.id and payload.user_id == ctx.author.id and \
                   ctx.channel.id == ctx.channel.id and payload.emoji.name == "📥"
        try:
            await self.bot.wait_for("raw_reaction_add", check=reaction_event, timeout=10)
        except asyncio.TimeoutError:
            await msg.clear_reaction("📥")
            await msg.edit(content="Timed out. Resend your suggestion.")
            return

        suggestion = " ".join(suggestion)
        description = "By %s.\nReact with ✅ to vote for this suggestion, and ❌ to vote against this suggestion.\n0/0 can deny a suggestion by reacting with 🛑.\n" % (ctx.author.mention)
        suggestion_embed = discord.Embed(title="Suggestion",
                                         description=description,
                                         color=discord.Color.dark_red())
        suggestion_embed.add_field(name="Suggestion", value=suggestion)
        try:
            suggestion_channel = self.bot.get_channel(796428867715596358)
            msg: discord.Message = await suggestion_channel.send(embed=suggestion_embed)
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
            await msg.add_reaction("🛑")
        except discord.HTTPException:
            await ctx.send(_("Failed to send suggestion due to a Discord error. Try again."))
        else:
            await ctx.send(_("Sent suggestion successfully."))
            active_suggestions[msg.id] = suggestion  # dicts are speed, also a nice way to store the suggestion

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.emoji.name == "🛑" and payload.channel_id == 796428867715596358:
            if payload.user_id in self.bot.owner_ids and payload.message_id in active_suggestions:
                denied_suggestion = discord.Embed(color=discord.Color.dark_red(), title="Denied Suggestion!",
                                                  description="This suggestion was denied by 0/0#0001."). \
                    add_field(name="Suggestion", value=active_suggestions[payload.message_id])
                channel: discord.TextChannel = self.bot.get_channel(payload.channel_id)
                msg: discord.Message = await channel.fetch_message(payload.message_id)
                await msg.edit(embed=denied_suggestion)
                await msg.clear_reactions()
            else:
                user: Optional[discord.User] = self.bot.get_user(payload.user_id)
                if user is not None:
                    await user.send("You don't have permission to deny this suggestion!")


setup = SuggestionsCommands.setup
