#!/usr/bin/python3
"""
Module that defines MyList class
"""


class MyList(list):
    """
    MyList class that inherits from list
    """
    
    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
