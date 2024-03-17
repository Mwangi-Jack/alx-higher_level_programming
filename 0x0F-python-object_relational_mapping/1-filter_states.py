#!/usr/bin/python3

"""
This script lists all states with a 'name'
starting with 'N' (uppercase N) from the database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2],
        database=sys.argv[3], port=3306)
    conn = db.cursor()
    # cur.execute("SELECT * FROM states WHERE UPPER(name) LIKE 'N%' ")
    conn.execute("SELECT * \
    FROM states \
    WHERE CONVERT(`name` USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")

    states = conn.fetchall()

    for state in states:
        print(state)
