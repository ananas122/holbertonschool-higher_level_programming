#!/usr/bin/python3
"""Lists all states  starting with 'N' from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution requêtes SQL
    cur.execute("SELECT * FROM states \
                WHERE name LIKE '{}' \
                ORDER BY states.id ASC".format('Arizona'))

    # Récupération des résultats
    states = cur.fetchall()

    # Affichage des résultats
    for state in states:
        print(state)

    cur.close()
    db.close()
