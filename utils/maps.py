# coding=utf-8
from selenium.common import exceptions
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import os
import logging
import io
from utils.async_helpers import wrap_in_async
from typing import Optional

# 1: what to rename the file to
# 2: the URL to get the image from
# 3: optional description
data = [["total_covid_cases_per_million.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map"
                                              "&zoomToSelection=true&country=~OWID_WRL&region=World&casesMetric=true"
                                              "&interval=total&hideControls=true&perCapita=true&smoothing=0&pickerMetric=location&pickerSort=asc", ""],
        ["total_covid_cases.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true"
                                  "&country=~OWID_WRL&region=World&casesMetric=true&interval=total&hideControls=true"
                                  "&smoothing=0&pickerMetric=location&pickerSort=asc", ""],
        ["total_deaths.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true"
                             "&country=~OWID_WRL&region=World&deathsMetric=true&interval=total&hideControls=true"
                             "&smoothing=0&pickerMetric=location&pickerSort=asc", ""],
        ["total_deaths_per_million.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map"
                                         "&zoomToSelection=true&country=~OWID_WRL&region=World&deathsMetric=true"
                                         "&interval=total&hideControls=true&perCapita=true&smoothing=0&pickerMetric"
                                         "=location&pickerSort=asc", ""],
        ["tests.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true&country"
                      "=~OWID_WRL&region=World&testsMetric=true&interval=total&hideControls=true&smoothing=0"
                      "&pickerMetric=location&pickerSort=asc", ""],
        ["tests_per_1k.png", "https://ourworldindata.org/coronavirus-data-explorer?tab=map&zoomToSelection=true"
                             "&country=~OWID_WRL&region=World&testsMetric=true&interval=total&hideControls=true"
                             "&perCapita=true&smoothing=0&pickerMetric=location&pickerSort=asc", ""]]


class MapGetter:
    def __init__(self, base_path):
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

    def _check_if_set_up(self):
        if not self.set_up:
            raise RuntimeError("The map system is not initialized! Call initalize_firefox() ASAP!")

    def initalize_firefox(self):
        """
        Simply starts up Firefox. Running this function means the client is ready to use.
        :return: always None
        """
        self.firefox = await wrap_in_async(webdriver.Firefox, thread_pool=True,
                                           firefox_profile=self.firefox_profile, options=self.options)
        self.set_up = True

    def download_maps(self):
        self._check_if_set_up()
        self.logger.info("Setting up Firefox...")
        ff = self.firefox
        ff.set_window_size(1920, 1080)  # 1080p
        self.logger.info("Done setting up Firefox!")

        self.logger.info("Getting maps...")
        for each_graph in data:
            self.logger.info(f"Getting graph {each_graph[0].split('.')[0]}...")
            ff.get(each_graph[1])

            sleep(15)  # it takes a little while to load the page

            try:
                share_button = ff.find_element_by_css_selector("li.tab:nth-child(5)")
            except exceptions.NoSuchElementException:
                print("No share button!")
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
                print("No download link!")
                continue
            else:
                # noinspection PyStatementEffect
                download.location_once_scrolled_into_view
                download.click()
            sleep(5)
            os.rename(f"{self.base_path}/coronavirus-data-explorer.png", f"{self.base_path}/{each_graph[0]}")
            print("done!")

        print("Shutting down Firefox...", end=" ")
        ff.quit()
        print("done!")
