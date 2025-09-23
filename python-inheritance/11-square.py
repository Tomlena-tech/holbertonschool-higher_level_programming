#!/usr/bin/python3
"""A class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Classe Square in inheriting from Rectangle"""

    def __init__(self, size):
        """
        Builder for Square

        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Retourne l’aire du carré"""
        return self.__size * self.__size
    
    def __str__(self):
        """ return the square
        """
        return"[Square] {}/{}".format(self.__size, self.__size)

