#!/usr/bin/python3
"""Module for basic JSON serialization and deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """ Serialize a Python dictionnary to a Json file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """ Load and deserialize data from Json"""
    with open(filename, 'r',encoding='utf-8') as file:
        return json.load(file)
