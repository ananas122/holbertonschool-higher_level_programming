#!/usr/bin/python3
"""
Module for Verification
"""


def inherits_from(obj, a_class):
    """Returns True or false if obj inherits from a_class or not"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
