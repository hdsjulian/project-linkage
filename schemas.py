from typing import List, Optional

from pydantic import BaseModel

class HandoverBase(BaseModel):
    lat: float
    lon: float
    text: str
    timestamp: int
    predecessor_id: Optional[int] = None
    recipient_id: int
    giver_id: int
    coin_id: int
    
class HandoverCreate(HandoverBase): 
    pass

class Handover(HandoverBase): 
    id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    email: str
    password: str

class User(UserBase):
    id: int
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

class HandoverReturn(BaseModel):
    handover: Handover
    giver: Optional[User] = None
    receiver: Optional[User]=None
