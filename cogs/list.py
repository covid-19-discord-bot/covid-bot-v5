# coding=utf-8
"""
File designed for you to copy over and over again as a template for new parts of your bot
"""
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext


class ListCommands(Cog):
    @commands.group(name="list")
    async def _list(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            await ctx.send_help("list")

    @_list.command(name="countries", aliases=["country"])
    async def _countries(self, ctx: MyContext, *first_letter):
        """
        List countries that can be used in /covid country.
        """
        _ = await ctx.get_translate_function()
        if len(first_letter) == 0:
            await ctx.reply(_("I can't send the entire country list: it's over Discord's 6,000 character limit! Try "
                              "`{0}{1} <letter>` to get only "
                              "countries starting with `<letter>`.", ctx.prefix, ctx.command.qualified_name))
            return
        first_letter = " ".join(first_letter)
        embed = await embeds.list_embed(ctx, " ".join(first_letter))
        if embed is not None:
            try:
                await ctx.author.send(embed=embed)
            except discord.HTTPException:
                def file(reaction: discord.Reaction, user: discord.Member):
                    return reaction.message.id == ctx.message.id and ctx.author.id == user.id and reaction.emoji == "📔"

                msg = await ctx.reply(_("Whatever you have requested, it is over 6,000 characters. I can send a text "
                                        "file, however. React with 📔 any time in the next 15 seconds to be DMed a text "
                                        "file instead of a embed."))
                await msg.add_reaction("📔")
                try:
                    await self.bot.wait_for("reaction_add", check=file, timeout=15)
                except asyncio.TimeoutError:
                    await msg.edit(content=_("Timed out."))
                else:
                    msg = await list_file(ctx, first_letter)
                    await ctx.author.send(msg)  # the bot will convert this to a file for us, how nice
                    if ctx.guild is not None:
                        await ctx.reply(_("Sent you a DM!"))
            if ctx.message.guild is not None:
                await ctx.reply(_("DMed a list to you!"))
        else:
            await ctx.reply("Couldn't find any countries starting with those letters!")

    @staticmethod
    async def generate_list_embed(continents: list, type: tuple, ctx: MyContext):
        _ = await ctx.get_translate_function()
        emb = discord.Embed(title=_("List of {0}", type[1]),
                            description=_("Use `{0}covid {1} <name>` when getting stats for a {1}!",
                                          ctx.prefix, type[0]))
        for ctnt in continents:
            emb.add_field(name=_("Name"), value=ctnt)
        return emb

    @_list.command(name="continents", aliases=["continent"])
    async def _continents(self, ctx: MyContext):
        """
        DMs you a list of all continents that can be used in the /covid continent command!
        """
        _ = await ctx.get_translate_function()
        await ctx.author.send(embed=await self.generate_list_embed(self.bot.worldometers_api.continents,
                                                                   ("continent", "continents"),
                                                                   ctx))
        if ctx.guild is not None:
            await ctx.reply(_("DMed a list to you!"))

    @_list.command(name="states", aliases=["state"])
    async def _states(self, ctx: MyContext, page: int = 1):
        """
        DMs you a list of all continents that can be used in the /covid state command!
        """
        _ = await ctx.get_translate_function()
        state_list_embed = discord.Embed(title=_("List of American States"),
                                         description=_("Use the `{0}covid states <name>` command when getting "
                                                       "stats for `<name>`!", ctx.prefix))
        max_pages = ceil(len(self.bot.worldometers_api.american_states) / 24)
        if not 0 < page <= max_pages:
            await ctx.reply(_("The page number you have selected is not between 1 and "
                              "{0}. Please try again.", max_pages))
            return
        sect = self.bot.worldometers_api.american_states[(page - 1) * 24: page * 24]
        for state_name in sect:
            state_list_embed.add_field(name=_("Name"), value=state_name)
        if len(sect) == 24:
            state_list_embed.add_field(name=_("Page {0} of {1}", page, max_pages),
                                       value=_("To go to the next page, run `{0}{1} {2} {3}`", ctx.prefix,
                                               ctx.command.full_parent_name, ctx.invoked_with, page + 1))
        else:
            state_list_embed.add_field(name=_("Page {0} of {1}", page, max_pages), value="\u200b")
        await ctx.author.send(embed=state_list_embed)
        if ctx.guild is not None:
            await ctx.reply("DMed a list to you!")


setup = ListCommands.setup
