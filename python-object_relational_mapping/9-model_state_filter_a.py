#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    # make engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
