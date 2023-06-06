#!/usr/bin/python3
"""Write a func that returns a list with all val *a number ."""


def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x: x * number, my_list)))
