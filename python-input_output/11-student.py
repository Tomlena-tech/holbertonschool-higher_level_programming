#!/usr/bin/python3
"""Module that defines a Student class"""
import os
import sys


class Student:
    
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance
        
        Args:
            attrs: List of attribute names to retrieve (optional)
                   If None, all attributes are retrieved
        
        Returns:
            A dictionary containing the specified attributes
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        
        return self.__dict__
