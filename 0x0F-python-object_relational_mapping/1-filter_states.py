#!/usr/bin/python3
""" This lists all the states with a name starting with "N" """

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])
    cur= db.cursor()

    cur.execute("Select * FROM states WHERE states.name LIKE 'N%'\
            ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("({}, {})".format(row[0], row[1]))

    cur.close()
    db.close()
