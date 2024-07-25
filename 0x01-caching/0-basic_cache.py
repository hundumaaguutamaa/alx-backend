#!/usr/bin/env python3
"""
Base caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Inherited BaseCaching
    """

    def put(self, key, item):
        """
        Put key and data
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value of key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
