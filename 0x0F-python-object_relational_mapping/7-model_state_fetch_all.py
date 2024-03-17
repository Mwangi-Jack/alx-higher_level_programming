#!/usr/bin/python3

"""Script to fetch all 'state' objects from the
database 'hbtn_0e_6_usa
"""

import sys
from inflect import engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine(f'mysql://{args[1]}:{args[2]}@localhost:3306/{args[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()


    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
