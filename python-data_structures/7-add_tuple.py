#!/usr/bin/python3
"""Write a function that adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):

    listeA = list(tuple_a)
    listeB = list(tuple_b)

    listeA.extend((0, 0))
    listeB.extend((0, 0))

    resultat1 = listeA[0] + listeB[0]
    resultat2 = listeA[1] + listeB[1]

    return (resultat1, resultat2)
