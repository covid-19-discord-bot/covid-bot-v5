# coding=utf-8
import discord
from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db
import json


class UtilsCommands(Cog):
    @commands.command()
    async def credits(self, ctx: MyContext):
        """
        A simple credits screen
        """
        credits_embed = discord.Embed(color=discord.Color.dark_green(), title="Credits")
        symphonic: discord.User = await self.bot.fetch_user(263128260009787392)
        zeroslashzero: discord.User = await self.bot.fetch_user(661660243033456652)
        eyes: discord.User = await self.bot.fetch_user(138751484517941259)
        symphonic_mention: str = symphonic.mention
        zeroslashzero_mention: str = zeroslashzero.mention
        eyes_mention: str = eyes.mention
        credits_embed.set_footer(text="current bot version: v5.0.0-alpha4")
        credits_embed.add_field(name="v3+ Creator", value=zeroslashzero_mention)
        credits_embed.add_field(name="Original Creator", value=symphonic_mention)
        credits_embed.add_field(name="Bot Framework", value=eyes_mention)
        credits_embed.add_field(name='API Providers', value="https://corona.lmao.ninja", inline=False)
        credits_embed.add_field(name="Creators of discord.py", value="https://discordpy.readthedocs.io", inline=False)
        await ctx.send(embed=credits_embed)

    @commands.command()
    async def invite(self, ctx: MyContext):
        invite_embed = discord.Embed(color=discord.Color.purple(), title="Invite Links")
        oauth_url = discord.utils.oauth_url(client_id=str(self.bot.user.id),
                                            permissions=discord.Permissions(read_messages=True, send_messages=True,
                                                                            embed_links=True),
                                            redirect_uri="https://discord.com/oauth2/authorized")
        invite_embed.add_field(name="Bot Invite Link", value=oauth_url)
        invite_embed.add_field(name="Discord Server Invite Link", value="https://discord.gg/v8qDQDc")
        await ctx.send(embed=invite_embed)

    @commands.command()
    async def stats(self, ctx: MyContext):
        with open("stats.json", "r") as sf:
            sd = json.loads(sf.read())
        stats_embed = discord.Embed(color=discord.Color.blue(), title="Bot Stats")
        stats_embed.add_field(name="Number of servers the bot is in", value=sd["guildCount"])
        stats_embed.add_field(name="Number of users the bot can see", value=sd["userCount"])
        try:
            stats_embed.add_field(name="Number of shards the bot is running on", value=sd["shardCount"])
        except KeyError:
            pass
        stats_embed.add_field(name="Total days since bot was created", value=sd["daysSinceCreation"])
        await ctx.send(embed=stats_embed)

    @commands.command(name="is_premium_guild")
    async def is_premium(self, ctx: MyContext):
        db_guild = await get_from_db(ctx.guild)
        premium = db_guild.is_premium
        msg = f"This guild ({ctx.guild.name}, ID `{ctx.guild.id}`) is "
        if premium:
            msg += " a "
        else:
            msg += " not a "
        msg += "premium guild. "
        if premium:
            msg += "<3 from 0/0#0001!"
        else:
            msg += "To get a few perks and 0/0#0001's unconditional love, check out the `/donate` command!"
        await ctx.send(msg)

    @commands.command()
    async def ping(self, ctx: MyContext):
        """
        Check that the bot is online, and give the latency between the bot and discord servers.
        """
        _ = await ctx.get_translate_function()

        t_1 = time.perf_counter()
        await ctx.trigger_typing()  # tell Discord that the bot is "typing", which is a very simple request
        t_2 = time.perf_counter()
        time_delta = round((t_2 - t_1) * 1000)  # calculate the time needed to trigger typing
        await ctx.send(_("Pong. — Time taken: {miliseconds}ms", miliseconds=time_delta))  # send a message telling the
        # user the calculated ping time


setup = UtilsCommands.setup


'''
@commands.command()
@commands.has_guild_permissions(administrator=True)
async def claim(ctx):
    if ctx.message.guild is None:
        await ctx.send(
            'We\'re in a private DM channel: head to a server where you\'re a admin with this bot and try again!')
        return
    for member in ctx.message.guild.members:
        if member.id == 675390513020403731:
            await ctx.send('I\'ve detected the non-beta version of the bot in this server! Remove that bot to be able '
                           'to claim your beta tester role.')
            return
    botGuild = bot.get_guild(675390855716274216)
    betaRole = botGuild.get_role(723645816245452880)
    for member in botGuild.members:
        if member.id == ctx.author.id:
            member.add_roles(betaRole)
            await ctx.send("You are now a beta tester!")
            return
    await ctx.send("You don't seem to be part of the bot's support server. Try joining it and trying again: `/invite`")
'''
