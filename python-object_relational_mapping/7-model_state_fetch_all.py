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

    # Create the engine to connect to the database
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # Query all State objects and sort them by id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Iterate through the states and print their information
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
