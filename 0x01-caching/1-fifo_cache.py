#!/usr/bin/env python3
""" FIFO Caching module

This module defines the FIFOCache class which implements a First In, First Out (FIFO) caching system. 
The FIFOCache class inherits from BaseCaching and uses a dictionary to store cached items. 
Items are discarded in the order they were added when the cache exceeds its maximum size.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching system

    This class provides a caching system that follows the First In, First Out (FIFO) algorithm. 
    When the cache exceeds its maximum size, the oldest item (the first item added) is discarded. 
    This class inherits from BaseCaching and uses the cache_data dictionary from the parent class.
    """

    def __init__(self):
        """ Initialize the FIFO cache

        Calls the parent class's __init__ method to initialize cache_data.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache

        Args:
            key: The key for the cache item.
            item: The value for the cache item.

        This method adds an item to the cache. If the cache exceeds its maximum number of items 
        (BaseCaching.MAX_ITEMS), the oldest item (FIFO) is discarded. If the item already exists, 
        its value is updated and the key is moved to the end of the order list.
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

            self.cache_data[key] = item

        self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value of the key if it exists in the cache; otherwise, returns None.

        This method retrieves the value associated with the specified key. If the key does not 
        exist or is None, it returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
