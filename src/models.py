import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
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
    last_login = Column(DateTime())
    post = relationship("post", backref="user")
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False) 

    

class Character(Base):
      __tablename__ = "character"
      id = Column(Integer, primary_key=True)
      char_name = Column(String, nullable=False)
      planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)  # id del planeta de origen
      planet = relationship("Planet", backref="residents")  # Relación con la tabla Planet
      biography = Column(String(120), default="")
      avatar = Column(String(150), default="")
      users_id = Column(Integer, ForeignKey('users.id'), nullable=False, unique=True)     
      weapons = relationship("Weapon", backref="character")  # Relación con la tabla Weapon
      specie = relationship("species", backref="character")
      specie_id = Column(Integer, ForeignKey('specie.id'), nullable=False)



class Species(Base):
     __tablename__ = "specie"
     id = Column(Integer, primary_key=True)
     name = Column(String(20), default="")
     language = Column(String, nullable=False)
     characters = relationship("Character", backref="species")  # Relación con la tabla Character 



class Planet(Base):
     __tablename__ = "planet"
     id = Column(Integer, primary_key=True)
     planet_name = Column(String, nullable=False)
     characters = relationship("Character", backref="planet")  # Relación con la tabla Character
     residents = relationship("Character", backref="planet")  # Relación inversa con la tabla Character


class Weapon(Base):
      __tablename__ = "weapon"
      id = Column(Integer, primary_key=True)
      weapon_name = Column(String, nullable=False)
      character_id = Column(Integer, ForeignKey('character.id'))  # Agregar columna para la relación
      character = relationship("Character", backref="weapon")  # Relación con la tabla Character


    
class Favorites(Base):
     __tablename__ = "favorites"
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # id del user
     character_id = Column(Integer, ForeignKey('character.id'), nullable=False)  # id del characer
     user = relationship("User", backref="favorites")  # Relación con la tabla de user
     character = relationship("Character", backref="favorites")  # Relación con la tabla de personajes


class Post(Base):
     __tablename__ = "post"
     id = Column(Integer, primary_key=True)
     title = Column(String, nullable=False)  # Título de la publicación
     content = Column(String, nullable=False)  # Contenido de la publicación
     author_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # id del autor de la publicación
     user = relationship("User", backref="post")  # Relación con la tabla de usuarios de quien realizo el post


def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
