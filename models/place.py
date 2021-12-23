#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
import models
from models.review import Review
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float

storage_type = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if storage_type == "db":

        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False)

        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete")
    else:

        @property
        def reviews(self):
            """ Getter that that returns the list of Reviews instances """
            review_instances = models.storage.all(Review)
            new_list = []
            for value in review_instances.values():
                if value.place_id == (self.id):
                    new_list.append(value)
            return (new_list)

        @property
        def amenities(self):
            """ Getter that that returns the list of Amenities instances """
            amenities_instances = models.storage.all()
            new_list = []
            for value in amenities_instances.values():
                if value.id in self.amenity_ids:
                    new_list.append(value)
            return (new_list)

        @amenities.setter
        def amenities(self, obj):
            """ Append id to the atrribute """
            if obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)
