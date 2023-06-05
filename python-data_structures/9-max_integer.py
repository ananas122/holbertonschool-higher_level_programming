#!/usr/bin/python3
"""Write a function that finds the biggest integer of a list"""


def max_integer(my_list=[]):
    # If the list is empty, return None
    if my_list == 0:
        return None

    max_num = 0  #  initialize max_num to 0 for to get the first number in the list 
    for i in my_list:
        if i > max_num:
            max_num = i

    return max_num

