#!/usr/bin/python3
"""Write a func that returns a tuple with the len of a str, its 1st char"""


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
