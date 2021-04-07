# coding=utf-8
import random

import discord
import typing
from tortoise import Tortoise, fields
from tortoise.models import Model
import datetime
import enum

if typing.TYPE_CHECKING:
    from utils.ctx_class import MyContext


# TODO: https://github.com/long2ice/aerich


class AutoupdateTypes(enum.IntEnum):
    world = 1
    country = 2
    continent = 3
    # all types after this comment require voting to enable
    state = 4
    province = 5
    custom = 6
    graph = 7
    map = 8


class DiscordGuild(Model):
    id = fields.IntField(pk=True)
    discord_id = fields.BigIntField(index=True)
    name = fields.TextField()
    prefix = fields.CharField(20, null=True)
    permissions = fields.JSONField(default={})
    language = fields.CharField(6, default="en")
    overtime_confirmed = fields.BooleanField(default=False)
    is_premium = fields.BooleanField(default=False)
    enable_tips = fields.BooleanField(default=True)
    disable_simulations = fields.BooleanField(default=False)
    used_updaters = fields.SmallIntField(default=0)
    total_updaters = fields.SmallIntField(default=1)

    minigame_enabled = fields.BooleanField(default=False)
    log_channel = fields.BigIntField(default=None, null=True)
    infected_role = fields.BigIntField(default=None, null=True)
    cured_role = fields.BigIntField(default=None, null=True)
    dead_role = fields.BigIntField(default=None, null=True)

    class Meta:
        table = "guilds"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Guild name={self.name}>"


class DiscordChannel(Model):
    id = fields.IntField(pk=True)
    guild = fields.ForeignKeyField('models.DiscordGuild')
    discord_id = fields.BigIntField(index=True)
    name = fields.TextField()
    autoupdater = fields.ManyToManyField('models.AutoupdaterData')
    permissions = fields.JSONField(default={})
    api_key = fields.TextField(default="0"*32)
    disabled_api = fields.BooleanField(default=False)

    class Meta:
        table = "channels"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Channel name={self.name}>"


class DiscordUser(Model):
    id = fields.IntField(pk=True)
    discord_id = fields.BigIntField(index=True)
    name = fields.TextField()
    discriminator = fields.CharField(4)
    last_modified = fields.DatetimeField(auto_now=True)
    times_ran_example_command = fields.IntField(default=0)
    permissions = fields.JSONField(default={})
    language = fields.CharField(6, default="en")
    is_premium = fields.BooleanField(default=False)
    future_simulation = fields.ForeignKeyField('models.FutureSimulations')
    updater_credits = fields.SmallIntField(default=0)
    opened_support_tickets = fields.SmallIntField(default=0)

    class Meta:
        table = "users"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<User name={self.name}#{self.discriminator}>"


class DiscordMember(Model):
    id = fields.IntField(pk=True)
    guild = fields.ForeignKeyField('models.DiscordGuild')
    user = fields.ForeignKeyField('models.DiscordUser')
    permissions = fields.JSONField(default={})

    class Meta:
        table = "members"

    def __repr__(self):
        return f"<Member user={self.user} guild={self.guild}>"


class AutoupdaterData(Model):
    id = fields.IntField(pk=True)
    discord_id = fields.BigIntField(null=False)
    already_set = fields.BooleanField(default=False)
    country_name = fields.TextField(default="i'm a idiot", null=True)
    delay = fields.BigIntField(default=-1)  # Shouldn't run into issues, delay is able to be set to up
    # to 250 billion years and if someone is stupid enough to do that... oy vey. I will have little hope for humanity
    # making it through the rest of this pandemic :P
    last_updated = fields.DatetimeField(auto_now_add=True)
    force_update = fields.BooleanField(default=False)
    do_update_at = fields.DatetimeField(default=datetime.datetime.utcfromtimestamp(-1))
    type = fields.IntEnumField(AutoupdateTypes)
    channel: fields.ReverseRelation[DiscordChannel]

    class Meta:
        table = "autoupdater_data"

    def __repr__(self):
        return f"<AutoupdaterData country_name={self.country_name} delay={self.delay} " \
               f"last_updated={self.last_updated} force_update={self.force_update} " \
               f"do_update_at={self.do_update_at} type={self.type}>"


class FutureSimulations(Model):
    """
    Model to help with saving user's future simulation data.
    All times are in days unless otherwise noted.
    """
    id = fields.IntField(pk=True)

    # Has this model been set up yet?
    is_set_up = fields.BooleanField(default=False)

    # What country is this model for? Defaults to world.
    country_name = fields.CharField(max_length=3, default="WRL")

    # Simulate 4 weeks by default: 32,767 days is about 89 years and 10 months: plenty of time
    time_to_simulate = fields.SmallIntField(default=28)

    # Population size.(IntField won't work here after a country is selected with 2.1b+ people [aka global])
    population_size = fields.BigIntField(default=-1)

    # Infected count
    infected = fields.BigIntField(default=-1)

    # Recovered count
    recovered = fields.BigIntField(default=-1)

    # Same as above, but may we never see the day when 2,147,483,647 people die from COVID-19 alone
    dead = fields.BigIntField(default=-1)

    # If 2,147,483,647 people die in a single day it's probably gonna be a worldwide nuclear event that spreads COVID or
    # something like that, hopefully that doesn't happen :P
    # UPDATE: december 30th, 2020: it hasn't happened
    dead_today = fields.BigIntField(default=-1)

    # Rate of infected who need to be admitted to hospital
    hosp_rate = fields.FloatField(default=0.15)

    # Rate of infected who need to be admitted to ICU
    icu_rate = fields.FloatField(default=0.05)

    # Rate of infected who need a ventilator
    vent_rate = fields.FloatField(default=0.02)

    # Rate of infected who die from COVID-19
    death_rate = fields.FloatField(default=4.3)

    # Percent contact reduced by social distancing: or in other terms, this is the percent reduction in the number of
    # people someone would meet daily without social distancing: 0 means no social distancing, and 100 means absolute
    # perfect isolation: most places would be around 5-25%: related to beta_decay
    contact_reduction = fields.FloatField(default=0)

    # time from infection to death
    t_death = fields.SmallIntField(default=20)

    # time to double the number of infected
    t_double = fields.SmallIntField(default=73)

    # decay rate of beta, which represents how often a contact results in a new infection: related to contact_reduction
    beta_decay = fields.FloatField(default=0)

    # time one patient takes up a normal hospital bed
    hosp_los = fields.SmallIntField(default=7)

    # time one patient takes up a ICU bed
    icu_los = fields.SmallIntField(default=9)

    # time one patient takes up a ventilator
    vent_los = fields.SmallIntField(default=10)

    # time to get better: or it takes this many days to shift from I to R
    recover_time = fields.SmallIntField(default=23)

    class Meta:
        table = "future_simulations"


class AlignmentLaw(enum.IntEnum):
    lawful = 1
    neutral = 2
    chaotic = 3


class AlignmentGood(enum.IntEnum):
    good = 1
    neutral = 2
    evil = 3


class Isolation(enum.IntEnum):
    """The closer to 0 the most isolated they become"""
    lives_in_bunker = 1
    stays_at_home_country = 10
    stays_at_home_city = 15
    works_from_home = 20
    essential_worker = 20
    normal_life = 25
    construction_worker = 30
    medical_personnel = 35
    goes_to_parties = 40


class Player(Model):
    discord_id = fields.BigIntField(pk=True)
    discord_name = fields.CharField(max_length=200)

    percent_infected = fields.IntField(default=0)

    cured = fields.BooleanField(default=False)
    doctor = fields.BooleanField(default=False)
    immunodeficient = fields.BooleanField(default=False)

    total_infected_points = fields.IntField(default=0)
    total_cured_points = fields.IntField(default=0)
    maximum_infected_points = fields.IntField(default=0)

    isolation = fields.IntEnumField(Isolation, default=Isolation.normal_life)

    touched_last = fields.DatetimeField(auto_now_add=True)

    good = fields.IntEnumField(AlignmentGood)
    law = fields.IntEnumField(AlignmentLaw)
    charisma = fields.IntField()

    inventory: fields.ReverseRelation["Inventory"]
    achievements: fields.ReverseRelation["Achievements"]
    statistics: fields.ReverseRelation["Statistics"]

    def is_dead(self) -> bool:
        return self.percent_infected >= 100

    def is_infected(self) -> bool:
        return self.percent_infected > 0

    def can_be_touched(self) -> bool:
        if not self.is_dead():
            return self.touched_last + datetime.timedelta(hours=3) < datetime.datetime.utcnow()
        else:
            return self.touched_last + datetime.timedelta(hours=1) < datetime.datetime.utcnow()

    def infect(self, add_infected: int = None) -> None:
        if add_infected is None:
            add_infected = random.randint(1, 8)

        if self.achievements.vaccinated:
            add_infected = min(0, add_infected)

        self.total_infected_points += max(0, add_infected)
        self.total_cured_points -= min(0, add_infected)
        self.percent_infected += add_infected
        self.percent_infected = max(self.percent_infected, 0)
        self.maximum_infected_points = max(self.maximum_infected_points, self.percent_infected)

        if self.total_infected_points >= 50 and self.percent_infected == 0:
            self.cured = True

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.discord_name


class Inventory(Model):
    player: fields.OneToOneRelation[Player] = fields.OneToOneField(
        "models.Player", on_delete=fields.CASCADE, related_name="inventory", pk=True
    )

    education = fields.BigIntField(default=1)
    knowledge_points = fields.BigIntField(default=0)
    working_points = fields.BigIntField(default=0)
    research_points = fields.BigIntField(default=0)
    money = fields.BigIntField(default=0)  # Comes from work
    soap = fields.IntField(default=1)  # Can be bought
    food = fields.IntField(default=2)  # Can be bought
    airplane_ticket = fields.IntField(default=0)  # Can be bought
    lottery_ticket = fields.IntField(default=0)  # Can be bought
    herb = fields.IntField(default=0)  # Can be found
    music_cd = fields.IntField(default=0)  # Can be found
    pill = fields.IntField(default=0)  # Can be given to by doctors
    vaccine = fields.IntField(default=0)  # Can be given to by doctors
    mask = fields.IntField(default=0)  # Can be given to by doctors
    toilet_paper = fields.IntField(default=6)  # Can be used only
    gun = fields.IntField(default=0)  # Can be used only
    dagger = fields.IntField(default=1)  # Can be used only
    virus_test = fields.IntField(default=0)  # Can be given to by doctors


class ItemsEmojis(enum.Enum):
    education = "🧠"
    knowledge_points = "🔬"
    working_points = "🛠"
    money = "💰"
    soap = "🧼"
    food = "🥔"
    herb = "🌿"
    music_cd = "💿"
    pill = "💊"
    vaccine = "💉"
    mask = "😷"
    airplane_ticket = "✈"
    lottery_ticket = "🎫"
    toilet_paper = "🧻"
    gun = "🔫"
    dagger = "🔪"
    virus_test = "📊"


class Achievements(Model):
    player: fields.OneToOneRelation[Player] = fields.OneToOneField(
        "models.Player", on_delete=fields.CASCADE, related_name="achievements", pk=True
    )
    hospital_stay = fields.BooleanField(default=False)
    it_was_just_a_cold = fields.BooleanField(default=False)
    symptoms = fields.BooleanField(default=False)
    bad_symptoms = fields.BooleanField(default=False)
    tested_positive = fields.BooleanField(default=False)
    vaccinated = fields.BooleanField(default=False)
    suicided = fields.BooleanField(default=False)
    murderer = fields.BooleanField(default=False)
    victim = fields.BooleanField(default=False)
    died = fields.BooleanField(default=False)
    cured = fields.BooleanField(default=False)
    traveler = fields.BooleanField(default=False)
    back_from_the_dead = fields.BooleanField(default=False)


class AchievementsEmojis(enum.Enum):
    hospital_stay = "🏥"
    it_was_just_a_cold = "🤧"
    symptoms = "🤢"
    bad_symptoms = "🤮"
    tested_positive = "🦠"
    vaccinated = "💉"
    suicided = "💀"
    murderer = "🔫"
    victim = "☮"
    died = "☣"
    cured = "🕶️"
    traveler = "✈️"
    back_from_the_dead = "⛪️"


class Statistics(Model):
    player: fields.OneToOneRelation[Player] = fields.OneToOneField(
        "models.Player", on_delete=fields.CASCADE, related_name="statistics", pk=True
    )
    worked_times = fields.BigIntField(default=0)
    researched_times = fields.BigIntField(default=0)
    hugs_given = fields.BigIntField(default=0)
    hugs_received = fields.BigIntField(default=0)
    made_vaccines = fields.BigIntField(default=0)
    heals = fields.BigIntField(default=0)
    been_eaten_times = fields.BigIntField(default=0)
    eaten_brains = fields.BigIntField(default=0)


class Tag(Model):
    owner = fields.ForeignKeyField('models.DiscordUser', related_name='tags')

    # Statistics
    created = fields.DatetimeField(auto_now_add=True)
    last_modified = fields.DatetimeField(auto_now=True)
    uses = fields.IntField(default=0)
    revisions = fields.IntField(default=0)

    # Tag
    official = fields.BooleanField(default=False)
    name = fields.CharField(max_length=90, db_index=True, unique=True)
    content = fields.TextField()

    @property
    def pages(self):
        return [page.strip(" \n") for page in "\n".join(self.content.splitlines()).split('\n\n---')]

    def __str__(self):
        return f"{self.name}"


class TagAlias(Model):
    owner = fields.ForeignKeyField('models.DiscordUser', related_name='tags_aliases')
    tag = fields.ForeignKeyField('models.Tag', related_name='aliases')

    uses = fields.IntField(default=0)

    name = fields.CharField(max_length=90, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name} -> {self.tag.name}"


async def get_tag(name, increment_uses=True) -> typing.Optional[Tag]:
    tag: typing.Optional[Tag] = await Tag.filter(name=name).first()
    if tag:
        if increment_uses:
            tag.uses += 1
            await tag.save()
        return tag
    else:
        # Search for an alias
        alias: typing.Optional[TagAlias] = await TagAlias.filter(name=name).prefetch_related("tag").first()
        if alias:
            tag: Tag = alias.tag
            if increment_uses:
                alias.uses += 1
                tag.uses += 1

                await alias.save()
                await tag.save()
            return tag
        else:
            # No alias and no tag
            return None


# noinspection PyUnresolvedReferences
async def get_from_db(discord_object, as_user=True):
    if isinstance(discord_object, discord.Guild):
        db_obj = await (DiscordGuild.filter(discord_id=discord_object.id).first())
        if not db_obj:
            db_obj = DiscordGuild(discord_id=discord_object.id,
                                  name=discord_object.name)
            await db_obj.save()
        return db_obj
    elif isinstance(discord_object, discord.abc.GuildChannel):
        db_obj = await DiscordChannel.filter(discord_id=discord_object.id).first().prefetch_related("autoupdater")
        if not db_obj:
            db_obj = DiscordChannel(discord_id=discord_object.id,
                                    name=discord_object.name,
                                    guild=await get_from_db(discord_object.guild))
            await db_obj.save()
        return db_obj
    elif isinstance(discord_object, discord.Member) and not as_user:
        db_obj = await DiscordMember.filter(
            user__discord_id=discord_object.id).first().prefetch_related("user", "guild")
        if not db_obj:
            db_obj = DiscordMember(guild=await get_from_db(discord_object.guild),
                                   user=await get_from_db(discord_object, as_user=True))
            await db_obj.save()
        return db_obj
    elif isinstance(discord_object, discord.User) or isinstance(discord_object, discord.Member) and as_user:
        db_obj = await DiscordUser.filter(discord_id=discord_object.id).first().prefetch_related("future_simulation")
        if not db_obj:
            future_sims = FutureSimulations()
            await future_sims.save()
            db_obj = DiscordUser(discord_id=discord_object.id,
                                 name=discord_object.name,
                                 discriminator=discord_object.discriminator,
                                 future_simulation=future_sims)
            await db_obj.save()
        return db_obj


async def get_ctx_permissions(ctx: 'MyContext') -> dict:
    """
    Discover the permissions for a specified context. Permissions are evaluated first from the default permissions
    specified in the config file, then by the guild config, the channel conifg, and again from the member_specific
    permissions, then by the fixed permissions as seen in the config file, and finally using user overrides set by
    the bot administrator in the database.
    :param ctx:
    :return:
    """
    if ctx.guild:
        db_member: DiscordMember = await get_from_db(ctx.author, as_user=False)
        db_channel: DiscordChannel = await get_from_db(ctx.channel)
        db_user: DiscordUser = db_member.user
        db_guild: DiscordGuild = db_member.guild
        guild_permissions = db_guild.permissions
        channel_permissions = db_channel.permissions
        member_permissions = db_member.permissions
        user_permissions = db_user.permissions
        subguild_permissions = {}
        subchannel_permissions = {}
        for role in ctx.author.roles:
            subguild_permissions = {**subguild_permissions, **guild_permissions.get(str(role.id), {})}
            subchannel_permissions = {**subchannel_permissions, **channel_permissions.get(str(role.id), {})}
    else:
        subguild_permissions = {}
        subchannel_permissions = {}
        member_permissions = {}
        db_user: DiscordUser = await get_from_db(ctx.author, as_user=True)
        user_permissions = db_user.permissions

    default_permissions = ctx.bot.config['permissions']['default']
    fixed_permissions = ctx.bot.config['permissions']['fixed']

    permissions = {**default_permissions,
                   **subguild_permissions,
                   **subchannel_permissions,
                   **member_permissions,
                   **fixed_permissions,
                   **user_permissions}
    return permissions


async def init_db_connection(config):
    tortoise_config = {
        'connections': {
            # Dict format for connection
            'default': {
                'engine': 'tortoise.backends.asyncpg',
                'credentials': {
                    'host': config['host'],
                    'port': config['port'],
                    'user': config['user'],
                    'password': config['password'],
                    'database': config['database'],
                }
            },
        },
        'apps': {
            'models': {
                'models': ["utils.models", "aerich.models"],
                'default_connection': 'default',
            }
        }
    }

    await Tortoise.init(tortoise_config, use_tz=True)

    await Tortoise.generate_schemas()


async def get_player(user: typing.Union[discord.User, discord.Member]) -> Player:
    player = await Player.filter(discord_id=user.id).first()

    if not player:
        player = Player(discord_id=user.id,
                        discord_name=user.name,
                        immunodeficient=random.randint(0, 100) <= 15,
                        doctor=random.randint(0, 100) <= 2,
                        good=random.choice(list(AlignmentGood)),
                        law=random.choice(list(AlignmentLaw)),
                        charisma=random.randint(0, 10)
                        )
        await player.save()
        inventory = Inventory(player=player)
        await inventory.save()
        achievements = Achievements(player=player)
        await achievements.save()
        statistics = Statistics(player=player)
        await statistics.save()

    await player.fetch_related('inventory', 'statistics', 'achievements')
    return player


# noinspection PyUnresolvedReferences
async def save_player(player: Player) -> None:
    await player.save()
    await player.inventory.save()
    await player.achievements.save()
    await player.statistics.save()
