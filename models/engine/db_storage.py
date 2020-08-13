#!/usr/bin/python3
""" a new engine"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """database class"""
    __engine = None
    __session = None

    def __init__(self):
        """init for dbstorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv("HBNB_MYSQL_USER"),
                getenv("HBNB_MYSQL_PWD"),
                getenv("HBNB_MYSQL_HOST"),
                getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("") == 'test':
             Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query some objects on the current database session"""
        objects={}
        classes= ["State", "City", "User", "Place", "Review", "Amenity"]
        if cls is None:
            for i in classes:
                ob = self.__session.query(i)
                for j in ob:
                    key = "{}.{}".format(type(j).__name__, j.id)
                    objects[key] = j
        else:
            ob = self.__session.query(cls).all()
            for j in ob:
                key = "{}.{}".format(cls, j.id)
                objects[key] = j
        return objects

    def new(self, obj):
        """add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ create all tables """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
                                 bind=self.__engine, expire_on_commit=False))
        self.__session = Session()
