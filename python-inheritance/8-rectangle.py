#!/usr/bin/python3
"""
    class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class inherits from basegeometry """

    def __init__(self, width, height):
        """
        Initializes a rectangle
        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width
