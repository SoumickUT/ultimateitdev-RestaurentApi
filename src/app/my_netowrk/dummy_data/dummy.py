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
from . import data_insertion
from sqlalchemy import func



router = APIRouter(prefix=properties.skill, tags=[properties.dummy_tag])




get_db = database.get_db



######################################

@router.post("/insert_dummy_data")
async def insert_data(db: Session = Depends(get_db)):
    data_insertion.insert_dummy_data(db)
    return {"message": "Dummy data inserted successfully!"}


# @router.get("/temp_order_1_data_types")
# async def get_temp_order_1(db: Session = Depends(get_db)):
#     try:
#         query = text("SELECT * FROM [Haldi].[dbo].[TEMP_ORDER_1]")
#         result = db.execute(query)

#         # Fetch column names and data types
#         columns = result.keys()
#         data_types = [desc[1] for desc in result.cursor.description]

#         # Fetch all rows and format as list of dictionaries
#         data = []
#         for row in result.fetchall():
#             data.append({col: {"value": val, "type": dtype} for col, val, dtype in zip(columns, row, data_types)})

#         return {"data": data}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")
    
########################################################################################


    
# # Community Routes
# @router.post("/communities/")
# def create_community(community: schemas.CommunityCreate, db: Session = Depends(get_db)):
#     return main.create_community(db=db, community=community)


# # Endpoint to get a single community by ID
# @router.get("/communities/{community_id}")
# def read_community(community_id: int, db: Session = Depends(get_db)):
#     query = text("""
#     SELECT
#         json_build_object(
#             'communityId', c.community_id,
#             'name', c.name,
#             'description', c.description,
#             'createdAt', c.created_at,
#             'admin', json_build_object(
#                 'userId', u.id,
#                 'username', u.username,
#                 'email', u.email
#             ),
#             'members', (
#                 SELECT json_agg(
#                     json_build_object(
#                         'userId', m.id,
#                         'username', m.username,
#                         'email', m.email,
#                         'roles', (
#                             SELECT array_agg(r.id)
#                             FROM roles r
#                             JOIN community_member_role cmr ON cmr.role_id = r.id
#                             WHERE cmr.community_member_id = cm.id
#                         ),
#                         'joinedAt', cm.joined_at
#                     )
#                 )
#                 FROM community_member cm
#                 JOIN users m ON m.id = cm.user_id
#                 WHERE cm.community_id = c.id
#             ),
#             'roles', (
#                 SELECT json_agg(
#                     json_build_object(
#                         'roleId', r.id,
#                         'name', r.name,
#                         'permissions', r.permissions
#                     )
#                 )
#                 FROM roles r
#             )
#         ) AS community
#     FROM communities c
#     JOIN users u ON u.id = c.admin_id
#     WHERE c.id = :community_id;
#     """)
    
#     result = db.execute(query, {"community_id": community_id}).fetchone()
#     if result is None:
#         raise HTTPException(status_code=404, detail="Community not found")
    
#     return result[0]  # Fetchone returns a tuple

# # Endpoint to get all communities
# @router.get("/communities")
# def read_all_communities(db: Session = Depends(get_db)):
#     query = text("""
#     SELECT
#         json_build_object(
#             'communityId', c.community_id,
#             'name', c.name,
#             'description', c.description,
#             'createdAt', c.created_at,
#             'admin', json_build_object(
#                 'userId', u.id,
#                 'username', u.username,
#                 'email', u.email
#             ),
#             'members', (
#                 SELECT json_agg(
#                     json_build_object(
#                         'userId', m.id,
#                         'username', m.username,
#                         'email', m.email,
#                         'roles', (
#                             SELECT array_agg(r.id)
#                             FROM roles r
#                             JOIN community_member_role cmr ON cmr.role_id = r.id
#                             WHERE cmr.community_member_id = cm.id
#                         ),
#                         'joinedAt', cm.joined_at
#                     )
#                 )
#                 FROM community_member cm
#                 JOIN users m ON m.id = cm.user_id
#                 WHERE cm.community_id = c.id
#             ),
#             'roles', (
#                 SELECT json_agg(
#                     json_build_object(
#                         'roleId', r.id,
#                         'name', r.name,
#                         'permissions', r.permissions
#                     )
#                 )
#                 FROM roles r
#             )
#         ) AS community
#     FROM communities c
#     JOIN users u ON u.id = c.admin_id;
#     """)
    
#     result = db.execute(query).fetchall()
#     if not result:
#         raise HTTPException(status_code=404, detail="No communities found")
    
#     return [row[0] for row in result]  # Fetchall returns a list of tuples



######################## Roles ###########

# Role Routes
# @router.post("/roles/", response_model=schemas.Role)
# def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
#     return main.create_role(db=db, role=role)

# @router.get("/roles/")
# def read_roles( db: Session = Depends(get_db)):
#     roles = main.get_roles(db)
#     return roles

# @router.get("/roles/{role_id}", response_model=schemas.Role)
# def read_role(role_id: int, db: Session = Depends(get_db)):
#     role = main.get_role(db, role_id=role_id)
#     if role is None:
#         raise HTTPException(status_code=404, detail="Role not found")
#     return role

# @router.put("/roles/{role_id}", response_model=schemas.Role)
# def update_role(role_id: int, role_update: schemas.RoleCreate, db: Session = Depends(get_db)):
#     role = main.update_role(db, role_id=role_id, role_update=role_update)
#     if role is None:
#         raise HTTPException(status_code=404, detail="Role not found")
#     return role

# # Community Member Routes
# @router.post("/communities/{community_id}/members/")
# def add_member_to_community(member: schemas.CommunityMemberCreate, db: Session = Depends(get_db)):
#     return main.add_member_to_community(db=db, member=member)


# @router.get("/communities/{community_id}/members/", response_model=List[schemas.CommunityMember])
# def read_members_of_community(community_id: int, db: Session = Depends(get_db)):
#     members = main.get_members_of_community(db, community_id=community_id)
#     return members

