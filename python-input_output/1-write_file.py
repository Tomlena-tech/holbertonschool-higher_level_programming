#!/usr/bin/python3
""" Create a function who's write a string into a text and returns number of character"""


def write_file(filename="", text=""):
    """Write and count the number of character"""
    with open(filename, 'w', encoding= 'utf-8') as f:
        return f.write(text)
