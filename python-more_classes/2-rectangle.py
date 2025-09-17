#!/usr/bin/python3
""" Defines a Rectangle class with width and height properties, and methods to calculate area and perimeter.
"""
class Rectangle:
    """Defines a rectangle by width and height."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle with validation"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value
    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """sets the height of the rectangle with validation"""
        if value < 0: 
            raise ValueError("height must be >= 0")
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        self.__height = value
     
    def area(self): 
        """Defines the area of the redctangle"""
        return self.__width * self.__height
    def perimeter(self):
        """ Defines parameter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)
