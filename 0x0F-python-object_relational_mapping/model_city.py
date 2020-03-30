#!/usr/bin/python3
"""
Write a python file that contains the class definition of a City and an
instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# base class for our classes definitions.
Base = declarative_base()


class City(Base):
    """ City class """

    # to indicate what is the name of the table that will support this class.
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
