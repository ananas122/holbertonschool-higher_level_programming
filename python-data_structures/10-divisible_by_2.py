#!/usr/bin/python3
"""Write a function that finds all multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    newList = []
    for number in my_list:
        if number % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
    return newList
