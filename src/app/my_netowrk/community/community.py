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



router = APIRouter(prefix=properties.skill, tags=[properties.skill_tag])




get_db = database.get_db



######################################

def get_new_memo_no(db: Session):
    # SQL query to find the last MEMO_NO
    last_memo_no = db.query(func.max(models.TempOrder.MEMO_NO)).scalar()

    # Calculating the new MEMO_NO
    if last_memo_no is not None:
        new_memo_no = int(last_memo_no) + 1
    else:
        new_memo_no = 1  # Default to 1 if no records are found

    return new_memo_no

@router.post("/create_order/")
def create_order(order: schemas.OrderBase, db: Session = Depends(get_db)):
    new_memo_no = get_new_memo_no(db)
    
    db_order = models.TempOrder(
        MEMO_NO=new_memo_no,
        KOT_NO=order.KOT_NO,
        TABLE_CODE=order.TABLE_CODE,
        FOR_PERSONS=order.FOR_PERSONS,
        ORDER_TYPE=order.ORDER_TYPE,
        ATTENDANT=order.ATTENDANT,
        ORDER_DATE=order.ORDER_DATE,
        START_TIME=order.START_TIME,
        SUBTOTAL=order.SUBTOTAL,
        SALES_TAX=order.SALES_TAX,
        DISCOUNT_RATE=order.DISCOUNT_RATE,
        DISCOUNT_AMT=order.DISCOUNT_AMT,
        SERVICE_CHARGE=order.SERVICE_CHARGE,
        TOTAL_AMOUNT=order.TOTAL_AMOUNT,
        CUS_NAME=order.CUS_NAME,
        DISC_TYPE=order.DISC_TYPE,
        ITEM_DESC=order.ITEM_DESC,
        BILL_PRINTED=order.BILL_PRINTED,
        STATUS=order.STATUS,
        Waiter=order.Waiter,
        ManualKot=order.ManualKot,
        EntryTime=order.EntryTime,
        Insert_Synced=order.Insert_Synced,
        KotPrinted=order.KotPrinted,
        KotResubmitted=order.KotResubmitted,
        ReKotPrinted=order.ReKotPrinted,
        CUS_ID=order.CUS_ID,
        CUS_PHONE=order.CUS_PHONE,
        SupplimetaryAmount=order.SupplimetaryAmount,
        MachineName=order.MachineName,
        Location=order.Location,
        SCRate=order.SCRate,
        VatRate=order.VatRate
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.orderItems:
        db_order_item = models.TempOrder2(
            KOT_NO=item.KOT_NO,
            SLNO=item.SLNO,
            MENU_ID=item.MENU_ID,
            MENU_NAME=item.MENU_NAME,
            MENU_TYPE=item.MENU_TYPE,
            QUANTITY=item.QUANTITY,
            PRICE=item.PRICE,
            AMOUNT=item.AMOUNT,
            INCLUDEVAT=item.INCLUDEVAT,
            INCLUDESC=item.INCLUDESC,
            PromotionID=item.PromotionID,
            PromotionPercent=item.PromotionPercent,
            Cat_ID=item.Cat_ID,
            Insert_Synced=item.Insert_Synced,
            SupplimetaryAmt=item.SupplimetaryAmt,
            TaxRate=item.TaxRate
        )
        db.add(db_order_item)

    for customer in order.customerInfo:
        db_customer = models.CustomerInfo(
            CardNo=customer.CardNo,
            CUS_NAME=customer.CUS_NAME,
            ADDRESS1=customer.ADDRESS1,
            ADDRESS2=customer.ADDRESS2,
            OPENNING_BALANCE=customer.OPENNING_BALANCE,
            PHONE_NO=customer.PHONE_NO,
            MOBILE_NO=customer.MOBILE_NO,
            FAX_NO=customer.FAX_NO,
            EMAIL_ID=customer.EMAIL_ID,
            ParentID=customer.ParentID,
            LR=customer.LR,
            CorporateAccID=customer.CorporateAccID,
            AccId=customer.AccId,
            SourceID=customer.SourceID
        )
        db.add(db_customer)

    db.commit()

    return {"message": "Order created successfully"}


@router.get("/temp_orders/{memo_no}", response_model=schemas.TempOrder)
def read_temp_order(memo_no: int, db: Session = Depends(get_db)):
    db_temp_order = main.get_temp_order(db, memo_no=memo_no)
    if db_temp_order is None:
        raise HTTPException(status_code=404, detail="TempOrder not found")
    return db_temp_order

@router.get("/temp_orders/")
def read_temp_orders( db: Session = Depends(get_db)):
    temp_orders = main.get_temp_orders(db)
    return temp_orders

# @router.get("/temp_order_1")
# async def get_temp_order_1(db: Session = Depends(get_db)):
#     query = text("SELECT * FROM [Res_Halditest_Db].[dbo].[TEMP_ORDER_1]")
#     result = db.execute(query)
#     columns = result.keys()
#     data = [dict(zip(columns, row)) for row in result.fetchall()]
#     return {"data": data}

@router.get("/temp_order_1")
async def get_temp_order_1(db: Session = Depends(get_db)):
    query = text("SELECT * FROM TEMP_ORDER_1")
    result = db.execute(query)
    columns = result.keys()
    data = [dict(zip(columns, row)) for row in result.fetchall()]
    return {"data": data}

@router.put("/update_order/{MEMO_NO}")
def update_order(MEMO_NO: int, order: schemas.OrderBase, db: Session = Depends(get_db)):
    db_order = db.query(models.TempOrder).filter(models.TempOrder.MEMO_NO == MEMO_NO).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Update order details
    db_order.KOT_NO = order.KOT_NO
    db_order.TABLE_CODE = order.TABLE_CODE
    db_order.FOR_PERSONS = order.FOR_PERSONS
    db_order.ORDER_TYPE = order.ORDER_TYPE
    db_order.ATTENDANT = order.ATTENDANT
    db_order.ORDER_DATE = order.ORDER_DATE
    db_order.START_TIME = order.START_TIME
    db_order.SUBTOTAL = order.SUBTOTAL
    db_order.SALES_TAX = order.SALES_TAX
    db_order.DISCOUNT_RATE = order.DISCOUNT_RATE
    db_order.DISCOUNT_AMT = order.DISCOUNT_AMT
    db_order.SERVICE_CHARGE = order.SERVICE_CHARGE
    db_order.TOTAL_AMOUNT = order.TOTAL_AMOUNT
    db_order.CUS_NAME = order.CUS_NAME
    db_order.DISC_TYPE = order.DISC_TYPE
    db_order.ITEM_DESC = order.ITEM_DESC
    db_order.BILL_PRINTED = order.BILL_PRINTED
    db_order.STATUS = order.STATUS
    db_order.Waiter = order.Waiter
    db_order.ManualKot = order.ManualKot
    db_order.EntryTime = order.EntryTime
    db_order.Insert_Synced = order.Insert_Synced
    db_order.KotPrinted = order.KotPrinted
    db_order.KotResubmitted = order.KotResubmitted
    db_order.ReKotPrinted = order.ReKotPrinted
    db_order.CUS_ID = order.CUS_ID
    db_order.CUS_PHONE = order.CUS_PHONE
    db_order.SupplimetaryAmount = order.SupplimetaryAmount
    db_order.MachineName = order.MachineName
    db_order.Location = order.Location
    db_order.SCRate = order.SCRate
    db_order.VatRate = order.VatRate

    db.commit()
    db.refresh(db_order)

    # Update order items
    for item in order.orderItems:
        db_order_item = db.query(models.TempOrder2).filter(
            models.TempOrder2.KOT_NO == item.KOT_NO,
            models.TempOrder2.SLNO == item.SLNO
        ).first()
        if db_order_item:
            db_order_item.MENU_ID = item.MENU_ID
            db_order_item.MENU_NAME = item.MENU_NAME
            db_order_item.MENU_TYPE = item.MENU_TYPE
            db_order_item.QUANTITY = item.QUANTITY
            db_order_item.PRICE = item.PRICE
            db_order_item.AMOUNT = item.AMOUNT
            db_order_item.INCLUDEVAT = item.INCLUDEVAT
            db_order_item.INCLUDESC = item.INCLUDESC
            db_order_item.PromotionID = item.PromotionID
            db_order_item.PromotionPercent = item.PromotionPercent
            db_order_item.Cat_ID = item.Cat_ID
            db_order_item.Insert_Synced = item.Insert_Synced
            db_order_item.SupplimetaryAmt = item.SupplimetaryAmt
            db_order_item.TaxRate = item.TaxRate

    # Update customer info
    for customer in order.customerInfo:
        db_customer = db.query(models.CustomerInfo).filter(
            models.CustomerInfo.CardNo == customer.CardNo
        ).first()
        if db_customer:
            db_customer.CUS_NAME = customer.CUS_NAME
            db_customer.ADDRESS1 = customer.ADDRESS1
            db_customer.ADDRESS2 = customer.ADDRESS2
            db_customer.OPENNING_BALANCE = customer.OPENNING_BALANCE
            db_customer.PHONE_NO = customer.PHONE_NO
            db_customer.MOBILE_NO = customer.MOBILE_NO
            db_customer.FAX_NO = customer.FAX_NO
            db_customer.EMAIL_ID = customer.EMAIL_ID
            db_customer.ParentID = customer.ParentID
            db_customer.LR = customer.LR
            db_customer.CorporateAccID = customer.CorporateAccID
            db_customer.AccId = customer.AccId
            db_customer.SourceID = customer.SourceID

    db.commit()

    return {"message": "Order updated successfully"}


import logging

@router.get("/get_orders/{MEMO_NO}/{KOT_NO}", response_model=schemas.OrderBase)
def get_order(MEMO_NO: int, KOT_NO: int, db: Session = Depends(get_db)):
    try:
        db_order = db.query(models.TempOrder).filter(models.TempOrder.MEMO_NO == MEMO_NO).first()
        if not db_order:
            raise HTTPException(status_code=404, detail="Order not found")

        order_items = db.query(models.TempOrder2).filter(models.TempOrder2.KOT_NO == KOT_NO).all()
        customer_info = db.query(models.CustomerInfo).filter(models.CustomerInfo.CardNo == db_order.CUS_ID).all()

        logging.info("Order Fields: %s", db_order.__dict__)
        logging.info("Order Items: %s", [item.__dict__ for item in order_items])
        logging.info("Customer Info: %s", [customer.__dict__ for customer in customer_info])

        order = schemas.OrderBase(
            KOT_NO=db_order.KOT_NO,
            TABLE_CODE=db_order.TABLE_CODE,
            FOR_PERSONS=db_order.FOR_PERSONS,
            ORDER_TYPE=db_order.ORDER_TYPE,
            ATTENDANT=db_order.ATTENDANT,
            ORDER_DATE=db_order.ORDER_DATE,
            START_TIME=db_order.START_TIME,
            SUBTOTAL=db_order.SUBTOTAL,
            SALES_TAX=db_order.SALES_TAX,
            DISCOUNT_RATE=db_order.DISCOUNT_RATE,
            DISCOUNT_AMT=db_order.DISCOUNT_AMT,
            SERVICE_CHARGE=db_order.SERVICE_CHARGE,
            TOTAL_AMOUNT=db_order.TOTAL_AMOUNT,
            CUS_NAME=db_order.CUS_NAME,
            DISC_TYPE=db_order.DISC_TYPE,
            ITEM_DESC=db_order.ITEM_DESC,
            BILL_PRINTED=db_order.BILL_PRINTED,
            STATUS=db_order.STATUS,
            Waiter=db_order.Waiter,
            ManualKot=db_order.ManualKot,
            EntryTime=db_order.EntryTime,
            Insert_Synced=db_order.Insert_Synced,
            KotPrinted=db_order.KotPrinted,
            KotResubmitted=db_order.KotResubmitted,
            ReKotPrinted=db_order.ReKotPrinted,
            CUS_ID=db_order.CUS_ID,
            CUS_PHONE=db_order.CUS_PHONE,
            SupplimetaryAmount=db_order.SupplimetaryAmount,
            MachineName=db_order.MachineName,
            Location=db_order.Location,
            SCRate=db_order.SCRate,
            VatRate=db_order.VatRate,
            orderItems=[
                schemas.OrderItem(
                    KOT_NO=item.KOT_NO,
                    SLNO=item.SLNO,
                    MENU_ID=item.MENU_ID,
                    MENU_NAME=item.MENU_NAME,
                    MENU_TYPE=item.MENU_TYPE,
                    QUANTITY=item.QUANTITY,
                    PRICE=item.PRICE,
                    AMOUNT=item.AMOUNT,
                    INCLUDEVAT=item.INCLUDEVAT,
                    INCLUDESC=item.INCLUDESC,
                    PromotionID=item.PromotionID,
                    PromotionPercent=item.PromotionPercent,
                    Cat_ID=item.Cat_ID,
                    Insert_Synced=item.Insert_Synced,
                    SupplimetaryAmt=item.SupplimetaryAmt,
                    TaxRate=item.TaxRate
                ) for item in order_items
            ],
            customerInfo=[
                schemas.CustomerInfo(
                    CardNo=customer.CardNo,
                    CUS_NAME=customer.CUS_NAME,
                    ADDRESS1=customer.ADDRESS1,
                    ADDRESS2=customer.ADDRESS2,
                    OPENNING_BALANCE=customer.OPENNING_BALANCE,
                    PHONE_NO=customer.PHONE_NO,
                    MOBILE_NO=customer.MOBILE_NO,
                    FAX_NO=customer.FAX_NO,
                    EMAIL_ID=customer.EMAIL_ID,
                    ParentID=customer.ParentID,
                    LR=customer.LR,
                    CorporateAccID=customer.CorporateAccID,
                    AccId=customer.AccId,
                    SourceID=customer.SourceID
                ) for customer in customer_info
            ]
        )

        return order

    except Exception as e:
        logging.error("Error occurred: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred while fetching the order")

# Make sure to configure logging
logging.basicConfig(level=logging.INFO)


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

