#!/usr/bin/python3
""" Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object """
import sys


def class_to_json(obj):
    """Return the description in dictionnary of an object for Json"""
    return obj.__dict__
