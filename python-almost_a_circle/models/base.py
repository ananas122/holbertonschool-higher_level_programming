#!/usr/bin/python3
""" A module class Base """
import json


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

    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        return json.dumps(list_dictionaries)
