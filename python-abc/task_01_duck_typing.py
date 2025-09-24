#!/usr/bin/env python3
"""History around the DuckShape with area and perimeter !!!"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass
