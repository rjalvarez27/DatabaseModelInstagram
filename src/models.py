import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    firstname = Column(String(10), nullable=True)
    lastname = Column(String(10), nullable= True)
    password = Column(String(50), nullable=False)
    follower =  relationship('follower')
    post = relationship('post')
    comment = relationship('comment')

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable = False)
    url = Column(String(80),nullable= False) 
    Post_id = Column(Integer, ForeignKey('Post.id'), nullable= False)
    


class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable= False)
    user = relationship(User)    
    comment = relationship('Comment')
    media = relationship('Media')
    
    
    
class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(120), nullable=True)   
    author_id = Column(Integer, ForeignKey('User.id'), nullable= False)
    user = relationship(User) 
    post_id =  Column(Integer, ForeignKey('Post.id'), nullable= False)
    
    

class Follower(Base):
    __tablename__ = "Follower"    
    id = Column(Integer, primary_key=True)     
    #User fron id
    user_From_id = Column(Integer, ForeignKey('User.id'), nullable= True)
    user = relationship(User)      
    #user to id 
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable= True)
    user = relationship(User)   


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
