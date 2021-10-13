#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """ append_write appends a text to a file """
    return json.dumps(my_obj)
