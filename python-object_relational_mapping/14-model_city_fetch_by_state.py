#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


# make engine for database
user = sys.argv[1]
passwd = sys.argv[2]
db = sys.argv[3]
engine = create_engine(
    f'mysql+mysqldb://{user}:{passwd}@localhost/{db}',
    pool_pre_ping=True)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
query = session.query(City, State).join(State)

# Query all City objects and join with State on state_id to get state information
cities = session.query(City, State).join(State).order_by(City.id).all()

# Iterate through the cities and print their information
for city, state in cities:
    print(f"{state.name}: ({city.id}) {city.name}")
