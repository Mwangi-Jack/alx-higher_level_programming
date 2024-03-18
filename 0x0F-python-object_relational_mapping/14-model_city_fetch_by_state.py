#!/usr/bin/python3

"""
a script to print  all 'City' objects from the database
'hbtn_0e_14_usa'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]),
                           pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    result = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
