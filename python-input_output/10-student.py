#!/usr/bin/python3
"""student class"""


class Student:
    """class stuff"""
    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if isinstance(attrs, list) and all(isinstance(key, str) for key in attrs):
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        else:
            return self.__dict__
