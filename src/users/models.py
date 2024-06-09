from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, index=True)
    fname = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    paswword = Column(String)
