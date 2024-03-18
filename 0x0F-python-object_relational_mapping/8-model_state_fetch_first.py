#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.
                           format(args[1], args[2], args[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    print(f"{state.id}: {state.name}")
