#!/usr/bin/python3
"""Write a function that returns the weighted average of all integers tuple (<score>, <weight>)"""

def weight_average(my_list=[]):
    if not my_list:  # Check if the list is empty
        return 0

    total_weight = 0
    weighted_sum = 0

    for score, weight in my_list:
        total_weight += weight
        weighted_sum += score * weight

    return weighted_sum / total_weight
