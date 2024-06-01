#!/usr/bin/env python3
""" FIFO caching system """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for k, v in self.cache_data.items():
                    print(f"DISCARD: {list(self.cache_data.keys())[0]}")
                    break
                self.cache_data.pop(k)

    def get(self, key):
        """get an item by key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
