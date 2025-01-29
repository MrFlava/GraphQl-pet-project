from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey('user.id'))


