#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.org import relationship, backref
from sqlalchemy import MetaData

class Place(BaseModel):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
        user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, defult=0)
        number_bathrooms = Column(Integer, nullable=False, defult=0)
        max_guest = Column(Integer, nullable=False, defult=0)
        price_by_night = Column(Integer, nullable=False, defult=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []
        reviews = relationship('Review', cascade="all, delete-orphan",
                               backref='place')
        amenities = relationship('Amenity' secondary='place_amenity',
                                 viewonly=False)

    else:
	city_id = ""
    	user_id = ""
    	name = ""
    	description = ""
    	number_rooms = 0
    	number_bathrooms = 0
    	max_guest = 0
    	price_by_night = 0
    	latitude = 0.0
    	longitude = 0.0
    	amenity_ids = []

        from models.engine import file_storage
	@property
        def amenities(self):
            return self.amenity_ids
        @amenities.setter
        def amenities(self, obj=None):
            if obj is not None and type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)

class plase_amenity(BaseModel):
    """ Instance of many to many relationship between
        Place and Amenities
    """
    __tablename__ = 'place_amenity'
    metadata = Base.metadata
    place_id = Column((String60), ForeignKey('places.id'), primary_key=True, nullable=False)
    amenity_id = Column((String60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
