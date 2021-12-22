#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship('Place', cascade="all, delete-orphan",
                              backref='user')
        reviews = relationship('Review', cascade="all, delete-orphan",
                               backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
