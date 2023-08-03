#!/usr/bin/python3
"""
prints all City objects from the db hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


# Make engine for database
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                        format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(City, State).join(State)

# Query all City objects and join with State on state_id to get state info
cities = session.query(City, State).join(State).order_by(City.id).all()

# Iterate through the cities and print their info
for city, state in cities:
    print(f"{state.name}: ({city.id}) {city.name}")

