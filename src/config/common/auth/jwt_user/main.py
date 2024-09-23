# from sqlalchemy.orm import Session
# from src.app.common.schemas import schemas
# from src.app.common.models import models 
# from fastapi import HTTPException, status
# from src.config.common.auth.hashing import Hash


# def create(request: schemas.User, db: Session):
#     new_user = models.JWT_API_Authentication(
#         name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# def get_all_jwt_user(db: Session):
#     get_all_jwt_user = db.query(models.JWT_API_Authentication).all()
#     if not get_all_jwt_user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"There is nothing in database create one to see")
#     return get_all_jwt_user

# def show(id: int, db: Session):
#     user = db.query(models.JWT_API_Authentication).filter(models.JWT_API_Authentication.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id {id} is not available")
#     return user

# def update_jwt(id: int,  request: schemas.User, db: Session):
#     update_jwt = db.query(models.JWT_API_Authentication).filter(models.JWT_API_Authentication.id == id)
#     if not update_jwt.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"writing test  with id {id} not found")
#     update_jwt.update({'name':request.name,'email':request.email,'password':request.password})
#     db.commit()
#     return {'detail': f'successfully updated the jwt user with id {id} in database'}

# def delete_jwt(id: int, db: Session):
#     delete_jwt = db.query(models.JWT_API_Authentication).filter(models.JWT_API_Authentication.id ==id)
#     if not delete_jwt.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with id {id} not found")
#     db.execute(f'DROP TABLE alembic_version;')                         
#     delete_jwt.delete(synchronize_session=False)
#     db.commit()
#     return {'detail': f'successfully deleted the delete_jwt with id {id}'}