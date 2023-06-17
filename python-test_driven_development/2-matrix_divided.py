#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
module 2-matrix_divided.py
"""


def matrix_divided(matrix, div):

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("All elements of the matrix should be integers or floats")

    new_matrix = [list(map(lambda x: round(x/div, 2), row)) for row in matrix]

    return new_matrix
