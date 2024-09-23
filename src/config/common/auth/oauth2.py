from datetime import date
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
#from . import jwt_token
from src.config.common.database import database
from sqlalchemy.orm import Session
from src.config.common.database.database import get_db
from typing import Optional
from src.app.my_netowrk.SubMenu import main
from src.config.common.auth.jwt_user import jwt_authentication

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

from datetime import datetime, timedelta
import jose
from jose import jwt, JWTError
from . import schemas
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES= 10
# ACCESS_TOKEN_EXPIRE_DAYS= 90


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("username")
    if username is None:
      raise credentials_exception
  except JWTError:
    raise credentials_exception
  user = main.get_user_by_username(db, username=username)
  if user is None:
    raise credentials_exception
  return user