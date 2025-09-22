#!/usr/bin/python3

"""Defines a function that returns True if the object is an instance 
    of a class that inherited (directly or indirectly) from the specified class ; otherwise False. """
    
def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited from a_class
    (but not if obj is exactly an instance of a_class)
    
    Args:
        obj: The object to check
        a_class: The class to compare against
        
    Returns:
        bool: True if obj inherits from a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
