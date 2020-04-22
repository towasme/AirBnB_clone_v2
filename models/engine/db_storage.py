#!/usr/bin/python3
"""This is the db storage class for AirBnB"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


all_classes = {'State': State,
               'City': City,
               'User': User,
               'Place': Place,
               'Review': Review,
               'Amenity': Amenity}


class DBStorage():
    """
    """
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        db_uri = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(db_uri, pool_pre_ping=True)

        self.reload()

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return dict for cls
        """
        entities = dict()
        if cls is None:
            for item in all_classes.keys():
                query = self.__session.query(all_classes[item])
                for instance in query:
                    k = instance.__class__.__name__ + "." + instance.id
                    entities[k] = instance
        elif cls is not None:
            if cls in all_classes:
                query = self.__session.query(all_classes[cls])
            else:
                query = self.__session.query(cls)
            for instance in query:
                k = instance.__class__.__name__ + "." + instance.id
                entities[k] = instance
        return entities

    def new(self, obj):
        """Add obj to the current database session."""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit changes to current db session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current db session"""
        try:
            self.__session.delete(obj)
        except:
            pass

    def reload(self):
        """Create all tables into database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ closes the session """
        self.__session.close()
