#!/usr/bin/python3
"""This creates the state 'Califonia' with the City
    'San Francisco' from the database hbtn_0e_100_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State
from relationship_city import City
from model_state import Base

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name="Califonia")
    newCity = City(name="San Francisco")
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)

    session.commit()
    session.close()
