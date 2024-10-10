from sqlalchemy.orm import Session
from src.app.common.schemas import schemas
from src.app.common.models import models
from fastapi import HTTPException, status
from datetime import datetime
import random

# Insert dummy data for TempOrder
def insert_temp_order(db: Session, temp_order_data: schemas.TempOrderCreate):
    temp_order = models.TempOrder(**temp_order_data.dict())
    db.add(temp_order)
    db.commit()
    db.refresh(temp_order)
    return temp_order

# Insert dummy data for TempOrder2
def insert_temp_order2(db: Session, temp_order2_data: schemas.TempOrder2Create):
    temp_order2 = models.TempOrder2(**temp_order2_data.dict())
    db.add(temp_order2)
    db.commit()
    db.refresh(temp_order2)
    return temp_order2

# Insert dummy data for CustomerInfo
def insert_customer_info(db: Session, customer_info_data: schemas.CustomerInfoCreate):
    customer_info = models.CustomerInfo(**customer_info_data.dict())
    db.add(customer_info)
    db.commit()
    db.refresh(customer_info)
    return customer_info

# Insert dummy data for WaiterInfo
def insert_waiter_info(db: Session, waiter_info_data: schemas.WaiterInfoCreate):
    waiter_info = models.WaiterInfo(**waiter_info_data.dict())
    db.add(waiter_info)
    db.commit()
    db.refresh(waiter_info)
    return waiter_info

# Insert dummy data for SaleMaster
def insert_sale_master(db: Session, sale_master_data: schemas.SaleMasterCreate):
    sale_master = models.SaleMaster(**sale_master_data.dict())
    db.add(sale_master)
    db.commit()
    db.refresh(sale_master)
    return sale_master

# Insert dummy data for Promotion
def insert_promotion(db: Session, promotion_data: schemas.PromotionCreate):
    promotion = models.Promotion(**promotion_data.dict())
    db.add(promotion)
    db.commit()
    db.refresh(promotion)
    return promotion

# Insert dummy data for Voucher
def insert_voucher(db: Session, voucher_data: schemas.VoucherCreate):
    voucher = models.Voucher(**voucher_data.dict())
    db.add(voucher)
    db.commit()
    db.refresh(voucher)
    return voucher

# Insert dummy data for MenuCategory
def insert_menu_category(db: Session, menu_category_data: schemas.MenuCategoryCreate):
    menu_category = models.MenuCategory(**menu_category_data.dict())
    db.add(menu_category)
    db.commit()
    db.refresh(menu_category)
    return menu_category

# Insert dummy data for MenuItem
def insert_menu_item(db: Session, menu_item_data: schemas.MenuItemCreate):
    menu_item = models.MenuItem(**menu_item_data.dict())
    db.add(menu_item)
    db.commit()
    db.refresh(menu_item)
    return menu_item

# Insert dummy data for SubCategory
def insert_sub_category(db: Session, sub_category_data: schemas.SubCategoryCreate):
    sub_category = models.SubCategory(**sub_category_data.dict())
    db.add(sub_category)
    db.commit()
    db.refresh(sub_category)
    return sub_category

# Insert dummy data for UserInfo
def insert_user_info(db: Session, user_info_data: schemas.UserInfoCreate):
    user_info = models.UserInfo(**user_info_data.dict())
    db.add(user_info)
    db.commit()
    db.refresh(user_info)
    return user_info

# Insert dummy data for TableInfo
def insert_table_info(db: Session, table_info_data: schemas.TableInfoCreate):
    table_info = models.TableInfo(**table_info_data.dict())
    db.add(table_info)
    db.commit()
    db.refresh(table_info)
    return table_info

# Example of how to insert data using these functions
def insert_dummy_data(db: Session):
    # Example of inserting TempOrder
    insert_temp_order(db, schemas.TempOrderCreate(
        MEMO_NO=random.randint(1000, 9999),
        KOT_NO=random.randint(1000, 9999),
        TABLE_CODE="T01",
        FOR_PERSONS=random.randint(1, 10),
        ORDER_TYPE="Dine-In",
        ATTENDANT="John Doe",
        ORDER_DATE=datetime.utcnow(),
        START_TIME="12:00 PM",
        SUBTOTAL=50.00,
        SALES_TAX=5.00,
        DISCOUNT_RATE=10,
        DISCOUNT_AMT=5.00,
        SERVICE_CHARGE=3.00,
        TOTAL_AMOUNT=53.00,
        CUS_NAME="Jane Smith",
        DISC_TYPE="Percentage",
        ITEM_DESC=0,
        BILL_PRINTED=1,
        STATUS="Completed",
        Waiter="Alice",
        ManualKot=0,
        Insert_Synced=True,
        KotPrinted=True,
        KotResubmitted=False,
        ReKotPrinted=False,
        CUS_ID=random.randint(1, 100),
        CUS_PHONE="123-456-7890",
        SupplimetaryAmount=0,
        MachineName="POS-1",
        Location="Downtown",
        SCRate=0,
        VatRate=15
    ))

    # Insert TempOrder2 as an example
    insert_temp_order2(db, schemas.TempOrder2Create(
        KOT_NO=random.randint(1000, 9999),
        SLNO=1,
        MENU_ID=random.randint(1, 100),
        MENU_NAME="Cheeseburger",
        MENU_TYPE=1,
        QUANTITY=2,
        PRICE=12.50,
        AMOUNT=25.00,
        INCLUDEVAT=1,
        INCLUDESC=1,
        PromotionID=0,
        PromotionPercent=0,
        Cat_ID=1,
        Insert_Synced=True,
        SupplimetaryAmt=0,
        TaxRate=15
    ))

    # Insert CustomerInfo
    insert_customer_info(db, schemas.CustomerInfoCreate(
        CardNo="CUST" + str(random.randint(10000, 99999)),
        CUS_NAME="Jane Smith",
        ADDRESS1="123 Elm St",
        ADDRESS2="Apt 4B",
        OPENNING_BALANCE=100.00,
        PHONE_NO="123-456-7890",
        MOBILE_NO="987-654-3210",
        FAX_NO="123-456-7891",
        EMAIL_ID="jane.smith@example.com",
        ParentID=0,
        LR="None",
        CorporateAccID=0,
        AccId=1234,
        SourceID=0
    ))

    # Insert WaiterInfo
    insert_waiter_info(db, schemas.WaiterInfoCreate(
        Name="Alice",
        Remarks="Experienced waiter"
    ))

    # Insert SaleMaster
    insert_sale_master(db, schemas.SaleMasterCreate(
        MEMO_NO=random.randint(1000, 9999),
        FOR_PERSONS=random.randint(1, 10),
        SALE_TYPE="Dine-In",
        ORDER_DATE=datetime.utcnow(),
        SUBTOTAL=50.00,
        VAT=5.00,
        SERVICE_CHARGE=3.00,
        DISCOUNT_AMT=5.00,
        TOTAL_AMOUNT=53.00,
        PAID_AMOUNT=53.00,
        DUE_AMOUNT=0.00,
        PAYMENT_METHOD="Cash",
        PAYMENT_MEDIA="Cash",
        MACHINE_OF="Machine 1",
        VID=random.randint(1, 100),
        PAIDVID=random.randint(1, 100),
        CUS_ID=random.randint(1, 100),
        USERID="user123",
        PRICE_PER=50.00,
        CARDVID=random.randint(1, 100),
        ID=random.randint(1, 100),
        TABLENO="Table 1",
        WAITER="Alice",
        KOT_NO=random.randint(1000, 9999),
        EntryTime=datetime.utcnow(),
        ManualKOT="No",
        InsertType="Manual",
        SupplimetaryAmount=0,
        ComplementaryAmt=0,
        CusName="Jane Smith"
    ))

    # Insert Promotion
    insert_promotion(db, schemas.PromotionCreate(
        MenuID=random.randint(1, 100),
        DiscountPercent=15.0
    ))

    # Insert Voucher
    insert_voucher(db, schemas.VoucherCreate(
        VDate=datetime.utcnow(),
        VType=1,
        VNO="V001",
        Posted="True",
        UserId="user123",
        Status=1,
        Particulars="Discount Voucher",
        Location=1,
        LastUpdated=datetime.utcnow()
    ))

    # Insert MenuCategory
    insert_menu_category(db, schemas.MenuCategoryCreate(
        NAME="Burgers"
    ))

    # Insert MenuItem
    insert_menu_item(db, schemas.MenuItemCreate(
        MENU_NAME="Cheeseburger",
        QUANTITY=100,
        QUNIT="pcs",
        PRICE=12.50,
        UNIT="pcs",
        CAT_ID=1,
        SUB_ID=1,
        NOTE="Delicious cheeseburger",
        ITEM_TYPE=1,
        MenuCode="CB001",
        IsVAT=True,
        IsDiscount=False,
        IsSupplimentary=False
    ))

    # Insert SubCategory
    insert_sub_category(db, schemas.SubCategoryCreate(
        NAME="Burgers",
        CAT_ID=1
    ))

    # Insert UserInfo
    insert_user_info(db, schemas.UserInfoCreate(
        UserName="Soumick",
        FullName="Soumick Apon",
        SetPassword="password123",
        UserType="Admin",
        Status=True,
        BackdateEntry=False
    ))

    # Insert TableInfo
    insert_table_info(db, schemas.TableInfoCreate(
        Name="Table 1",
        tblType="Dining",
        tblStatus="Available"
    ))
