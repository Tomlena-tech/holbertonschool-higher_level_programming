#!/usr/bin/python3
""" Defines a full rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
                 
class Rectangle(BaseGeometry):
    """Defines a rectangle instance"""
   
    def __init__(self, width, height): 
        """ 
        initialise a rectangle instance
        ARGS : width (int): rectangle width
        height (int): rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        
    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """Defines a representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    
    
    
        
            