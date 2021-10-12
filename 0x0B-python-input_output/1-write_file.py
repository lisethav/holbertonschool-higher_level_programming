#!/usr/bin/python3
"""
Function that writes a string to a text file and returns
the number of characters written
"""


def write_file(filename="", text=""):
    """ write_file writes a file or create """
    with open(filename, mode="w", encoding='utf-8') as file:
        return(file.write(text))
