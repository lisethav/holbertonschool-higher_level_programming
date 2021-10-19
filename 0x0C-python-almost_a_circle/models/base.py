#!/usr/bin/python3
"""
A module with a
class for the base of the rest of clases
"""
import json
import os


class Base():
    """ initialization method """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
