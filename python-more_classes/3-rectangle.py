#!/usr/bin/python3
"""that defines a rectangle by: (based on 2-rectangle.py)"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns a str using #, empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        #  Crée une ligne horiz
        row = "#" * self.width
        #  initialise le string avec la ligne horiz
        rect = row
        # parcours et ajoute les lignes horizontales
        for _ in range(self.height):
            rect += "\n" + row
        return rect
