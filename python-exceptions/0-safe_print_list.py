#!/usr/bin/python3
"""Write a func that prints the first x elm of a list and only int"""


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
