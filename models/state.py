#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        @property
        def cities(self):
            """ returns cities with same state id"""
            city_list = models.storage.all(City)
            city_state = []
            for key, value in city_list.items():
                if self.id == value.state_id:
                    city_state.append(value)
            return city_state


