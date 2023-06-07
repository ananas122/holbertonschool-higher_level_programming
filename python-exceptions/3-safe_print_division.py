#!/usr/bin/python3
"""Write a func that prints the first x elements of a list and only int"""


def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = "None"
    finally:
        print("Inside result: {}".format(result))
    return result
