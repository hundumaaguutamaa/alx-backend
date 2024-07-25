#!/usr/bin/env python3
""" LFU Caching module
"""

from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Caching implementation. """

    def __init__(self):
        """ Initialize the LFU cache """
        super().__init__()
        self.frequency = defaultdict(int)
        self.recency = OrderedDict()

    def put(self, key, item):
        """ Adding an item in the cache """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.recency.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                if len(lfu_keys) == 1:
                    discard = lfu_keys[0]
                else:
                    discard = next(k for k in self.recency if k in lfu_keys)

                del self.cache_data[discard]
                del self.frequency[discard]
                del self.recency[discard]
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.recency[key] = None

    def get(self, key):
        """ Get an item by it's key """
        if key is None or key not in self.cache_data:
            return None
        
        self.frequency[key] += 1
        self.recency.move_to_end(key)
        return self.cache_data[key]
