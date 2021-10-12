#!/usr/bin/python3
"""
Function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """ inherits_from check if a instance is a sublclass specific"""
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
