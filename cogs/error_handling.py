# coding=utf-8
import traceback
import sentry_sdk
import arrow
from cogs.future_simulations import SimulationsDisabled
from babel import dates
from discord.ext import commands
import discord
from utils import checks, wrap_in_async
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.bot_class import MyBot
from utils.interaction import escape_everything


async def submit_error_message(exc: BaseException, doing: str, ctx: MyContext, bot: MyBot):
    error_channel = bot.get_channel(796093696374079519)
    error_embed = discord.Embed(title=f"Fatal error while working on {doing}!",
                                description=f"Guild details:\n"
                                            f"    ID: `{ctx.guild.id}`\n"
                                            f"    Name: `{ctx.guild.name}`\n\n"
                                            f"Channel details:\n"
                                            f"    ID: `{ctx.channel.id}`\n"
                                            f"    Name: `{ctx.channel.name}`\n\n"
                                            f"Invoking message details:\n"
                                            f"    ID: `{ctx.message.id}`\n\n"
                                            f"Author details:\n"
                                            f"    ID: `{ctx.author.id}`\n"
                                            f"    Name: `{str(ctx.author)}`"  # Quick way to get name#disc
                                )
    tb = f"```py\n{''.join(traceback.format_tb(exc.__traceback__))}\n```"
    error_embed.add_field(name="Exception Name", value=str(exc.__class__))
    error_embed.add_field(name="Exception Reason", value=str(exc), inline=False)
    error_embed.add_field(name="Exception Traceback", value=tb if len(tb) < 1024 else "Too long!")
    await error_channel.send(embed=error_embed)


class CommandErrorHandler(Cog):
    @commands.Cog.listener()
    async def on_command_error(self, ctx: MyContext, exception: Exception) -> None:
        _ = await ctx.get_translate_function()

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound,)

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.

        # Anything in ignored will return and prevent anything happening.
        if isinstance(exception, ignored):
            return

        delete_error_message_after = 60
        command_invoke_help = f"{ctx.prefix}{ctx.command.qualified_name} {ctx.command.signature}"

        ctx.logger.warning(f"Error during processing: {exception} ({repr(exception)})")

        sentry_sdk.set_context("user", {"repr": repr(ctx.author), "id": ctx.author.id,
                                        "name": str(ctx.author)})
        sentry_sdk.set_context("channel", {"repr": repr(ctx.channel), "id": ctx.channel.id})
        sentry_sdk.set_context("guild", {"repr": repr(ctx.guild), "id": ctx.guild.id})
        sentry_sdk.set_context("message", {"repr": repr(ctx.message), "id": ctx.message.id})
        sentry_sdk.set_context("command", {"repr": repr(ctx.command)})

        # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.CommandError
        if isinstance(exception, commands.CommandError):
            if isinstance(exception, commands.ConversionError):
                original = exception.original
                message = _("There was an error converting one of your arguments with {0}. The "
                            "correct syntax would be `{1}`. The converter returned the following "
                            "error: {2}",
                            exception.converter,
                            command_invoke_help,
                            escape_everything(str(original)))
            elif isinstance(exception, commands.UserInputError):
                if isinstance(exception, commands.errors.MissingRequiredArgument):
                    message = _("This command is missing an argument. The correct syntax would be "
                                "`{0}`.", command_invoke_help)
                elif isinstance(exception, commands.errors.ArgumentParsingError):
                    if isinstance(exception, commands.UnexpectedQuoteError):
                        message = _("Too many quotes were provided in your message: don't forget to escape your "
                                    "quotes like this `\\{0}`. The correct syntax for the command is "
                                    "`{1}`.",
                                    exception.quote,
                                    command_invoke_help)
                    elif isinstance(exception, commands.InvalidEndOfQuotedStringError):
                        message = _("A space was expected after a closing quote, but I found {0}. "
                                    "Please check that you are using the correct syntax: `{1}`.",
                                    exception.char,
                                    command_invoke_help)
                    elif isinstance(exception, commands.ExpectedClosingQuoteError):
                        message = _("A closing quote was expected, but wasn't found. Don't forget to close your "
                                    "quotes with `{0}` at the end of your argument. Please check "
                                    "that you are using the correct syntax: `{1}`.",
                                    exception.close_quote,
                                    command_invoke_help)
                    elif isinstance(exception, commands.TooManyArguments):
                        message = _("Too many arguments were passed in this command. "
                                    "Please check that you are using the correct syntax: `{0}`.",
                                    command_invoke_help)
                    else:  # Should not trigger, just in case some more errors are added.
                        message = _("The way you are invoking this command is confusing me. The correct syntax would "
                                    "be `{0}`.",
                                    command_invoke_help)

                elif isinstance(exception, commands.BadArgument):
                    message = _("An argument passed was incorrect. `{0}`."
                                "Please check that you are using the correct syntax: `{command_invoke_help}`.",
                                str(exception),
                                command_invoke_help)
                elif isinstance(exception, commands.BadUnionArgument):
                    message = _("{0} Please check that you are using the correct syntax: `{1}`.",
                                str(exception),
                                command_invoke_help)
                else:
                    message = "{str(exception)} ({type(exception).__name__})"
                    ctx.logger.error("".join(traceback.format_exception(type(exception), exception,
                                                                        exception.__traceback__)))

            elif isinstance(exception, commands.CheckFailure):
                if isinstance(exception, commands.PrivateMessageOnly):
                    message = _("This command can only be used in a private message.")
                elif isinstance(exception, commands.NoPrivateMessage):
                    message = _("This command cannot be used in a private message.")
                elif isinstance(exception, commands.CheckAnyFailure):
                    message = _("Multiple errors were encountered when running your command: {0}",
                                exception.errors)
                elif isinstance(exception, commands.NotOwner):
                    message = _("You need to be the owner of the bot to run that.")
                # We could edit and change the message here, but the lib messages are fine and specify exactly what
                # permissions are missing
                elif isinstance(exception, commands.MissingPermissions):
                    message = _("You are missing permissions to run this command. {0}",
                                " ".join(exception.missing_perms))
                elif isinstance(exception, commands.BotMissingPermissions):
                    message = _("I am missing permissions to run this command. {0}",
                                " ".join(exception.missing_perms))
                elif isinstance(exception, commands.MissingRole):
                    message = _("You are missing the following role: {0}",
                                exception.missing_role)
                elif isinstance(exception, commands.BotMissingRole):
                    message = _("I am missing the following role: {0}",
                                exception.missing_role)
                elif isinstance(exception, commands.MissingAnyRole):
                    message = _("You are missing one of the following roles: {0}",
                                " ".join(exception.missing_roles))
                elif isinstance(exception, commands.BotMissingAnyRole):
                    message = _("I am missing one of the following roles: {0}",
                                " ".join(exception.missing_roles))
                elif isinstance(exception, commands.NSFWChannelRequired):
                    message = _("You need to be in a NSFW channel to run that.")

                # Custom checks errors
                elif isinstance(exception, checks.NotInServer):
                    correct_guild = self.bot.get_guild(exception.must_be_in_guild_id)
                    if correct_guild:
                        message = _("You need to be in the {0} server "
                                    "(`{1}`).",
                                    correct_guild.name,
                                    exception.must_be_in_guild_id)
                    else:
                        message = _("You need to be in a server with ID {0}.",
                                    exception.must_be_in_guild_id)
                elif isinstance(exception, checks.HavingPermission):
                    message = _("You have the `{0}` permission.",
                                exception.permission)
                elif isinstance(exception, checks.MissingPermission):
                    message = _("You need the `{0}` permission.",
                                exception.permission)
                elif isinstance(exception, checks.HavingPermissions):
                    message = _("You have {0} or more of the following permissions: "
                                "`{1}`.",
                                exception.required,
                                exception.permissions)
                elif isinstance(exception, checks.MissingPermissions):
                    message = _("You need {0} or more of the following permissions: "
                                "`{1}`.",
                                exception.required,
                                exception.permissions)
                elif isinstance(exception, checks.BotIgnore):
                    return
                else:
                    message = "Check error running this command : {str(exception)} ({type(exception).__name__})"
                    ctx.logger.error("".join(traceback.format_exception(type(exception), exception,
                                                                        exception.__traceback__)))
            elif isinstance(exception, commands.CommandNotFound):
                # This should be disabled.
                message = _("The provided command was not found.")
            elif isinstance(exception, commands.errors.DisabledCommand):
                message = _("That command has been disabled.")
            elif isinstance(exception, commands.CommandInvokeError):
                if isinstance(exception.original, discord.errors.Forbidden):
                    await ctx.author.send(_("I don't have permissions to send messages there! Try again somewhere I do "
                                            "have permissions to send messages!"))
                    return
                elif isinstance(exception.original, RuntimeError) and exception.original.args[0] == \
                        "The bot hasn't been set up yet! Ensure bot.async_setup is called ASAP!":
                    message = _("The bot's still setting up, please wait a few minutes and try again!")
                elif isinstance(exception.original, discord.errors.NotFound):
                    message = _("I can't find your original message, Discord may be having issues! Try again.")
                else:
                    message = _("There was an error running the specified command‽ This error has been logged.")    
                    # we want the original instead of the CommandError one
                    await submit_error_message(exception.original, "unknown thing", ctx, self.bot)
                    sentry_sdk.capture_exception(exception)
                    # ctx.logger.error("".join(traceback.format_exception(type(exception),
                    # exception, exception.__traceback__)))
            elif isinstance(exception, commands.errors.CommandOnCooldown):
                if await self.bot.is_owner(ctx.author) or checks.has_permission("bot.bypass_cooldowns"):
                    await ctx.reinvoke()
                    return
                else:
                    t = arrow.utcnow()
                    t.shift(seconds=min(round(exception.retry_after, 1), 1))
                    locale = await ctx.get_language_code()
                    # NOTE : This message uses a formatted, direction date in some_time. Formatted, it'll give something
                    # like: "This command is overused. Please try again *in 4 seconds*"
                    message = _("You are being ratelimited. Please try again {0}.",
                                t.humanize(locale=locale))
            elif isinstance(exception, commands.errors.MaxConcurrencyReached):
                bucket_types = {commands.BucketType.default: _("globally"),
                                commands.BucketType.user: _("per user"),
                                commands.BucketType.guild: _("per guild"),
                                commands.BucketType.channel: _("per channel"),
                                commands.BucketType.member: _("per member"),
                                commands.BucketType.category: _("per category"),
                                commands.BucketType.role: _("per role")}
                message = _("Too many users are using this command. Only {0} users can use it at the same time {1}.",
                            exception.number, bucket_types[exception.per])
            elif isinstance(exception, SimulationsDisabled):
                message = _("Simulations have been disabled in this guild due to a missing permission. Ask a admin to "
                            "give me the Manage Messages permission.")
            else:
                message = "{str(exception)} ({type(exception).__name__})"
                ctx.logger.error(
                    "".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
                await submit_error_message(exception, "unknown thing", ctx, ctx.bot)
        else:
            message = _("This should not have happened. A command raised an error that does not comes from "
                        "CommandError. Please inform the owner.")
            ctx.logger.error("".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))

        if message:
            await ctx.send("❌ " + message + _("\nFor help, join the bot's support server at "
                                              "{invite}", invite=self.bot.support_server_invite),
                           delete_after=delete_error_message_after)
        else:
            await ctx.send("❌ " + _("No message was defined. This error has been logged."))

    @commands.Cog.listener()
    async def on_error(self, event_method, *args, **kwargs):
        await self.bot.on_error(event_method, *args, **kwargs)


setup = CommandErrorHandler.setup
