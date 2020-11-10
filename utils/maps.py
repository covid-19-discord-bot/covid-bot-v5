# coding=utf-8
from selenium.common import exceptions
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import os
import logging
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

        self.firefox: Optional[webdriver.Firefox] = None

    async def initalize_firefox(self):
        """
        Simply starts up Firefox.
        :return:
        """
        self.firefox = await wrap_in_async(webdriver.Firefox, firefox_profile=self.firefox_profile, options=self.options)

    def get_maps(self):
        print("Initalizing Firefox... ", end="")
        try:
            ff = self.firefox
            ff.set_window_size(1920, 1080)  # 1080p
        except:
            print("\n", end="")
            raise
        else:
            print("done!")

        print("Downloading graphs...")
        for each_graph in data:
            print(f"Getting graph {each_graph[0].split('.')[0]}...", end=" ")
            ff.get(each_graph[1])

            sleep(15)

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
            os.rename(f"{BASE_PATH}/coronavirus-data-explorer.png", f"{BASE_PATH}/{each_graph[0]}")
            print("done!")

        print("Shutting down Firefox...", end=" ")
        ff.quit()
        print("done!")
