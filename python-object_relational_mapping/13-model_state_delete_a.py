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

    # Créer une session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour supprimer tous les objets State dont le nom contient la lettre "a"
    session.query(State).filter(State.name.like('%a%')).delete()

    # Commit des changements et fermeture de la session
    session.commit()
    session.close()