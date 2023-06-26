#!/usr/bin/python3
""" Defines the base model class """


class Base:
    """Base class for objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        "initialize a new object"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

