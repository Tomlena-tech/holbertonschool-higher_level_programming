#!/usr/bin/python3
""" Create a function who's write a string into a text and returns number of character"""


def write_file(filename="", text=""):
    with write_file(filename, 'w', text= "my_first_file.txt", encoding= 'utf-8') as f:
        print(f.read(), end='')
