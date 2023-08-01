#!/usr/bin/python3
"""
update state: given id, change state name
parameters given to script: username, password, database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # make engine for database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', 
        pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with id = 2
    state_id_to_update = 2
    state_to_update = session.query(State) \
        .filter_by(id=state_id_to_update).first()

    # Check if the State object exists
    if state_to_update is None:
        print(f"State with id = {state_id_to_update} not found")
    else:
        # Update the name of the State object
        new_name = "New Mexico"
        state_to_update.name = new_name
        session.commit()

    # Close the session
    session.close()
