from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/coin/{coin_id}")
async def get_coin(coin_id: int):
    coin = {
        'id': 23,
        'hash': 'b351c6a5e15110cb860cda4c0f4d6020af9fa1a31a22a9aec90f44ed61bb27cc'
    }
    return jsonable_encoder(coin)