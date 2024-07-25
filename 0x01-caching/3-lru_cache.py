#!/usr/bin/env python3
""" LRU Caching module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching implementation. """

    def __init__(self):
        """ Initializing the LRU cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache. """
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
        """ Get an item by key. """
        if key is None or key not in self.cache_data:
            return None
        
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

