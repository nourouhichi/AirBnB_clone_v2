#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from models.city import City
from sqlalchemy import Column, Integer, String
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
        "City",
        cascade="all,delete,delete-orphan",
        backref=backref("state", cascade="all,delete"),
        passive_deletes=True,
        single_parent=True)
    else:
        @property
        def cities(self):
            """ returns cities in a list """
            cities_list=[]
            for k, v in models.storage.all(City).items():
                if v.state_id == self.id:
                    cities_list.append(k)
