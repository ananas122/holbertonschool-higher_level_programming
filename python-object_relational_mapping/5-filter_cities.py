#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution requêtes SQL
    cur.execute(
        "SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id", (sys.argv[4],))

    # Recuperation des résultats
    rows = cur.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))

    cur.close()
    db.close()
