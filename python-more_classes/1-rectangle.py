#!/usr/bin/python3
class Rectangle:
    def width(self):
        return self.__width
    def width(self, value): 
        if value < 0:
            raise ValueError("width must be >= 0")
        if type value != int:
            raise TypeError("width must be an integer")
        return self.__width = value
