#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""

from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State class

    Keyword arguments:
    Base (class instance) -- this class inherits from the base Class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
