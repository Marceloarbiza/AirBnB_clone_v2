#!/usr/bin/python3
""" dsds """

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
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      os.getenv('HBNB_MYSQL_USER'),
                                      os.getenv('HBNB_MYSQL_PWD'),
                                      os.getenv('HBNB_MYSQL_HOST'),
                                      os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all """
        dicto = {}
        if cls:
            for s in self.__session.query(cls):
                k = type(s).__name__ + '.' + s.id
                dicto[k] = s
            return dicto
        else:
            for cl in dict_class.values():
                for s in self.__session.query(cl).all():
                    k = type(s).__name__ + '.' + s.id
                    dicto[k] = s

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
