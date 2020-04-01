#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    __tablename__ = "users"

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship("Place", backref="users",
                              cascade="all, delete-orphan")
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    elif os.getenv('HBNB_TYPE_STORAGE') == 'file':
        email = ""
        password = ""
        first_name = ""
        last_name = ""
