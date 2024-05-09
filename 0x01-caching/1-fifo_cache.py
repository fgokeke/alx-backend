#!/usr/bin/env python3
""" FIFOCache module """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and
    implements a caching system using FIFO algorithm"""

    def __init__(self):
        """ Initializes FIFOCache """
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache if key and item are not None"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """Get an item from the cache by
        key if key is not None and exists in the cache"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
