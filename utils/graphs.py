# coding=utf-8
"""
Utility module to generate graphs nicely.
"""
import random
import time
import datetime
import os
from multiprocessing import Lock
from typing import Optional
from matplotlib import pyplot, ticker

DISCORD_BG_COLOR = (0.15625, 0.16796875, 0.1875)

BASE_IMAGE_PATH = "/home/dustin/PycharmProjects/covid_bot_v5/temp_data/plots"
_IMAGE_IDS = {}
_NEXT_IMAGE_ID = 0
_LOCK = Lock()


def from_time_to_date(in_time: time.struct_time) -> datetime.date:
    """
    Convert a time.struct_time object to a datetime.date object quickly.

    :param in_time: The time.struct_time object you would like to convert.
    :return: datetime.date object that contains the same month/day/year as the struct_time object passed in.
    """
    return datetime.date(year=in_time.tm_year,
                         month=in_time.tm_mon,
                         day=in_time.tm_mday)


def get_new_path():
    with _LOCK:
        image_id = _NEXT_IMAGE_ID
        image_id += 1
        image_path = str(os.path.join(BASE_IMAGE_PATH, f"{image_id}.png"))
        _IMAGE_IDS[image_id] = image_path
        return image_path, image_id


def parse_percents(_input: float) -> float:
    return round(_input, 2)


def generate_line_plot(country_data: dict,
                       country_name: str,
                       start_time: Optional[datetime.date] = None,
                       end_time: Optional[datetime.date] = None,
                       logarithmic: bool = False):
    """
    Generate a plot detailing COVID-19 cases for a country.

    :param country_data: Data for the country: expects this to be a dict with root keys 'cases', 'recovered', and
                        'deaths'. Each of those keys should contain a dict with keys formatted 'mm/dd/yy' for the count
                        for that day.
    :param country_name: The country name. Set as the title, not used for anything else.
    :param start_time: Optional: filter to only show data points after this date. Note: the system used for calculating
                       the total number of dates to show isn't very smart and can sometimes make weird values if this is
                       set.
    :param end_time: Optional: filter to only show data points before this date. Same note as for start_time applies.
    :param logarithmic: Optional: defaults to false. If true, a logarithmic graph will be generated instead of a linear
                        one.
    :return: A ID that can be passed to get_image to get a absolute path to the image.
    """
    start_time = start_time or datetime.date(1970, 1, 1)
    end_time = end_time or datetime.date(2038, 1, 19)  # https://en.wikipedia.org/wiki/Year_2038_problem
    image_path, image_id = get_new_path()
    f: pyplot.Figure = pyplot.figure(image_id, (10.24, 10.24), 100, DISCORD_BG_COLOR, DISCORD_BG_COLOR, linewidth=5)
    for _key in ['cases', 'recovered', 'deaths']:
        a = []
        b = []
        if _key in country_data:
            for key, i in zip(country_data[_key], range(len(country_data[_key]))):
                date = from_time_to_date(time.strptime(key, "%m/%d/%y"))
                if start_time < date < end_time:
                    a.append(key)
                    b.append(country_data[_key][key] if logarithmic else country_data[_key][key] / 1000)
        if _key == "deaths":
            color = "red"
        elif _key == "cases":
            color = "blue"
        elif _key == "recovered":
            color = "green"
        elif _key == "active":
            color = "yellow"
        else:
            color = "black"
        pyplot.plot(a, b, label=_key.capitalize(), color=color)
    time_between_start_and_end = start_time - end_time
    if time_between_start_and_end.days < 8:
        delta = 1
    elif time_between_start_and_end.days < 15:
        delta = 2
    elif time_between_start_and_end.days < 29:
        delta = 4
    elif time_between_start_and_end.days < 50:
        delta = 7
    elif time_between_start_and_end.days < 100:
        delta = 14
    elif time_between_start_and_end.days < 150:
        delta = 21
    elif time_between_start_and_end.days < 200:
        delta = 28
    elif time_between_start_and_end.days < 300:
        delta = 56
    elif time_between_start_and_end.days < 400:
        delta = 84
    else:
        delta = 112
    ax = f.add_subplot(111)
    # noinspection SpellCheckingInspection
    ax.xaxis.set_major_locator(ticker.MultipleLocator(delta))
    pyplot.xticks(rotation=90)
    pyplot.xlabel("Date")
    if logarithmic:
        label = "Cases"
    else:
        label = "Cases (in thousands)"
    pyplot.ylabel(label)
    pyplot.legend()
    pyplot.title(f"COVID-19 Stats in {country_name}")
    pyplot.yscale("log" if logarithmic else "linear")
    f.savefig(image_path,
              facecolor=DISCORD_BG_COLOR,
              edgecolor=DISCORD_BG_COLOR,
              transparent=True,
              format="png")
    return image_path


def generate_pie_chart(overall_data: dict,
                       title: str,
                       force_include: Optional[str] = None, *,
                       ignore_below_pct: float = 1.25,
                       randomize: bool = False):
    """
    Generate a pie chart detailing COVID-19 cases/deaths/etc for a global area.

    :param overall_data: Expected to be a dict of data, the key will be the title, and the value is the value.
                         This dict must contain a 'all' key that is the total count of cases/deaths/etc..
    :param title: Chart title.
    :param force_include: Forcibly include this country in the list, no matter the percentage it makes up. If this is
                          passed, ignore_below_percent is set to at least 2.25.
    :param ignore_below_pct: Group countries making up less than this percentage of the total into "Other". Defaults to
                             1.5%.
    :param randomize: If true, randomize the order in which data is placed into the chart.
    :raises ValueError: if overall_data does not contain a 'all' key.
    :return: A ID that can be passed to get_image to get a absolute path to the image.
    """
    if 'all' not in overall_data:
        raise ValueError("The dict passed into generate_pie_chart() must contain a 'all' key!")
    if force_include is not None and ignore_below_pct < 2.25:
        ignore_below_pct = 2.25
    name = []
    data = []
    overall_total = overall_data['all']
    other_total = 0
    for key in overall_data:
        if key == "all":
            continue
        if (overall_data[key] / overall_total) * 100 <= ignore_below_pct:
            if force_include is not None:
                if not force_include.lower() == key.lower():
                    other_total += overall_data[key]
                    continue
            else:
                other_total += overall_data[key]
                continue
        if randomize:
            location_to_insert = random.randint(0, len(name))
            name.insert(location_to_insert, key)
            data.insert(location_to_insert, overall_data[key])
        else:
            name.append(key)
            data.append(overall_data[key])
    name.append("Other")
    data.append(other_total)
    pyplot.pie(data, labels=name, autopct=parse_percents, shadow=True)
    pyplot.title(title)
    image_path, image_id = get_new_path()
    pyplot.savefig(image_path,
                   facecolor=DISCORD_BG_COLOR,
                   edgecolor=DISCORD_BG_COLOR,
                   transparent=True,
                   format="png")
    return image_id


def get_image(_id: int) -> Optional[str]:
    """
    Returns absolute path to a chart, given the ID.
    One-time use function: the image ID is deleted after being retrieved via this function.

    :param _id: ID of the chart you'd like to get data for.
    :return: Absolute path to the chart: not a file-like object.
    """
    if _id not in _IMAGE_IDS:
        return None
    else:
        image_path = _IMAGE_IDS[_id]
        del _IMAGE_IDS[_id]
        return image_path
