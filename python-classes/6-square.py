#!/usr/bin/python3
"""module 6-square.py that defines a square by: (based on 5-square.py)"""
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """"initialise the data"""
        self.size = size
        self.position = position
        
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
        return(self.__position)
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value


