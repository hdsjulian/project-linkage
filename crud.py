from sqlalchemy.orm import Session
import models, schemas
from sqlalchemy import distinct

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
    return db.query(models.Handover).filter(distinct(coin_id)).order_by(handover.id).desc()

""" def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item """
