#!/usr/bin/python3
""" Write a function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    with open(filename, 'w', encoding='utf_8') as f:
        json.load(filename)
