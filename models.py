from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship, backref
from database import Base
from datetime import datetime
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)
    giver = relationship('Handover', foreign_keys='Handover.giver_id', backref='payer')
    receiver = relationship('Handover', foreign_keys='Handover.recipient_id', backref='receiver')

     
class Coin(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String, unique=True)
    travels = Column(Integer)
    handovers = relationship('Handover', backref='coin')

class Handover(Base):
    __tablename__ = "handovers"
    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    text = Column(Text)
    coin_id = Column(Integer, ForeignKey('coins.id'))
    timestamp = Column(Integer, index=True, default = datetime.utcnow)
    predecessor_id = Column(Integer, ForeignKey("handovers.id"))
    recipient_id = Column (Integer, ForeignKey("users.id"))
    giver_id = Column (Integer, ForeignKey("users.id"))
    predecessor = relationship('Handover', backref=backref('successor', remote_side=id))


