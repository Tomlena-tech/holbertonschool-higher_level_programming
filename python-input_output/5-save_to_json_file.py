#!/usr/bin/python3
""" Write a function that writes an Object to a text file, using a JSON representation """
import json

def save_to_json_file(my_obj, filename):
    """Function to save python object into json file"""
    with open(filename, 'w' ,encoding='utf-8') as f:
        json.dumb(my_obj, f)
