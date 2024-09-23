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



router = APIRouter(prefix=properties.skill, tags=[properties.menu_tag])




get_db = database.get_db



@router.get("/get_all_menu/")
def get_all_menu(db: Session = Depends(get_db),current_user: schemas.UserInfoBase = Depends(oauth2.get_current_user)):
    result = main.get_all_menu(db)
    if not result:
        raise HTTPException(status_code=404, detail="Menu items not found")
    return result

@router.get("/menus/")
def read_menu(CAT_ID: int, SUB_ID: int, db: Session = Depends(get_db)):
    result = main.get_menu(db, CAT_ID, SUB_ID)
    if not result:
        raise HTTPException(status_code=404, detail="Menu items not found")
    return result

