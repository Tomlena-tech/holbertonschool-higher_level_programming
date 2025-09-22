#!/usr/bin/python3
"""Defines a function who returns true or false if object is an istance or if the object is an instance of a class """


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherits from it

    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        bool: True if obj is an instance of a_class or inherits from it"""
    return isinstance(obj, a_class)
