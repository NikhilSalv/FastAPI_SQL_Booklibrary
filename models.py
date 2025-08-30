from sqlalchemy import Column, Integer, String
from database import Base



class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key= True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    rating = Column(Integer)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key= True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
