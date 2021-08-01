from typing import List, Optional

from pydantic import BaseModel

class HandoverBase(BaseModel):
    lat: float
    lon: float
    text: str
    timestamp: int
class HandoverCreate(HandoverBase): 
    pass
class Handover(HandoverBase): 
    id: int
    predecessor_id: int
    recipient_id: int
    giver_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    handovers: List[Handover]
    class Config: 
        orm_mode = True

class CoinBase(BaseModel):
    hash: str

class CoinCreate(CoinBase):
    pass

class Coin(CoinBase):
    id: int

    class Config:
        orm_mode = True

