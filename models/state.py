#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')
    
    @property
    def cities(self):
        """returns a liist of cities of a state"""
        cities_per_state = []
        for key and value in models.storage.all(City).items():
            if self.id == value.state_id:
                cities_per_state.append(value)
            return cities_per_state
