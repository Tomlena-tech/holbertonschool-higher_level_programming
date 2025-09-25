#!/usr/bin/env python3
"""History around the DuckShape with area and perimeter !!!"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



class Rectangle(Shape): 
    def __init__(self, height, width):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)    
     
    def shape_info(shape):
            print(f"Aire: {shape.area()}")
            print(f"Périmètre: {shape.perimeter()}")
     
     