# coding=utf-8
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


# noinspection PyUnresolvedReferences
async def get_from_db(discord_object, as_user=True):
    if isinstance(discord_object, discord.Guild):
        db_obj = await DiscordGuild.filter(discord_id=discord_object.id).first()
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

    await Tortoise.init(tortoise_config)

    await Tortoise.generate_schemas()
