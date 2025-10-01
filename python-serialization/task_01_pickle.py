#!/usr/bin/env python3
"""Create an instance of CustomObject"""


class CustomObject:
    def __init__(self, name, age, is_student):
        """Build CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Displaying attributs"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}") 
        print(f"Is_student: {self.Is_student}") 
    
    def serialize(self, filename):
        """Serialize the current instance to a file using pickle"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
                return None
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """ Deserialize an object from a file using pickle"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
            return None
