#!/usr/bin/python3
""" This function is used to generate the output of the command """
import json


class Student:
    """ Defines a class student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a JSON representation of the instance """
        # If no attributes were specified, return the instance's dict
        if attrs is None:
            return self.__dict__

        # If a list of attributes was specified, filter the dict
        elif isinstance(attrs, list):

            # Create a new dict empty for storing attributes specified
            newDict = {}

            # Loop over each key-value pair in the instance dict
            for key, value in self.__dict__.items():

                # check if the key is already in the dict
                if key in attrs:
                    # If the key is present, add the pair to a new dict
                    newDict[key] = value

        return newDict
