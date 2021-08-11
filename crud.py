from sqlalchemy.orm import Session, aliased
import models, schemas
from sqlalchemy import distinct, desc, func
from passlib.context import CryptContext
import os
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user["hashed_password"])
    db_user = db.query(models.User).filter(models.User.email == user["email"]).all()
    if (len(db_user)==0):
        db_user = models.User(email=user["email"], name=user["name"], hashed_password=hashed_password)
        db.add(db_user)
    else: 
        db_user = db_user[0]
        db_user.hashed_password = hashed_password
        db_user.name = user["name"]
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user:schemas.User):
    db.update(user)
    db.commit()
    db.refresh(user)
    return user

def check_user_password(db: Session, user_id: int, hashed_password: str):
    hashed_password = get_password_hash(hashed_password)
    db_user = db.query(models.User).filter(models.User.id == user_id, models.User.hashed_password == hashed_password).first()
    return db_user

def get_coins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coin).offset(skip).limit(limit).all()

def get_coin(db: Session, coin_id: int):
    return db.query(models.Coin).filter(models.Coin.id == coin_id).first()

def get_coin_by_hash(db: Session, hash: str):
    return db.query(models.Coin).filter(models.Coin.hash == hash).first()

def get_handover(db: Session, handover_id: int):
    result = db.query(models.Handover).filter(models.Handover.id == handover_id).first()
    return result

def get_handovers_by_coin(db:Session, coin_id: int, skip: int=0, limit: int=100):
    return db.query(models.Handover.lat, models.Handover.lon, models.Handover.id, models.Handover.predecessor_id, models.Handover.recipient_id).filter(models.Handover.coin_id == coin_id).order_by(desc(models.Handover.id)).offset(skip).limit(limit).all()

def get_handover_by_coin(db:Session, coin_id: int, skip: int=0, limit: int=100):
    return db.query(models.Handover).filter(models.Handover.coin_id == coin_id).order_by(desc(models.Handover.id)).offset(skip).limit(limit).all()

def get_handovers_by_user(db:Session, user_id: int):
    return db.query(models.Handover).filter(models.Handover.recipient_id == user_id).all()

def get_handovers(db: Session):
    subquery = db.query(func.max(models.Handover.id)).group_by(models.Handover.coin_id)
    result = db.query(models.Handover.coin_id, models.Handover.id, models.Handover.lat, models.Handover.lon, models.Handover.predecessor_id).filter(models.Handover.id.in_(subquery))
    return result.all()

def create_handover(db: Session, handover: schemas.HandoverCreate):
    db_handover = models.Handover(text=handover["text"], predecessor_id=handover["predecessor_id"], recipient_id=handover["recipient_id"], giver_id = handover["giver_id"], lat=handover["lat"], lon=handover["lon"], timestamp = handover["timestamp"], coin_id=handover["coin_id"])
    db.add(db_handover)
    db.commit()
    db.refresh(db_handover)
    return db_handover

def update_handover(db:Session, handover:schemas.Handover):
    db.update(handover)
    db.commit()
    db.refresh(handover)
    return handover



 

""" def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item """
