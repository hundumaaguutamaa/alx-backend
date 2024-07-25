#!/usr/bin/env python3
""" LRU Caching module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching system """

    def __init__(self):
        """ Initialize the LRU cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: the key for the cache item
            item: the value for the cache item
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            self.cache_data.pop(discard)
            print(f"DISCARD: {discard}")

    def get(self, key):
        """ Get an item by key
        Args:
            key: the key to retrieve from the cache
        Returns:
            The value of the key if it exists, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        return self.cache_data[key]
