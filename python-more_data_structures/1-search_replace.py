#!/usr/bin/python3
"""func that replaces all occurrences of an elm by another in a new list"""


def search_replace(my_list, search, replace):
    if my_list is None or search is None:
        return None
    if replace is None or search == replace:
        return my_list
    if search not in my_list:
        return my_list
    return [replace if x == search else x for x in my_list]
