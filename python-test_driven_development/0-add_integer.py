#!/usr/bin/python3
"""
Module that provides integer addition functionality.

This module contains a function to safely add two numbers,
ensuring they are integers or can be converted to integers.
It includes proper error handling for invalid input types.
The function supports default values for cleaner usage.
"""


def add_integer(a, b=98):
    """
    Return the sum of a and b as integers.
    
    This function validates input types and converts floats to integers.
    
    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.
    
    Returns:
        int: The sum of a and b as integers.
    
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
