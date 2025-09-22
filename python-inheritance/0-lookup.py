#!/usr/bin/python3
"""Defines how do you print attributes and methods of an objects"""
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
    
