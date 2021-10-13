#!/usr/bin/python3
"""
Function that writes an Object to a text file, using a JSON
representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ ave_to_json_file write a string respresetation in json"""
    with open(filename, mode="") as file:
        file.write(json.dumps(my_obj))
