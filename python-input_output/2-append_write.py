#!/usr/bin/python3
"""func that appends a str at the end of a text file
and returns the num of character added"""


def append_write(filename="", text=""):
    """Appends a str at the end of a text file and returns the number"""
    with open(filename, mode="a", encoding='utf-8') as file:
        return file.write(text)
