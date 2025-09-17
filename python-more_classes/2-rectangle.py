#!/usr/bin/python3
""" Defines a Rectangle class with width and height properties, and methods to calculate area and perimeter.
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if width < 0:
            raise ValueError("width must be >= 0")
