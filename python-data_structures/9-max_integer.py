#!/usr/bin/python3
"""Write a function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    # If the list is empty, return None
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
