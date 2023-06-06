#!/usr/bin/python3
""""Roman convertion"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    romanDic = {"I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
    num = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = romanDic.get(char, 0)
        num += value if value >= prev_value else -value
        prev_value = value

    return num
