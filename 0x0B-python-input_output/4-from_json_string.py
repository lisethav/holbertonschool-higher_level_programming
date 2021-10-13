#!/usr/bin/python3
"""
Function that returns an object (Python data structure) represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """ from_json_string returns a json string into a python object """
    return json.loads(my_str)
