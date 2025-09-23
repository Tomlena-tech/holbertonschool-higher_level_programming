#!/usr/bin/python3
"""
Module 10-square
Définit la classe Square qui hérite de Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square héritant de Rectangle"""

    def __init__(self, size):
        """
        Constructeur de Square

        Args:
            size (int): taille du carré
        """
        self.integer_validator("size", size)
        self.__size = size
        # Appel du constructeur de Rectangle avec size pour width et height
        super().__init__(size, size)

    def area(self):
        """Retourne l’aire du carré"""
        return self.__size * self.__size
