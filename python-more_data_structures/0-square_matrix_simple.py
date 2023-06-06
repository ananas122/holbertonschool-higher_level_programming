#!/usr/bin/python3
"""Write a function that computes the square val of all int of a matrix"""


def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x**2, row)) for row in matrix]
