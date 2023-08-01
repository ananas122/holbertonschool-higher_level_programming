#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    pool_pre_ping=True

    # Create the engine to connect to the db
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}', pool_pre_ping=True)

    # Create a session to interact with the db
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # Query all State objects and sort them by id in ASC
    states = session.query(State).order_by(State.id).all()

    # Iterate through the states and print
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
