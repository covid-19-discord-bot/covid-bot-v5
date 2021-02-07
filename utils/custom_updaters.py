# coding=utf-8
class CustomParserError(Exception):
    pass


class InvalidKeyError(CustomParserError):
    def __init__(self, key: str):
        self.key = key

    def __str__(self):
        return self.key


class CustomUpdater:
    wom_updater_gen = [lambda x: ["cases total",       x["cases"]],
                       lambda x: ["cases new",         x["todayCases"]],
                       lambda x: ["cases million",     x["casesPerOneMillion"]],
                       lambda x: ["deaths total",      x["deaths"]],
                       lambda x: ["deaths million",    x["deathsPerOneMillion"]],
                       lambda x: ["active total",      x["active"]],
                       lambda x: ["active million",    x["activePerOneMillion"]],
                       lambda x: ["recovered total",   x["recovered"]],
                       lambda x: ["recovered new",     x["todayRecovered"]],
                       lambda x: ["recovered million", x["recoveredPerOneMillion"]],
                       lambda x: ["tests total",       x["tests"]],
                       lambda x: ["tests million",     x["testsPerOneMillion"]],
                       ]

    def __init__(self, bot: "MyBot"):
        self.bot = bot
        self.data_dict = {}

    def parse(self, msg: str):
        try:
            return msg.format(**self.data_dict)
        except KeyError as e:
            raise InvalidKeyError(e.args[0]) from None

    async def setup(self):
        d = self.data_dict
        for i in ["global"] + [j["iso2"] for j in self.bot.worldometers_api.iso_codes]:
            for j in self.wom_updater_gen:
                if i == "global":
                    j = j(await self.bot.worldometers_api.get_global_stats())
                else:
                    j = j(await self.bot.worldometers_api.get_country_stats(i))
                # noinspection SpellCheckingInspection
                d[f"covid worldometers {j[0]}"] = str(j[1])
