from fastapi import APIRouter, Depends, status, Response, HTTPException,Request
from src.config.common.auth.hashing import Hash
from src.app.common.schemas import schemas
from src.app.common.models import models
from sqlalchemy.orm import Session
from typing import List
from src.config.common.database import database
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates
from src.app.common.properties import properties
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime
from src.config.common.auth import oauth2
from sqlalchemy import text
#  main functions Importing       ----------
from . import main
from sqlalchemy import func



router = APIRouter(prefix=properties.skill, tags=[properties.register_tag])




get_db = database.get_db




@router.post("/users/register")
def create_user(user: schemas.UserInfoCreate, db: Session = Depends(get_db)):
    db_user = models.UserInfo(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/all")
def get_user(db: Session = Depends(get_db)):
    db_user = db.query(models.UserInfo).all()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.UserID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{UserID}")
def update_user(UserID: int, user: schemas.UserInfoCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.UserID == UserID).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return {properties.update_message}

@router.delete("/users/{UserID}")
def delete_user(UserID: int, db: Session = Depends(get_db)):
    db_user = db.query(models.UserInfo).filter(models.UserInfo.UserID == UserID).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return {properties.delete_message}
