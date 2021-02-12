import logging
import typing
from datetime import datetime
from pythonjsonlogger import jsonlogger
import discord


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


def init_logger() -> logging.Logger:
    # Set root logger to log to file as JSON
    logger = logging.getLogger()
    log_handler = logging.FileHandler(filename='/tmp/covid_bot/log1.json')
    formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    # Create the logger

    base_logger = logging.getLogger("matchmaking")
    base_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    # Logging to a file
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('all.log', 'a', 10000000, 1)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    base_logger.addHandler(file_handler)

    file_handler = RotatingFileHandler('errors.log', 'a', 10000000, 1)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.WARNING)
    base_logger.addHandler(file_handler)

    # And to console

    # You can probably collapse the following two StreamHandlers.
    # They list the colors codes for windows and unix systems

    class _AnsiColorStreamHandler(logging.StreamHandler):
        DEFAULT = '\x1b[0m'
        RED = '\x1b[31m'
        GREEN = '\x1b[32m'
        YELLOW = '\x1b[33m'
        CYAN = '\x1b[36m'

        CRITICAL = RED
        ERROR = RED
        WARNING = YELLOW
        INFO = GREEN
        DEBUG = CYAN

        @classmethod
        def _get_color(cls, level):
            if level >= logging.CRITICAL:
                return cls.CRITICAL
            elif level >= logging.ERROR:
                return cls.ERROR
            elif level >= logging.WARNING:
                return cls.WARNING
            elif level >= logging.INFO:
                return cls.INFO
            elif level >= logging.DEBUG:
                return cls.DEBUG
            else:
                return cls.DEFAULT

        def __init__(self, stream=None):
            logging.StreamHandler.__init__(self, stream)

        def format(self, record):
            text = logging.StreamHandler.format(self, record)
            color = self._get_color(record.levelno)
            return color + text + self.DEFAULT

    class _WinColorStreamHandler(logging.StreamHandler):
        # wincon.h
        FOREGROUND_BLACK = 0x0000
        FOREGROUND_BLUE = 0x0001
        FOREGROUND_GREEN = 0x0002
        FOREGROUND_CYAN = 0x0003
        FOREGROUND_RED = 0x0004
        FOREGROUND_MAGENTA = 0x0005
        FOREGROUND_YELLOW = 0x0006
        FOREGROUND_GREY = 0x0007
        FOREGROUND_INTENSITY = 0x0008  # foreground color is intensified.
        FOREGROUND_WHITE = FOREGROUND_BLUE | FOREGROUND_GREEN | FOREGROUND_RED

        BACKGROUND_BLACK = 0x0000
        BACKGROUND_BLUE = 0x0010
        BACKGROUND_GREEN = 0x0020
        BACKGROUND_CYAN = 0x0030
        BACKGROUND_RED = 0x0040
        BACKGROUND_MAGENTA = 0x0050
        BACKGROUND_YELLOW = 0x0060
        BACKGROUND_GREY = 0x0070
        BACKGROUND_INTENSITY = 0x0080  # background color is intensified.

        DEFAULT = FOREGROUND_WHITE
        CRITICAL = BACKGROUND_YELLOW | FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_INTENSITY
        ERROR = FOREGROUND_RED | FOREGROUND_INTENSITY
        WARNING = FOREGROUND_YELLOW | FOREGROUND_INTENSITY
        INFO = FOREGROUND_GREEN
        DEBUG = FOREGROUND_CYAN

        @classmethod
        def _get_color(cls, level):
            if level >= logging.CRITICAL:
                return cls.CRITICAL
            elif level >= logging.ERROR:
                return cls.ERROR
            elif level >= logging.WARNING:
                return cls.WARNING
            elif level >= logging.INFO:
                return cls.INFO
            elif level >= logging.DEBUG:
                return cls.DEBUG
            else:
                return cls.DEFAULT

        def _set_color(self, code):
            import ctypes
            ctypes.windll.kernel32.SetConsoleTextAttribute(self._outhdl, code)

        # noinspection SpellCheckingInspection
        def __init__(self, stream=None):
            logging.StreamHandler.__init__(self, stream)
            # get file handle for the stream
            import ctypes.util
            # for some reason find_msvcrt() sometimes doesn't find msvcrt.dll on my system?
            crtname = ctypes.util.find_msvcrt()
            if not crtname:
                crtname = ctypes.util.find_library("msvcrt")
            crtlib = ctypes.cdll.LoadLibrary(crtname)
            # noinspection PyProtectedMember
            self._outhdl = crtlib._get_osfhandle(self.stream.fileno())

        def emit(self, record):
            color = self._get_color(record.levelno)
            self._set_color(color)
            logging.StreamHandler.emit(self, record)
            self._set_color(self.FOREGROUND_WHITE)

    # select ColorStreamHandler based on platform
    import platform

    if platform.system() == 'Windows':
        # noinspection PyPep8Naming
        ColorStreamHandler = _WinColorStreamHandler
    else:
        # noinspection PyPep8Naming
        ColorStreamHandler = _AnsiColorStreamHandler

    steam_handler = ColorStreamHandler()
    steam_handler.setLevel(logging.DEBUG)

    steam_handler.setFormatter(formatter)
    base_logger.addHandler(steam_handler)

    discord_logger = logging.getLogger('discord')
    discord_logger.setLevel(logging.INFO)

    discord_formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

    discord_steam_handler = ColorStreamHandler()
    discord_steam_handler.setLevel(logging.INFO)
    discord_steam_handler.setFormatter(discord_formatter)
    discord_logger.addHandler(discord_steam_handler)

    # override all changes made above and force debug
    logger.setLevel(logging.DEBUG)

    return base_logger


class FakeLogger:
    def __init__(self, logger: logging.Logger = None):
        if not logger:
            logger = init_logger()
        self.logger = logger

    @staticmethod
    def make_message_prefix(guild: typing.Optional[discord.Guild] = None,
                            channel: typing.Optional[discord.ChannelType] = None,
                            member: typing.Optional[discord.Member] = None):
        if guild and channel and member:
            return f"{guild.id} - #{channel.name[:15]} :: <{member.name}#{member.discriminator}> "

        elif guild and channel and not member:
            return f"{guild.id} - #{channel.name[:15]} :: "

        elif guild and not channel and not member:
            return f"{guild.id} = {guild.name[:15]} :: "

        elif not guild and not channel and member:
            return f"<{member.name}#{member.discriminator}> "

        else:
            return f""

    def debug(self, message: str,
              guild: typing.Optional[discord.Guild] = None,
              channel: typing.Optional[discord.ChannelType] = None,
              member: typing.Optional[discord.Member] = None):
        return self.logger.debug(self.make_message_prefix(guild, channel, member), str(message))

    def info(self, message: str,
             guild: typing.Optional[discord.Guild] = None,
             channel: typing.Optional[discord.ChannelType] = None,
             member: typing.Optional[discord.Member] = None):
        return self.logger.info(self.make_message_prefix(guild, channel, member), str(message))

    def warn(self, message: str,
             guild: typing.Optional[discord.Guild] = None,
             channel: typing.Optional[discord.ChannelType] = None,
             member: typing.Optional[discord.Member] = None):
        return self.logger.warning(self.make_message_prefix(guild, channel, member), str(message))

    def warning(self, message: str,
                guild: typing.Optional[discord.Guild] = None,
                channel: typing.Optional[discord.ChannelType] = None,
                member: typing.Optional[discord.Member] = None):
        return self.logger.warning(self.make_message_prefix(guild, channel, member), str(message))

    def error(self, message: str,
              guild: typing.Optional[discord.Guild] = None,
              channel: typing.Optional[discord.ChannelType] = None,
              member: typing.Optional[discord.Member] = None):
        return self.logger.error(self.make_message_prefix(guild, channel, member), str(message))

    def exception(self, message: str,
                  guild: typing.Optional[discord.Guild] = None,
                  channel: typing.Optional[discord.ChannelType] = None,
                  member: typing.Optional[discord.Member] = None,
                  exception_instance: BaseException = None):
        return self.logger.exception(self.make_message_prefix(guild, channel, member), str(message), exc_info=exception_instance)


class LoggerConstant:
    def __init__(self,
                 logger: FakeLogger,
                 guild: typing.Optional[discord.Guild] = None,
                 channel: typing.Optional[discord.ChannelType] = None,
                 member: typing.Optional[discord.Member] = None):
        self.logger = logger
        self.guild = guild
        self.channel = channel
        self.member = member

    def debug(self, message: str):
        return self.logger.debug(message, self.guild, self.channel, self.member)

    def info(self, message: str):
        return self.logger.info(message, self.guild, self.channel, self.member)

    def warn(self, message: str):
        return self.logger.warn(message, self.guild, self.channel, self.member)

    def warning(self, message: str):
        return self.logger.warning(message, self.guild, self.channel, self.member)

    def error(self, message: str):
        return self.logger.error(message, self.guild, self.channel, self.member)

    def exception(self, message: str):
        return self.logger.exception(message, self.guild, self.channel, self.member)

