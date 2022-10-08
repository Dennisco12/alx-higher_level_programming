#!/usr/bin/python3
"""This is the class definition of a state and an
    instance Base = declarative_base() """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
            unique=True, nullable=False)
    name = Column(String(128), nullable=False)
