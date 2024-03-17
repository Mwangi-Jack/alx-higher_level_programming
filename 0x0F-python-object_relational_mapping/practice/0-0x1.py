#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.sql import column
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+mysqldb://jason2000:Jack2000@localhost/hbtn_0c_0', echo=True)

engine = create_engine('mysql:///hbtn_0c_0')
Session = sessionmaker(bind=engine)
session = Session()

if not engine:
    print('Failed to connect to database')
else:
    print(engine)
    print('Connnetion successful')


conn = engine.connect()
print(conn)

for instance in session.query('first_table').all()
