#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""


from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sq

Base = declarative_base()


class State(Base):
    """
    Class State
    """
    __tablename__ = "states"
    id = sq.Column(sq.Integer, primary_key=True, unique=True, nullable=False)
    name = sq.Column(sq.String(128), nullable=False)
