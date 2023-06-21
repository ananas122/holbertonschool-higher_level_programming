#!/usr/bin/python3
""" Function that writes an Object to a text file,
using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ Write a JSON representation for to serial """
    with open(filename, "w") as filename:
        return json.dump(my_obj, filename)
