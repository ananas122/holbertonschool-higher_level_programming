#!/usr/bin/python3
""" Write a function that reload json """


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a JSON representation of the instance"""
        # If no attributes were specified, return the instance's dictionary
        if attrs is None:
            return self.__dict__

        # If a list of attributes was specified, filter the dictionary to only include those attributes
        elif isinstance(attrs, list):
            newDict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    newDict[key] = value
            return newDict
    def reload_from_json(self, json):
        """ reloads from json """
        self.__dict__ = json
