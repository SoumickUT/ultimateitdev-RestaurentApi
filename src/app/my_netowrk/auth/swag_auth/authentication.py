from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt
from fastapi import APIRouter, Depends, status, Response, HTTPException,Request
from src.config.common.auth.hashing import Hash
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
#  main functions Importing       ---------
from sqlalchemy import func
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from typing import Optional

router = APIRouter(prefix=properties.skill, tags=[properties.jwt_category_tag])



# Initialize the password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Helper function to hash the password
def get_password_hash(password):
    return pwd_context.hash(password)

# Dummy database with hashed password for 'secret'
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": get_password_hash("secret"),  # Update the hash for 'secret'
        "disabled": False,
    }
}

# Security configurations
SECRET_KEY = "aSdfgHjkLmNbVcxzQwertyUioP123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    user = db.get(username)
    if user:
        return user

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user['hashed_password']):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username)
    if user is None:
        raise credentials_exception
    return user

# Define the OAuth2 security scheme in the OpenAPI schema
@router.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    openapi_schema = get_openapi(
        title="Restaurent Project",
        version="1.0.0",
        description="This is your project description",
        routes=router.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/token",
                    "scopes": {}
                }
            }
        }
    }
    openapi_schema["security"] = [{
        "OAuth2PasswordBearer": []
    }]
    return JSONResponse(openapi_schema)


# # Initialize the password context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Helper function to hash the password
# def get_password_hash(password):
#     return pwd_context.hash(password)

# # Dummy database with hashed password for 'secret'
# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": get_password_hash("secret"),  # Update the hash for 'secret'
#         "disabled": False,
#     }
# }

# # Security configurations
# SECRET_KEY = "aSdfgHjkLmNbVcxzQwertyUioP123456"
# ALGORITHM = "HS256"  # HMAC-SHA256
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_user(db, username: str):
#     user = db.get(username)
#     if user:
#         return user

# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user['hashed_password']):
#         return False
#     return user

# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# @router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user["username"]}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username)
#     if user is None:
#         raise credentials_exception
#     return user

# # Define the OAuth2 security scheme in the OpenAPI schema
# @router.get("/openapi.json", include_in_schema=False)
# async def get_open_api_endpoint():
#     openapi_schema = get_openapi(
#         title="Your Project",
#         version="1.0.0",
#         description="This is your project description",
#         routes=router.routes,
#     )
#     openapi_schema["components"]["securitySchemes"] = {
#         "OAuth2PasswordBearer": {
#             "type": "oauth2",
#             "flows": {
#                 "password": {
#                     "tokenUrl": "/token",
#                     "scopes": {}
#                 }
#             }
#         }
#     }
#     openapi_schema["security"] = [{
#         "OAuth2PasswordBearer": []
#     }]
#     return JSONResponse(openapi_schema)


# def create_access_token(data: dict, expires_delta: timedelta = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.now() + expires_delta
#     else:
#         expire = datetime.now() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     user = db.get(username)
#     if user:
#         return user



# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# def fake_hash_password(password: str):
#     return "fakehashed" + password

# def authenticate_user(fake_db, username: str, password: str):
#     user = fake_db.get(username)
#     if not user:
#         return False
#     if not fake_hash_password(password) == user["hashed_password"]:
#         return False
#     return UserInDB(**user)



# @router.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=400,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}

# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(
#                 status_code=401,
#                 detail="Could not validate credentials",
#                 headers={"WWW-Authenticate": "Bearer"},
#             )
#         token_data = username
#     except jwt.PyJWTError:
#         raise HTTPException(
#             status_code=401,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     user = fake_users_db.get(token_data)
#     if user is None:
#         raise HTTPException(
#             status_code=401,
#             detail="Could not validate credentials",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     return UserInDB(**user)

# @router.get("/users/me")
# async def read_users_me(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username)
#     if user is None:
#         raise credentials_exception
#     return user