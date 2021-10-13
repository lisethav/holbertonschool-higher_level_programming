#!/usr/bin/python3
"""
Function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ append_write appends a text to a file """
    with open(filename, mode="w", encoding='utf-8') as file:
        return(file.write(text))
