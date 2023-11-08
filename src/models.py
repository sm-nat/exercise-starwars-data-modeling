import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    active = Column(Boolean, default=False)

    

class Character(Base):
      __tablename__ = "character"
      id = Column(Integer, primary_key=True)
      char_name = Column(String, nullable=False)
      planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)  # id del planeta de origen
      planet = relationship("Planet", back_populates="residents")  # Relación con la tabla Planet
      biography = Column(String(120), default="")
      avatar = Column(String(150), default="")
      users_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)     


class Species(Base):
     __tablename__ = "specie"
     id = Column(Integer, primary_key=True)
     name = Column(String(20), default="")
     language = Column(String, nullable=False)
     characters = relationship("Character", back_populates="specie")  # Relación con la tabla Character 



class Planet(Base):
     __tablename__ = "planet"
     id = Column(Integer, primary_key=True)
     planet_name = Column(String, nullable=False)
     characters = relationship("Character", back_populates="planet")  # Relación con la tabla Character
     residents = relationship("Character", back_populates="planet")  # Relación inversa con la tabla Character


class Weapon(Base):
      __tablename__ = "weapon"
      id = Column(Integer, primary_key=True)
      weapon_name = Column(String, nullable=False)

    
class Favorites(Base):
     __tablename__ = "favorites"
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # id del user
     character_id = Column(Integer, ForeignKey('character.id'), nullable=False)  # id del characer
     user = relationship("User", back_populates="favorites")  # Relación con la tabla de user
     character = relationship("Character", back_populates="favorites")  # Relación con la tabla de personajes


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
