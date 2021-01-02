# coding=utf-8
import asyncio
from typing import Optional

import discord
from discord.ext import commands
from utils.models import get_from_db
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class VoteSystemCog(Cog):
    @commands.command()
    async def transfer_votes(self, ctx: MyContext, amount: Optional[str] = "all"):
        _ = await ctx.get_translate_function()
        try:
            amount = int(amount)
        except ValueError:
            await ctx.reply(_("You must pass a number or {0}.", "`all`"))
            return
        guild: discord.Guild = ctx.guild
        user: discord.Member = ctx.author
        db_guild = await get_from_db(guild)
        db_user = await get_from_db(user)
        if amount == "all":
            amount = db_user.updater_credits
        if amount > db_user.updater_credits or amount == 0:
            await ctx.reply(_("You don't have enough credits to transfer. Go vote on top.gg for more!\n{0}",
                              f"https://top.gg/bot/{self.bot.user.id}/vote"))
            return
        msg = await ctx.reply(_("You are going to transfer {0} updater credits to this guild ({1}). This action is "
                                "irreversible. Type {2} within 30 seconds to confirm.", amount, guild.name, "`ok`"))

        def event(m: discord.Message):
            return m.author.id == user.id and m.guild.id == guild.id and m.content.lower().strip() == "ok"

        try:
            m1 = await self.bot.wait_for("message", timeout=30, check=event)
        except asyncio.TimeoutError:
            await msg.edit(content=_("Timed out waiting for response."))
            return
        else:
            await m1.delete()

        db_user.updater_credits -= amount
        db_guild.total_updaters += amount
        await db_user.save()
        await db_guild.save()
        await msg.edit(content=_("Transferred {0} credits to {1}.", amount, guild.name))


setup = VoteSystemCog.setup
