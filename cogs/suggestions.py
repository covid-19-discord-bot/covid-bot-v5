# coding=utf-8
import traceback
from typing import Optional

import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext

active_suggestions = {}


class SuggestionsCommands(Cog):
    @commands.command()
    async def suggest(self, ctx: MyContext, *suggestion):
        _ = await ctx.get_translate_function()
        suggestion = " ".join(suggestion)
        suggestion_embed = discord.Embed(title="Suggestion",
                                         description="By {ctx.author.mention}.\n"
                                                     "React with ✅ to vote for this suggestion, and ❌ to vote "
                                                     "against this suggestion.\n"
                                                     "0/0 can deny a suggestion by reacting with 🛑.\n")
        suggestion_embed.add_field(name="Suggestion", value=suggestion)
        try:
            suggestion_channel = self.bot.get_channel(681498131699073139)
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
        if payload.emoji.name == "🛑" and payload.channel_id == 681498131699073139:
            if payload.user_id in self.bot.owner_ids and payload.message_id in active_suggestions:
                denied_suggestion = discord.Embed(title="Denied Suggestion!",
                                                  description="This suggestion was denied by 0/0#0001."). \
                    add_field(name="Suggestion", value=active_suggestions[payload.message_id])
                chnl: discord.TextChannel = self.bot.get_channel(payload.channel_id)
                msg: discord.Message = await chnl.fetch_message(payload.message_id)
                await msg.edit(embed=denied_suggestion)
                await msg.clear_reactions()
            else:
                user: Optional[discord.User] = self.bot.get_user(payload.user_id)
                if user is not None:
                    await user.send("You don't have permission to deny this suggestion!")


setup = SuggestionsCommands.setup
