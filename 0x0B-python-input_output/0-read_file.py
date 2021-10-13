#!/usr/bin/python3
"""
Function that reads a text file 
"""


def read_file(filename=""):
    """ Function that reads and print """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
