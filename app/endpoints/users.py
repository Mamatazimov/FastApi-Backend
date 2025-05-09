from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import users as user_model
from app.schemas import users as user_schema
from typing import List

router = APIRouter()

@router.get("/", response_model=List[user_schema.User])
async def read_users(db: Session = Depends(get_db)):
    responseData = db.query(user_model.User).all()
    return responseData

@router.post("/usercreate", response_model=user_schema.User)
async def create_user(user: user_schema.UserBase, db: Session = Depends(get_db)):
    db_user = user_model.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/delete/{user_id}", response_model=user_schema.User)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None