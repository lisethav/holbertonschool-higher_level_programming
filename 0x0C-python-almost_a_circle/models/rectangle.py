#!/usr/bin/python3
"""
A module that holds a class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ A class that inherits from base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
