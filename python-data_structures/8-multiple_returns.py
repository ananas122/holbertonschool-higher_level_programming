#!/usr/bin/python3
"""Write a func that returns a tuple with the len of a str, its 1st char"""


def multiple_returns(sentence):
    if sentence == "": # no return statement for empty string returns a tuple
        return (0, None) # empty string returns (0, None) as a tuple with len 0 and the 1st char returned as None as a tuple
    return (len(sentence), sentence[0])
