from sqlalchemy import Column, Integer, String, Text
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True , unique=True)
    message = Column(Text)
    gender = Column(String)
