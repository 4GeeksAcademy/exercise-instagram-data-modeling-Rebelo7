import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'

  id = Column(Integer, primary_key=True)
  username = Column(String(250), nullable=False)
  firstname = Column(String(250), nullable=False)
  lastname = Column(String(250), nullable=False)
  email = Column(String(250), unique=True)

  posts = relationship('Post')
  comments = relationship('Comment')
  followers = relationship('Follower')
  following = relationship('Follower')

class Follower(Base):
  __tablename__ = 'follower'

  id = Column(Integer, primary_key=True)
  user_form_id = Column(Integer, ForeignKey('user.id'))
  user_to_id = Column(Integer, ForeignKey('user.id'))

  user_from = relationship('User')
  user_to = relationship('User')

class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('user.id'))

  user = relationship('User')
  media = relationship('Media')
  comments = relationship('Comment')

class Media(Base):
  __tablename__ = 'media'

  id = Column(Integer, primary_key=True)
  type = Column(String(250), nullable=False)
  url = Column(String(250), nullable=False)
  post_id = Column(Integer, ForeignKey('post.id'))

  post = relationship('Post')

class Comment(Base):
  __tablename__ = 'comment'

  id = Column(Integer, primary_key=True)
  comment_text = Column(String(250), nullable=False)
  author_id = Column(Integer, ForeignKey('user.id'))
  post_id = Column(Integer, ForeignKey('post.id'))

  author = relationship('User')
  post = relationship('Post')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
