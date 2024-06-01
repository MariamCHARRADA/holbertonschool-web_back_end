#!/usr/bin/env python3
""" LIFO caching system """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mostRecent = self.remove
            self.cache_data.pop(mostRecent)
            print("DISCARD:", mostRecent)
        if key:
            self.remove = key

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
