#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """ Mylist is subclass of list class """

    def __init__(self):
        """Initialization of the class"""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted array"""
        print(sorted(self))
