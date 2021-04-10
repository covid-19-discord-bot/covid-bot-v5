# coding=utf-8
"""
Tags are snippet of text that can be used to quickly send a message.
"""
from typing import List

import discord
from discord.ext import commands, menus

from utils.checks import BotIgnore
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.models import Tag, get_tag, get_from_db, TagAlias, DiscordUser, \
    get_ctx_permissions


class TagName(commands.clean_content):
    async def convert(self, ctx, argument):
        converted = await super().convert(ctx, argument)
        lower = converted.lower().strip()

        if not lower:
            raise commands.BadArgument('Missing tag name')

        if " " in lower:
            raise commands.BadArgument("Tags names can't contain spaces")

        if "/" in lower:
            raise commands.BadArgument("Tags names can't contain slashes (`/`)")

        if "#" in lower:
            raise commands.BadArgument("Tags names can't contain hashes (`#`)")

        if "?" in lower:
            raise commands.BadArgument("Tags names can't contain question marks (`?`)")

        if "&" in lower:
            raise commands.BadArgument("Tags names can't contain and signs (`&`)")

        if ":" in lower:
            raise commands.BadArgument("Tags names can't contain `:`")

        if len(lower) > 90:
            raise commands.BadArgument('Tag name is a maximum of 90 characters')

        return lower


class TagMenuSource(menus.ListPageSource):
    def __init__(self, ctx: MyContext, tag: Tag):
        self.ctx = ctx
        self.tag = tag

        data = tag.pages
        super().__init__(data, per_page=1)

    async def format_page(self, menu, entry):
        e = discord.Embed()
        e.title = self.tag.name.replace('_', ' ').title()
        e.color = discord.Color.dark_red()

        if len(entry) == 0:
            entry = " "

        # Embed the image directly
        lines = entry.splitlines()
        last_line = lines[-1]
        if (last_line.endswith(".jpg") or last_line.endswith(".png") or last_line.endswith(".gif")) and \
                last_line.startswith("https://") and " " not in last_line:
            e.set_image(url=last_line)
            entry = "\n".join(lines[:-1])

        e.description = entry[:2047]

        return e


class MultiplayerMenuPage(menus.MenuPages):
    def __init__(self, source, more_users=None, **kwargs):
        super().__init__(source, **kwargs)
        if more_users is None:
            self.more_users = []
        else:
            self.more_users = more_users

    def reaction_check(self, payload: discord.RawReactionActionEvent) -> bool:
        # self.ctx: MyContext
        if payload.message_id != self.message.id:
            return False
        if payload.user_id not in {self.bot.owner_id, self._author_id, *[m.id for m in self.ctx.message.mentions],
                                   *self.bot.owner_ids, *self.more_users}:
            return False

        return payload.emoji in self.buttons


async def show_tag_embed(ctx: MyContext, tag: Tag):
    pages = MultiplayerMenuPage(source=TagMenuSource(ctx, tag), clear_reactions_after=True)
    await pages.start(ctx)


class TagsListMenuSource(menus.ListPageSource):
    def __init__(self, ctx: MyContext, tags: List[Tag]):
        self.ctx = ctx
        self.tags = tags

        super().__init__(tags, per_page=10)

    async def format_page(self, menu: menus.MenuPages, entries):
        e = discord.Embed()
        e.description = "This is the list of all the tags on this server. They are ordered by official tags and " \
                        "most used first.\nThe list doesn't include tag aliases"
        e.color = discord.Color.dark_red()

        for tag in entries:
            e.add_field(inline=False, name=tag.name, value=f"{tag.uses} uses, {tag.revisions} revisions.")

        maximum = self.get_max_pages()
        if maximum > 1:
            current_page = menu.current_page + 1
            entries = len(self.entries)
            text = f'Page {current_page}/{maximum} ({entries} tags)'
            e.set_footer(text=text)

        return e


async def show_tag_list_embed(ctx: MyContext, tags: List[Tag]):
    pages = menus.MenuPages(source=TagsListMenuSource(ctx, tags), clear_reactions_after=True)
    await pages.start(ctx)


class Tags(Cog):
    async def cog_check(self, ctx: MyContext):
        if ctx.guild and ctx.guild.id in self.config()['allowed_in_guilds']:
            return True
        else:
            # Raise BotIgnore to fail silently.
            raise BotIgnore()

    # noinspection PyUnusedLocal
    @commands.command(aliases=["t"])
    async def tag(self, ctx: MyContext, tag_name: TagName, users: str = None):
        """
        Show a given tag based on the name.

        The command accept tags names or aliases, and will display then in a nice paginator, directly in discord.
        You can click the link in the title to read the tag online if you prefer.

        You can add mentions at the end of your message to allow others to control the tag pagination too.
        """
        tag = await get_tag(tag_name)

        if tag:
            await show_tag_embed(ctx, tag)
        else:
            _ = await ctx.get_translate_function()
            await ctx.reply(_("❌ There is no tag with that name."))

    @commands.group()
    async def tags(self, ctx: MyContext):
        """
        Commands to interact with tags : creations, editions, deletions, ...
        """
        if not ctx.invoked_subcommand:
            await ctx.send_help(ctx.command)

    @tags.command()
    async def create(self, ctx: MyContext, tag_name: TagName, *, tag_content=""):
        """
        Create a new tag. The tag name must not be an existing tag or tag alias.
        """
        _ = await ctx.get_translate_function()
        tag = await get_tag(tag_name, increment_uses=False)

        if len(ctx.message.attachments):
            url = ctx.message.attachments[0].url
            if tag_content:
                tag_content += "\n\n" + url
            else:
                tag_content = url

        if not tag_content:
            await ctx.reply(_("❌ You didn't specify what you want your tag to say."))

        if tag:
            await ctx.reply(_("❌ This tag already exists."))
        else:
            db_user = await get_from_db(ctx.author, as_user=True)
            tag = Tag(name=tag_name, content=tag_content, owner=db_user)

            await tag.save()
            await ctx.reply(_("👌 Tag created: {0} (`{1}`)", tag.name, tag.pk))

    @tags.command()
    async def alias(self, ctx: MyContext, alias_name: TagName, tag_name: TagName):
        """
        Alias an existing tag to a new name.
        This is useful to give the same tag multiple names, and be able to edit them in sync.
        """
        _ = await ctx.get_translate_function()
        alias_tag = await get_tag(alias_name, increment_uses=False)
        if alias_tag:
            alias_name, tag_name = tag_name, alias_name  # Maybe there was a slight confusion on the arguments order.
            alias_tag = await get_tag(alias_name, increment_uses=False)
            if alias_tag:
                await ctx.reply(_("❌ Both tags already exist, what are you trying to do?"))
                return

        target_tag = await get_tag(tag_name, increment_uses=False)

        if not target_tag:
            await ctx.reply(_("❌ Neither tag exists."))
            return

        db_user = await get_from_db(ctx.author, as_user=True)
        tag_alias = TagAlias(owner=db_user, tag=target_tag, name=alias_name)
        await tag_alias.save()

        await ctx.reply(
            _("👌 Alias created: {0} -> {1} (`{2}`)", tag_alias.name, tag_alias.tag.name, tag_alias.pk))

    @tags.command()
    async def edit(self, ctx: MyContext, tag_name: TagName, *, tag_content=""):
        """
        Edit an existing tag, changing the text.
        """
        _ = await ctx.get_translate_function()

        tag = await get_tag(tag_name, increment_uses=False)
        if not tag:
            await ctx.reply(_("❌ This tag doesn't exist yet. You might want to create it."))
            return

        tag_owner: DiscordUser = await tag.owner
        perms = await get_ctx_permissions(ctx)
        if tag_owner.discord_id != ctx.author.id and perms.get("tags.manage", False):
            await ctx.reply(_("❌ You don't own that tag, you can't edit it."))
            return

        if len(ctx.message.attachments):
            url = ctx.message.attachments[0].url
            if tag_content:
                tag_content += "\n\n" + url
            else:
                tag_content = url

        if not tag_content:
            await ctx.reply(_("❌ You didn't specify what you want your tag to say."))

        tag.content = tag_content
        tag.revisions += 1
        await tag.save()
        await ctx.reply(_("👌 Tag {0} edited.", tag.name))

    @tags.command()
    async def delete(self, ctx: MyContext, tag_name: TagName):
        """
        Delete an existing tag.
        """
        _ = await ctx.get_translate_function()

        tag = await get_tag(tag_name, increment_uses=False)
        if not tag:
            await ctx.reply(_("❌ This tag doesn't exist."))
            return

        tag_owner: DiscordUser = await tag.owner
        perms = await get_ctx_permissions(ctx)
        if tag_owner.discord_id != ctx.author.id and perms.get("tags.manage", False):
            await ctx.reply(_("❌ You don't own that tag, you can't delete it."))
            return

        await tag.delete()
        await ctx.reply(_("👌 Tag {0} deleted.", tag.name))

    @tags.command()
    async def list(self, ctx: MyContext):
        """
        List all the existing tags.
        """
        _ = await ctx.get_translate_function()

        tags = await Tag.all().order_by('-official', '-uses')

        await show_tag_list_embed(ctx, tags)

    @tags.command()
    async def raw(self, ctx: MyContext, *, tag_name: TagName):
        """
        View the raw version of the tag, with markdown escaped. This is useful to use as a base for editing a tag.
        """
        _ = await ctx.get_translate_function()

        tag = await get_tag(tag_name)

        if not tag:
            await ctx.reply(_("❌ This tag doesn't exist yet. You might want to create it."))
            return

        escaped_content = discord.utils.escape_markdown(tag.content)

        await ctx.reply(escaped_content)


setup = Tags.setup
