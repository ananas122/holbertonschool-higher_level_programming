#!/usr/bin/python3
"""A module with a simple class"""


class Base:
    """ A simple class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is a constructor function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
