#!/usr/bin/python3
""""
Function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ is_same_class is a method that checks if an object
     is an instance of a given class"""
    if type(obj) == a_class:
        return True
    else:
        return False
