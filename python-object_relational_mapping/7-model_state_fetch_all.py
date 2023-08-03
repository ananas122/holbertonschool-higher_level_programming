#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    # Create the engine to connect to the db with pool_pre_ping=True
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}',
        pool_pre_ping=True
        )

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)

    # create a Session
    with Session() as session:
        # Query all State objects and sort them by id in ascending order
        for state in session.query(State).order_by(State.id):
            print(f"{state.id}: {state.name}")
