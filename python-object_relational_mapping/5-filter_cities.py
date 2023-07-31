import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s", (sys.argv[4],))

    rows = cur.fetchall()
    cities = set([row[0] for row in rows])

    print(", ".join(cities))

    cur.close()
    db.close()
