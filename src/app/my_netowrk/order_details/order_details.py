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


@router.post("/create/sales/")
def create_sale(sale: schemas.SaleMasterBase, db: Session = Depends(get_db)):
    db_sale = models.SaleMaster(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return properties.create_message

@router.get("/get_all/sales/")
def read_sale(db: Session = Depends(get_db)):
    db_sale = main.get_all_sale(db)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale


@router.get("/sales/{ORDER_NUMBER}")
def read_sale(ORDER_NUMBER: int, db: Session = Depends(get_db)):
    db_sale = main.get_sale(db, ORDER_NUMBER)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.put("/sales/{ORDER_NUMBER}", response_model=schemas.SaleMaster)
def update_sale(ORDER_NUMBER: int, sale: schemas.SaleMasterUpdate, db: Session = Depends(get_db)):
    db_sale = main.update_sale(db, ORDER_NUMBER, sale)
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale