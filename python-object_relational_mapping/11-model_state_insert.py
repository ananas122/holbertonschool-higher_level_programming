#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':

    # Create the engine to connect to the db with pool_pre_ping=True
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a session to interact with the db
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # query python
    new = State(name="Louisiana")
    session.add(new)
    session.commit()

    print(f"{new.id}")

    session.close()
