#!/usr/bin/python3
"""
Module for Verification
"""

def inherits_from(obj, a_class):
    return (isinstance(obj, a_class) and type(obj) != a_class)
