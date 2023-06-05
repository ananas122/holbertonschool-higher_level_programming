#!/usr/bin/python3
"""Write a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in row:
            print("{:d}".format(index), end=" ")
        print()
