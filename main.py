from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#app.mount("/frontend", StaticFiles(directory="frontend-svelte/public", html=True), name="frontend")
#app.mount("/build", StaticFiles(directory="frontend-svelte/public/build"), name="build")
"""
@app.get('/')
async def frontend():
    return RedirectResponse(url='frontend')
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/hash/{hash}", response_model=schemas.CoinVerify)
def verify_coin(hash: str, db: Session = Depends(get_db)):
    db_coin = crud.get_coin_by_hash(db, hash)
    if db_coin is None:
        raise HTTPException(status_code=404, detail="Coin not found")
    else: 
        return db_coin

@app.get("/coins/{coin_id}", response_model=schemas.Coin)
def read_coin(coin_id: int, db: Session=Depends(get_db)):
    db_coin = crud.get_coin(db, coin_id=coin_id)
    if db_coin is None:
        raise HTTPException(status_code=404, detail="Coin not found")
    return db_coin

@app.get("/coins/", response_model=List[schemas.Coin])
def read_coins(skip: int = 0, limit: int = 120, db: Session = Depends(get_db)):
    coins = crud.get_coins(db, skip=skip, limit=limit)
    return coins

@app.get("/coins/{coin_id}/handovers/", response_model=List[schemas.Handover])
def get_handovers_for_coin(coin_id: int, db: Session=Depends(get_db)):
    print(coin_id)
    handovers = crud.get_handovers_by_coin(db, coin_id)
    return handovers

@app.get("/handovers/{handover_id}", response_model=schemas.HandoverData)
def read_handover(handover_id: int, db: Session=Depends(get_db)):
    db_handover = crud.get_handover(db, handover_id=handover_id)
    if db_handover is None:
        raise HTTPException(status_code=404, detail="Handover not found")
    print(db_handover.coin_id)
    print("--------------")
    db_recipient = crud.get_user(db, user_id=db_handover.recipient_id)
    db_coin = crud.get_coin(db, db_handover.coin_id)
    if db_handover.giver_id is not None:
        db_giver = crud.get_user(db, user_id=db_handover.giver_id)
    else: 
        db_giver = None
    db_handover.giver = db_giver
    db_handover.recipient = db_recipient
    db_handover.coin = db_coin
    returnStuff = {'data': {'handover': db_handover}}

    return returnStuff

@app.get("/handovers/", response_model=List[schemas.Handover])
def read_handovers(db: Session=Depends(get_db)):
    handovers = crud.get_handovers(db)
    return handovers
