#!/usr/bin/python3
""" Class Square that defines a square by: (based on 3-square.py) """ 
class Square:
    """ Class Square that defines a square by: (based on 3-square.py) """
    def __init__(self, size=0):
        """ Initialize the data. """
        self.size = size

    @property
    def size(self):
        """ Get the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square. """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the current square area. """
        return self.__size * self.__size
