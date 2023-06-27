#!/usr/bin/python3
""" module Square that inherits from Rectangle:"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class a Square that inherites by Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        # Call the superclass constructor to initialize the obj
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Define a string representation of a Rectangle obj """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Get the size of the Square """
        return self.width

    @size.setter
    def size(self, value):
        """ Set the size of the Square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update rectangle attributes. """
        # Arg positionnel
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

        # Arg keyword
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.width = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """ Retrun dictonary """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
