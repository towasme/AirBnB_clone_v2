#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models
from models.city import City
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            city_list = []
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
