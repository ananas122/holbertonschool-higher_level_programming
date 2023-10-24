#!/usr/bin/python3
"""
return all state objects from database
"""



from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # make engine
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{passwd}@localhost/{db}', pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    if firstInstance := session.query(State).order_by(State.id).first():
        print("{:d}: {:s}".format(firstInstance.id, firstInstance.name))
    else:
        print("Nothing")

    session.close()
