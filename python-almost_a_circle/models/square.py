#!/usr/bin/python3
""" module Square that inherits from Rectangle:"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class a Square that inherites by Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        # Call the superclass constructor to initialize the obj
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Define a string representation of a Rectangle obj """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
