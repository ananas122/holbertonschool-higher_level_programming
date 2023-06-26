#!/usr/bin/python3
""" module Rectangle based class Base """
from models.base import Base


class Rectangle(Base):
    """Class a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute."""
        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height attribute."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height


    def __str__(self):
        """Define a string representation of a Rectangle obj """
        return (f"[Rectangle]({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def display(self):
        """
        Display a rectangle with the given height
        and width at the x and y location.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
