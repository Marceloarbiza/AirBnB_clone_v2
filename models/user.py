#!/usr/bin/python3
""" create a class user """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """User class"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place', cascade="all,delete-orphan", backref='user')
    reviews = relationship('Review', cascade="all,\
        delete-orphan", backref='user')
