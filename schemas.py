from typing import List, Optional

from pydantic import BaseModel, ValidationError
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.selectable import TextAsFrom
from fastapi_camelcase import CamelModel


class ArticleBase(BaseModel):
    headline: str
    text: str
    author_id: int

class Article(ArticleBase):
    id: int
    class Config:
        orm_mode = True

class HandoverBase(CamelModel):
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
    travels: Optional[int] = 0
    
class CoinCreate(CoinBase):
    hash: str

class Coin(CoinBase):
    id: int
    class Config:
        orm_mode = True

class CoinVerify(Coin):
    hash: str

class HandoverReturn(Handover):
    giver: Optional[User] = None
    recipient:  Optional[User]=None
    coin: Optional[Coin] = None

class HandoverHandoverReturn(CamelModel):
    handover: HandoverReturn

class HandoverData(CamelModel):
    data: HandoverHandoverReturn

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None  
