#!/usr/bin/env python3
""" MRU Caching module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching implemenmtation. """

    def __init__(self):
        """ Initializing the MRU cache. """
        super().__init__()
        self.recency = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache. """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.recency.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """Discard the most recently used item""" 
                discard = next(reversed(self.recency))
                del self.cache_data[discard]
                self.recency.pop(discard)
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item
            self.recency[key] = None

    def get(self, key):
        """ Get an item by key. """
        if key is None or key not in self.cache_data:
            return None
        
        self.recency.move_to_end(key)
        return self.cache_data[key]

