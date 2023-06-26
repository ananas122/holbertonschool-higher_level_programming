#!/usr/bin/python3
""" module Rectangle based class Base """
from models.base import Base


class Rectangle(Base):
    """ Rectangle that inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Construct a Rectangle from a Rectangle object """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
