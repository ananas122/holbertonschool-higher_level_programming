#!/usr/bin/python3
""" Function to return dictionary description for JSON serialization"""


def class_to_json(obj):
    """returns dictionary description for JSON serialization"""
    return obj.__dict__
