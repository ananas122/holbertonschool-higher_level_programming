#!/usr/bin/python3
"""Write a func that replaces an elm in a list at a specific
position without modifying the original list"""


def new_in_list(my_list, idx, element):
    # Return a copy of the original list if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()  # Create a copy of the original list
    new_list[idx] = element  # Replace the element at the specified index
    return new_list  # Return the new list
