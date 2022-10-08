#!/usr/bin/python3
""" Class declaration of the model_city"""

from relationship_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """This defines the class"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
            primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
