#!/usr/bin/python3
"""Write a function that replaces an elm of a list at a specific position"""


def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list
