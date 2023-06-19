#!/usr/bin/python3
"""
Module 8-rectangle
class BaseGeometry (based on 7-base_geometry.py).
 width and height must be private.
        No getter or setter
        width and height must be positive integers,
        validated by integer_validator
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle"""
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
