#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv
    # db = MySQLdb.connect(host='localhost', database='hbtn_0e_0_usa')
    db = MySQLdb.connect(database=args[3], password=args[2], host=args[1])

    conn = db.cursor()

    conn.execute("""SELECT * FROM states ORDER BY id ASC""")


    states = conn.fetchall()

    for state in states:
        print(state)
