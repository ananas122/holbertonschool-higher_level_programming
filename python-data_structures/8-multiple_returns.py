#!/usr/bin/python3
"""Write a func that returns a tuple with the len of a str, its 1st char"""


def multiple_returns(sentence):
    return (0, None) if sentence == "" else (len(sentence), sentence[0])
