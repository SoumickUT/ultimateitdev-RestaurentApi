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



router = APIRouter(prefix=properties.skill, tags=[properties.OrderSale_tag])




get_db = database.get_db


@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserInfoCreate, db: Session = Depends(get_db)):
    db_user = models.UserInfo(
        UserName=user.UserName,
        FullName=user.FullName,
        SetPassword=user.SetPassword,
        UserType=user.UserType,
        Status=user.Status,
        BackdateEntry=user.BackdateEntry
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

