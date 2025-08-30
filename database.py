from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} )

sessionlocal = sessionmaker(autocommit=False,autoflush= False, bind=engine)

Base = declarative_base()

SQLALCHEMY_USER_DATABASE_URL = "sqlite:///./user.db"

user_engine = create_engine(SQLALCHEMY_USER_DATABASE_URL, connect_args={"check_same_thread": False} )

sessionlocal = sessionmaker(autocommit=False,autoflush= False, bind=user_engine)





