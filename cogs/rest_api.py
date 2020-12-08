# coding=utf-8
import json
from datetime import datetime

import aiohttp_cors
import discord
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound, HTTPForbidden, HTTPBadRequest
import datetime

from utils.cog_class import Cog
from utils.models import get_from_db


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
        bot.loop.create_task(self.run())

    def cog_unload(self):
        self.bot.logger.info(f"COVID-19 Bot JSON API is shutting down...")
        self.bot.loop.create_task(self.site.stop())

    async def authenticate_request(self, request, channel=None):
        api_key = request.headers.get('Authorization')
        if api_key is None:
            raise HTTPForbidden(reason="No API key provided in Authorization header")

        api_key = api_key.lower()

        if api_key in self.config()["global_access_keys"]:
            return True

        if not channel:
            raise HTTPForbidden(reason="This route requires a GLOBAL api key. Ask the bot owner.")

        if channel:
            db_channel = await get_from_db(channel)
            channel_api_key = str(db_channel.api_key)
            if api_key == "00000000000000000000000000000000":
                raise HTTPForbidden(reason="No API key has been generated for this channel yet. Run '/settings api_key "
                                           "set' to generate a key.")
            if channel_api_key != api_key:
                raise HTTPForbidden(reason="The API key provided isn't valid for the specified channel.")
            else:
                return True

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
                'last_updated': last_updated.isoformat()
            }
            channel_data["autoupdater"]["data"] = autoupdater_data

        return web.json_response(channel_data)

    async def manage_updater(self, request: web.Request):
        channel = self.bot.get_channel(int(request.match_info["channel_id"]))
        await self.authenticate_request(request, channel)
        db_channel = await get_from_db(channel)
        try:
            data = json.load(request.content)
        except MemoryError:  # if someone wants to try to DoS this by sending large data forms...
            # they aren't getting anything, since it'll just time out
            return ""
        except json.JSONDecodeError:
            raise HTTPBadRequest(reason="Malformed JSON") from None
        if "autoupdater" not in data:
            raise HTTPBadRequest(reason="No autoupdater data sent")
        ad = data["autoupdater"]
        if "enabled" not in ad:
            raise HTTPBadRequest(reason="Didn't specify whether to enable updater.")
        if ad["enabled"]:
            db_channel.autoupdater.already_set = True
            if "country_name" in ad:
                name = await self.bot.worldometers_api.try_to_get_name(ad["country_name"])
                if name[0] in ("country", "world"):
                    db_channel.autoupdater.country_name = name[1]
                else:
                    raise HTTPBadRequest(reason="Country not found")
            if "delay" in ad:
                try:
                    delay = int(ad["delay"])
                except ValueError:
                    raise HTTPBadRequest(reason="Delay is not numeric")
                if 600 <= delay < 31536000:
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
        await db_channel.autoupdater.save()
        await db_channel.save()
        return web.json_response({"result": "ok"})

    async def bot_is_in_server(self, request):
        """
        /protected/is_in_server/<server_id>
        Returns JSON data, with one key ("is_in_server") that is True if the bot is in the server, False if not.
        Requires global API key.
        """
        await self.authenticate_request(request)

        guild = self.bot.get_guild(int(request.match_info["guild_id"])) or self.bot.fetch_guild(int(
            request.match_info["guild_id"]))

        if guild:
            resp = {"is_in_server": True}
        else:
            resp = {"is_in_server": False}
        return web.json_response(resp)

    async def check_channel_permissions(self, request):
        """
        /protected/manage_channel/<guild_id>/<user_id>
        Returns a list of dicts of details of channels where the user has permissions to manage messages.
        The dicts have two keys: 'id' for channel ID and 'name' for channel name.
        Could return nothing but a empty list, and probably will do so often
        Requires global API key.
        """
        await self.authenticate_request(request)
        guild: discord.Guild = self.bot.get_guild(request.match_info["guild_id"])
        if not guild:
            guild: discord.Guild = await self.bot.fetch_guild(request.match_info["guild_id"])
            if not guild:
                raise HTTPNotFound(reason="No guild with that ID found")
        member: discord.Member = await guild.get_member(request.match_info["user_id"])
        if not member:
            member: discord.Member = await guild.fetch_member(request.match_info["user_id"])
            if not member:
                raise HTTPNotFound(reason="No member with that ID found")
        channels_with_permissions = []
        for channel in guild.channels:
            channel: discord.TextChannel
            if channel.permissions_for(member).manage_messages:
                channels_with_permissions.append({"name": channel.name, "id": channel.id})
        return web.json_response(channels_with_permissions)

    async def run(self):
        await self.bot.wait_until_ready()
        listen_ip = self.config()['listen_ip']
        listen_port = self.config()['listen_port']
        route_prefix = self.config()['route_prefix']
        routes = [
            ('GET', f'{route_prefix}/channels/{{channel_id:\\d+}}', self.channel_info),
            ('GET', f'{route_prefix}/protected/bot_is_in_server/{{guild_id:\\d+}}', self.bot_is_in_server),
            ('GET', f'{route_prefix}/protected/manage_channel/{{guild_id:\\d+}}/{{user_id:\\d+}}',
             self.check_channel_permissions),
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
                })

        await self.runner.setup()
        self.site = web.TCPSite(self.runner, listen_ip, listen_port)
        await self.site.start()
        self.bot.logger.info(f"COVID-19 Bot JSON API listening on http://{listen_ip}:{listen_port}")


setup = RestAPI.setup
