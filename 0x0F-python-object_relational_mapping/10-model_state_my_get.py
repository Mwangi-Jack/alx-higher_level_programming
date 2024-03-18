#!/usr/bin/python3

"""
Script that prints 'State' object with the 'name'
passed as argument from the database 'hbtn_0e_6_usa'
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))

    Session = sessionmaker()
    session = Session(bind=engine)

    state = session.query(State).filter(State.name == args[4]).first()

    if not state:
        print('Not found')
    else:
        print(state.id)
