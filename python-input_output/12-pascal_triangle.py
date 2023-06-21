#!/usr/bin/python3
""" Create a function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n """



def pascal_triangle(n):
    """ Representing the pascal's triangle of n. """
    # Define matrix
    matrix = []

    # n stands for number of rows so we will iterate n times
    for x in range(n):
        # Define rows
        rows = []

        for y in range(x + 1):
            # Find the combination of x and y
            result = comb(x, y)

            # Append result to inner list
            rows.append(result)

        # Append inner list to matrix
        matrix.append(rows)

    # Return list of list
    return matrix