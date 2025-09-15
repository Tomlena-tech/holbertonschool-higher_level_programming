#!/usr/bin/python3
class Rectangle:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    def width(self):
        return self.__width
    
    def width(self, value): 
        if value < 0:
            raise ValueError("width must be >= 0")
        if type (value) != int:
            raise TypeError("width must be an integer")
        self.__width = value
    
    
    def height(self):
        return self.__height
    
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if type (value) != int:
            raise TypeError ("height must be an integer")
        self.__height = value
