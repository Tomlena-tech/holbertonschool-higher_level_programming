#!/usr/bin/python3
"""module 6-square.py that defines a square by: (based on 5-square.py)"""
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """initialise the data"""
        self.size = size
        self.position = position
        
    @property
    def size(self):
        """Getter for size

        Returns:
            _type_: self.__size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value (_type_): value to set size to
        returns:
            _type_: None
        """
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        """Position getter"""
        return(self.__position)
    
    @position.setter
    def position(self, value):
        """position Setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def area(self):
        """ Area method that returns the current square area"""
        return(self.__size ** 2)
    
    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)


