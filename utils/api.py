# coding=utf-8
# Licenced under the CC BY-NC-SA 4.0 licence: by modifying any code you agree to be bound by the terms of the
# licence: https://creativecommons.org/licenses/by-nc-sa/4.0/

import asyncio
import warnings
import logging
import aiohttp
import datetime
from typing import Optional, List, AnyStr, Dict, Union

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


class NoDataAvalible(BaseAPIException):
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
        else:
            return None
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
        else:
            return
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
        else:
            return
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


# TODO: fix JHUCSSE API: basically everything about it
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
        self._has_been_updated: bool = False
        self._update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats Worldometers", level=logging_level)
        self.last_updated_utc: int = -1  # 0 is 00:00:00 1 Jan 1970, don't want that
        self.global_historical_stats: dict = {}
        self.historical_stats: dict = {}
        if update_stats:
            self.update_covid_19_virus_stats()

    # noinspection PyTypeChecker
    async def update_covid_19_virus_stats(self, *, session: aiohttp.ClientSession = aiohttp.ClientSession()):
        """
        Updates the stats, parses them, and loads it into memory.

        :param session: Optional: aiohttp.ClientSession to use. Defaults to making a new session.
        :return: None
        :raises NetworkException: if a AIOHttp error is raised, this error is raised. You can get the original
                                  exception via e.exc.
        """
        pass


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
        self._has_been_updated: bool = False
        self._update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats Worldometers", level=logging_level)
        self.last_updated_utc: datetime.datetime = datetime.datetime.utcfromtimestamp(-1)
        self.global_stats: dict = {}
        self.country_stats: Dict[dict] = {}
        self.continent_stats: list = []
        self.continents: list = []
        self.iso_codes: List[dict] = []
        if update_stats:
            self.update_covid_19_virus_stats()

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
                self.logger.exception("ClientException while getting vaccine data!",
                                      e.exc)
                if self._has_been_updated:
                    return  # We know there's valid data in here, so leave it be
                elif self._update_tries <= MAX_UPDATE_TRIES:
                    await self.update_covid_19_virus_stats()  # Force another update if we haven't reached the max
                    # tries count
                else:
                    self.logger.fatal("Failed to update! Data will not be avalible! Expect exceptions on later calls!")
                    self._update_tries = 0
                return
            self.logger.info("Got country data! Parsing data and loading it into memory...")
            for country in data:
                if country['countryInfo']['iso2'] is not None:
                    try:
                        country["activeCaseChange"] = country["todayCases"] - (country["todayDeaths"] +
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
        self.last_updated_utc = datetime.datetime.utcnow()
        self._has_been_updated = True
        self.data_is_valid = True
        self.logger.info("Done!")

    async def _check_stats_are_valid(self):
        """
        Checks that all stats are valid.

        :raises NoDataAvalible: when data isn't valid
        :return: always None
        """
        if not self._has_been_updated:
            raise NoDataAvalible()

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
    async def get_country_stats(self, iso2_code: str) -> dict:
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
                country_stats.append(country)
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
            self.logger.debug(f"Country list: {country_list}")
            self.logger.debug(f"Sort ID: {sort_id}")
            return sorted(country_list, key=lambda k: k[sort_id], reverse=reverse)
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
            else:  # Should never happen
                raise RuntimeError("Data in self.continent_stats must have been modified between entering this "
                                   "function and trying to return data!")


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
        self.has_been_updated: bool = False
        self.update_tries: int = 0
        self.data_is_valid: bool = False
        self.add_ids: bool = add_ids
        self.logger: logging.Logger = logging.Logger("COVID-19 Stats for Vaccine", level=logging_level)
        self.last_updated_utc: datetime.datetime = datetime.datetime.utcfromtimestamp(-1)
        self.source: AnyStr = ""
        self.total_candidates: int = 0
        self.phases: dict = {}
        self.candidates: List[dict] = []
        if update_stats:
            self.update_covid_19_vaccine_stats()

    # noinspection PyTypeChecker
    # PyCharm ain't smart here
    async def update_covid_19_vaccine_stats(self, *, session: Optional[aiohttp.ClientSession] = None):
        self.update_tries += 1
        self.logger.info('Opening new AIOHttp session...')
        session = session if session is not None else aiohttp.ClientSession()
        async with session as session:
            self.logger.info("Getting new vaccine data...")
            try:
                data = await get_data(session, "https://disease.sh/v3/covid-19/vaccine")
                self.logger.debug(f"Vaccine data: {data}")
            except NetworkException as e:
                self.logger.exception("ClientException while getting vaccine data!",
                                      e.exc)
                if self.has_been_updated:
                    return  # We know there's valid data in here, so leave it be
                elif self.update_tries <= MAX_UPDATE_TRIES:
                    await self.update_covid_19_vaccine_stats()  # Force another update if we haven't reached the max
                    # tries count
                else:
                    self.logger.fatal("Failed to update! Data will not be avalible! Expect exceptions on later calls!")
                    self.update_tries = 0
                return
            self.logger.info("Got vaccine data! Parsing and loading it into memory...")
            self.total_candidates = data['totalCandidates']
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
