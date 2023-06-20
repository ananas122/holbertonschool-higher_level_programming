#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """ List of MyList instances """

    def print_sorted(self):

        """ Print the list as a sorted list """
        print(sorted(self))
