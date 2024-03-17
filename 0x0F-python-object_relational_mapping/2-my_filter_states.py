#!/usr/bin/python3

"""
This script takes in an argument and displays all values in the 'states'
table of 'hbtn_0e_0_usa' where 'name' matches the argument
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    args = sys.argv
    db = MySQLdb.connect(host=args[1], password=args[2], database=args[3])

    conn = db.cursor()

    conn.execute("SELECT * FROM states WHERE name=%s", (args[4],))

    states = conn.fetchall()

    for state in states:
        print(state)
