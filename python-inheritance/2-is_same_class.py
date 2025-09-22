#!/usr/bin/python3
"""Defines a function who returns the object / instance / class true or false""" 
def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, otherwise False
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
