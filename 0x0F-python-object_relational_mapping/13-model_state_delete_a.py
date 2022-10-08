#!/usr/bin/python3
"""This deletes all state objects wth a name containing the letter
'a' from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)

    for result in results:
        for n in range(len(result.name)):
            if result.name[n] == 'a':
                session.delete(result)
                break

    session.commit()
    session.close()
