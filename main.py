from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
