from sqlalchemy.orm import Session
from src.app.common.schemas import schemas
from src.app.common.models import models 
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy import func, select
import os
import yaml
import logging.config
import logging
import coloredlogs

from src.app.common.properties import properties

def setup_logging(default_path='data/temp/logs/esj_backend_log.yaml', default_level=logging.DEBUG, env_key='LOG_CFG'):

   
    log_file = str(datetime.utcnow().strftime('%m_%d_%Y_%I_%M_%S')) + '.log'
    logging.basicConfig(filename=log_file, format='  %(asctime)s | %(levelname)s | %(message)s', datefmt='%d/%b/%Y %H:%M:%S.%M%S', level=logging.DEBUG)
    

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
                coloredlogs.install()
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        coloredlogs.install(level=default_level)
        print('Failed to load configuration file. Using default configs')

   

# add worning info and error
    logging.debug('go to log file')
    logging.info('for informations')
    logging.warning('and this for warning')
    logging.error('for error')



setup_logging()


########################################
# # Community CRUD Operations
# def create_community(db: Session, community: schemas.CommunityCreate):
#     db_community = models.Community(**community.dict())
#     db.add(db_community)
#     db.commit()
#     db.refresh(db_community)
#     return db_community




# # Role CRUD Operations
# def create_role(db: Session, role: schemas.RoleCreate):
#     db_role = models.Role(**role.dict())
#     db.add(db_role)
#     db.commit()
#     db.refresh(db_role)
#     return db_role

# def get_role(db: Session, role_id: int):
#     role = db.query(models.Role).filter(models.Role.id == role_id).first()
#     if role and isinstance(role.permissions, str):
#         # Convert comma-separated string to list
#         role.permissions = role.permissions.split(',')
#     return role

# def update_role(db: Session, role_id: int, role_update: schemas.RoleCreate):
#     role = db.query(models.Role).filter(models.Role.id == role_id).first()
#     if role:
#         role.name = role_update.name
#         role.permissions = role_update.permissions
#         db.commit()
#         db.refresh(role)
#     return role

# def get_roles(db: Session):
#     return db.query(models.Role).all()

# # CommunityMember CRUD Operations
# def add_member_to_community(db: Session, member: schemas.CommunityMemberCreate):
#     db_member = models.CommunityMember(
#         user_id=member.user_id,
#         community_id=member.community_id,
#         joined_at=datetime.utcnow()  # Assuming you want to set the joined_at field to the current time
#     )
#     db.add(db_member)
#     db.commit()
#     db.refresh(db_member)
    
#     # Add roles
#     for role_id in member.roles:
#         role = db.query(models.Role).filter(models.Role.id == role_id).first()
#         if role:
#             db_member.roles.append(role)
    
#     db.commit()
#     return db_member


# def get_members_of_community(db: Session, community_id: int):
#     return db.query(models.CommunityMember).filter(models.CommunityMember.community_id == community_id).all()


def get_temp_order(db: Session, memo_no: int):
    return db.query(models.TempOrder).filter(models.TempOrder.MEMO_NO == memo_no).first()

def get_temp_orders(db: Session):
    return db.query(models.TempOrder).all()

