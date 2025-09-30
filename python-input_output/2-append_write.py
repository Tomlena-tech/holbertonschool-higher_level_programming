#!/usr/bin/python3
""" Create a function who's appends a string a the end of a text and returns number of character added"""


def append_write(filename="", text=""):
    """Add a string a the end of a string and count the number of character"""
    with open(filename, 'a', encoding= 'utf-8') as f:
        return f.write(text)
