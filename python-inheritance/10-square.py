#!/usr/bin/python3
""" Write a square class inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    
    def __init__(self, size): 
        """Initialyse a square with size"""
        
        
        self.integer_validator("size", size)
        super().__init__(size, size)
    
