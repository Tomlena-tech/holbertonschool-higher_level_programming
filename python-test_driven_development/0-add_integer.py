#!/usr/bin/python3
def add_integer(a, b=98):
    """Return the sum of a and b as integers.

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number. Defaults to 98.
if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

    Returns:
        int: The sum of a and b as integers.
    """
    if not isinstance(a and b), (int, float)):
        raise TypeError("a must be an integer")
        raise TypeError("b must be an integer")
    return int(a) + int(b)
