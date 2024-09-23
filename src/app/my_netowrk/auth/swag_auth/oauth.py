from fastapi import APIRouter, Depends, status, Response, HTTPException,File, UploadFile
from src.app.common.schemas import schemas
from src.config.common.database import database
from src.config.common.auth import oauth2
from sqlalchemy.orm import Session
from typing import List
from src.config.common.database.database import get_db
from src.app.common.properties import properties

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from src.app.common.schemas import schemas
from src.app.common.models import models 
from fastapi import HTTPException, status
from src.config.common.auth.hashing import Hash
from starlette.responses import JSONResponse
from datetime import datetime,timedelta
#router = APIRouter(tags=[properties.jwt_tag]) 
router = APIRouter(tags=[properties.login_tag])


@router.post(properties.student_user_login)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.UserInfo).filter(
        models.UserInfo.UserName == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not (user.SetPassword, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect Pasword for this account Please Provide Correct Password")
    # if not user.is_verified == True:
    #         return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"detail": "Your account has not been verified.Please verify your email address","existing_email_verified":False})                    
    # if not user.is_active == True:
    #         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #                             detail="You are an inactive user. Contact the helpline Number")
   

    access_token = oauth2.create_access_token(data={'username': user.UserName})
    # new_notification=models.Notification_My_Activity(user_id=user.id, title="logged in", description="Successfully logged in",time=datetime.now())
    # user_login_date = db.query(models.UserInfo).filter(models.UserInfo.username == request.username)
    # if user_login_date:
    #         user_login_date.update({'last_login_date':datetime.now() + timedelta(hours=+12)})
    # db.add(new_notification)
    # db.commit()
    user = db.query(models.UserInfo).filter(models.UserInfo.UserName == request.username).first()
    return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_information': user,
  }
