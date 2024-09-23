# from fastapi import APIRouter, Depends, status, Response, HTTPException,File, UploadFile
# from src.app.common.schemas import schemas
# from src.config.common.database import database
# from sqlalchemy.orm import Session
# from typing import List
# from src.config.common.database.database import get_db
# from src.app.common.properties import properties

# from src.config.common.auth import oauth2

# from . import main


# router = APIRouter(
#     prefix=properties.service_student_admin,
#     tags=[properties.jwt_tag]
# )

# get_db = database.get_db


# @router.post(properties.jwt_user_create, response_model=schemas.User)
# def create_user(request: schemas.User, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return main.create(request, db)

# @ router.get(properties.get_all_jwt_user,status_code=200)
# def get_all_jwt_user(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return main.get_all_jwt_user(db)

# @router.get(properties.get_one_jwt_user, response_model=schemas.User)
# def get_user(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return main.show(id, db)

# #Routing Code for the update writing test   - 10/01/2022
# @router.put(properties.update_jwt_user, status_code=status.HTTP_202_ACCEPTED)
# def update_jwt(id: int,  request: schemas.User, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return main.update_jwt(id, request, db)

# @router.delete(properties.destroy_jwt_user, status_code=status.HTTP_200_OK)
# def delete_jwt(id: int, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return main.delete_jwt(id, db)