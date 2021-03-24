# coding=utf-8
"""
Credit for this cog goes to Eyesofcreeper#0001. It's almost a direct copy from DuckHunt, just changed to fit the
COVID-19 bot.
"""
import asyncio
import datetime
import re
from typing import Dict, List

import discord
from babel.dates import format_datetime, format_timedelta
from discord.ext import commands, tasks
from discord.utils import snowflake_time

from utils.bot_class import MyBot
from utils.checks import NotInServer
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import get_from_db, DiscordUser


class PrivateMessagesSupport(Cog):
    def __init__(self, bot: MyBot, *args, **kwargs):
        super().__init__(bot, *args, **kwargs)
        self.webhook_cache: Dict[discord.TextChannel, discord.Webhook] = {}
        self.users_cache: Dict[int, discord.User] = {}
        self.blocked_ids: List[int] = []
        self.index = 0
        self.background_loop.start()

        self.invites_regex = re.compile(
            r"""
                discord      # Literally just discord
                (?:app\s?\.\s?com\s?/invite|\.\s?gg)\s?/ # All the domains
                ((?!.*[Ii10OolL]).[a-zA-Z0-9]{5,12}|[a-zA-Z0-9\-]{2,32}) # Rest of the fucking owl.
                """, flags=re.VERBOSE | re.IGNORECASE)

    def cog_unload(self):
        self.background_loop.cancel()

    @tasks.loop(hours=1)
    async def background_loop(self):
        """
        Check for age of the last message sent in the channel.
        If it's too old, consider the channel inactive and close the ticket.
        """
        category = await self.get_forwarding_category()
        now = datetime.datetime.now()
        one_day_ago = now - datetime.timedelta(days=1)
        for ticket_channel in category.text_channels:
            last_message_id = ticket_channel.last_message_id
            if last_message_id:
                # We have the ID of the last message, there is no need to fetch the API, since we can just extract the
                # datetime from it.
                last_message_time = snowflake_time(last_message_id)
            else:
                # For some reason, we couldn't get the last message, so we'll have to go the expensive route.
                # In my testing, I didn't see it happen, but better safe than sorry.
                try:
                    last_message = (await ticket_channel.history(limit=1).flatten())[0]
                except IndexError:
                    # No messages at all.
                    last_message_time = now
                else:
                    last_message_time = last_message.created_at

            inactive_for = last_message_time - now
            inactive_for_str = format_timedelta(inactive_for, granularity='minute', locale='en', threshold=1.1)
            self.bot.logger.debug(f"[SUPPORT GARBAGE COLLECTOR] "
                                  f"#{ticket_channel.name} has been inactive for {inactive_for_str}.")

            if last_message_time <= one_day_ago:
                self.bot.logger.debug(f"[SUPPORT GARBAGE COLLECTOR] "
                                      f"Deleting #{ticket_channel.name}...")
                # The last message was sent a day ago, or more.
                # It's time to close the channel.
                async with ticket_channel.typing():
                    user = await self.get_user(ticket_channel.name)

                    inactivity_embed = discord.Embed(
                        color=discord.Color.orange(),
                        title="DM Timed Out",
                        description="It seems like nothing has been said here for a long time, "
                                    "so I've gone ahead and closed your ticket, deleting its history. "
                                    "Thanks for using COVID-19 Bot DM support. "
                                    "If you need anything else, feel free to open a new ticket by sending a message "
                                    "here.",
                    )

                    inactivity_embed.add_field(name="Support server",
                                               value="For all your questions, there is a support server. "
                                                     "Click [here](https://discord.gg/myJh5hkjpS) to join.")

                    try:
                        await user.send(embed=inactivity_embed)
                    except discord.DiscordException as e:
                        self.bot.logger.exception(f"Failed to send message to {user!s}!", exception_instance=e)

                    await self.clear_caches(ticket_channel)

                    await ticket_channel.delete(reason=f"Automatic deletion for inactivity.")

    @background_loop.before_loop
    async def before(self):
        await self.bot.wait_until_ready()

    async def is_in_forwarding_channels(self, ctx):
        category = await self.get_forwarding_category()
        if not ctx.guild:
            raise commands.NoPrivateMessage()
        elif ctx.guild.id != category.guild.id:
            raise NotInServer(must_be_in_guild_id=category.guild.id)
        elif ctx.channel.category != category:
            return False
        return True

    async def get_user(self, user_id):
        user_id = int(user_id)
        user = self.users_cache.get(user_id, None)
        if user is None:
            user = await self.bot.fetch_user(user_id)
            self.users_cache[user_id] = user

        return user

    async def get_forwarding_category(self) -> discord.CategoryChannel:
        return self.bot.get_channel(self.config()['forwarding_category'])

    async def get_or_create_channel(self, user: discord.User) -> discord.TextChannel:
        forwarding_category = await self.get_forwarding_category()

        channel = discord.utils.get(forwarding_category.text_channels, name=str(user.id))
        if not channel:
            self.bot.logger.info(f"[SUPPORT] creating a DM channel for {user.name}#{user.discriminator}.")

            now_str = format_datetime(datetime.datetime.now(), locale='en')
            # noinspection SpellCheckingInspection
            channel = await forwarding_category.create_text_channel(
                name=str(user.id),
                topic=f"This is the logs of a DM with {user.name}#{user.discriminator}. "
                      f"What's written in here will be sent back to them, except if "
                      f"the message starts with > or is a DuckHunt command.\nChannel opened: {now_str}"
                      f"\n\n\n[getbeaned:disable_automod]\n[getbeaned:disable_logging]",
                reason="Received a DM.")

            self.bot.logger.debug(f"[SUPPORT] creating a webhook for {user.name}#{user.discriminator}.")

            webhook = await channel.create_webhook(name=f"{user.name}#{user.discriminator}",
                                                   avatar=await user.avatar_url_as(format="png", size=512).read(),
                                                   reason="Received a DM.")
            self.webhook_cache[channel] = webhook
            self.bot.logger.debug(f"[SUPPORT] channel created for {user.name}#{user.discriminator}.")
            await self.handle_ticket_opening(channel, user)
        else:
            if self.webhook_cache.get(channel, None) is None:
                self.bot.logger.debug(f"[SUPPORT] recovering {user.name}#{user.discriminator} channel webhook.")

                webhook = (await channel.webhooks())[0]
                self.webhook_cache[channel] = webhook
        return channel

    async def send_mirrored_message(self, channel: discord.TextChannel, user: discord.User, **send_kwargs):
        self.bot.logger.info(f"[SUPPORT] Sending mirror message to {user.name}#{user.discriminator}")

        channel_message = await channel.send(**send_kwargs)

        try:
            await user.send(**send_kwargs)
        except discord.HTTPException as e:
            await channel_message.add_reaction(emoji="❌")
            await channel.send(content=f"❌ Couldn't send the above message, `dh!ps close` to close the channel.\n"
                                       f"{e!s}")

    async def handle_ticket_opening(self, channel: discord.TextChannel, user: discord.User):
        self.bot.logger.info("Handling ticket opening")
        db_user: DiscordUser = await get_from_db(user, as_user=True)
        db_user.opened_support_tickets += 1
        await db_user.save()

        await channel.send(content=f"Opening a DM channel with {user.name}#{user.discriminator} ({user.mention}).\n"
                                   f"Every message in here will get sent back to them if it's not a bot message, "
                                   f"command, or if it doesn't start with the > character.\n"
                                   f"You can use many commands in the DM channels, detailed in "
                                   f"`c!help private_support`\n"
                                   f"• `c!ps close` will close the channel, sending a DM to the user.\n"
                                   f"• `c!ps block` will block the user from opening further channels.\n"
                                   f"• `c!ps huh` should be used if the message is not a support request, "
                                   f"and will silently close the channel.\n"
                                   f"Attachments are supported in messages.\n\n"
                                   f"Thanks for helping with the bot DM support! <3")

        info_embed = discord.Embed(color=discord.Color.blurple(), title="Support information")

        info_embed.description = "Information in this box isn't meant to be shared outside of this channel, and is " \
                                 "provided for support purposes only. \n" \
                                 "Nothing was sent to the user about this."

        info_embed.set_author(name=f"{user.name}#{user.discriminator}", icon_url=str(user.avatar_url))
        info_embed.set_footer(text="Private statistics")
        info_embed.add_field(name="Tickets created", value=str(db_user.opened_support_tickets))

        await channel.send(embed=info_embed)

        welcome_embed = discord.Embed(color=discord.Color.green(), title="Support ticket opened")
        welcome_embed.description = "Welcome to COVID-19 Bot DM support.\nMessages here are relayed to a select " \
                                    "group of volunteers and bot moderators to help you use the bot. For general " \
                                    "questions, we also have a support server " \
                                    "[here](https://discord.gg/myJh5hkjpS).\nIf you opened the ticket by mistake, " \
                                    "just say `close` and we'll close it for you, otherwise, we'll get back to " \
                                    "you soon."
        welcome_embed.set_footer(text="Support tickets are deleted after 24 hours of inactivity")

        try:
            await user.send(embed=welcome_embed)
        except discord.Forbidden:
            await channel.send(content="❌ It seems I can't send messages to the user, you might want to close the DM. "
                                       "`dh!ps close`.")

    async def handle_support_message(self, message: discord.Message):
        user = await self.get_user(message.channel.name)

        self.bot.logger.info(f"[SUPPORT] answering {user.name}#{user.discriminator} with a message from "
                             f"{message.author.name}#{message.author.discriminator}")

        support_embed = discord.Embed(color=discord.Color.blurple(), title="Support response")
        support_embed.set_author(name=f"{message.author.name}#{message.author.discriminator}",
                                 icon_url=str(message.author.avatar_url))
        support_embed.description = message.content

        if len(message.attachments) == 1:
            url = str(message.attachments[0].url)
            if not message.channel.nsfw \
                    and (url.endswith(".webp") or url.endswith(".png") or url.endswith(".jpg")):
                support_embed.set_image(url=url)
            else:
                support_embed.add_field(name="Attached", value=url)

        elif len(message.attachments) > 1:
            for attach in message.attachments:
                support_embed.add_field(name="Attached", value=attach.url)

            support_embed.add_field(name="Attachments persistence",
                                    value="Images and other attached data to the message will get deleted once your "
                                          "ticket is closed. Make sure to save them beforehand if you wish.")

        try:
            await user.send(embed=support_embed)
        except Exception as e:
            await message.channel.send(f"❌: {e}\nYou can use `c!private_support close` to close the channel.")

    async def handle_auto_responses(self, message: discord.Message):
        forwarding_channel = await self.get_or_create_channel(message.author)
        content = message.content

        user = message.author

        if self.invites_regex.search(content):
            dm_invite_embed = discord.Embed(color=discord.Color.purple(),
                                            title="This is not how you invite COVID-19 Bot.")
            dm_invite_embed.description = "COVID-19 Bot, like other discord bots, can't join servers by using an " \
                                          "invite link.\nYou instead have to be a server admin (or at least have the" \
                                          " Manage Server permission). You can invite the bot " \
                                          "[here](https://covid19.imaskeleton.me/invite) If you need more help, you " \
                                          "can ask here and we'll get back to you."

            dm_invite_embed.set_footer(text="This is an automatic message.")

            await self.send_mirrored_message(forwarding_channel, user, embed=dm_invite_embed)

    async def handle_dm_message(self, message: discord.Message):
        self.bot.logger.info(f"[SUPPORT] received a message from {message.author.name}#{message.author.discriminator}")
        await self.bot.wait_until_ready()

        forwarding_channel = await self.get_or_create_channel(message.author)
        forwarding_webhook = self.webhook_cache[forwarding_channel]

        self.bot.logger.debug(
            f"[SUPPORT] got {message.author.name}#{message.author.discriminator} channel and webhook.")

        attachments = message.attachments
        files = [await attach.to_file() for attach in attachments]
        embeds = message.embeds

        self.bot.logger.debug(f"[SUPPORT] {message.author.name}#{message.author.discriminator} message prepared.")

        await forwarding_webhook.send(content=message.content,
                                      embeds=embeds,
                                      files=files,
                                      allowed_mentions=discord.AllowedMentions.none(),
                                      wait=True)

        self.bot.logger.debug(f"[SUPPORT] {message.author.name}#{message.author.discriminator} message forwarded.")

    async def clear_caches(self, channel: discord.TextChannel):
        try:
            self.users_cache.pop(int(channel.name))
        except KeyError:
            # Cog reload, probably.
            pass

        try:
            self.webhook_cache.pop(channel)
        except KeyError:
            # Cog reload, probably.
            pass

    @Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            # Don't listen to bots (ourselves in this case)
            return

        guild = message.guild
        ctx = await self.bot.get_context(message, cls=MyContext)
        if ctx.valid:
            # It's just a command.
            return

        if guild:
            if message.channel.category == await self.get_forwarding_category():
                if message.content.startswith(">"):
                    return
                # This is a support message.
                async with message.channel.typing():
                    await self.handle_support_message(message)
        else:
            # New DM message.
            if message.author.id in self.blocked_ids:
                # Blocked
                self.bot.logger.debug(
                    f"[SUPPORT] received a message from {message.author.name}#{message.author.discriminator} -> "
                    f"Ignored because of blacklist"
                )
                return
            else:
                async with message.channel.typing():
                    await self.handle_dm_message(message)
                    await self.handle_auto_responses(message)

    @commands.group(aliases=["ps"])
    async def private_support(self, ctx: MyContext):
        """
        The DuckHunt bot DMs are monitored. All of these commands are used to control the created channels, and to
        interact with remote users.
        """
        await self.is_in_forwarding_channels(ctx)

        if not ctx.invoked_subcommand:
            await ctx.send_help(ctx.command)

    @private_support.command()
    async def close(self, ctx: MyContext):
        """
        Close the opened DM channel. Will send a message telling the user that the DM was closed.
        """
        await self.is_in_forwarding_channels(ctx)

        user = await self.get_user(ctx.channel.name)

        close_embed = discord.Embed(
            color=discord.Color.red(),
            title="DM Closed",
            description="Your support ticket was closed and the history deleted. Thanks for using COVID-19 Bot DM "
                        "support. If you need anything else, feel free to open a new ticket by sending a message here."
        )

        close_embed.add_field(
            name="Support server",
            value="For all your questions, there is a support server. "
                  "Click [here](https://discord.gg/myJh5hkjpS) to join."
        )

        async with ctx.typing():
            await ctx.send(content="🚮 Deleting channel... Don't send messages anymore!")

            try:
                await user.send(embed=close_embed)
            except discord.DiscordException:
                pass

            await asyncio.sleep(5)  # To let people stop writing

            await self.clear_caches(ctx.channel)

            await ctx.channel.delete(
                reason=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) closed the DM.")

    @private_support.command(aliases=["not_support", "huh"])
    async def close_silent(self, ctx: MyContext):
        """
        Close the opened DM channel. Will not send a message, since it wasn't a support request.
        """
        await self.is_in_forwarding_channels(ctx)

        async with ctx.typing():
            await ctx.send(content="🚮 Deleting channel... Don't send messages anymore!")
            await asyncio.sleep(5)  # To let people stop writing

            await self.clear_caches(ctx.channel)

            await ctx.channel.delete(
                reason=f"{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id}) closed the DM.")

    @private_support.command()
    async def block(self, ctx: MyContext):
        """
        Block the user from opening further DMs channels.
        """
        await self.is_in_forwarding_channels(ctx)

        self.blocked_ids.append(int(ctx.channel.name))
        await ctx.send("👌")


setup = PrivateMessagesSupport.setup
