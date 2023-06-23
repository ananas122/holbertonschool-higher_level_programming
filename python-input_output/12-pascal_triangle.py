#!/usr/bin/python3
""" Returns a list of lists of integers
representing the Pascal’s triangle of n """


def pascal_triangle(n):

    if n <= 0:
        return []

    # Initialize the first row of the triangle with a single value of 1
    triangle = [[1]]

    for row_num in range(1, n):
        # Init a new row with the first and last values set to 1
        curr_row = [1] * (row_num + 1)

        # Loop over the col in the new row, from col 1 to col row_num-1
        for col_num in range(1, row_num):
            # Sum the curr_col value as the sum of the values from the prev row
            curr_row[col_num] = triangle[row_num-1][col_num-1] + \
                     triangle[row_num-1][col_num]

        # Add the new row to the triangle
        triangle.append(curr_row)

    # Return the completed triangle
    return triangle
