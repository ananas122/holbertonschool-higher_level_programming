"""Write a function that adds all unique integers in a list"""


def uniq_add(my_list=[]):

    result = sum(set(my_list))
    return result


