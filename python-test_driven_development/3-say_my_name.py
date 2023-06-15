#!/usr/bin/python3
"""
Write a function that prints My name is <first name> <last name>

"""

def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    print(f"My name is {first_name} {last_name}")

