#!/usr/bin/env python3
"""LFU caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache is a caching system that inherits from BaseCaching.
    It discards the least frequency used item (LFU algorithm).
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.keys = []
        self.counts = {}

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
                self.counts[key] += 1
            else:
                if len(self.keys) >= self.MAX_ITEMS:
                    min_freq_key = min(self.counts, key=lambda k: (self.counts[k], self.keys.index(k)))
                    self.keys.remove(min_freq_key)
                    del self.cache_data[min_freq_key]
                    del self.counts[min_freq_key]
                    print(f"DISCARD: {min_freq_key}")
                self.counts[key] = 1
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is not None and key in self.cache_data:
            self.counts[key] += 1
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None

