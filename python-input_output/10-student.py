#!/usr/bin/python3
""" This function is used to generate the output of the command """
import json


class Student:
    """ Defines a class student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs = None):
   
        if attrs is None:
            return self.__dict__

        if attrs:
            if not all(isinstance(attr, str) for attr in attrs):
               raise TypeError
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

        return self.__dict__
