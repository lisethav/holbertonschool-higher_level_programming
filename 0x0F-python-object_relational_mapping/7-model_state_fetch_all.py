#!/usr/bin/python3
"""
This is module 7-model_state_fetch_all
After using mysqldb to connect to a mysql database, same questions are done
again with sqlalchemy
"""
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), echo=False)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    for state in session.query(State.id, State.name).order_by(State.id).all():
        print("{:d}: {}".format(state.id, state.name))

    session.close()
