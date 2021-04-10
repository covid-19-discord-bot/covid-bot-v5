# coding=utf-8
import io
from math import ceil
from typing import Optional

import discord
from discord.ext import commands

from utils.cog_class import Cog
from utils.ctx_class import MyContext


class VaccineCog(Cog):
    @commands.group()
    async def vaccine(self, ctx: MyContext):
        """
        See COVID-19 vaccine stats. For help on subcommands, run help vaccine
        """
        if ctx.invoked_subcommand is None:
            _ = await ctx.get_translate_function()
            vaccine_phases = ""
            for phase in self.bot.vaccine_api.phases:
                vaccine_phases += _("{0}: {1} candidates\n", phase['phase'], phase['candidates'])
            vaccine_embed = discord.Embed(color=discord.Color.dark_red(), name=_("Vaccine Updates"),
                                          description=_("(For more details, run `{0}help vaccine`)\nThere are a total "
                                                        "of **{1} vaccine candidates**.\n__**Phases**__\n{2}",
                                                        ctx.prefix, self.bot.vaccine_api.total_candidates,
                                                        vaccine_phases))
            vaccine_embed.set_footer(text=_("Last updated at"))
            vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
            await ctx.send(embed=vaccine_embed)

    @vaccine.command(aliases=["list_all", "list"])
    async def list_all_candidates(self, ctx: MyContext, page: Optional[int] = 1):
        """
        List all the possible vaccine candidates for COVID-19!
        """
        _ = await ctx.get_translate_function()
        vaccine_embed = discord.Embed(title=_("Vaccine Candidates"),
                                      description=_("To get more details on a vaccine candidate, run "
                                                    "`{0}vaccine details <id>`\n"
                                                    "The ID of any given candidate is under the name.", ctx.prefix), color=discord.Color.dark_red())
        max_pages = ceil(len(self.bot.vaccine_api.candidates) / 24)
        ids = {}
        for data, i in zip(self.bot.vaccine_api.candidates, range(len(self.bot.vaccine_api.candidates))):
            ids[data['details']] = i
        if not 0 < page <= max_pages:
            await ctx.send(_("The page number you have selected is not between 1 and "
                             "{0}. Please try again.", max_pages))
            return
        sect = self.bot.vaccine_api.candidates[(page - 1) * 24: page * 24]
        for candidate in sect:
            vaccine_embed.add_field(name=candidate['candidate'], value=ids[candidate['details']])
        if len(sect) == 24:
            vaccine_embed.add_field(name=_("Page {0} of {1}", page, max_pages),
                                    value=_("To go to the next page, run "
                                            "`{0}{1} {2} {3}`",
                                            ctx.prefix, ctx.command.full_parent_name, ctx.invoked_with, page + 1))
        else:
            vaccine_embed.add_field(name=_("Page {0} of {1}", page, max_pages), value="\u200b")
        vaccine_embed.set_footer(text=_("Last updated at"))
        vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
        await ctx.send(embed=vaccine_embed)

    @vaccine.command()
    async def details(self, ctx: MyContext, _id: int):
        """
        Get details on a specific vaccine candidate from vaccine list
        """
        _ = await ctx.get_translate_function()
        try:
            vaccine = self.bot.vaccine_api.candidates[_id]
        except IndexError:
            await ctx.send(_("That isn't a valid vaccine ID! View all the IDs in "
                             "{0}!", "`{0}vaccine list_all_candidates`".format(ctx.prefix)))
            return
        if len(vaccine["details"]) <= 2048:
            desc = vaccine["details"]
            file = None
        else:
            desc = _("Description is too long! Download the attachment to see it!")
            file = discord.File(io.BytesIO(bytes(vaccine["details"], encoding="utf-8")), filename="description.txt")
        vaccine_embed = discord.Embed(color=discord.Color.dark_red(), title=vaccine['candidate'],
                                      description=desc)
        vaccine_embed.add_field(name=_("Mechanism"), value=vaccine["mechanism"])
        sponsor_str = ""
        for sponsor, i in zip(vaccine["sponsors"], range(1, len(vaccine["sponsors"])+1)):
            sponsor_str += f"#{i}: {sponsor}\n"
        vaccine_embed.add_field(name=_("Sponsors"), value=sponsor_str)
        vaccine_embed.add_field(name=_("Phase"), value=vaccine["trialPhase"])
        institutions_str = ""
        for institution, i in zip(vaccine["institutions"], range(1, len(vaccine["institutions"])+1)):
            institutions_str += f"#{i}: {institution}\n"
        vaccine_embed.add_field(name=_("Institutions"), value=institutions_str)
        vaccine_embed.set_footer(text=_("Last updated at"))
        vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
        if file:
            await ctx.send(embed=vaccine_embed, file=file)
        else:
            await ctx.send(embed=vaccine_embed)


setup = VaccineCog.setup
