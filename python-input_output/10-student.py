#!/usr/bin/python3
""" Function that returns a list of strings representing the"""
import json


class Student:
    """A simple Student Class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age



    def to_json(self, attrs=None):
        if attrs is None:
            return json.dumps(self.__dict__)

        if not isinstance(attrs, list):
            return json.dumps(self.__dict__)

        new_dict = {}
        for attr in attrs:
            if not isinstance(attr, str):
                return json.dumps(self.__dict__)

            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]

        return json.dumps(new_dict)
