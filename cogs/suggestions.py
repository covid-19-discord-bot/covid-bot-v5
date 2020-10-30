# coding=utf-8
import traceback

import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class SuggestionsCommands(Cog):
    @commands.command()
    async def suggest(self, ctx: MyContext, *suggestion):
        suggestion = " ".join(suggestion)
        suggestion_embed = discord.Embed(title="Suggestion",
                                         description=f"By {ctx.author.mention}.\n"
                                                     f"React with ✅ to vote for this suggestion, and ❌ to vote "
                                                     f"against this suggestion.\n"
                                                     f"{suggestion}")
        try:
            suggestion_channel = self.bot.get_channel(681498131699073139)
            msg: discord.Message = await suggestion_channel.send(embed=suggestion_embed)
            await msg.add_reaction("✅")
            await msg.add_reaction("❌")
        except discord.HTTPException as e:
            await ctx.send("Failed to send suggestion due to a Discord error. Try again.")
        else:
            await ctx.send("Sent suggestion sucessfully.")

    @commands.Cog.listener()
    async def on_error(self, ctx: MyContext):
        pass


setup = SuggestionsCommands.setup
