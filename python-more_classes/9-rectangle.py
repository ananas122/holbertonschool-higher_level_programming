#!/usr/bin/python3
"""
Module creates the Rectangle class by 7-rectangle.py
"""


class Rectangle:
    """
    Class Rectangle with validated private instance attributes width and height
    """
    number_of_instances = 0  # New attribut of instances of Rectangle class
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the calculated area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of Rectangle instance"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """Returns a string of Rectangle instance using #, empty string"""
        if self.width == 0 or self.height == 0:
            return ""
        row = str(self.print_symbol) * self.width
        rect = row  # mise à jour
        for i in range(self.height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """"Returns a string representation of Rectangle instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.width * rect_1.height >= rect_2.width * rect_2.height:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
