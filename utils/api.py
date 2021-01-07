# coding=utf-8
# Licenced under the CC BY-NC-SA 4.0 licence: by modifying any code you agree to be bound by the terms of the
# licence: https://creativecommons.org/licenses/by-nc-sa/4.0/

import asyncio
import datetime
import logging
import time
from typing import Optional, List, AnyStr, Dict, Tuple

import aiohttp

MAX_UPDATE_TRIES = 5
SORT_TYPES = ("cases", "recovered", "deaths", "critical", "tests", "population")


class BaseAPIException(Exception):
    pass


class IncorrectSortType(BaseAPIException):
    pass


class NetworkException(BaseAPIException):
    def __init__(self, exc, *args):
        super().__init__(*args)
        self.exc = exc


class NoCountryDataFields(BaseAPIException):
    pass


class NoDataAvailable(BaseAPIException):
    pass


class CountryNotFound(BaseAPIException):
    pass


class ProvinceNotFound(BaseAPIException):
    pass


def get_iso2_code(_input: str, _list: list) -> [str, None]:
    """
    Returns a ISO2 code, given any of the 3 types of codes.
    :param _input: The name to convert to a ISO2 code.
    :param _list: Country list to get the ISO2 code from.
    :return: ISO2 code if found, otherwise None.
    """
    _input = str(_input).lower()
    try:
        for country in _list:
            country_codes = (str(country['country']).lower(),
                             str(country['iso2']).lower(),
                             str(country['iso3']).lower())
            if _input in country_codes:
                return country['iso2']
    except IndexError:
        raise NoCountryDataFields()


# Same as getISO2Code(), returns a ISO3 code
def get_iso3_code(_input: str, _list: list) -> [str, None]:
    """
    Returns a ISO3 code, given a ISO2 code.
    :param _input: The ISO2 code. This is converted automatically to a code if it isn't one.
    :param _list: Country list to get the ISO3 code from.
    :return: ISO3 code if found, otherwise None.
    """
    _input = get_iso2_code(_input, _list)
    if not _input:
        return
    try:
        for country in _list:
            if _input == str(country["iso2"]):
                return country["iso3"]
    except IndexError:
        raise NoCountryDataFields()


# Same as getISO2Code(), only returns a country name
def get_country_name(_input, _list) -> [str, None]:
    """
    Returns a country name, given a ISO2 code.
    :param _input: The ISO2 code. This is converted automatically to a code if it isn't one.
    :param _list: Country list to get the ISO2 code from.
    :return: ISO2 code if found, otherwise None.
    """
    _input = get_iso2_code(_input, _list)
    if not _input:
        return
    try:
        for country in _list:
            if _input == str(country["iso2"]):
                return country["country"]
    except IndexError:
        raise NoCountryDataFields()


# Given a URL, this will return the JSON of that page
async def get_data(session: aiohttp.ClientSession,
                   url: str, *,
                   formatted_as_json: bool = True):
    """
    Returns JSON/text of a URL

    :param session: aiohttp.ClientSession object to use: must already be open.
    :param url: URL to grab data from
    :param formatted_as_json: Try to parse as JSON? If true, returns parsed JSON. If false, returns text directly
                              without parsing
    :return: Text or JSON-formatted data, depending on formatted_as_json
    :raises NetworkException: if a aiohttp.ClientError is raised. The original exception is avalible via e.exc.
    """
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            if formatted_as_json:
                return await response.json()
            else:
                return await response.text()
    except (aiohttp.ClientError, aiohttp.ClientConnectorError) as e:
        raise NetworkException(e)


def from_time_to_date(in_time: time.struct_time) -> datetime.date:
    """
    Convert a time.struct_time object to a datetime.date object quickly.

    :param in_time: The time.struct_time object you would like to convert.
    :return: datetime.date object that contains the same month/day/year as the struct_time object passed in.
    """
    return datetime.date(year=in_time.tm_year,
                         month=in_time.tm_mon,
                         day=in_time.tm_mday)


async def _check_stats_are_valid(cls):
    if not cls._has_been_updated:
        raise NoDataAvailable()


async def _handle_client_exceptions(cls, e):
    cls.logger.exception(f"ClientException while getting data in class {cls.__class__.__name__}!",
                         e.exc)
    if cls._has_been_updated:
        return
    elif cls._update_tries <= MAX_UPDATE_TRIES:
        await cls._do_update()
    else:
        cls.logger.fatal("Failed to update! Data will not be available! Expect exceptions on later calls!")
        cls._update_tries = 0


class ISOCodeHelper:
    def __init__(self, *, logging_level=logging.INFO):
        self.logger: logging.Logger = logging.Logger("ISO Code Helper", level=logging_level)
        self.logger.setLevel(logging_level)
        self.iso_codes = []
        self.logger = logging.Logger(self.__class__.__name__)
        self._has_been_updated = False
        self._update_tries = 0

    # noinspection PyTypeChecker
    async def update_data(self, *, session: Optional[aiohttp.ClientSession] = None):
        session = session or aiohttp.ClientSession()
        async with session as session:
            self.logger.info("Getting new country data...")
            try:
                data = await get_data(session, "https://disease.sh/v3/covid-19/countries?allowNull=true")
            except NetworkException as e:
                await _handle_client_exceptions(self, e)
                return
            self.logger.info("Got ISO codes! Parsing data and loading it into memory...")
            for country in filter(lambda x: x["countryInfo"]["iso2"] is not None, data):
                iso_code = dict(country=country["country"], iso2=country["countryInfo"]["iso2"],
                                iso3=country["countryInfo"]["iso3"])
                self.iso_codes.append(iso_code)

    async def _do_update(self):
        await self.update_data()


class Covid19JHUCSSEStats:
    """
    Class for stats on COVID-19 via the https://disease.sh API's JHUCSSE section.
    """

    def __init__(self, add_ids: bool = False, *, update_stats: bool = False,
                 logging_level=logging.INFO):
        """
        Class to get data + historical data about COVID-19 for every country (data from JHUCSSE).

        :param add_ids: Add a unique ID to every country, starting from 1.
        :param update_stats: Whether to update stats on class initalization or wait for a explicit call to do so.
                             Doing it in the __init__ makes the init time a lot longer, and it's synchronous: for this
                             reason, it defaults to being disabled.
        """
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats JHUCSSE", level=logging_level)
        self.logger.setLevel(logging_level)
        self._has_been_updated: bool = False
        self._update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.last_updated_utc: datetime.datetime = datetime.datetime.utcfromtimestamp(-1)
        self.global_historical_stats: dict = {}
        self.historical_stats: dict = {}
        self.american_states: list = []
        self.american_state_stats: dict = {}
        self.iso_codes = ISOCodeHelper()
        self.provinces: dict = {}
        self.countries: dict = {}
        if update_stats:
            self.update_covid_19_virus_stats()
            self.iso_codes.update_data()

    async def _do_update(self):
        await self.update_covid_19_virus_stats()

    async def _check_stats_are_valid(self):
        """
        Checks that all stats are valid.

        :raises NoDataAvalible: when data isn't valid
        :return: always None
        """
        if not self._has_been_updated:
            raise NoDataAvailable()

    async def update_covid_19_virus_stats(self, *, session: aiohttp.ClientSession = None):
        """
        Updates the stats, parses them, and loads it into memory.

        :param session: Optional: aiohttp.ClientSession to use. Defaults to making a new session.
        :return: None
        :raises NetworkException: if a AIOHttp error is raised, this error is raised. You can get the original
                                  exception via e.exc.
        """
        self._update_tries += 1
        self.logger.info('Opening new AIOHttp session...')
        session = session or aiohttp.ClientSession()
        async with session as session:
            self.logger.info("Getting ISO codes...")
            await self.iso_codes.update_data()
            self.logger.info("Done!")
            self.logger.info("Getting new global data...")
            try:
                data: dict = await get_data(session,
                                            "https://disease.sh/v3/covid-19/historical/all?lastdays=all&allowNull=1")
            except NetworkException as e:
                await _handle_client_exceptions(self, e)
                return
            self.global_historical_stats = data
            self.logger.info("Getting country stats...")
            for code in self.iso_codes.iso_codes:
                try:
                    data: dict = await get_data(session,
                                                f"https://disease.sh/v3/covid-19/historical/{code['iso2']}"
                                                f"?lastdays=all&allowNull=1")
                except NetworkException as e:
                    if e.exc.code == 404:
                        continue
                self.countries[code["iso2"]] = data
            self.logger.info("Getting provincial stats...")
            data: list = await get_data(session, "https://disease.sh/v3/covid-19/historical?lastdays=all")
            for country in self.iso_codes.iso_codes:
                cty_data = {}
                for i in filter(lambda x: x["country"] == country["country"], data):
                    if i["province"] is None:
                        cty_data["all"] = i
                        self.countries[i["country"]] = i
                    else:
                        cty_data[i["province"]] = i
                        self.provinces[i["province"].lower()] = i
                self.historical_stats[country["iso2"]] = cty_data
            self.logger.info("Getting US states...")
            data: list = await get_data(session, "https://disease.sh/v3/covid-19/historical/usacounties?lastdays=all")
            self.american_states = data
            for state in data:
                state_data = await get_data(session, f"https://disease.sh/v3/covid-19/historical/usacounties/{state}?"
                                                     f"lastdays=all")
                sd = {"all": {"timeline": {"cases": {}, "deaths": {}}}}

                def check(y):
                    if y is None or y["county"] is None:
                        return False
                    return not y["county"].startswith("out of") or y["county"] == "unassigned"

                for county, i in zip(filter(check, state_data), range(len(state_data))):
                    if i == 0:
                        for j in ["cases", "deaths"]:
                            tc = {}
                            for k in county["timeline"][j]:
                                tc[k] = 0
                            sd["all"]["timeline"][j] = tc

                    for j in ["cases", "deaths"]:
                        tc = sd["all"]["timeline"][j]
                        for k in county["timeline"][j]:
                            tc[k] += county["timeline"][j][k]
                        sd["all"]["timeline"][j] = tc

                    sd[county["county"]] = county
                self.american_state_stats[state] = sd
        self.last_updated_utc = datetime.datetime.utcnow()
        self._has_been_updated = True
        self.data_is_valid = True
        self.logger.info("Done!")

    def try_to_get_name(self, name: str) -> Optional[Tuple[str, Optional[str]]]:
        name = name.lower()
        if name in ("global", "world", "ot"):
            return "world", None
        possible_country_names = (get_country_name(name, self.iso_codes.iso_codes),
                                  get_iso2_code(name, self.iso_codes.iso_codes),
                                  get_iso3_code(name, self.iso_codes.iso_codes))
        if name in (x.lower() for x in possible_country_names if x is not None):
            return "country", name
        elif name in self.provinces:
            return "province", name
        elif name in self.american_states:
            return "state", name
        return None

    @staticmethod
    async def _parse_datetime_strings(data_dict: dict):
        """
        Parses date strings from a dict and returns datetime.date objects instead of strings

        :param data_dict: Dictionary of data that will be parsed.
        :return: Same data dict, but with date objects instead of strings.
        """
        out_dict = {}
        for key in data_dict:
            if isinstance(key, str):
                continue
            dt = from_time_to_date(time.strptime(key, "%m/%d/%y"))
            out_dict[dt] = data_dict[key]
        return out_dict

    async def get_country_stats(self, country: str):
        """
        Return historical stats for any given country.

        :param country: ISO-3166 2-digit country code, or anything accepted by get_iso2_code.
        :return: The stats for the country if found. Provinces are included in the data. If not found, returns None.
        """
        await self._check_stats_are_valid()
        if country not in self.countries:
            iso2_code = get_iso2_code(country.lower(), self.iso_codes.iso_codes)
            if iso2_code not in self.countries:
                raise CountryNotFound()
        else:
            iso2_code = country
        return self.countries[iso2_code]

    async def get_province_stats(self, province: str):
        """"""
        await self._check_stats_are_valid()
        province = province.lower()
        if province in self.provinces:
            return self.provinces[province]
        raise ProvinceNotFound()

    async def get_state_stats(self, state: str):
        """"""
        await self._check_stats_are_valid()
        state = state.lower()
        if state in self.american_states:
            return self.american_state_stats[state]["all"]
        raise ProvinceNotFound()

    @staticmethod
    async def _get_stats_for_day(stats: dict, date: datetime.date):
        if date in stats["timeline"]["cases"]:
            return {"cases": stats["timeline"]["cases"][date],
                    "recovered": stats["timeline"]["recovered"][date],
                    "deaths": stats["timeline"]["deaths"][date]}
        date_str = f"{date.month}/{date.day}/{str(date.year)[2:4]}"
        if date_str in stats["timeline"]["cases"]:
            return {"cases": stats["timeline"]["cases"][date_str],
                    "recovered": stats["timeline"]["recovered"][date_str],
                    "deaths": stats["timeline"]["deaths"][date_str]}
        return None

    @staticmethod
    async def _get_stats_for_dates(stats: dict, dates: List[datetime.date]):
        final_data = {"cases": {},
                      "recovered": {},
                      "deaths": {}}
        for key in ["cases", "recovered", "deaths"]:
            for date in filter(lambda x: x in dates, stats["timeline"][key]):
                final_data[key][date] = stats["timeline"][key][date]
        return final_data

    async def get_country_stats_for_day(self, country: str, date: datetime.date):
        """"""
        cty_stats = await self.get_country_stats(country)
        return await self._get_stats_for_day(cty_stats, date)

    async def get_province_stats_for_day(self, country: str, province: str, date: datetime.date):
        """"""
        cty_stats = await self.get_province_stats(province)
        return await self._get_stats_for_day(cty_stats, date)

    async def get_country_stats_for_dates(self, country: str, dates: List[datetime.date]):
        """"""
        cty_stats = await self.get_country_stats(country)
        return await self._get_stats_for_dates(cty_stats, dates)

    async def get_province_stats_for_dates(self, country: str, province: str, dates: List[datetime.date]):
        """"""
        cty_stats = await self.get_province_stats(province)
        return await self._get_stats_for_dates(cty_stats, dates)


class Covid19StatsWorldometers:
    """
    Class for stats on COVID-19 via the https://disease.sh API's Worldometers section.
    """

    def __init__(self, add_ids: bool = False, *, update_stats: bool = False,
                 logging_level=logging.INFO):
        """
        Class to get data about COVID-19 for every country (data from Worldometers).

        :param add_ids: Add a unique ID to every country, starting from 1.
        :param update_stats: Whether to update stats on class initalization or wait for a explicit call to do so.
                             Doing it in the __init__ makes the init time a lot longer, and it's synchronous: for this
                             reason, it defaults to being disabled.
        """
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats Worldometers", level=logging_level)
        self.logger.setLevel(logging_level)
        self._has_been_updated: bool = False
        self._update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.last_updated_utc: datetime.datetime = datetime.datetime.utcfromtimestamp(-1)
        self.global_stats: dict = {}
        self.country_stats: Dict[dict] = {}
        self.continent_stats: list = []
        self.continents: list = []
        self.american_states: list = []
        self.american_state_stats: Dict[dict] = {}
        self.iso_codes: List[dict] = []
        if update_stats:
            self.update_covid_19_virus_stats()

    async def _do_update(self):
        await self.update_covid_19_virus_stats()

    # noinspection PyTypeChecker
    async def update_covid_19_virus_stats(self, *, session: aiohttp.ClientSession = None):
        """
        Updates the stats, parses them, and loads it into memory.

        :param session: Optional: aiohttp.ClientSession to use. Defaults to making a new session.
        :return: None
        :raises NetworkException: if a AIOHttp error is raised, this error is raised. You can get the original
                                  exception via e.exc.
        """
        self._update_tries += 1
        self.logger.info('Opening new AIOHttp session...')
        session = session if session is not None else aiohttp.ClientSession()
        async with session as session:
            self.logger.info("Getting new country data...")
            try:
                data = await get_data(session, "https://disease.sh/v3/covid-19/countries?allowNull=true")
            except NetworkException as e:
                await _handle_client_exceptions(self, e)
                return
            self.logger.info("Got country data! Parsing data and loading it into memory...")
            for country in data:
                if country['countryInfo']['iso2'] is not None:
                    try:
                        country["activeCaseChange"] = int(country["todayCases"]) - (country["todayDeaths"] +
                                                                                    country["todayRecovered"])
                    except TypeError:
                        country["activeCaseChange"] = None
                    self.country_stats[country['countryInfo']['iso2']] = country
                    iso_code = dict(country=country["country"], iso2=country["countryInfo"]["iso2"],
                                    iso3=country["countryInfo"]["iso3"])
                    self.iso_codes.append(iso_code)
            self.logger.info("Getting world stats...")
            self.global_stats = await get_data(session, "https://disease.sh/v3/covid-19/all?allowNull=true")
            self.logger.info("Got world stats.")
            self.logger.info("Getting continent stats...")
            self.continent_stats = await get_data(session, "https://disease.sh/v3/covid-19/continents?allowNull=true")
            for continent in self.continent_stats:
                self.continents.append(continent["continent"])
            self.logger.info("Got continent stats.")
            self.logger.info("Getting American state stats...")
            us_state_stats = await get_data(session, "https://disease.sh/v3/covid-19/states?allowNull=true")
            for state in us_state_stats:
                self.american_states.append(state["state"].lower())
                self.american_state_stats[state["state"].lower()] = state
        self.last_updated_utc = datetime.datetime.utcnow()
        self._has_been_updated = True
        self.data_is_valid = True
        self.logger.info("Done!")

    async def try_to_get_name(self, test_name: str) -> Optional[Tuple[str, Optional[str]]]:
        test_name = test_name.lower()
        if test_name in ("global", "world", "ot"):
            return "world", None
        possible_country_names = (get_country_name(test_name, self.iso_codes),
                                  get_iso2_code(test_name, self.iso_codes),
                                  get_iso3_code(test_name, self.iso_codes))
        if test_name in (x.lower() for x in possible_country_names if x is not None):
            return "country", test_name
        for name in self.continents:
            if test_name == name.lower():
                return "continent", test_name
        for name in self.american_states:
            if test_name == name.lower():
                return "state", test_name
        return None

    async def _check_stats_are_valid(self):
        """
        Checks that all stats are valid.

        :raises NoDataAvalible: when data isn't valid
        :return: always None
        """
        if not self._has_been_updated:
            raise NoDataAvailable()

    async def get_all_iso_codes(self) -> list:
        """
        Returns a global ISO code/country name list for all countries.

        :return: List of all ISO2/ISO3/country name mappings.
        """
        await self._check_stats_are_valid()
        return self.iso_codes  # waaaaaaay too simple lol

    async def get_global_stats(self) -> dict:
        """
        Returns stats for the world.

        :return: Dictionary of data about the world stats.
        """
        await self._check_stats_are_valid()
        return self.global_stats

    # noinspection PyTypeChecker
    async def get_country_stats(self, iso2_code: str) -> Optional[dict]:
        """
        Returns stats on a single country.

        :param iso2_code: ISO2 code for the country to return data for. Does not need to be a ISO2 code, will be
                          converted automatically.

        :return: Dictionary of data about the country (formatted the same as in get_global_stats). If a country is not
                 found, returns None.
        """
        await self._check_stats_are_valid()
        if iso2_code not in self.country_stats:
            iso2_code = get_iso2_code(iso2_code, self.iso_codes)
        if iso2_code not in self.country_stats:
            return None
        return self.country_stats[iso2_code]

    async def get_all_country_stats(self, *, use_list: bool = False):
        """
        Returns data for every single country avalible.

        :param use_list: Returns data formatted as a list.
        :return: Dict or List
        """
        await self._check_stats_are_valid()
        if use_list:
            country_stats = []
            for country in self.country_stats:
                country_stats.append(self.country_stats[country])
            return country_stats
        else:
            return self.country_stats

    async def get_sorted_list(self, sort_id: str, *,
                              reverse: bool = False) -> list:
        """
        Returns a list of data, sorted by the value passed in.

        :param sort_id: The key to sort by. Must be one of ("cases", "recovered", "deaths", "critical", "tests",
                        "population")
        :param reverse: If true, sort by least first.
        :return: List of data, sorted by the key passed in.
        :raises IncorrectSortType: when the sort type is incorrect.
        """
        await self._check_stats_are_valid()
        sort_id = str(sort_id).lower()
        if sort_id not in SORT_TYPES:
            raise IncorrectSortType("Need to sort by a valid sort type!")
        country_list = await self.get_all_country_stats(use_list=True)
        try:
            self.logger.info(f"Country list: {country_list}")
            self.logger.info(f"Sort ID: {sort_id}")
            return sorted(country_list, key=lambda k: k[sort_id], reverse=not reverse)
        except TypeError:
            raise IncorrectSortType()

    async def get_single_data(self, data: str):
        """
        Returns a dictionary of data, with keys being ISO2 IDs and the data being the sort type passed in.

        :param data: Must be one of SORT_TYPES. This is the data of each key.
        :return: Dictionary of data as described in the description.
        """
        await self._check_stats_are_valid()
        if data not in SORT_TYPES:
            raise IncorrectSortType("Need to sort by a valid sort type!")
        country_list = await self.get_all_country_stats(use_list=True)
        final_data = {}
        for country in country_list:
            final_data[country['countryInfo']['iso2']] = country[data]
        return final_data

    async def get_continent_stats(self, continent_name: str):
        await self._check_stats_are_valid()
        if continent_name.lower() not in [i.lower() for i in self.continents]:
            return None
        else:
            for continent in self.continent_stats:
                if continent_name.lower() == continent["continent"].lower():
                    return continent

    async def get_state_stats(self, state_name: str):
        await self._check_stats_are_valid()
        if state_name.lower() not in self.american_states:
            return None
        else:
            return self.american_state_stats[state_name.lower()]


class VaccineStats:
    """
    Class for stats on COVID-19 via the https://disease.sh API's vaccine section.
    """

    def __init__(self, add_ids: bool = False, *, update_stats: bool = False,
                 logging_level=logging.INFO):
        """
        Class to get data about the COVID-19 vaccine trials.

        :param add_ids: Add a unique ID to every country, starting from 1.
        :param update_stats: Whether to update stats on class initalization or wait for a explicit call to do so.
                             Doing it in the __init__ makes the init time a lot longer, and it's synchronous: for this
                             reason, it defaults to being disabled.
        """
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats for Vaccine", level=logging_level)
        self.logger.setLevel(logging_level)
        self.has_been_updated: bool = False
        self.update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.last_updated_utc: datetime.datetime = datetime.datetime.utcfromtimestamp(-1)
        self.source: AnyStr = ""
        self.total_candidates: int = 0
        self.phases: dict = {}
        self.candidates: List[dict] = []
        if update_stats:
            self.update_covid_19_vaccine_stats()

    async def _do_update(self):
        await self.update_covid_19_vaccine_stats()

    # noinspection PyTypeChecker
    # PyCharm ain't smart here
    async def update_covid_19_vaccine_stats(self, *, session: Optional[aiohttp.ClientSession] = None):
        self.update_tries += 1
        self.logger.info('Opening new AIOHttp session...')
        session = session or aiohttp.ClientSession()
        async with session as session:
            self.logger.info("Getting new vaccine data...")
            try:
                data = await get_data(session, "https://disease.sh/v3/covid-19/vaccine")
            except NetworkException as e:
                await _handle_client_exceptions(self, e)
                return
            self.logger.debug(f"Vaccine data: {data}")
            self.logger.info("Got vaccine data! Parsing and loading it into memory...")
            self.total_candidates = int(data['totalCandidates'])
            self.source = data['source']
            self.phases = data['phases']
            self.candidates = data['data']
            self.last_updated_utc = datetime.datetime.utcnow()
            if not len(self.candidates) == self.total_candidates:
                self.logger.fatal(f"Total number of vaccine candidates ({len(self.candidates)}) doesn't match the "
                                  f"amount returned by the API ({self.total_candidates})! Leaving data in place to "
                                  f"avoid more exceptions later.")
                self.data_is_valid = False
                return
            self.data_is_valid = True
            self.logger.info("Parsed and loaded vaccine data into memory sucessfully!")


if __name__ == '__main__':
    asyncio.run(VaccineStats(update_stats=False).update_covid_19_vaccine_stats())
