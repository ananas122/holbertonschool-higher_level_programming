#!/usr/bin/python3
"""Write a function that returns a new dictionary with all values * 2"""


def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
