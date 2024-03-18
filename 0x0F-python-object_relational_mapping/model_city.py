#!/usr/bin/python3

"""A database model 'City' """

from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """
    Class City
    """

    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False,)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
