#!/usr/bin/env python3
""" LIFO Caching module
"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching implementation. """

    def __init__(self):
        """ Initialize the LIFO cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: the key for the cache item
            item: the value for the cache item
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop()
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item

        self.order.append(key)

    def get(self, key):
        """ Get an item by key
        Args:
            key: the key to retrieve from the cache
        Returns:
            The value of the key if it exists, otherwise None
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]

