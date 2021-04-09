# coding=utf-8
import random
import discord
import typing
from datetime import timedelta, datetime
from discord.ext import commands
from utils import models
from utils.checks import BotIgnore
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_player, save_player, get_from_db, DiscordGuild, Statistics


async def game_enabled(ctx: MyContext):
    db_guild = await get_from_db(ctx.guild)
    if db_guild.minigame_enabled:
        return True
    else:
        raise BotIgnore()


class Coronavirus(Cog):
    async def cog_check(self, ctx: MyContext):
        return await game_enabled(ctx)

    async def log_message(self, db_guild: DiscordGuild, message):
        self.bot.logger.debug(f"Logging message \"{message}\"")
        global_log_channel = self.bot.get_channel(self.config()["log_channel"])
        if global_log_channel is not None:
            await global_log_channel.send(message)
        guild_log_channel = self.bot.get_channel(db_guild.log_channel)
        if guild_log_channel is not None:
            await guild_log_channel.send(message)

    @staticmethod
    async def maybe_find(player, message):
        if player.is_dead():
            return

        find_chance = int(player.isolation / 2)
        if random.randint(0, 1000) <= find_chance:
            # herb = fields.IntField(default=0)  # Can be found
            # music_cd = fields.IntField(default=0)  # Can be found
            items = models.ItemsEmojis

            choices = [items.herb, items.music_cd, items.toilet_paper,
                       items.virus_test, items.music_cd, items.toilet_paper,
                       items.virus_test, items.music_cd,
                       items.virus_test, items.mask]  # 1/10 of each

            choice = random.choice(choices)

            item_attr_name = items(choice).name
            player.inventory.__setattr__(item_attr_name, player.inventory.__getattribute__(item_attr_name) + 1)
            await save_player(player)
            await message.channel.send(f"Hey {message.author.mention}, is that {choice.value} yours? I found it in "
                                       f"this channel, guess you can keep it, I have no use for it anyway.")

    async def maybe_infect(self, player, message):
        if player.is_dead():
            return

        if player.achievements.vaccinated:
            return

        infection_chance = 10
        channel_history = message.channel.history(limit=10, before=message.created_at,
                                                  after=message.created_at - timedelta(minutes=15))
        talking_with_members = {m.author async for m in channel_history}

        for member in talking_with_members:
            member_player = await get_player(member)
            if member_player.is_infected():
                infection_chance += 8
            elif member_player.is_dead():
                infection_chance += 20

        if player.immunodeficient:
            infection_chance *= 2

        infection_chance *= player.isolation / 10

        if player.is_infected():
            # Less chance to up the infection is we are already infected
            infection_chance -= 10
            infection_chance /= 2

        infection_chance /= 4

        if player.cured:
            infection_chance /= 2

        infection_chance = max(round(infection_chance), 1)
        infect = random.randint(0, 100) <= infection_chance

        self.bot.logger.debug(message=f"Infection chance is {infection_chance}%, infect={infect}", guild=message.guild,
                              channel=message.channel, member=message.author)
        if infect:
            player.infect()
            await save_player(player)

    async def maybe_test(self, player, message: discord.Message):
        db_guild = await get_from_db(message.guild)
        if player.is_dead():
            if not player.achievements.died:
                player.achievements.died = True
                await save_player(player)
                await message.channel.send(f"🎈 RIP {message.author.mention}. He's dead, Jim!")
                await self.log_message(db_guild, f"Looks like {message.author.mention} is dead :(")
                if not message.author.discriminator == "0000":
                    try:
                        await message.author.add_roles(message.guild.get_role(db_guild.dead_role), reason="RIP!")
                    except discord.DiscordException:
                        pass
            return

        if player.achievements.tested_positive:
            return

        if not player.is_infected() or player.percent_infected <= 15:
            return

        if random.randint(0, 100) <= int(player.percent_infected / 10):
            if player.percent_infected <= 30:
                player.achievements.it_was_just_a_cold = True
                await message.channel.send(f"🤒 Bruh {message.author.mention}, you don't feel so well... Maybe you "
                                           f"should have some rest!")
            elif player.percent_infected <= 40:
                player.achievements.symptoms = True
                await message.channel.send(f"🤒 Bruh {message.author.mention}, you don't feel so well... Maybe you "
                                           f"should see a doctor!")
            elif player.percent_infected <= 50:
                player.achievements.bad_symptoms = True
                await message.channel.send(
                    f"🤒 Bruh {message.author.mention}, control yourself and stop vomiting on my "
                    f"shoes!")
            else:
                player.achievements.hospital_stay = True
                await message.channel.send(f"🤒 Bruh {message.author.mention}, you should go to the hospital!")

            player.achievements.tested_positive = True
            await save_player(player)
            if not message.author.discriminator == "0000":
                try:
                    await message.author.add_roles(message.guild.get_role(db_guild.infected_role),
                                                   reason="Achoo!")
                except discord.DiscordException:
                    pass

            await self.log_message(db_guild, f"Looks like {message.author.mention} is infected :(")

    # noinspection PyUnresolvedReferences
    @commands.command()
    @commands.cooldown(2, 600, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(3, commands.BucketType.category)
    async def work(self, ctx: MyContext):
        """
        Work and gain some 🛠️ you can exchange for 💰 (salary)️ later at the shop.
        """
        _ = await ctx.get_translate_function()

        player = await get_player(ctx.author)
        if player.is_dead():
            await ctx.reply(_("❌ It's harder to work if you are dead :("))
            return

        player.inventory.working_points += 2
        player.statistics.worked_times += 1

        if random.randint(0, 100) <= 6:
            player.isolation = models.Isolation.construction_worker

        await save_player(player)
        await ctx.reply(_("🧰 You worked for a while"))

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(3, commands.BucketType.category)
    async def school(self, ctx: MyContext):
        """
        When I grow up, I wanna become a doctor!
        """
        _ = await ctx.get_translate_function()

        player = await get_player(ctx.author)
        if player.is_dead():
            await ctx.reply(_("❌ It's harder to do science when you are dead :("))
            return

        if random.randint(0, 100) <= 35 * (1 + int(player.doctor)):
            player.inventory.education += (1 + int(player.inventory.education / 10))
            if random.randint(0, 100) <= 6:
                player.isolation = models.Isolation.essential_worker
            await ctx.reply(_("🧬 Let's practice medicine"))

        elif not player.doctor and (random.randint(0, 100) <= 10 or player.inventory.education >= 15):
            player.inventory.education += 3
            player.doctor = True
            if random.randint(0, 100) <= 6:
                player.isolation = models.Isolation.essential_worker
            await ctx.reply(_("🎓️ Doctor, you completed your degree!"))
        else:
            await ctx.reply("❌ You really should stop going out every night, it would be better for your studies...")
            if random.randint(0, 100) <= 6:
                player.isolation = models.Isolation.goes_to_parties

        await save_player(player)

    @commands.command()
    @commands.cooldown(1, 1200, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(3, commands.BucketType.category)
    async def research(self, ctx: MyContext):
        """
        Serious place for serious people to get to know 🧠 more about the sickness. Find me a cure, buddy!
        """
        _ = await ctx.get_translate_function()

        player = await get_player(ctx.author)
        if player.is_dead():
            await ctx.reply(_("❌ It's harder to do science when you are dead :("))
            return

        if not player.doctor:
            await ctx.reply(_("❌ Maybe you should leave that to professionals :("))
            return

        player.statistics.researched_times += 1

        if random.randint(0, 100) <= 5:
            await ctx.reply(_("👎️ You failed your research, badly :("))
            player.inventory.knowledge_points = int(player.inventory.knowledge_points / 10) + 1
        else:
            player.inventory.knowledge_points += 2 * player.inventory.education

            if random.randint(0, 100) <= 6:
                player.isolation = models.Isolation.medical_personnel
            await ctx.reply(_("🧬 You are searching for a cure..."))

        await save_player(player)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 200, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.guild)
    async def hug(self, ctx: MyContext, *, target: discord.Member):
        """
        I love you!
        """
        _ = await ctx.get_translate_function()

        if target.id == ctx.author.id:
            await ctx.reply(_("❌ So cute... Hugging yourself... (call the psychologists!)"))
            return

        player = await get_player(ctx.author)
        target_player = await get_player(target)

        if player.is_dead():
            await ctx.reply(_("❌ Ghost hug? :("))
            return
        if not player.can_be_touched():
            await ctx.reply(_("❌ You probably shouldn't be doing that right now..."))
            return

        if not target_player.can_be_touched():
            await ctx.reply(_("❌ Don't hug me, I'm not feeling well..."))
            return

        player.touched_last = datetime.utcnow()
        target_player.touched_last = datetime.utcnow()
        player.statistics.hugs_given += 1
        target_player.statistics.hugs_received += 1

        if player.is_infected() or target_player.is_infected():
            player.infect()
            player.infect()
            target_player.infect()

        await save_player(player)
        await save_player(target_player)
        await ctx.reply(
            _("❤️ Love is good, in these times of hardness. {0} 💑 {1}", ctx.author.mention, target.mention))

    @commands.command(aliases=["buy"])
    @commands.cooldown(2, 10, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.category, wait=True)
    async def shop(self, ctx: MyContext, what: str):
        """
        This place is quite empty since many people bought so many things to prepare for quarantine.
        Maybe, with what's left, you'll be able to survive.

        The shopkeeper's name is Jeff.
        Don't go there too often, you don't wanna catch the virus I guess.
        """
        _ = await ctx.get_translate_function()

        items = models.ItemsEmojis
        items_list = [e.value for e in models.ItemsEmojis]
        player = await get_player(ctx.author)
        if player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that you are not alive :("))
            return

        if len(what) >= 3:
            await ctx.reply(_("It's {0} and we still don't know how to use emoji lol", datetime.now().year))
            return

        item = next((item for item in items_list if item in what), None)

        if not item:
            messages = [_("It's {0} and we still don't know how to use emoji lol", datetime.now().year),
                        _("Hmm... what are you buying? 🤔"),
                        _("I'm sorry Dave, I'm afraid I cannot let you do that...")]
            await ctx.reply(random.choice(messages))
            return

        ctx.logger.debug(f"{item} buy in progress")

        # money = fields.BigIntField(default=0)  # Comes from work
        # soap = fields.IntField(default=1)  # Can be bought
        # food = fields.IntField(default=2)  # Can be bought
        # airplane_ticket = fields.IntField(default=0)  # Can be bought
        # lottery_ticket = fields.IntField(default=0)  # Can be bought

        if item == items.money.value:
            if player.inventory.working_points >= 6:
                money_to_add = random.randint(5, 30)
                player.inventory.working_points -= random.randint(1, 6)
                player.inventory.money += money_to_add
                await ctx.reply(_("{0}: Here's your pay... [**money**: {1}]", item, money_to_add))
            else:
                await ctx.reply(_("{0}: Go to work, you lazy ass!", item))
        elif item == items.soap.value:
            if player.inventory.money >= 60:
                cost = random.randint(-40, -10)
                player.inventory.money += cost
                player.inventory.soap += 1
                await ctx.reply(_("{0}: Wash your hands regularly... [**soap**: 1, **money**: {1}]", item, cost))
            else:
                await ctx.reply(_("{0}: Y'know, I also need payment sometimes... Get some {1} and come back later!",
                                  item, items.money.value))
        elif item == items.food.value:
            if player.inventory.money >= 70:
                cost = random.randint(-70, -5)
                player.inventory.money += cost
                player.inventory.food += 1
                await ctx.reply(_("{0}: Don't forget to eat 5 vegetables a day... [**food**: 1, **money**: {1}]",
                                  item, cost))
            else:
                await ctx.reply(_("{0}: I know, we all want to eat, but still... Get some {1} and come back later!",
                                  item, items.money.value))
        elif item == items.airplane_ticket.value:
            if player.inventory.money >= 3000:
                cost = -2500
                player.inventory.money += cost
                player.inventory.airplane_ticket += 1
                await ctx.reply(_("{0}: Flying during a global outbreak of a deadly pandemic? Sure!... "
                                  "[**airplane ticket**: 1, **money**: {1}]", item, cost))
            else:
                await ctx.reply(_("{0}: WTF No, don't fly during this outbreak!", item))
        elif item == items.lottery_ticket.value:
            if player.inventory.money >= 150:
                cost = random.randint(-150, 5)
                player.inventory.money += cost
                player.inventory.lottery_ticket += 1
                await ctx.reply(_("{0}: Your chances of winning are so small... "
                                  "[**lottery ticket**: 1, **money**: {1}]", item, cost))
            else:
                await ctx.reply(_("{0}: You are not even rich enough to buy a friggin' lottery ticket... "
                                  "Get some {1} and come back later!", item, items.money.value))
        else:
            await ctx.reply(_("{0}: I'm sorry, I don't have stock for {0} yet... "
                              "Hopefully there will be a delivery sometime soon...", item))

        if random.randint(1, 100) <= 2:
            player.isolation = models.Isolation.goes_to_parties

        await save_player(player)

    @commands.command()
    @commands.cooldown(2, 90, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.category, wait=True)
    async def hospital(self, ctx: MyContext, what: str):
        """
        The people here are trying their best to find a cure. Let them work, they are only using a lot of 🔬 anyway.
        """
        _ = await ctx.get_translate_function()

        items = models.ItemsEmojis

        player = await get_player(ctx.author)

        if player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that you are not alive. You should be going to the morgue, not "
                              "the hospital :("))
            return

        if not player.doctor:
            if random.randint(0, 100) <= 2:
                await ctx.reply(_("❌ Sorry dude, this is a restricted area. You need to be part of the hospital to "
                                  "enter. (You managed to steal 1x{0} before leaving)",
                                  items.toilet_paper.value))
                player.inventory.toilet_paper += 1
                await save_player(player)
            else:
                await ctx.reply("❌ Sorry dude, this is a restricted area. You need to be part of the hospital to enter")
            return

        if len(what) >= 2:
            await ctx.reply(_("It's {0} and we still don't know how to use emoji lol", datetime.now().year))
            return

        medical_items = {
            items.vaccine.value: 10000,
            items.soap.value: 300,
            items.herb.value: 200,
            items.mask.value: 2500,
            items.toilet_paper.value: 69,
            items.pill.value: 5000,
            items.virus_test.value: 420
        }

        items_list = list(medical_items.keys())
        item = next((item for item in items_list if item in what), None)

        if not item:
            messages = [_("It's {0} and we still don't know what emoji to use lol", datetime.now().year),
                        _("Hmm... what are you making? 🤔"),
                        _("I know, science can be hard to understand, but that??"),
                        _("Heh, is that thing a {0}? No? Then maybe find something else to do.",
                          random.choice(items_list)),
                        _("I'd really prefer to see you creating a new {0}...", random.choice(items_list)),
                        _("Why don't you make a {0} instead?", random.choice(items_list))
                        ]
            await ctx.reply(random.choice(messages))
            return

        item_cost = medical_items[item]

        if player.inventory.knowledge_points >= item_cost:
            player.inventory.knowledge_points -= item_cost
            item_attr_name = items(item).name
            player.inventory.__setattr__(item_attr_name, player.inventory.__getattribute__(item_attr_name) + 10)
            await ctx.reply(_("{0}: Heh, I made that myself! [**{1}**: 10]", item, item_attr_name))

            if item == items.vaccine.value:
                player.statistics.made_vaccines += 10
        else:
            await ctx.reply(_("{0}: This laboratory is not a place for interns. Go away!", item))

        await save_player(player)

    @commands.command()
    @commands.cooldown(4, 10, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.category, wait=True)
    async def give(self, ctx: MyContext, who: discord.Member, what: str):
        """
        Sharing is caring, or at least that's what they told us. Should I share things or stay home?
        Better stay home I think.
        """
        _ = await ctx.get_translate_function()

        if who.id == ctx.author.id:
            await ctx.reply(_("❌ Stop wasting my time, go away!"))
            return

        player = await get_player(ctx.author)
        target_player = await get_player(who)

        if player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that you are not alive :("))
            return

        if target_player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that they are not alive :("))
            return

        if len(what) >= 2:
            await ctx.reply(_("It's {0} and we still don't know how to use emoji lol", datetime.now().year))
            return

        items = models.ItemsEmojis
        items_list = [e.value for e in models.ItemsEmojis]
        item = next((item for item in items_list if item in what), None)

        if not item:
            messages = [_("Don't you think you could give me something useful?"),
                        _("Hmm... what are you making? 🤔"),
                        _("What do you want to give to me??")]
            await ctx.reply(random.choice(messages))
            return

        if item in [items.education.value, items.knowledge_points.value, items.working_points.value]:
            await ctx.reply(_("{0}: It's like, hard to give something that doesn't exist.", item))
            return

        item_attr_name = items(item).name

        if player.inventory.__getattribute__(item_attr_name) >= 1:
            player.inventory.__setattr__(item_attr_name, player.inventory.__getattribute__(item_attr_name) - 1)
            target_player.inventory.__setattr__(item_attr_name, target_player.inventory.__getattribute__(item_attr_name)
                                                + 1)

            await ctx.reply(_("{0}: You gave {1} an {0}.", item, who.mention))

        else:
            await ctx.reply(_("{0}: Spirit of giving is good, but you need to get something to give first!", item))

        await save_player(player)
        await save_player(target_player)

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.category, wait=True)
    async def heal(self, ctx: MyContext, *, who: discord.Member):
        """
        Good ol' medicine.
        """
        _ = await ctx.get_translate_function()

        if who.id == ctx.author.id:
            await ctx.reply(_("❌ Do you need a doctor, sir? 😟"))
            return

        player = await get_player(ctx.author)
        target_player = await get_player(who)

        if player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that you are not alive :("))
            return

        if target_player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that they are dead. Call the morgue at that point. :("))
            return

        if not player.doctor:
            if random.randint(1, 100) <= 90:
                await ctx.reply(_("❌ You don't really have the credentials there, buddy..."))
                return
        else:
            if target_player.doctor and random.randint(1, 100) <= 75:
                failures = [_("❌ You tried to heal, but you missed and injected the pavement!"),
                            _("❌ I'm pretty sure they can manage to heal themselves. You have better to do.")]
                await ctx.reply(random.choice(failures))
                return

            if random.randint(1, 100) <= 10:
                await ctx.reply(_("❌ Did you forget your magical healing powers? Anyway, that didn't work..."))
                return

        player.statistics.heals += 1
        heal_pct = int(min(int(random.randint(-40, -6) / (int(target_player.doctor) + 1)) /
                           (int(player.statistics.heals / 10) + 1), -1))
        target_player.infect(heal_pct)

        await save_player(player)
        await save_player(target_player)

        await ctx.reply(_("⚕ {0} already feels better ({1}%).", who.mention, heal_pct))

    @commands.command(aliases=["brains", "eat"])
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.category, wait=True)
    async def brain(self, ctx: MyContext, *, who: discord.Member):
        """
        BRAINNNNNNS!
        """
        _ = await ctx.get_translate_function()

        player = await get_player(ctx.author)
        target_player = await get_player(who)

        if not player.is_dead():
            await ctx.reply(_("Oh no! It appears that you are in fact alive and very much not a zombie 🧟"))
            return

        if target_player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that they are dead. dead=bad."))
            return

        if not player.can_be_touched():
            await ctx.reply(_("❌ You probably shouldn't be doing that right now..."))
            return

        if not target_player.can_be_touched():
            await ctx.reply(_("❌ Get your hands off of me!"))
            return

        player.touched_last = datetime.utcnow()
        target_player.touched_last = datetime.utcnow()

        eaten_brains = min(max(1, int(target_player.inventory.education / 6)), 30)
        target_player.statistics.been_eaten_times += 1

        if target_player.inventory.education - eaten_brains <= 0:
            target_player.inventory.education = 0
            target_player.infect()
        else:
            target_player.inventory.education = target_player.inventory.education - eaten_brains

        player.statistics.eaten_brains += eaten_brains

        if player.statistics.eaten_brains >= 35 and not player.achievements.back_from_the_dead and \
                random.randint(0, 100) <= 75:
            # Revive player!
            player.achievements.back_from_the_dead = True
            player.education = int(player.statistics.eaten_brains / 15)
            player.immunodeficient = True
            player.doctor = False
            player.percent_infected = 20
            player.law = models.AlignmentLaw.chaotic
            player.good = target_player.good

            db_guild = await get_from_db(ctx.guild)

            if not ctx.author.discriminator == "0000":
                try:
                    await ctx.author.remove_roles(ctx.guild.get_role(db_guild.dead_role), reason="UN-RIP!")
                except discord.DiscordException:
                    pass

            await self.log_message(db_guild, f"Looks like {ctx.author.mention} is back from the morgue... I was pretty "
                                             f"sure they were dead... Anyway, party on I guess :)")
        else:
            await ctx.reply(_("🧟 Yummy! {0} brains are good to eat! [**brains**: {1}]", who.mention, eaten_brains))

        await save_player(player)
        await save_player(target_player)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(8, 20, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.max_concurrency(3, commands.BucketType.category)
    async def use(self, ctx: MyContext, what: str, target: typing.Optional[discord.Member] = None):
        """
        I bought this! Let me open it!
        """
        _ = await ctx.get_translate_function()

        items = models.ItemsEmojis
        items_list = [e.value for e in models.ItemsEmojis]
        player = await get_player(ctx.author)
        if player.is_dead():
            await ctx.reply(_("❌ Oh no! It appears that you are not alive, you can't use things if you are dead :("))
            return

        if len(what) >= 3:
            await ctx.reply(_("It's {0} and we still don't know how to use emoji lol", datetime.now().year))
            return

        item = next((item for item in items_list if item in what), None)

        if not item:
            messages = [_("It's {0} and we still don't know what emoji to use lol", datetime.now().year),
                        _("Hmm... what are you using? 🤔"),
                        _("I'm sorry Dave, I'm afraid I cannot let you do that..."),
                        _("You saw an {0} in a delivery truck yesterday, maybe you could try to buy it instead?",
                          random.choice(items_list))]
            await ctx.reply(random.choice(messages))
            return

        ctx.logger.debug(f"{item} use in progress")

        # soap = fields.IntField(default=1)  # Can be bought
        # food = fields.IntField(default=2)  # Can be bought
        # airplane_ticket = fields.IntField(default=0)  # Can be bought
        # lottery_ticket = fields.IntField(default=0)  # Can be bought
        # herb = fields.IntField(default=0)  # Can be found
        # music_cd = fields.IntField(default=0)  # Can be found
        # pill = fields.IntField(default=0)  # Can be given to by doctors
        # vaccine = fields.IntField(default=0)  # Can be given to by doctors
        # mask = fields.IntField(default=0)  # Can be given to by doctors
        # toilet_paper = fields.IntField(default=6)  # Can be used only
        # gun = fields.IntField(default=1)  # Can be used only
        # dagger = fields.IntField(default=1)  # Can be used only

        if item == items.soap.value:
            if player.inventory.soap >= 1:
                player.inventory.soap -= 1
                player.infect(-3)
                await ctx.reply(_("{0}: You washed your hands. Good job! [**soap**: -1]", item))
            else:
                await ctx.reply(_("{0}: Go and buy some {0} first!", item))
        elif item == items.food.value:
            if player.inventory.food >= 1:
                player.inventory.food -= 1
                player.infect(-4)
                await ctx.reply(_("{0}: Home cooked meals FTW!... [**food**: -1]", item))
            else:
                await ctx.reply(_("{0}: Oh no! Your fridge is empty!", item))
        elif item == items.airplane_ticket.value:
            if player.inventory.airplane_ticket >= 1:
                player.inventory.airplane_ticket -= 1
                player.infect(25)
                player.isolation = models.Isolation.goes_to_parties
                player.achievements.traveler = True
                await ctx.reply(_("{0}: I'm going to the airport and flying to another channel to avoid the virus!",
                                  item), file=discord.File("memes/airplane_ticket.png"))
            else:
                await ctx.reply(_("{0}: Airports are closed!", item))
        elif item == items.lottery_ticket.value:
            if player.inventory.lottery_ticket >= 1:
                player.inventory.lottery_ticket -= 1
                random_number = random.randint(0, 100)
                if random_number == 0:
                    player.cured = False
                    player.immunodeficient = True
                    player.charisma = -999
                    player.infect(100)
                    await ctx.reply(_("{0}: Oops...", item))
                elif random_number <= 31:
                    player.inventory.money += 100
                    await ctx.reply(_("{0}: Jackpot!", item))
                elif random_number == 100:
                    player.inventory.money += 5000
                    await ctx.reply(_("{0}: Jackpot! 💸", item))
                else:
                    await ctx.reply(_("{0}: You won nothing. Better luck next time!", item))
            else:
                await ctx.reply(_("{0}: You are still poor!", item))
        elif item == items.herb.value:
            if player.inventory.herb >= 1:
                player.inventory.herb -= 1
                player.infect(random.randint(-10, 10))
                player.isolation = models.Isolation.stays_at_home_country
                await ctx.reply(_("{0}: Does homeopathy work?!", item))
            else:
                await ctx.reply(_("{0}: lol no.", item))
        elif item == items.music_cd.value:
            if player.inventory.music_cd >= 1:
                player.inventory.music_cd -= 1
                player.infect(random.randint(-14, 5))
                if random.randint(0, 100) <= 15:
                    player.isolation = models.Isolation.goes_to_parties
                await ctx.reply(_("{0}: Music cures boredom?!", item))
            else:
                await ctx.reply(_("{0}: Maybe if you sing out loud it could have the same effect.", item))
        elif item == items.pill.value:
            if player.inventory.pill >= 1:
                player.inventory.pill -= 1
                if random.randint(0, 100) <= 8:
                    await ctx.reply(_("{0}: Huh?! It's rat poison, why would you eat that?", item))
                    player.infect()
                else:
                    player.infect(random.randint(-70, 0))
                    if random.randint(0, 100) <= 15:
                        player.isolation = models.Isolation.normal_life
                    await ctx.reply(_("{0}: Acetaminophen cures cancer, change my mind?!", item))
            else:
                await ctx.reply(_("{0}: You'd have to go and see a doctor for that buddy.", item))
        elif item == items.vaccine.value:
            if player.inventory.vaccine >= 1:
                if random.randint(0, 100) <= 70:
                    player.inventory.vaccine -= 1
                    player.infect(-100)
                    player.achievements.vaccinated = True
                    player.cured = True
                    db_guild = await get_from_db(ctx.guild)
                    if not ctx.author.discriminator == "0000":
                        try:
                            await ctx.author.add_roles(ctx.guild.get_role(db_guild.cured_role),
                                                       reason="Vaccine! (won)")
                        except discord.DiscordException:
                            pass
                    await self.log_message(db_guild, f"Looks like {ctx.author.mention} got a vaccine...")

                    await ctx.reply(_("{0}: IMMUNITY!", item))

                else:
                    player.inventory.vaccine -= 1
                    player.infect()
                    await ctx.reply(_("{0}: You fucking junkie!", item))
            else:
                await ctx.reply(_("{0}: Creating a vaccine takes 18 months, do you really expect that you'll be "
                                  "provided one?", item))
        elif item == items.mask.value:
            if player.inventory.mask >= 1:
                player.inventory.mask -= 1
                player.infect(random.randint(-6, 0))
                if random.randint(0, 100) <= 15:
                    player.isolation = models.Isolation.stays_at_home_city
                await ctx.reply(_("{0}: Achoo?!", item))
            else:
                await ctx.reply(_("{0}: There is no more of that, buddy.", item))
        elif item == items.toilet_paper.value:
            if player.inventory.toilet_paper >= 1:
                player.inventory.toilet_paper -= 1
                player.infect(random.randint(-3, -1))
                await ctx.reply(_("{0}: Clean ass!", item))
            else:
                await ctx.reply(_("{0}: There is no more of that, buddy.", item))
        elif item == items.gun.value:
            if player.inventory.gun >= 1:
                if not target:
                    await ctx.reply(_("{0}: Do not kill me, I swear I'll do no harm!", item))
                    return
                target_player = await get_player(target)

                if target.id == ctx.author.id:
                    await ctx.reply(_("{0}: Suicide sure is an option to not get infected!", item))
                    player.achievements.suicided = True
                    target_player = player

                player.inventory.gun = 0  # Confiscated
                player.inventory.dagger = 0  # Confiscated
                player.isolation = models.Isolation.lives_in_bunker
                player.achievements.murderer = True
                player.infect(random.randint(25, 75))

                target_player.achievements.victim = True
                target_player.infect(random.randint(25, 75))
                await save_player(target_player)

                await ctx.reply(_("{0}: BLOODY MURDER! YOU FUCKING SHOT {1}!!!!!!", item, target.mention))

            else:
                await ctx.reply(_("{0}: You are too young to use firearms anyway.", item))
        elif item == items.dagger.value:
            if player.inventory.dagger >= 1:

                if not target:
                    player.inventory.dagger -= 1
                    player.inventory.food += 3
                    await ctx.reply(_("{0}: You cooked yourself some meals!", item))
                else:

                    target_player = await get_player(target)
                    if target.id == ctx.author.id:
                        await ctx.reply(_("{0}: Suicide sure is an option to not get infected!", item))
                        player.achievements.suicided = True
                        target_player = player

                    player.inventory.gun = 0  # Confiscated
                    player.inventory.dagger = 0  # Confiscated
                    player.isolation = models.Isolation.lives_in_bunker
                    player.achievements.murderer = True
                    player.infect(random.randint(5, 25))
                    target_player.achievements.victim = True
                    target_player.infect(random.randint(5, 23))

                    if random.randint(0, 100) <= 10:
                        target_player.inventory.gun += 1  # Revenge
                        await ctx.reply(_("{0}: Stabby stabby {1}!", item, target.mention))
                    else:
                        await ctx.reply(_("{0}: BLOODY MURDER! YOU FUCKING STABBED {1}!!!!!!",
                                          item, target.mention))

                    await save_player(target_player)
            else:
                await ctx.reply(_("{0}: You don't have any clean {0} left.", item))
        elif item == items.virus_test.value:
            if player.inventory.virus_test >= 1:
                player.inventory.virus_test -= 1
                await ctx.reply(_("{0}: An extensive test was done on your virtual body. You are infected at {1}%. "
                                  "If this goes to 100% you are dead.\nHistorical analysis reveals you were infected "
                                  "at {2}% maximum, and you managed to cure yourself from {3}% of the sickness.",
                                  item, player.percent_infected, player.maximum_infected_points,
                                  player.total_cured_points))
            else:
                await ctx.reply(_("{0}: You need a test first, to test yourself, y'know.", item))
        else:
            await ctx.reply(_("{0}: Do you know how to use an {0} anyway?", item))
            return

        if random.randint(1, 100) <= 2:
            player.isolation = models.Isolation.stays_at_home_city

        await save_player(player)

    @commands.command()
    @commands.cooldown(2, 20, commands.BucketType.user)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def profile(self, ctx: MyContext, *, who: discord.User = None):
        """
        Who am I? Who are they?
        """
        _ = await ctx.get_translate_function()

        if who is None:
            who = ctx.author
        player = await get_player(who)

        achievements_embed = discord.Embed(colour=discord.Colour.blurple(), title=_("Achievements"))
        achievements_embed.set_author(name=f"{who.name}#{who.discriminator}", icon_url=str(who.avatar_url))

        for achievement_name, achievement in models.AchievementsEmojis.__members__.items():
            achievement_emoji = achievement.value
            if player.achievements.__getattribute__(achievement_name):
                achievements_embed.add_field(name=achievement_emoji, value=achievement_name, inline=True)

        inventory_embed = discord.Embed(colour=discord.Colour.blurple(), title="Inventory")
        inventory_embed.set_author(name=f"{who.name}#{who.discriminator}", icon_url=str(who.avatar_url))

        for item_name, item in models.ItemsEmojis.__members__.items():
            item_emoji = item.value
            qty = player.inventory.__getattribute__(item_name)
            if qty > 0:
                inventory_embed.add_field(name=item_emoji, value=str(qty), inline=True)

        inventory_embed.add_field(name=_("Isolation"), value=str(player.isolation.name), inline=False)

        other_embed = discord.Embed(colour=discord.Colour.blurple(), title=_("Other"))
        other_embed.set_author(name=f"{who.name}#{who.discriminator}", icon_url=str(who.avatar_url))
        other_embed.add_field(name=_("Is a doctor"), value=str(player.doctor), inline=True)
        other_embed.add_field(name=_("Is immunodeficient"), value=str(player.immunodeficient), inline=True)
        other_embed.add_field(name=_("Worked"), value=f"{player.statistics.worked_times} times", inline=False)
        other_embed.add_field(name=_("Researched"), value=f"{player.statistics.researched_times} times", inline=False)
        other_embed.add_field(name=_("Lawful"), value=f"{player.law.name}", inline=True)
        other_embed.add_field(name=_("Good"), value=f"{player.good.name}", inline=True)
        other_embed.add_field(name=_("Charisma"), value=f"{player.charisma}", inline=True)
        other_embed.add_field(name=_("Vaccines made"), value=f"{player.statistics.made_vaccines}", inline=True)

        await ctx.reply(embed=inventory_embed)
        await ctx.reply(embed=other_embed)
        await ctx.reply(embed=achievements_embed)

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.guild)
    async def pause(self, ctx: MyContext):
        """
        Pause the simulation, cancelling everything that happen normally.
        """
        _ = await ctx.get_translate_function()

        await ctx.reply(_("❌ Do you really think life has a pause button?"))

    @commands.command()
    @commands.cooldown(2, 600, commands.BucketType.user)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def statistics(self, ctx: MyContext):
        """
        Shows some cool statistics about the game.
        """
        _ = await ctx.get_translate_function()

        embed = discord.Embed(colour=discord.Colour.dark_green(),
                              title=_("Have you been infected yet?"),
                              description=_("Global game statistics. • Event made by Eyesofcreeper#0001 in one night, "
                                            "inspired by Rapptz event bot.\nWho said statistics had to be exact?\n"
                                            "Source code available, with spoilers: "
                                            "||https://github.com/DuckHunt-discord/Coroned-event||\n"
                                            "Pull requests accepted and encouraged. Have fun, don't remove credit :)"))

        # https://tortoise-orm.readthedocs.io/en/latest/query.html#filtering

        infected_count = await models.Achievements.filter(tested_positive=True).count()
        vaccines_count = await models.Statistics.filter(made_vaccines__gt=0).count()

        embed.add_field(name=_("People infected"), value=str(infected_count), inline=True)
        embed.add_field(name=_("Virus name"), value="COVID-19", inline=True)
        embed.add_field(name=_("Vaccines made"), value=str(vaccines_count), inline=True)

        await ctx.reply(embed=embed)

    @commands.command()
    async def game_top(self, ctx: MyContext):
        """
        Who's the top user?

        Bot admins are not included in this list.
        """
        _ = await ctx.get_translate_function()

        embed = discord.Embed(color=discord.Color.dark_green(),
                              title=_("Global Top Users"),
                              description=_("These are the users who have made the most vaccines. The top user at the "
                                            "end of each month can claim a gift of Nitro Classic!"))

        top_vaccines: typing.List[Statistics] = await models.Statistics.filter(made_vaccines__gt=0). \
            order_by("made_vaccines").limit(10).prefetch_related("player")
        user_made_vaccine = False
        for i, user in enumerate(top_vaccines):
            if user.player.discord_id not in self.bot.owner_ids:
                embed.add_field(name=f"#{i+1}: {user.player.discord_name}", value=user.made_vaccines, inline=False)
                user_made_vaccine = True
            else:
                embed.add_field(name=f"#{i+1}: Bot Admin", value=user.made_vaccines, inline=False)
        if not user_made_vaccine:
            embed.add_field(name=_("No users have made a vaccine!"),
                            value=_("Will you be the first? Go to school until you complete your degree and then "
                                    "research until you have 10k 🔬! After that you're on your own to figure out how "
                                    "to get the vaccine."))
        await ctx.reply(embed=embed)

    async def dispatch_maybes(self, message: discord.Message):
        if message.guild is None:
            return

        player = await get_player(message.author)
        await self.maybe_infect(player, message)
        await self.maybe_test(player, message)

        if message.author.id == self.bot.user.id:
            return

        await self.maybe_find(player, message)

    @commands.Cog.listener()
    @commands.max_concurrency(1, commands.BucketType.user, wait=True)
    async def on_command_completion(self, ctx: MyContext):
        if not await game_enabled(ctx):
            return

        await self.dispatch_maybes(ctx.message)

    @commands.Cog.listener()
    @commands.max_concurrency(1, commands.BucketType.user, wait=True)
    async def on_message(self, message: discord.Message):
        """
        Main on_message listener
        """
        if message.author.bot:
            return

        ctx = await self.bot.get_context(message, cls=MyContext)

        if ctx.valid:
            # ctx.logger.debug("Ignoring message since it's a command")
            return

        if not await game_enabled(ctx):
            return

        await self.dispatch_maybes(message)


setup = Coronavirus.setup
