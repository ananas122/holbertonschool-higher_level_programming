#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns the attribute or method of an object"""
    return dir(obj)
