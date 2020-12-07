# coding=utf-8
import discord
from discord.ext import commands
from discord.ext.commands import BucketType

from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db
from typing import Optional, Union


class PremiumSettings(Cog):
    @commands.command()
    @commands.cooldown(1, 300, BucketType.user)
    async def is_premium(self, ctx: MyContext, user_or_guild: Optional[bool]):
        if user_or_guild:
            db_item = await get_from_db(ctx.author)
            msg = "This user is "
        else:
            db_item = await get_from_db(ctx.guild)
            msg = "This guild is "
        msg += "{'a' if db_item.is_premium else 'not a'} premium {'user' if user_or_guild else 'guild'}."
        await ctx.send(msg)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def set_premium(self, ctx: MyContext, item: Union[discord.Member, discord.Guild]):
        db_item = await get_from_db(item)
        db_item.is_premium = True
        await db_item.save()
        await ctx.send("Set item as premium.")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unset_premium(self, ctx: MyContext, item: Union[discord.Member, discord.Guild]):
        db_item = await get_from_db(item)
        db_item.is_premium = False
        await db_item.save()
        await ctx.send("Unset item as premium.")

    @commands.command()
    async def donate(self, ctx: MyContext):
        donate_embed = discord.Embed(title="Donation Information",
                                     description="Hi there! 0/0#0001 would appreciate it a lot if you donated!\n"
                                                 "This bot took a lot of work, and costs money to host. Anything "
                                                 "counts!\n"
                                                 "Donation Link: https://patreon.com/ImASkeleton\n"
                                                 "To claim your rewards after donating, ping 0/0#0001 in the bot's "
                                                 "support server: `/invite`. Thanks!\n"
                                                 "Here's a list of perks you might like:",
                                     color=discord.Color.from_rgb(136, 138, 133))
        donate_embed.add_field(name="Perk 01", value="Access to premium features globally")
        donate_embed.add_field(name="Perk 02", value="Give up to 3 guilds access to premium features")
        donate_embed.add_field(name="Perk 03", value="Get autoupdates in DMs")
        donate_embed.add_field(name="Perk 04", value="Set any autoupdate delay you want, from 1 second to 1 year")
        donate_embed.add_field(name="Perk 05", value="Advanced simulations for future COVID-19 trends (this took a lot "
                                                     "of work and is still unfinished)")
        donate_embed.add_field(name="Perk 06", value="AI-powered autocorrect")
        donate_embed.add_field(name="Perk ??", value="If you want another perk, let 0/0#0001 know in the bot's support "
                                                     "server via `/invite`!")
        await ctx.send(embed=donate_embed)


setup = PremiumSettings.setup
