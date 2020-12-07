# coding=utf-8
from typing import Optional

import discord
from discord.ext import commands
from utils.cog_class import Cog
from utils.ctx_class import MyContext
import io
from math import ceil


class Vaccine(Cog):
    @commands.group()
    async def vaccine(self, ctx: MyContext):
        if ctx.invoked_subcommand is None:
            vaccine_phases = ""
            for phase in self.bot.vaccine_api.phases:
                vaccine_phases += "{phase['phase']}: {phase['candidates']} candidates\n"
            vaccine_embed = discord.Embed(name="Vaccine Updates",
                                          description="(For more details, run `{ctx.prefix}help vaccine`)\n"
                                                      "There are a total of **{self.bot.vaccine_api.total_candidates} "
                                                      "vaccine candidates**."
                                                      "\n__**Phases**__\n{vaccine_phases}")
            vaccine_embed.set_footer(text="Last updated at:")
            vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
            await ctx.send(embed=vaccine_embed)

    @vaccine.command(aliases=["list_all", "list"])
    async def list_all_candidates(self, ctx: MyContext, page: Optional[int] = 1):
        """
        List all the possible vaccine candidates for COVID-19!
        """
        vaccine_embed = discord.Embed(title="Vaccine Candidates",
                                      description="To get more details on a vaccine candidate, run "
                                                  "`{ctx.prefix}vaccine details <id>`\n"
                                                  "The ID of any given candidate is under the name.")
        max_pages = ceil(len(self.bot.vaccine_api.candidates) / 24)
        ids = {}
        for data, i in zip(self.bot.vaccine_api.candidates, range(len(self.bot.vaccine_api.candidates))):
            ids[data['details']] = i
        if not 0 < page <= max_pages:
            await ctx.send("The page number you have selected is not between 1 and "
                           "{max_pages}. Please try again.")
            return
        sect = self.bot.vaccine_api.candidates[(page - 1) * 24: page * 24]
        for candidate in sect:
            vaccine_embed.add_field(name=candidate['candidate'], value=ids[candidate['details']])
        if len(sect) == 24:
            vaccine_embed.add_field(name="Page {page} of {max_pages}",
                                    value="To go to the next page, run "
                                          "`{ctx.prefix}{ctx.command.full_parent_name} {ctx.invoked_with} {page + 1}`")
        else:
            vaccine_embed.add_field(name="Page {page} of {max_pages}", value="\u200b")
        vaccine_embed.set_footer(text="Last updated at:")
        vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
        await ctx.send(embed=vaccine_embed)

    @vaccine.command()
    async def details(self, ctx: MyContext, _id: int):
        try:
            vaccine = self.bot.vaccine_api.candidates[_id]
        except IndexError:
            await ctx.send("That isn't a valid vaccine ID! View all the IDs in "
                           "`{ctx.prefix}vaccine list_all_candidates`!")
            return
        if len(vaccine["details"]) <= 2048:
            desc = vaccine["details"]
            file = None
        else:
            desc = "Description is too long! Download the attachment to see it!"
            file = discord.File(io.BytesIO(bytes(vaccine["details"], encoding="utf-8")), filename="description.txt")
        vaccine_embed = discord.Embed(title=vaccine['candidate'],
                                      description=desc)
        vaccine_embed.add_field(name="Mechanism", value=vaccine["mechanism"])
        sponsor_str = ""
        for sponsor, i in zip(vaccine["sponsors"], range(1, len(vaccine["sponsors"])+1)):
            sponsor_str += "#{i}: {sponsor}\n"
        vaccine_embed.add_field(name="Sponsors", value=sponsor_str)
        vaccine_embed.add_field(name="Phase", value=vaccine["trialPhase"])
        institutions_str = ""
        for institution, i in zip(vaccine["institutions"], range(1, len(vaccine["institutions"])+1)):
            institutions_str += "#{i}: {institution}\n"
        vaccine_embed.add_field(name="Institutions", value=institutions_str)
        vaccine_embed.set_footer(text="Last updated at:")
        vaccine_embed.timestamp = self.bot.vaccine_api.last_updated_utc
        if file:
            await ctx.send(embed=vaccine_embed, file=file)
        else:
            await ctx.send(embed=vaccine_embed)


setup = Vaccine.setup
