#!/usr/bin/python3
""" Defines a Rectangle class with width and height properties, and methods to calculate area and perimeter.
"""
class Rectangle:
    """Defines a rectangle by width and height."""
    number_of_instances = 0
    """Defines number of instances counting"""
    print_symbol = "#"
    """Print symbol reprensentation"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
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
        """Defines the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """ Defines perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)
    def __str__(self):
        """Returns the rectangle as a string of # characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])
        """print symbol into the string"""
        
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width
            if i != self.__height - 1:
                rect += "\n"
        return rect
    def __repr__(self):
        """Returns a string representation that can recreate the instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """Deleting an instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
