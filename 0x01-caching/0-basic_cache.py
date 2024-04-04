#!/usr/bin/env python3
""" Caching system. """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Class inhereted from BaseCaching"""

    def put(self, key, item):
    """ Add an item in the cache. """
    if all([key, item]):
        self.cache_data[key] = item


    def get(self, key):
    """ Get an item by key. """
    return self.cache_data.get(key) if all([key, key in self.cache_data]) else None
