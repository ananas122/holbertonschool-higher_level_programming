#!/usr/bin/python3
"""Write a function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index in row: # for each element in the row of the matrix that should be printed as  an integer
            if index is not row[len(row) - 1]: # if the last element is not the last element in the row and index is not the last element in the row then print the element as an integer with a space between each element and the last element in
                print("{:d}".format(index), end=" ") # print the element as an integer with a space between each element
            else: # if the last element is not the last element in the row and index is not the last element in the row then print the element as an integer with a space between each element
                print("{:d}".format(index), end="")
        print()
