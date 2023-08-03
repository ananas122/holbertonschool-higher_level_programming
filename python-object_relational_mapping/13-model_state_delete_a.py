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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                            format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)

    # Créer une session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour sup ts les objets State dont le nom contient "a"
    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)

    # Commit des changements et fermeture de la session
    session.commit()
    session.close()
