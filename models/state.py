#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    """for sqlalchemy"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="states")

    @property
    def cities(self):
        """getter aall cities of State"""
        from models import storage
        all_cities = []
        for c in list(storage.all(City).values()):
            if c.state_id == self.id:
                all_cities.append(c)
        return all_cities
