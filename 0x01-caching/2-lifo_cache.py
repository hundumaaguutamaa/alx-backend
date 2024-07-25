#!/usr/bin/env python3
""" LIFO Caching module

This module contains the LIFOCache class which implements a Last In, First Out (LIFO) caching system. 
It inherits from the BaseCaching class and provides a caching mechanism that discards the most 
recently added item when the cache reaches its maximum capacity.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching system

    This class provides a caching system that follows the Last In, First Out (LIFO) algorithm. 
    When the cache exceeds the maximum number of items allowed, the most recently added item 
    is discarded. It uses an internal list to keep track of the order in which items were added.
    """

    def __init__(self):
        """ Initialize the LIFO cache

        Sets up the cache and initializes an empty list to keep track of the order of items.
        Calls the parent class's initializer to set up the cache_data dictionary.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache

        Args:
            key: The key for the cache item.
            item: The value for the cache item.

        This method adds an item to the cache. If the cache exceeds the maximum number of items 
        allowed (BaseCaching.MAX_ITEMS), the most recently added item is discarded according to 
        the LIFO principle. If the item already exists, its value is updated and the key is moved 
        to the end of the order list.
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
