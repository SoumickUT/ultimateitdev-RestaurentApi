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

    # # Insert MenuCategory
    # insert_menu_category(db, schemas.MenuCategoryCreate(
    #     NAME="Burgers"
    # ))

    # # Insert MenuItem
    # insert_menu_item(db, schemas.MenuItemCreate(
    #     MENU_NAME="Cheeseburger",
    #     QUANTITY=100,
    #     QUNIT="pcs",
    #     PRICE=12.50,
    #     UNIT="pcs",
    #     CAT_ID=1,
    #     SUB_ID=1,
    #     NOTE="Delicious cheeseburger",
    #     ITEM_TYPE=1,
    #     MenuCode="CB001",
    #     IsVAT=True,
    #     IsDiscount=False,
    #     IsSupplimentary=False
    # ))

    # # Insert SubCategory
    # insert_sub_category(db, schemas.SubCategoryCreate(
    #     NAME="Burgers",
    #     CAT_ID=1
    # ))


    # Example of inserting multiple MenuCategories
    # Insert multiple MenuCategories
    categories = [
        {"NAME": "Burgers"},
        {"NAME": "Pizzas"},
        {"NAME": "Salads"},
        {"NAME": "Drinks"},
        {"NAME": "Desserts"},
        {"NAME": "Appetizers"},
        {"NAME": "Main Courses"},
        {"NAME": "Side Dishes"},
        {"NAME": "Breakfast"},
        {"NAME": "Snacks"},
    ]

    for category in categories:
        insert_menu_category(db, schemas.MenuCategoryCreate(**category))

    # Insert multiple SubCategories for the "Burgers" category
    # subcategories = [
    #     {"NAME": "Beef Burgers", "CAT_ID": 1},
    #     {"NAME": "Veggie Burgers", "CAT_ID": 1},
    #     {"NAME": "Chicken Burgers", "CAT_ID": 1},
    #     {"NAME": "Fish Burgers", "CAT_ID": 1},
    #     {"NAME": "Spicy Burgers", "CAT_ID": 1},
    # ]
    
    subcategories =[
    {
        "NAME": "Beef Burgers",
        "CAT_ID": 1
    },
    {
        "NAME": "Veggie Burgers",
        "CAT_ID": 1
    },
    {
        "NAME": "Chicken Burgers",
        "CAT_ID": 1
    },
    {
        "NAME": "Fish Burgers",
        "CAT_ID": 1
    },
    {
        "NAME": "Spicy Burgers",
        "CAT_ID": 1
    },
    {
        "NAME": "Margherita Pizza",
        "CAT_ID": 2
    },
    {
        "NAME": "Pepperoni Pizza",
        "CAT_ID": 2
    },
    {
        "NAME": "BBQ Chicken Pizza",
        "CAT_ID": 2
    },
    {
        "NAME": "Veggie Pizza",
        "CAT_ID": 2
    },
    {
        "NAME": "Hawaiian Pizza",
        "CAT_ID": 2
    },
    {
        "NAME": "Caesar Salad",
        "CAT_ID": 3
    },
    {
        "NAME": "Greek Salad",
        "CAT_ID": 3
    },
    {
        "NAME": "Cobb Salad",
        "CAT_ID": 3
    },
    {
        "NAME": "Garden Salad",
        "CAT_ID": 3
    },
    {
        "NAME": "Pasta Salad",
        "CAT_ID": 3
    }
]


    for subcategory in subcategories:
        insert_sub_category(db, schemas.SubCategoryCreate(**subcategory))

    # Insert multiple MenuItems for the "Burgers" category and subcategories
    menu_items = [
    {
        "MENU_NAME": "Cheeseburger",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 12.50,
        "UNIT": "pcs",
        "CAT_ID": 1,
        "SUB_ID": 1,
        "NOTE": "Delicious cheeseburger",
        "ITEM_TYPE": 1,
        "MenuCode": "CB001",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Veggie Burger",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 10.00,
        "UNIT": "pcs",
        "CAT_ID": 1,
        "SUB_ID": 2,
        "NOTE": "Healthy veggie burger",
        "ITEM_TYPE": 1,
        "MenuCode": "VB001",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Chicken Burger",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 11.00,
        "UNIT": "pcs",
        "CAT_ID": 1,
        "SUB_ID": 3,
        "NOTE": "Juicy chicken burger",
        "ITEM_TYPE": 1,
        "MenuCode": "CBG001",
        "IsVAT": True,
        "IsDiscount": True,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Fish Burger",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 12.00,
        "UNIT": "pcs",
        "CAT_ID": 1,
        "SUB_ID": 4,
        "NOTE": "Fresh fish burger",
        "ITEM_TYPE": 1,
        "MenuCode": "FB001",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Spicy Burger",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 13.50,
        "UNIT": "pcs",
        "CAT_ID": 1,
        "SUB_ID": 5,
        "NOTE": "Extra spicy burger",
        "ITEM_TYPE": 1,
        "MenuCode": "SB001",
        "IsVAT": True,
        "IsDiscount": True,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Margherita Pizza",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 15.00,
        "UNIT": "pcs",
        "CAT_ID": 2,
        "SUB_ID": 1,
        "NOTE": "Classic Margherita pizza",
        "ITEM_TYPE": 1,
        "MenuCode": "PZ001",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Pepperoni Pizza",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 18.00,
        "UNIT": "pcs",
        "CAT_ID": 2,
        "SUB_ID": 2,
        "NOTE": "Loaded with pepperoni",
        "ITEM_TYPE": 1,
        "MenuCode": "PZ002",
        "IsVAT": True,
        "IsDiscount": True,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "BBQ Chicken Pizza",
        "QUANTITY": 1,
        "QUNIT": "pcs",
        "PRICE": 20.00,
        "UNIT": "pcs",
        "CAT_ID": 2,
        "SUB_ID": 3,
        "NOTE": "Topped with BBQ chicken",
        "ITEM_TYPE": 1,
        "MenuCode": "PZ003",
        "IsVAT": True,
        "IsDiscount": True,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Caesar Salad",
        "QUANTITY": 1,
        "QUNIT": "bowl",
        "PRICE": 9.00,
        "UNIT": "bowl",
        "CAT_ID": 3,
        "SUB_ID": 1,
        "NOTE": "Classic Caesar salad",
        "ITEM_TYPE": 1,
        "MenuCode": "SL001",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Greek Salad",
        "QUANTITY": 1,
        "QUNIT": "bowl",
        "PRICE": 10.00,
        "UNIT": "bowl",
        "CAT_ID": 3,
        "SUB_ID": 2,
        "NOTE": "Greek-style salad with feta",
        "ITEM_TYPE": 1,
        "MenuCode": "SL002",
        "IsVAT": True,
        "IsDiscount": True,
        "IsSupplimentary": False
    },
    {
        "MENU_NAME": "Garden Salad",
        "QUANTITY": 1,
        "QUNIT": "bowl",
        "PRICE": 8.50,
        "UNIT": "bowl",
        "CAT_ID": 3,
        "SUB_ID": 3,
        "NOTE": "Fresh garden salad",
        "ITEM_TYPE": 1,
        "MenuCode": "SL003",
        "IsVAT": True,
        "IsDiscount": False,
        "IsSupplimentary": False
    }
]


    for item in menu_items:
        insert_menu_item(db, schemas.MenuItemCreate(**item))
    
    # Insert 20 TableInfo records
    for i in range(1, 60):
        insert_table_info(db, schemas.TableInfoCreate(
            Name=f"Table {i}",
            tblType="Dining",
            tblStatus=random.choice(["Available", "Occupied", "Reserved"])
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


