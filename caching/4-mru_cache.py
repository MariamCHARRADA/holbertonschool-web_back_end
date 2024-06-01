#!/usr/bin/python3
""" LIFO caching system """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.mostRecentKey = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.mostRecentKey:
                print("DISCARD: {}".format(self.mostRecentKey))
                self.cache_data.pop(self.mostRecentKey)

        self.cache_data[key] = item
        self.mostRecentKey = key

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            item = self.cache_data[key]
            self.mostRecentKey = key
            return item
        return None
