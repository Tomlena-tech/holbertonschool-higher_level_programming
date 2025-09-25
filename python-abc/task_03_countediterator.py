#!/usr/bin/env python3
""" Build an iterator who gives elements one by one"""

class CountedIterator:
    """Create a class CountedIterator"""
    
    def __init__(self, iterable):
        """Builder"""
        self.iterator = iter(iterable)
        self.count = 0
        
    def get_count(self):
        """Defines counting """
        return self.count
    
    def __next__(self):
        """Next method for counting"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
    def __iter__(self):
        """Pour que ça marche avec for loops"""
        return self
