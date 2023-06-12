#!/usr/bin/python3
""""Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """Define a class Square that defines a square by: (based on 5-square.py"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.__size = size
        self.__position = 0
        self.__position = position

    @property
    def position(self):
        return self.__position

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

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positives integers")
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        return self.__size * self.size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
