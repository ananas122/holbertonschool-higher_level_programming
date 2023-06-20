#!/usr/bin/python3
""" Function that returns the dict description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object """

import json


def class_to_json(obj):
    return obj.__dict__
