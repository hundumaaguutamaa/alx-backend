class MRUCache(BaseCaching):
    """MRUCache is a caching system that inherits from BaseCaching.
    It discards the most recently used item (MRU algorithm).
    """

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.keys) >= self.MAX_ITEMS:
                discard = self.keys.pop()
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Get an item by key."""
        if key is not None and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data.get(key)
        return None
