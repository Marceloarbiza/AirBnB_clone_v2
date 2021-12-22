""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # name = ""
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        """ init """
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        """ storage """
        from models import storage
        ret_cities = []
        all_cities = storage.all(City)
        for c in all_cities.values():
            if c.state_id == seld.id:
                ret_cities.append(c)
        return ret_cities
