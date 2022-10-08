#!/usr/bin/python3
"""This prints all the city objects from the database hbtn_0e_14_usa"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id)
    for city in cities:
        states = session.query(State).all()
        for state in states:
            if state.id == city.state_id:
                print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
