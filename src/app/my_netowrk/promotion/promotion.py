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



router = APIRouter(prefix=properties.skill, tags=[properties.Promotion_tag])




get_db = database.get_db



@router.get("/get_all/promotion/")
def get_all_promotion(db: Session = Depends(get_db)):
    db_sale = main.get_all_Promotion(db)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale


@router.get("/promotion/{PromotionID}")
def get_one_promotion(PromotionID: int, db: Session = Depends(get_db)):
    db_sale = main.get_Promotion(db, PromotionID)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="promotion not found")
    return db_sale



@router.get("/get_all/voucher/")
def get_all_voucher(db: Session = Depends(get_db)):
    db_sale = main.get_all_Voucher(db)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale


@router.get("/promotion/{voucherID}")
def get_one_voucher(voucherID: int, db: Session = Depends(get_db)):
    db_sale = main.get_Voucher(db, voucherID)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="promotion not found")
    return db_sale