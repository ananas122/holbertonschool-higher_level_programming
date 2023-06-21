#!/usr/bin/python3
""" Write a class Student that defines a student by:
(based on 10-student.py)"""


class Student:
    """ Defines student class"""
    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(key) is str for key in attrs):
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of instance."""
        for key, value in json.items():
            setattr(self, key, value)
