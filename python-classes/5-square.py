#!/usr/bin/python3
"""module 5-square.py that defines a square by: (based on 4-square.py) """
class Square:
    """Defines a square with size and area methods, and a my_print method."""
    
    def __init__(self, size=0):
        """"initialise the data"""
        self.size = size
        
    @property
    def size (self):
        return self.__size
        
    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
    
    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
