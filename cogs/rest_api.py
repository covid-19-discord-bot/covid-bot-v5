# coding=utf-8
from datetime import datetime

import aiohttp_cors
from aiohttp import web
from aiohttp.web_exceptions import HTTPNotFound, HTTPForbidden
from discord.ext import commands, tasks
from utils.cog_class import Cog
from utils.models import get_from_db


class RestAPI(Cog):
    """
    If someone wants to do a dashboard or something to control DuckHunt, there are a few api routes already. They all return JSON or HTTP404/403/500.
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
    - Global keys, that allow UNLIMITED access to every channel data. They are available on request with me.
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
        self.bot.logger.info(f"DuckHunt JSON API is shutting down...")
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

    async def channel_settings(self, request):
        """
        /channels/<channel_id>/settings
        Get information about a specific channel ID
        """
        channel = self.bot.get_channel(int(request.match_info['channel_id']))

        if channel is None:
            raise HTTPNotFound(reason="Unknown channel")

        await self.authenticate_request(request, channel=channel)

        db_channel = await get_from_db(channel)

        return web.json_response(db_channel.serialize())

    async def channel_top(self, request):
        """
        /channels/<channel_id>/top
        Get players data, ordered by experience
        """
        channel = self.bot.get_channel(int(request.match_info['channel_id']))

        if not channel:
            raise HTTPNotFound(reason="Unknown channel")

        players = await Player.all().filter(channel__discord_id=channel.id).order_by('-experience').prefetch_related(
            "member__user")

        if not players:
            raise HTTPNotFound(reason="Unknown channel in database")

        fields = ["experience", "best_times", "killed", "last_giveback"]

        return web.json_response([
            player.serialize(serialize_fields=fields) for player in players
        ])

    async def player_info(self, request):
        """
        /channels/<channel_id>/player/<player_id>
        Get players data, ordered by experience
        """
        channel = self.bot.get_channel(int(request.match_info['channel_id']))

        await self.authenticate_request(request, channel=channel)

        player = await Player \
            .filter(channel__discord_id=channel.id,
                    member__user__discord_id=int(request.match_info['player_id'])) \
            .first() \
            .prefetch_related("member__user")

        if not player:
            raise HTTPNotFound(reason="Unknown player/channel/user")

        return web.json_response(player.serialize())

    async def run(self):
        await self.bot.wait_until_ready()
        listen_ip = self.config()['listen_ip']
        listen_port = self.config()['listen_port']
        route_prefix = self.config()['route_prefix']
        routes = [
            ('GET', f'{route_prefix}/channels/{{channel_id:\\d+}}', self.channel_info),
            ('GET', f'{route_prefix}/channels/{{channel_id:\\d+}}/settings', self.channel_settings),
            ('POST', f'{route_prefix}/channels/{{channel_id:\\d+}}/settings/{{setting:\\d+}}', self.player_info),
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
        self.bot.logger.info(f"DuckHunt JSON API listening on http://{listen_ip}:{listen_port}")


setup = RestAPI.setup
