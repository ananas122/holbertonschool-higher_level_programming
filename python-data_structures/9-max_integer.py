#!/usr/bin/python3
"""Write a function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    # If the list is empty, return None
    if my_list == 0:
        return None
#  initialize to 0 for to get the first number in the list
    max_integer = 0
    for i in my_list:
        if i > max_integer:
            max_integer = i

    return max_integer
