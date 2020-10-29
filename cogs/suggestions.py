# coding=utf-8
import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.bot_class import MyBot


def submit_error_message(self, exc: BaseException, doing: str, ctx: MyContext, bot: MyBot):
    error_channel = await bot.get_channel(771065447561953298)
    error_embed = discord.Embed(title=f"Fatal error while working on {doing}!",
                                description=f"```Guild details:\n"
                                            f"    ID: {ctx.guild.id}\n"
                                            f"    Name: {ctx.guild.name}\n\n"
                                            f"Channel details:\n"
                                            f"    ID: {ctx.channel.id}\n"
                                            f"    Name: {ctx.channel.name}\n\n"
                                            f"Invoking message details:\n"
                                            f"    ID: {ctx.message.id}\n\n"
                                            f"Author details:\n"
                                            f"    ID: {ctx.author.id}\n"
                                            f"    Name: {str(ctx.author)}\n\n"  # Quick way to get name#disc
                                )
    error_embed.add_field(name="Exception Name", value="")


class Template(Cog):
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


setup = Template.setup
