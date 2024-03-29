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
    text: Optional[str] = None
    answer: Optional[str] = None
    timestamp: int
    predecessor_id: Optional[int] = None
    recipient_id: int
    giver_id: Optional[int] = None
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
    question: Optional[str] = ""
    
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
    next_id: Optional[int] = None
    prev_id: Optional[int] = None
    coin_id: Optional[int] = None

class HandoverHandoverReturn(CamelModel):
    handover: HandoverReturn

class HandoverData(CamelModel):
    data: HandoverHandoverReturn

class CoinReturn(Coin):
    handover: Optional[HandoverReturn]=None
    prev_id: Optional[str] = None
    next_id: Optional[str] = None

class CoinCoinReturn(CamelModel):
    coin: CoinReturn

class CoinData(CamelModel):
    data: CoinCoinReturn

class CoinList(CamelModel):
    handover_id: int
    prev_coin_handover_id: int
    next_coin_handover_id: int

class CoinListData(CamelModel):
    data: CoinList

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None  

class HandoverVerification(BaseModel):
    hash: str
    password: str

class EnterHandover(CamelModel):
    recipient_name: str
    recipient_password: str
    recipient_email: str
    hash: str
    lat: float
    lon: float
    text: Optional[str]
    question: Optional[str]
    answer: Optional[str]
    predecessor_id: Optional[int] = None
    giver_id: Optional[int] = None
    recipient_id: Optional[int] = None

class HandoverStripped(CamelModel):
    lat: float
    lon: float
    id: int
    predecessor_id: Optional[int] = None