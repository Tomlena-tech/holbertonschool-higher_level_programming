#!/usr/bin/python3
"""Crete a function who's returns an Python's object from json string"""
import json

def from_json_string(my_str):
    """Return an object from json"""
    return json.loads(my_str)
