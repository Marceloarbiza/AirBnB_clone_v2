""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.city import City, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # name = ""
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
			  cascade='all, delete-orphan')
    
    @property
    def cities(self):
        """ storage """
        from models.engine import file_storage
        ret_cities = []
        all_cities = file_storage.all(City)        
        for c in all_cities:
            if c.state_id == self.id:
                ret_cities.append(c)
        return ret_cities
