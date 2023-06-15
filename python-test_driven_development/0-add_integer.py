#!/usr/bin/python3
""" Write a function that adds 2 integers."""


def add_integer(a, b=98):
    """
    Verify is they are int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
