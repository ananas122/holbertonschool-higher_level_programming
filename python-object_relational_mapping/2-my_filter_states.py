#!/usr/bin/python3
'''
    Prend un argument et affiche toutes les valeurs de la table des états de
    hbtn_0e_0_usa où le nom correspond à l'argument
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id".format(argv[4])
    )
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    db.close()
