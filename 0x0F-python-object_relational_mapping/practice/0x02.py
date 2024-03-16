#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(database='hbtn_0c_0')

conn = db.cursor()

conn.execute("""SELECT * from first_table""")

items = conn.fetchall()

for item in items:
    print(item)
