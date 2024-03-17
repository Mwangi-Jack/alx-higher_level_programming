#!/usr/bin/python3

"""
script that takes in the 'name' of a state as an argument
 and lists all 'cities' of that state using the database
 'hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(host='localhost',
                         user=args[1], passwd=args[2], database=args[3])

    conn = db.cursor()

    conn.execute("SELECT name FROM \
        cities WHERE state_id = (SELECT id \
        FROM states WHERE name = %s);", (args[4],))

    cities = conn.fetchall()

    for city in cities:
        print(city[0], end=" ")
