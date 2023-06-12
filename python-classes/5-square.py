#!/usr/bin/python3
class Square:
    """Define a class Square that defines a square by: (based on 3-square.py"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("the message size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.size

    def my_print(self):
        for index in range(self.__size):
            for lenght in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
