#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.sql.schema import Table
from models.review import Review
import models

# Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="delete, all", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False)
    else:

        @property
        def reviews(self):
            """ list of reviews"""
            review_instances = models.storage.all(Review)
            new_list = []
            for value in review_instances.values():
                if value.place_id == (self.id):
                    new_list.append(value)
            return (new_list)

        @property
        def amenities(self):
            """ list of amenities """
            amenities_list = []
            for value in models.storage.all().values():
                if value.id in self.amenity_ids:
                    amenities_list.append(value)
            return (amenities_list)

        @amenities.setter
        def amenities(self, obj):
            """ set id to respective atrribute """
            if obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
