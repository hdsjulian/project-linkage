from os import pread
from typing import List
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
import sys

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Main App")
api_app=FastAPI(title="Api App")
app.mount('/api', api_app)
app.mount('/build', StaticFiles(directory="frontend-svelte/public/build", html=True), name="build")
app.mount('/image', StaticFiles(directory="frontend-svelte/public/image", html=True), name="image")
app.mount('/font', StaticFiles(directory="frontend-svelte/public/font", html=True), name="font")



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/{full_path:path}")
async def read_index(request: Request, full_path: str):
    sys.stdout.flush()
    return FileResponse('frontend-svelte/public/index.html')
        
        
@api_app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@api_app.post("/verify_user/")
def check_user_password(verificationItem: schemas.HandoverVerification, db: Session = Depends(get_db)):
    db_coin = crud.get_coin_by_hash(db, verificationItem.hash)
    if (db_coin is None):
        return {'is_verified': False}
    handover = crud.get_handover_by_coin(db, db_coin.id, limit = 1)
    if (len(handover) == 0):
        return {'is_verified': "No Handover found"}
    db_user = crud.check_user_password(db = db, user_id = handover[0].recipient_id, hashed_password = verificationItem.password)
    if (db_user is None):
        return {'is_verified': False}
    else:
        return {'is_verified': True}

@api_app.post("/submit_handover")
def submit_handover(enterHandoverItem: schemas.EnterHandover, db: Session=Depends(get_db)):
    db_coin = crud.get_coin_by_hash(db, enterHandoverItem.hash)
    if (db_coin is None):
        return {'is_verified': False}
    last_handover = crud.get_handover_by_coin(db, db_coin.id, limit=1)
    if (len(last_handover)) == 0:
        enterHandoverItem.predecessor_id = None
    else: 
        enterHandoverItem.predecessor_id = last_handover[0].id
    if (enterHandoverItem.predecessor_id is not None):
        giver_id = last_handover[0].giver_id
    else: 
        giver_id = None
        
    user = {
        "hashed_password": enterHandoverItem.recipient_password,
        "email": enterHandoverItem.recipient_email,
        "name": enterHandoverItem.recipient_name
    }
    db_user = crud.create_user(db, user)
    handover = {
        "text": enterHandoverItem.text, 
        "lat": enterHandoverItem.lat, 
        "lon": enterHandoverItem.lon, 
        "giver_id": giver_id,
        "recipient_id": db_user.id,
        "predecessor_id": enterHandoverItem.predecessor_id, 
        "timestamp": int(datetime.timestamp(datetime.utcnow())),
        "coin_id": db_coin.id
    }
    db_handover = crud.create_handover(db, handover)
    print("new handover")
    print (db_handover.id)
    db_coin.travels += 1
    db.commit()
    return {'is_saved': True, "handover_id": db_handover.id }  



@api_app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@api_app.get("/hash/{hash}", response_model=schemas.CoinData)
def verify_coin(hash: str, db: Session = Depends(get_db)):
    db_coin = crud.get_coin_by_hash(db, hash)
    if db_coin is None:
        raise HTTPException(status_code=404, detail="Coin not found")
    else: 
        return {"data": {"coin": db_coin}}

@api_app.get("/coins/{coin_id}", response_model=schemas.CoinData)
def read_coin(coin_id: int, db: Session=Depends(get_db)):
    db_coin = crud.get_coin(db, coin_id=coin_id)
    if db_coin is None:
        raise HTTPException(status_code=404, detail="Coin not found")
    handovers = crud.get_handovers(db)
    coin_ids = []
    for h in handovers:
        coin_ids.append(h.coin_id)
    if (coin_id in coin_ids): 
        index = coin_ids.index(coin_id)
    else: 
        index = 0
    print(coin_ids)
    if index == 0: 
        print("a")
        db_coin.prev_id = coin_ids[-1]
        db_coin.next_id = coin_ids[1]
    elif index == len(coin_ids)-1:
        print("b")
        db_coin.prev_id = coin_ids[0]
        db_coin.next_id = coin_ids[index-2]
    else:
        print(index)
        db_coin.prev_id = coin_ids[index-1]
        db_coin.next_id = coin_ids[index+1]

    db_handover = crud.get_handover_by_coin(db, coin_id, limit=1) 
    if db_handover is not None and db_handover != []: 
        db_handover = db_handover[0]
        db_coin.handover=db_handover
        db_coin.handover.coin=db_coin
        db_coin.handover.recipient = crud.get_user(db, db_coin.handover.recipient_id)
        db_coin.handover.giver = crud.get_user(db, db_coin.handover.giver_id)

        

    else: 
        db_handover = {}
    
    
    return {'data': {'coin': db_coin}}

@api_app.get("/coins/", response_model=List[schemas.Coin])
def read_coins(skip: int = 0, limit: int = 120, db: Session = Depends(get_db)):
    coins = crud.get_coins(db, skip=skip, limit=limit)
    return coins

@api_app.get("/coins/{coin_id}/handovers/", response_model=List[schemas.HandoverStripped])
def get_handovers_for_coin(coin_id: int, db: Session=Depends(get_db)):
    handovers = crud.get_handovers_by_coin(db, coin_id)
    return handovers


@api_app.get("/handovers/{handover_id}", response_model=schemas.HandoverData)
def read_handover(handover_id: int, db: Session=Depends(get_db)):
    db_handover = crud.get_handover(db, handover_id=handover_id)
    if db_handover is None:
        raise HTTPException(status_code=404, detail="Handover not found")
    db_recipient = crud.get_user(db, user_id=db_handover.recipient_id)
    db_coin = crud.get_coin(db, db_handover.coin_id)
    if db_handover.giver_id is not None:
        db_giver = crud.get_user(db, user_id=db_handover.giver_id)
    else: 
        db_giver = None
    db_handover.giver = db_giver
    db_handover.recipient = db_recipient
    db_handover.coin = db_coin
    handovers = crud.get_handovers_by_coin(db, coin_id = db_coin.id)
    handover_ids = []
    for h in handovers:
        handover_ids.append(h.id)
    if (handover_id in handover_ids): 
        index = handover_ids.index(handover_id)
    else: 
        index = 0
    if index == 0: 
        db_handover.prev_id = handover_ids[-1]
        if (len(handover_ids) == 1):
            db_handover.next_id = handover_ids[0]
        else: 
            db_handover.next_id = handover_ids[1]
    elif index == len(handover_ids)-1:
        db_handover.prev_id = handover_ids[0]
        db_handover.next_id = handover_ids[index-2]
    else:
        db_handover.prev_id = handover_ids[index-1]
        db_handover.next_id = handover_ids[index+1]


    returnStuff = {'data': {'handover': db_handover}}

    return returnStuff

@api_app.get("/handovers/", response_model=List[schemas.HandoverStripped])
def read_handovers(db: Session=Depends(get_db)):
    handovers = crud.get_handovers(db)
    return handovers
