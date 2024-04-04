#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Implements basic caching system.
    """
    def put(self, key, item):
        """ Add item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item by key.
        """
        return self.cache_data.get(key, None)
