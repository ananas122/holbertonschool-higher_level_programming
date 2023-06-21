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
         if attrs is None or type(attrs) is not list:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
            else:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
        return new_dict
