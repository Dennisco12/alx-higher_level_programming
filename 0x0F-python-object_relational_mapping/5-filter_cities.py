#!/usr/bin/python3

"""This takes in the name of a state as argument and lists all cities
    of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id=states.id\
            WHERE states.name LIKE %s\
            ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()
    word = []
    for row in rows:
        word.append(row[0])
    print(", ".join(word))

    cur.close()
    db.close()
