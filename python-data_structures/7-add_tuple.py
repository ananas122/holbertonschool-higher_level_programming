#!/usr/bin/python3
"""Write a function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):

    listeA = list(tuple_a) # convert tuple to list for concatenation
    listeB = list(tuple_b)

    listeA.extend((0, 0)) # add 0 to the first tuple and add 0 to the second tuple (because they have the same length)
    listeB.extend((0, 0)) # add 0 to the first tuple

    resultat1 = listeA[0] + listeB[0] # add 0 to the first tuple and add 1 to the second tuple
    resultat2 = listeA[1] + listeB[1] # add 1 to the first tuple and add 1 to the second tuple

    return (resultat1, resultat2) # return the result
