import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

from fastapi import APIRouter, Depends, status, Response, HTTPException,File, UploadFile
from src.app.common.schemas import schemas
from src.config.common.database import database
from sqlalchemy.orm import Session
from typing import List
from src.config.common.database.database import get_db
from src.app.common.properties import properties

from . import main


router = APIRouter(
    prefix=properties.service_student_admin,
    tags=[properties.swagger_tag]
)


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "esjadmin")
    correct_password = secrets.compare_digest(credentials.password, "#S10@dmin")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return properties.successful_login


@router.get("/users/me")
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}




import secrets

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

from fastapi import APIRouter, Depends, status, Response, HTTPException,File, UploadFile
from src.app.common.schemas import schemas
from src.config.common.database import database
from sqlalchemy.orm import Session
from typing import List
from src.config.common.database.database import get_db
from src.app.common.properties import properties

from . import main


router = APIRouter(
    prefix=properties.service_student_admin,
    tags=[properties.swagger_tag]
)


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "esjadmin")
    correct_password = secrets.compare_digest(credentials.password, "#S10@dmin")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return properties.successful_login


@router.get(properties.swagger_autentication)
def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}




