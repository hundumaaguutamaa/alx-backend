#!/usr/bin/env python3
""" Caching system. """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class inhereted from BaseCaching"""

    def put(self, key, item):
    """ Add an item in the cache. """
        if not (key is None or item is None):
            self.cache_data[key] = item


    def get(self, key):
    """ Get an item by key. """
    if key is None or key not in self.cache_data:
        return None
    return self.cache_data.get(key)
