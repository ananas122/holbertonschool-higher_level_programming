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

    def __str__(self) -> str:
        string = "[Rectangle] " + "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    def display(self):
        """ Print the Rectangle using the `#` character  """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """ Update rectangle attributes. """
        # Arg positionnel
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

        # Arg keyword
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'width' in kwargs:
            self.width = kwargs['width']
        if 'height' in kwargs:
            self.height = kwargs['height']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self):
        """ Return dictonary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
