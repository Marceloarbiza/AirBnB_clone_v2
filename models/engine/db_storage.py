#!/usr/bin/python3
"""
    DB - Storage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import os
from os import getenv


dict_class = {'State': State,
              'City': City,
              'User': User,
              'Place': Place,
              'Review': Review,
              'Amenity': Amenity}


class DBStorage():
    """ storage """
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)
        if ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        if cls is None:
            for c in CLASSES.values():
                for obj in self.__session.query(c).all():
                    key = type(obj).__name__ + "." + obj.id
                    del obj.__dict__["_sa_instance_state"]
                    new_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = type(obj).__name__ + "." + obj.id
                new_dict[key] = obj

            return (new_dict)

    def new(self, obj):
        """  add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables in the database (feature of SQLAlchemy) """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ close session """
        self.__session.remove()
