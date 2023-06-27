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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Converts a list of dictionaries """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            json.dump([obj.to_dictionary() for obj in list_objs], file)

    def from_json_string(json_string):
        """Create a new instance of the class from a json string """
        if not json_string:
            return "[]"
        return json.loads(json_string)
