# coding=utf-8
"""
All credit to Eyesofcreeper#0001, i just changed it up a little
"""
import asyncio
import datetime
import json
from datetime import datetime
from typing import Dict, List, Union

import aiohttp_cors
import discord
import tortoise
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound, HTTPForbidden, HTTPBadRequest, HTTPInternalServerError
from discord.ext import tasks

from utils.cog_class import Cog
from utils.models import get_from_db, DiscordUser


class RestAPI(Cog):
    """
    If someone wants to do a dashboard or something to control the bot, there are a few api routes already. They all return JSON or HTTP404/403/500.
    **Routes**:
    `/api/channels`  [Global Authentication required] -> Returns some information about all channels enabled on the bot.
    `/api/channels/{channel_id}`  [Authentication required] -> Returns information about the channel, like the ducks currently spawned.
    `/api/channels/{channel_id}/settings`  [Authentication required] -> Returns channel settings
    `/api/channels/{channel_id}/top` [No authentication required] -> Returns the top scores (all players on the channel and some info about players)
    `/api/channels/{channel_id}/player/{player_id}` [No authentication required] -> Returns *all* the data for a specific user
    **Authentication**:
    If you have one, pass the API key on the Authorization HTTP header.
    Two types of keys exist :
    - Channel specific keys, available with `settings api_key`. They only work for a specific channel data.
    - Global keys, that allow UNLIMITED access to every channel data. They are available on request with me (0/0#0001).
    Api keys (local or global) are uuid4, and look like this : `d84af260-c806-4066-8387-1d5144b7fa72`
    """

    def __init__(self, bot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.app = web.Application()
        self.cors = aiohttp_cors.setup(self.app)
        self.runner = web.AppRunner(self.app, access_log=self.bot.logger.logger)
        self.site = None
        self.bot.reload_config()
        self.user_callbacks: Dict[int, asyncio.Task] = {}
        self.done_user_callbacks: Dict[int, asyncio.Task] = {}
        bot.loop.create_task(self.run())

    def cog_unload(self):
        self.bot.logger.info(f"COVID-19 Bot JSON API is shutting down...")
        self.bot.loop.create_task(self.site.stop())

    async def authenticate_request(self, request, channel=None):
        api_key = request.headers.get('Authorization')
        if api_key is None:
            raise HTTPForbidden(reason="No API key provided in Authorization header")

        api_key = api_key.lower()

        if api_key in self.config()["global_api_keys"]:
            return True

        if channel:
            db_channel = await get_from_db(channel)
            channel_api_key = str(db_channel.api_key)
            if channel_api_key is None:
                raise HTTPForbidden(reason="No API key has been generated for this channel yet. Run '/settings api_key "
                                           "set' to generate a key.")
            elif channel_api_key != api_key:
                raise HTTPForbidden(reason="The API key provided isn't valid for the specified channel.")
            else:
                return True
        else:
            raise HTTPForbidden(reason="This route requires a GLOBAL api key. Ask the bot owner.")

    async def add_votes(self, request: web.Response):
        await self.authenticate_request(request)
        # noinspection PyCallingNonCallable
        data = json.loads(await request.text())
        self.bot.logger.info(f"Vote Request: {data}")
        user = await self.bot.fetch_user(data["user"])
        if user is not None:
            db_user: DiscordUser = await get_from_db(user)
        else:
            return
        if data["isWeekend"]:
            votes = 2
        else:
            votes = 1
        db_user.updater_credits += votes
        await db_user.save()
        try:
            msg = "Thank you for voting! You got "
            if data["isWeekend"]:
                msg += "2 credits (+1 for weekend bonus)."
            else:
                msg += "1 credit."
            msg += " I'll remind you to vote again in 12 hours."
            await user.send(msg)
        except discord.DiscordException:
            pass  # we don't care about any discord exceptions

        task = asyncio.create_task(self.vote_reminder(user))
        self.user_callbacks[user.id] = task

        return web.json_response({"result": "ok"})

    async def vote_reminder(self, user: discord.User):
        await asyncio.sleep(86460)
        e = discord.Embed(title="Vote Reminder", description="Hi there {0}! It's been 12 hours since you voted, and "
                                                             "this is a friendly reminder to do so again! Here's the "
                                                             "link: https://top.gg/bot/675390513020403731/vote."
                                                             "Thanks again for using this bot.".
                          format(user.display_name))
        e.set_footer(text="Thanks from 0/0#0001")
        await user.send(embed=e)
        user_callback = self.user_callbacks.pop(user.id)
        if isinstance(user_callback, asyncio.Task):
            self.done_user_callbacks[user.id] = user_callback

    @tasks.loop(hours=24)
    async def await_user_callbacks(self):
        for user_id in self.done_user_callbacks:
            self.bot.logger.debug(f"Awaiting {user_id}'s vote callback")
            cb = self.done_user_callbacks.pop(user_id)
            try:
                await cb
            except Exception as e:
                self.bot.logger.exception("Ignoring exception in callback.", exception_instance=e)
            else:
                self.bot.logger.debug("Callback awaited successfully.")

    async def channel_info(self, request):
        """
        /channels/<channel_id>
        Get information about a specific channel ID
        """
        channel = self.bot.get_channel(int(request.match_info['channel_id']))

        if channel is None:
            raise HTTPNotFound(reason="Unknown channel")

        await self.authenticate_request(request, channel=channel)

        db_channel = await get_from_db(channel)
        channel_data = {'id': channel.id,
                        'name': channel.name,
                        'autoupdater': {
                            'enabled': db_channel.autoupdater.already_set
                        }
                        }
        if channel_data["autoupdater"]["enabled"]:
            last_updated: datetime = db_channel.autoupdater.last_updated
            autoupdater_data = {
                'country_name': db_channel.autoupdater.country_name,
                'delay': db_channel.autoupdater.delay,
                'last_updated': last_updated.isoformat(),
                'force_update': db_channel.autoupdater.force_update,
            }
            channel_data["autoupdater"]["data"] = autoupdater_data

        return web.json_response(channel_data)

    async def manage_updater(self, request: web.Request):
        channel = self.bot.get_channel(int(request.match_info["channel_id"]))
        await self.authenticate_request(request, channel)
        try:
            data = json.loads(await request.content.read())
        except MemoryError:  # if someone wants to try to DoS this by sending large data forms...
            # they aren't getting anything
            return ""
        except json.JSONDecodeError:
            raise HTTPBadRequest(reason="Malformed JSON") from None
        db_channel = await get_from_db(channel)
        if "autoupdater" not in data:
            raise HTTPBadRequest(reason="No autoupdater data sent")
        ad = data["autoupdater"]
        if "enabled" not in ad:
            raise HTTPBadRequest(reason="Didn't specify whether to enable updater.")
        if ad["enabled"]:
            db_channel.autoupdater.already_set = True
            if "country_name" in ad:
                name = await self.bot.worldometers_api.try_to_get_name(ad["country_name"])
                if name[0] in ("country", "world", "continent"):
                    db_channel.autoupdater.country_name = name[1]
                else:
                    raise HTTPBadRequest(reason="Country/continent not found")
            if "delay" in ad:
                try:
                    delay = int(ad["delay"])
                except ValueError:
                    raise HTTPBadRequest(reason="Delay is not numeric")
                if 600 >= delay > 31536000:
                    raise HTTPBadRequest(reason="Delay outside of constraints: 3153600 > delay >= 600")
                db_channel.autoupdater.delay = delay
            if "force_update" in ad:
                try:
                    force_update = bool(ad["force_update"])
                except ValueError:
                    raise HTTPBadRequest(reason="Force update not boolean")
                db_channel.autoupdater.force_update = force_update
            if "do_update_at" in ad:
                try:
                    do_update_at = datetime.utcfromtimestamp(float(ad["do_update_at"]))
                except ValueError:
                    raise HTTPBadRequest(reason="Update time not a valid UTC unix timestamp")
                db_channel.autoupdater.do_update_at = do_update_at
        else:
            db_channel.autoupdater.already_set = False
        try:
            await db_channel.autoupdater.save(force_update=True)
            await db_channel.save(force_update=True)
        except tortoise.exceptions.IntegrityError:
            raise HTTPInternalServerError(reason="Database integrity error")
        return web.json_response({"result": "ok"})

    async def bot_is_in_server(self, request):
        """
        /protected/is_in_server/<server_id>
        Returns JSON data, with one key ("is_in_server") that is True if the bot is in the server, False if not.
        Requires global API key.
        """
        await self.authenticate_request(request)

        try:
            guild = self.bot.get_guild(int(request.match_info["guild_id"])) or await self.bot.fetch_guild(int(
                request.match_info["guild_id"]))
        except discord.Forbidden:
            resp = {"is_in_server": False}
        else:
            if guild:
                resp = {"is_in_server": True}
            else:
                resp = {"is_in_server": False}

        return web.json_response(resp)

    async def bot_is_in_servers(self, request):
        """
        /protected/is_in_servers/<server_ids>
        IDs should be separated by dashes
        Returns JSON data, with keys (guild IDs) that are True if the bot is in the server, False if not.
        Requires global API key.
        """
        await self.authenticate_request(request)

        guilds = request.match_info["guild_ids"].split("-")
        results = []
        for guild in guilds:
            try:
                if self.bot.get_guild(int(guild)):
                    results.append(int(guild))
            except discord.Forbidden:
                pass
        return web.json_response(results)

    async def check_channel_permissions(self, request):
        """
        /protected/manage_channel/<guild_id>/<user_id>
        Returns a list of dicts of details of channels where the user has permissions to manage messages.
        The dicts have two keys: 'id' for channel ID and 'name' for channel name.
        Could return nothing but a empty list, and probably will do so often
        Requires global API key.
        """
        await self.authenticate_request(request)
        guild: discord.Guild = self.bot.get_guild(request.match_info["guild_id"]) or await self.bot.fetch_guild(
            request.match_info["guild_id"])
        if not guild:
            raise HTTPNotFound(reason="No guild with that ID found")

        member: discord.Member = guild.get_member(request.match_info["user_id"]) or await guild.fetch_member(
            request.match_info["user_id"])
        if not member:
            raise HTTPNotFound(reason="No member with that ID found")

        channels = guild.channels if len(guild.channels) > 0 else await guild.fetch_channels()
        channels_with_permissions = []
        for channel in channels:
            if not isinstance(channel, discord.TextChannel):
                continue
            channel: discord.TextChannel
            if (channel.permissions_for(member).value & 0x10) == 0x10:
                channels_with_permissions.append({"name": channel.name, "id": channel.id})
        return web.json_response(channels_with_permissions)

    async def add_extra_votes(self, request):
        await self.authenticate_request(request)
        try:
            user: discord.User = self.bot.get_user(request.match_info["user_id"]) or \
                                 await self.bot.fetch_user(request.match_info["user_id"])
        except discord.Forbidden:
            raise HTTPForbidden(reason="Discord raised Forbidden")
        if not user:
            raise HTTPNotFound(reason="No user with that ID found")
        db_user = await get_from_db(user)
        db_user.updater_credits += 1
        await db_user.save()
        return web.json_response({"result": "ok"})

    async def get_guild_details(self, request):
        await self.authenticate_request(request)
        try:
            guild: discord.Guild = self.bot.get_guild(request.match_info["guild_id"]) or \
                                   await self.bot.fetch_guild(request.match_info["guild_id"])
        except discord.Forbidden:
            raise HTTPForbidden(reason="Discord raised Forbidden")
        if not guild:
            raise HTTPNotFound(reason="No guild with that ID found")
        try:
            member: discord.Member = guild.get_member(request.match_info["user_id"]) or \
                                     await guild.fetch_member(request.match_info["user_id"])
        except discord.Forbidden:
            raise HTTPForbidden(reason="Discord raised Forbidden")
        if not member:
            raise HTTPNotFound(reason="No member with that ID found")

        result = {}

        channels_with_perms: List[Dict[str, Union[str, int]]]
        if guild.owner_id == member.id:
            channels_with_perms = [{"name": channel.name, "id": channel.id}
                                   for channel in guild.channels]
        else:
            channels_with_perms = [{"name": channel.name, "id": channel.id}
                                   for channel in guild.channels if channel.permissions_for(member).manage_messages]
        result["channels"] = channels_with_perms
        print(channels_with_perms)

        db_guild = await get_from_db(guild)
        result["used_credits"] = db_guild.used_updaters
        result["total_credits"] = db_guild.total_updaters
        result["available_credits"] = db_guild.total_updaters - db_guild.used_updaters

        return web.json_response(result)

    async def run(self):
        await self.bot.wait_until_ready()
        listen_ip = self.config()['listen_ip']
        listen_port = self.config()['listen_port']
        route_prefix = self.config()['route_prefix']
        routes = [
            ('GET', f'{route_prefix}/channels/{{channel_id:\\d+}}', self.channel_info),
            ('POST', f'{route_prefix}/channels/{{channel_id:\\d+}}', self.manage_updater),
            ('GET', f'{route_prefix}/protected/bot_is_in_server/{{guild_id:\\d+}}', self.bot_is_in_server),
            ('GET', f'{route_prefix}/protected/bot_is_in_servers/{{guild_ids}}', self.bot_is_in_servers),
            ('GET', f'{route_prefix}/protected/manage_channel/{{guild_id:\\d+}}/{{user_id:\\d+}}',
             self.check_channel_permissions),
            ('POST', f'{route_prefix}/protected/add_votes/{{user_id:\\d+}}/', self.add_extra_votes),
            ('POST', f'{route_prefix}/votes/', self.add_votes),
            ('GET', f'{route_prefix}/protected/guild_info/{{guild_id:\\d+}}/{{user_id:\\d+}}', self.get_guild_details)
        ]
        for route_method, route_path, route_coro in routes:
            resource = self.cors.add(self.app.router.add_resource(route_path))
            self.cors.add(
                resource.add_route(route_method, route_coro), {
                    "*": aiohttp_cors.ResourceOptions(
                        allow_credentials=True,
                        allow_headers=("X-Requested-With", "Content-Type", "Authorization",),
                        max_age=3600,
                    )
                }
            )

        await self.runner.setup()
        self.site = web.TCPSite(self.runner, listen_ip, listen_port)
        await self.site.start()
        self.bot.logger.info(f"COVID-19 Bot JSON API listening on http://{listen_ip}:{listen_port}")


setup = RestAPI.setup
