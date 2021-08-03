from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import distinct, desc, func

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user:schemas.User):
    db.update(user)
    db.commit()
    db.refresh(user)
    return user


def get_coins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coin).offset(skip).limit(limit).all()

def get_coin(db: Session, coin_id: int):
    return db.query(models.Coin).filter(models.Coin.id == coin_id).first()

def get_handover(db: Session, handover_id: int):
    return db.query(models.Handover).filter(models.Handover.id == handover_id).first()

def get_handovers_by_coin(db:Session, coin_id: int, skip: int=0, limit: int=100):
    return db.query(models.Handover).filter(models.Handover.coin_id == coin_id).offset(skip).limit(limit).all()

def get_handovers_by_user(db:Session, user_id: int):
    return db.query(models.Handover).filter(models.Handover.recipient_id == user_id).all()

def get_handovers(db: Session):
    result = db.query(models.Handover).filter(models.Handover.id.in_((models.Handover.id).filter(func.max(models.Handover.id)).group_by(models.Handover.coin_id)))
    return result

def create_handover(db: Session, handover: schemas.HandoverCreate):
    db_handover = models.Handover(text=handover.text, predecessor_id=handover.predecessor_id, recipient_id=handover.recipient_id, giver_id = handover.giver_id, lat=handover.lat, lon=handover.lon, timestamp = handover.timestamp, coin_id=handover.coin_id)
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
