import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

""" class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) """


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    

class Character(Base):
      __tablename__ = "character"
      id = Column(Integer, primary_key=True)
      char_name = Column(String, nullable=False)
      planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)  # id del planeta de origen
      planet = relationship("Planet")  # Relación con la tabla Planet


class Planet(Base):
     __tablename__ = "planet"
     id = Column(Integer, primary_key=True)
     planet_name = Column(String, nullable=False)

class Weapon(Base):
      __tablename__ = "weapon"
      id = Column(Integer, primary_key=True)
      weapon_name = Column(String, nullable=False)

    
class Favorites(Base):
     __tablename__ = "favorites"
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # id del user
     character_id = Column(Integer, ForeignKey('character.id'), nullable=False)  # id del characer
     user = relationship("User")  # Relación con la tabla de user
     character = relationship("Character")  # Relación con la tabla de personajes


class Post(Base):
     __tablename__ = "post"
     id = Column(Integer, primary_key=True)
     title = Column(String, nullable=False)  # Título de la publicación
     content = Column(String, nullable=False)  # Contenido de la publicación
     author_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # id del autor de la publicación
     author = relationship("User")  # Relación con la tabla de usuarios (autor de la publicación)


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
