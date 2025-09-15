#!/usr/bin/python3
"""Module that defines a Square class."""
class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
