# coding=utf-8
import itertools


# noinspection PyUnreachableCode
async def find_nearest_match(msg: str, country_list: list):
    return NotImplemented
    nearest_matches = []
    itertools.permutations("STRING", 1)
    for letter, i in zip(msg, range(0, len(msg))):
        for country in country_list:
            if country["country"][i] == letter:
                pass
