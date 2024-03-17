#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

"""
Contains State class and Base, an instance of declarative_base()
"""


class State(Base):
    """State class

    Keyword arguments:
    Base (class instance) -- this class inherits from the base Class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
