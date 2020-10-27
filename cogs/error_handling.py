import datetime
import traceback
from cogs.future_simulations import SimulationsDisabled
from babel import dates
from discord.ext import commands
from utils import checks
from utils.cog_class import Cog
from utils.ctx_class import MyContext
from utils.interaction import escape_everything


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

        # https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.CommandError
        if isinstance(exception, commands.CommandError):
            if isinstance(exception, commands.ConversionError):
                original = exception.original
                message = _("There was an error converting one of your arguments with {exception.converter}. The "
                            "correct syntax would be `{command_invoke_help}`. The converter returned the following "
                            "error: {original}",
                            command_invoke_help=command_invoke_help,
                            original=escape_everything(str(original)))
            elif isinstance(exception, commands.UserInputError):
                if isinstance(exception, commands.errors.MissingRequiredArgument):
                    message = _("This command is missing an argument. The correct syntax would be "
                                "`{command_invoke_help}`.", command_invoke_help=command_invoke_help)
                elif isinstance(exception, commands.errors.ArgumentParsingError):
                    if isinstance(exception, commands.UnexpectedQuoteError):
                        message = _("Too many quotes were provided in your message: don't forget to escape your "
                                    "quotes like this `\\{exception.quote}`. The correct syntax for the command is "
                                    "`{command_invoke_help}`.",
                                    command_invoke_help=command_invoke_help,
                                    exception=exception)
                    elif isinstance(exception, commands.InvalidEndOfQuotedStringError):
                        message = _("A space was expected after a closing quote, but I found {exception.char}. "
                                    "Please check that you are using the correct syntax: `{command_invoke_help}`.",
                                    command_invoke_help=command_invoke_help,
                                    exception=exception)
                    elif isinstance(exception, commands.ExpectedClosingQuoteError):
                        message = _("A closing quote was expected, but wasn't found. Don't forget to close your "
                                    "quotes with `{exception.close_quote}` at the end of your argument. Please check "
                                    "that you are using the correct syntax: `{command_invoke_help}`.",
                                    command_invoke_help=command_invoke_help,
                                    exception=exception)
                    elif isinstance(exception, commands.TooManyArguments):
                        message = _("Too many arguments were passed in this command. "
                                    "Please check that you are using the correct syntax: `{command_invoke_help}`.",
                                    command_invoke_help=command_invoke_help)
                    else:  # Should not trigger, just in case some more errors are added.
                        message = _("The way you are invoking this command is confusing me. The correct syntax would "
                                    "be `{command_invoke_help}`.",
                                    command_invoke_help=command_invoke_help)

                elif isinstance(exception, commands.BadArgument):
                    message = _("An argument passed was incorrect. `{exception}`."
                                "Please check that you are using the correct syntax: `{command_invoke_help}`.",
                                command_invoke_help=command_invoke_help,
                                exception=exception)
                elif isinstance(exception, commands.BadUnionArgument):
                    message = _("{exception} Please check that you are using the correct syntax: "
                                "`{command_invoke_help}`.", command_invoke_help=command_invoke_help,
                                exception=str(exception))
                else:
                    message = f"{str(exception)} ({type(exception).__name__})"
                    ctx.logger.error("".join(traceback.format_exception(type(exception), exception,
                                                                        exception.__traceback__)))

            elif isinstance(exception, commands.CheckFailure):
                if isinstance(exception, commands.PrivateMessageOnly):
                    message = _("This command can only be used in a private message.")
                elif isinstance(exception, commands.NoPrivateMessage):
                    message = _("This command cannot be used in a private message.")
                elif isinstance(exception, commands.CheckAnyFailure):
                    message = _("Multiple errors were encountered when running your command: {exception.errors}",
                                exception=exception)
                elif isinstance(exception, commands.NotOwner):
                    message = _("You need to be the owner of the bot to run that.")
                # We could edit and change the message here, but the lib messages are fine and specify exactly what
                # permissions are missing
                elif isinstance(exception, commands.MissingPermissions):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.BotMissingPermissions):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.MissingRole):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.BotMissingRole):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.MissingAnyRole):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.BotMissingAnyRole):
                    message = f"{str(exception)}"
                elif isinstance(exception, commands.NSFWChannelRequired):
                    message = _("You need to be in a NSFW channel to run that.")

                # Custom checks errors
                elif isinstance(exception, checks.NotInServer):
                    correct_guild = self.bot.get_guild(exception.must_be_in_guild_id)
                    if correct_guild:
                        message = _("You need to be in the {correct_guild.name} server "
                                    "(`{exception.must_be_in_guild_id}`).",
                                    correct_guild=correct_guild,
                                    exception=exception)
                    else:
                        message = _("You need to be in a server with ID {exception.must_be_in_guild_id}.",
                                    exception=exception)
                elif isinstance(exception, checks.HavingPermission):
                    message = _("You have the `{exception.permission}` permission.",
                                exception=exception)
                elif isinstance(exception, checks.MissingPermission):
                    message = _("You need the `{exception.permission}` permission.",
                                exception=exception)
                elif isinstance(exception, checks.HavingPermissions):
                    message = _("You have {exception.required} or more of the following permissions: "
                                "`{exception.permissions}`.",
                                exception=exception)
                elif isinstance(exception, checks.MissingPermissions):
                    message = _("You need {exception.required} or more of the following permissions: "
                                "`{exception.permissions}`.",
                                exception=exception)
                elif isinstance(exception, checks.BotIgnore):
                    return
                else:
                    message = f"Check error running this command : {str(exception)} ({type(exception).__name__})"
                    ctx.logger.error("".join(traceback.format_exception(type(exception), exception,
                                                                        exception.__traceback__)))
            elif isinstance(exception, commands.CommandNotFound):
                # This should be disabled.
                message = _("The provided command was not found.")
            elif isinstance(exception, commands.errors.DisabledCommand):
                message = _("That command has been disabled.")
            elif isinstance(exception, commands.CommandInvokeError):
                message = _("There was an error running the specified command. Contact the bot admins.")
                ctx.logger.error(
                    "".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
            elif isinstance(exception, commands.errors.CommandOnCooldown):
                if await self.bot.is_owner(ctx.author) or checks.has_permission("bot.bypass_cooldowns"):
                    await ctx.reinvoke()
                    return
                else:
                    delta = datetime.timedelta(seconds=min(round(exception.retry_after, 1), 1))
                    # NOTE : This message uses a formatted, direction date in some_time. Formatted, it'll give something
                    # like: "This command is overused. Please try again *in 4 seconds*"
                    message = _("This command is overused. Please try again {some_time}.",
                                some_time=dates.format_timedelta(delta, add_direction=True,
                                                                 locale=await ctx.get_language_code()))
            elif isinstance(exception, commands.errors.MaxConcurrencyReached):
                message = f"{str(exception)}"  # The message from the lib is great.
            elif isinstance(exception, SimulationsDisabled):
                message = _("Simulations have been disabled in this guild due to a missing permission. Ask a admin to "
                            "give me the Manage Messages permission.")
            else:
                message = f"{str(exception)} ({type(exception).__name__})"
                ctx.logger.error(
                    "".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))
        else:
            message = _("This should not have happened. A command raised an error that does not comes from "
                        "CommandError. Please inform the owner.")
            ctx.logger.error("".join(traceback.format_exception(type(exception), exception, exception.__traceback__)))

        if message:
            await ctx.send("❌ " + message, delete_after=delete_error_message_after)


setup = CommandErrorHandler.setup
