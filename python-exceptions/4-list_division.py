#!/usr/bin/python3
"""Write a function that divides element by element 2 lists"""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists"""
    result = []
    for i in range(list_length):
        division = 0
        try:
            division = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("wrong type")
        except (ZeroDivisionError, ValueError):
            print("division by zero")
        except (IndexError):
            print("out of range")
        finally:
            result.append(division)
    return result
