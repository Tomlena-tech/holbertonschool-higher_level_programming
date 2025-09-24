#!/usr/bin/env/python3
"""Set up and implement Abstract class"""
from abc import ABC, abstractmethod

class Animal(ABC):
    pass
    @abstractmethod
    def sound(self):
        pass
        
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
    
    
