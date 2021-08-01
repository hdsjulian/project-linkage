from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    recipient = relationship("Handover", back_populates="recipient")
    giver = relationship("Handover", back_population="giver")

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
    timestamp = Column(int, index=True, default = datetime.utcnow)
    #predecessor = relationship("Handover", backref="predecessor")
    predecessor_id = Column(Integer, ForeignKey("handovers.id")
    owner_id = Column (Integer, ForeignKey("users.id"))
    giver_id = Column (Integer, ForeignKey("users.id"))
    giver = relationship("User", back_populates="hadovers_given")
    recipient = relationship("User", back_populates="handovers_received")
    

