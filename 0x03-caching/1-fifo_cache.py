#!/usr/bin/python3
""" BaseCache module"""
BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """FIFOCache system class"""
    def __init__(self) -> None:
        super().__init__()
        
    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard = list(self.cache_data)[0]
                self.cache_data.pop(discard)
                print(f'DISCARD:{discard}')
    
    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
