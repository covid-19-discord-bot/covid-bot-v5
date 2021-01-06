# coding=utf-8
import time
from typing import Optional, Any


class TTLCache:
    def __init__(self, expiry_time: int = 3600, **kwargs):
        """
        Create a dict that has items that expire after a time.
        :param expiry_time:
        """
        self.expiry_time = expiry_time
        self._items = {}
        for arg in kwargs:
            self.__setitem__(arg, kwargs[arg])

    def __getitem__(self, item):
        if item in self._items:
            init_time = self._items[item][1]
            if time.time() - init_time >= self.expiry_time:
                del self._items[item]
                return
            else:
                return self._items[item][0]
        else:
            return

    def __delitem__(self, key):
        """
        Deletes the item from the internal dictionary. Calls del self._items[key], so can raise KeyError if not found.
        :param key:
        :return:
        """
        del self._items[key]

    def __setitem__(self, key, value):
        entry_time = time.time()
        self._items[key] = [value, entry_time]

    def get(self, key, if_not_found: Optional[Any] = None):
        item = self._items.get(key, if_not_found)
        if item == if_not_found:
            return if_not_found
        else:
            if time.time() - item[1] >= self.expiry_time:
                del self._items[key]
                return if_not_found
            else:
                return item[0]

    def __contains__(self, item):
        """
        Strongly recommended to use .get instead. If the item is found, it will get it, meaning this operation could
        take as long as 100 microseconds.
        :param item: 
        :return: 
        """
        item_is_in = item in self._items
        if not item_is_in:
            return False
        else:
            if time.time() - self._items[item][0] >= self.expiry_time:
                del self._items[item]
                return False
            else:
                return True
