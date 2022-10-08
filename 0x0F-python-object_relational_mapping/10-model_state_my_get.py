#!/usr/bin/python3
"""This prints the State object with the name passes as argument
from database hbtn_0e_6_usa"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).filter_by(name=sys.argv[4]).first()
    if not results:
        print("Not found")
    else:
        print(results.id)

    session.close()

