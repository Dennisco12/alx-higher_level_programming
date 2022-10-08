#!/usr/bin/python3
"""This lists all the states that contains the letter "a" from the database
hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)

    for result in results:
        for n in range(len(result.name)):
            if result.name[n] == 'a':
                print("{}: {}".format(result.id, result.name))
                break

    session.close()
