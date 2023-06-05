#!/usr/bin/python3
"""Write a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in row:
            if index is not row[len(row) - 1]:
                print("{:d}".format(index), end=" ")
            else:
                print("{:d}".format(index), end="")
        print()
