#!/usr/bin/python3
""" Create a fonction who's reading text """

def read_file(filename=""):
    """Read a file text in utf8 and print it int stdout"""
    with open(filename, 'r', encoding= 'utf-8') as f:
        print(f.read(), end='')
