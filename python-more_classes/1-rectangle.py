#!/usr/bin/python3
    """Defines a Rectangle class with width and height properties, and methods to calculate area and perimeter.
    """
    class Rectangle:
    """ Represents a rectangle with width and height.
    """

    def __init__(self, width=0, height=0):
        """ Initialize a Rectangle instance."""
        self.width = width
        self.height = height
        
    def width(self):
        """ Getter for width"""
        return self.__width
    
    def width(self, value): 
        """ Setter for width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if type (value) != int:
            raise TypeError("width must be an integer")
        self.__width = value
    
    
    def height(self):
        """getter for height"""
        return self.__height
    
    def height(self, value):
        """setter for height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type (value) != int:
            raise TypeError ("height must be an integer")
        self.__height = value
