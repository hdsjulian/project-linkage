from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    
class Coin(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, unique=True)
    handovers = relationship("Handover", back_populates="coin")

class Handover(Base):
    __tablename__ = "handovers"
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    text = Column(Text)
    timestamp = Column(Integer, index=True, default = datetime.utcnow)
    predecessor_id = Column(Integer, ForeignKey("handovers.id"))
    recipient_id = Column (Integer, ForeignKey("users.id"))
    giver_id = Column (Integer, ForeignKey("users.id"))
    giver = relationship("User", back_populates="handovers_given")
    recipient = relationship("User", back_populates="handovers_received")
    

