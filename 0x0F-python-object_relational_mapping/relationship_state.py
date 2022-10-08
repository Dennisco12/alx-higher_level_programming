#!/usr/bin/python3
"""This is the class definition of a state and an
    instance Base = declarative_base() """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
Base = declarative_base()


class State(Base):
    """this defines the State class"""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
            unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='save-update, merge, delete',
            backref='state')
