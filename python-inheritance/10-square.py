#!/usr/bin/python3
"""
    class Square that inherits from Rectangle (9-rectangle.py):
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square inherits from rectangle class """

    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        return self.__size * self.__size
