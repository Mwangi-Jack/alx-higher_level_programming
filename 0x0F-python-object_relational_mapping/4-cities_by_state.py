#!/usr/bin/python3

"""
Script to list all 'cities' from the database
'hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], database=args[3])

    conn = db.cursor()

    conn.execute("SELECT id, name, \
        (SELECT name FROM states WHERE id = state_id) from cities")

    cities = conn.fetchall()

    for city in cities:
        print(city)
