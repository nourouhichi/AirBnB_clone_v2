#!/usr/bin/python3
""" new database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """new class """
    __engine = None
    __session = None
    def __init__(self):
        """ fn init """
        self.__engine = create_engine(
                        'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        )


    def all(self, cls=None):
        """querying data"""
        inst = {}
        if cls == None:
        classes = ["Statee", "City", "User", "Place", "Review", "Amenity"]
            for name in classes:
                objs = self.__session.query(eval(name))
                for obj in objs:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    inst[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                inst[key] = obj


    def new(self, obj):
        """adding obj"""
        self.__session.add(obj)
    

    def save(self):
        """commiting obj"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleting obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloading session """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind = self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """closing session"""
        self.__session.close()