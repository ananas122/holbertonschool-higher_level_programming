#!/usr/bin/python3
""" Module 0 """


def add_integer(a, b=98):
    """Return the sum of a and b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
