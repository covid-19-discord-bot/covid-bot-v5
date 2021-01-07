# coding=utf-8
import copy
import io
import logging
import os
from time import sleep
from typing import Optional

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.options import Options

map_identifiers = {"total_cases_per_million": ["total_covid_cases_per_million.png", "Total COVID-19 Cases Per Million",
                                               "https://ourworldindata.org/coronavirus-data-explorer?tab=map"
                                               "&zoomToSelection=true&country=~OWID_WRL&region=World&casesMetric=true"
                                               "&interval=total&hideControls=true&perCapita=true&smoothing=0"
                                               "&pickerMetric=location&pickerSort=asc"],
                   "total_cases": ["total_covid_cases.png", "Total COVID-19 Cases",
                                   "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true"
                                   "&country=~OWID_WRL&region=World&casesMetric=true&interval=total&hideControls=true"
                                   "&smoothing=0&pickerMetric=location&pickerSort=asc"],
                   "total_deaths": ["total_deaths.png", "Total COVID-19 Deaths",
                                    "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true"
                                    "&country=~OWID_WRL&region=World&deathsMetric=true&interval=total&hideControls=true"
                                    "&smoothing=0&pickerMetric=location&pickerSort=asc"],
                   "total_deaths_per_million": ["total_deaths_per_million.png", "Total COVID-19 Deaths Per Million",
                                                "https://ourworldindata.org/coronavirus-data-explorer?tab=map"
                                                "&zoomToSelection=true&country=~OWID_WRL&region=World&deathsMetric=true"
                                                "&interval=total&hideControls=true&perCapita=true&smoothing=0"
                                                "&pickerMetric=location&pickerSort=asc"],
                   "tests": ["tests.png", "Total COVID-19 Tests",
                             "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true&country"
                             "=~OWID_WRL&region=World&testsMetric=true&interval=total&hideControls=true&smoothing=0"
                             "&pickerMetric=location&pickerSort=asc"],
                   "tests_per_thousand": ["tests_per_1k.png", "Total COVID-19 Tests per Thousand",
                                          "https://ourworldindata.org/coronavirus-data-explorer?tab=map"
                                          "&zoomToSelection=true&country=~OWID_WRL&region=World&testsMetric=true"
                                          "&interval=total&hideControls=true&perCapita=true&smoothing=0"
                                          "&pickerMetric=location&pickerSort=asc"]}


class MapGetter:
    def __init__(self, base_path, *, save_resources=False):
        """
        :param base_path: Base path where images will be temporarily downloaded. They will be deleted shortly
                          after download.
        :param save_resources: Whether to save resources by quitting Firefox after use.
        """
        self.save_resources = save_resources

        self.logger = logging.Logger("Maps System")
        self.logger.info("Initalizing map system...")

        options = Options()
        options.headless = True

        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', base_path)
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'image/png')

        self.options = options
        self.firefox_profile = profile
        self.base_path = base_path
        self.firefox: Optional[webdriver.Firefox] = None
        self.set_up = False
        self._local_init_call = False  # unused if self.save_resources is false
        self.maps = {}
        self.logger.info("Initalized map system.")

    def _check_if_set_up(self):
        if not self.set_up:
            raise RuntimeError("The map system is not initialized! Call initalize_firefox() ASAP!")

    def initalize_firefox(self):
        """
        Simply starts up Firefox. Running this function means the client is ready to use.
        :return: always None
        """
        if self.save_resources and not self._local_init_call:
            raise RuntimeError("You cannot manually initalize Firefox when save_resources is True!")
        self.firefox = webdriver.Firefox(firefox_profile=self.firefox_profile, options=self.options)
        self.set_up = True

    def download_maps(self):
        if not self.save_resources:
            self._check_if_set_up()
        self.logger.info("Setting up Firefox...")
        if self.save_resources:
            self._local_init_call = True
            self.initalize_firefox()
            self._local_init_call = False
        self._check_if_set_up()
        ff = self.firefox
        ff.set_window_size(1920, 1080)  # 1080p
        self.logger.info("Done setting up Firefox!")

        self.logger.info("Getting maps...")
        for each_graph in map_identifiers:
            self.logger.info(f"Getting graph {each_graph}...")
            ff.get(map_identifiers[each_graph][2])

            sleep(15)  # it takes a little while to load the page

            try:
                share_button = ff.find_element_by_css_selector("li.tab:nth-child(5)")
            except exceptions.NoSuchElementException:
                self.logger.error("No share button!")
                continue
            else:
                # noinspection PyStatementEffect
                share_button.location_once_scrolled_into_view
                share_button.click()
            sleep(5)

            try:
                download = ff.find_element_by_css_selector(".img-downloads > a:nth-child(1) > div:nth-child(1) > "
                                                           "aside:nth-child(2) > h2:nth-child(1)")
            except exceptions.NoSuchElementException:
                self.logger.error("No download link!")
                continue
            else:
                # noinspection PyStatementEffect
                download.location_once_scrolled_into_view
                download.click()
            sleep(10)

            with open(f"{self.base_path}/coronavirus-data-explorer.png", "rb") as f:
                self.maps[each_graph] = io.BytesIO(f.read())
            os.unlink(f"{self.base_path}/coronavirus-data-explorer.png")
            self.logger.info("done!")
        if self.save_resources:
            ff.quit()

    @staticmethod
    def get_map_names() -> list:
        return [key for key in map_identifiers]

    def get_map(self, map_name: str) -> Optional[io.BytesIO]:
        self._check_if_set_up()
        if map_name not in map_identifiers:
            return None
        return copy.deepcopy(self.maps[map_name])  # we know it's already a io.BytesIO object
