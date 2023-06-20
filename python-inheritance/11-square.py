#!/usr/bin/python3
"""
    class Square that inherits from Rectangle (9-rectangle.py):
    based on task 10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square object representing a square rectangle with square """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        return super().area()
