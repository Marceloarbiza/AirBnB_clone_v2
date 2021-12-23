#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if storage_type == "db":
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete, delete-orphan",
            passive_deletes=True)
    else:
        @property
        def cities(self):
            """ Getter that that returns the list of City instances """
            cities_instances = models.storage.all(City)
            new_list = []
            for value in cities_instances.values():
                if value.state_id == (self.id):
                    new_list.append(value)
            return (new_list)
