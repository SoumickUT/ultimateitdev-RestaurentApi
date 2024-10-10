from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    BigInteger, Column, Float, Integer, String, 
    ForeignKey, DateTime, Boolean, JSON, LargeBinary, Date, Table
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy_utils import URLType
from datetime import datetime, timezone, timedelta
from email.policy import default
import email

from src.app.common.properties import properties

Base = declarative_base()
metadata = Base.metadata

# # Association Table for Community Members and Roles
# community_member_role = Table('community_member_role', Base.metadata,
#     Column('community_member_id', Integer, ForeignKey('community_member.id'), primary_key=True),
#     Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
# )

# class Community(Base):
#     __tablename__ = 'communities'

#     id = Column(Integer, primary_key=True, index=True)
#     community_id = Column(String, unique=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     admin_id = Column(Integer, ForeignKey('users.id'))

#     admin = relationship("User", backref=backref('admin_of'))
#     members = relationship("CommunityMember", backref="community")

# class Role(Base):
#     __tablename__ = "roles"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True)
#     permissions = Column(ARRAY(String))

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     # other fields...

# class CommunityMember(Base):
#     __tablename__ = 'community_member'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     community_id = Column(Integer, ForeignKey('communities.id'))
#     joined_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship("User", backref=backref('communities'))
#     roles = relationship("Role", secondary=community_member_role, backref="members")


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True)
#     email = Column(String(120), unique=True, index=True)
#     full_name = Column(String(100))
#     hashed_password = Column(String(128))
#     is_active = Column(Boolean, default=True)
#     created_at = Column(DateTime, default=datetime.utcnow)


class TempOrder(Base):
    __tablename__ = 'TEMP_ORDER_1'
    
    Id = Column(Integer, primary_key=True, index=True)
    MEMO_NO = Column(Integer)
    KOT_NO = Column(Integer)
    TABLE_CODE = Column(String)
    FOR_PERSONS = Column(Integer)
    ORDER_TYPE = Column(String)
    ATTENDANT = Column(String)
    ORDER_DATE = Column(DateTime)
    START_TIME = Column(String)
    SUBTOTAL = Column(Float)
    SALES_TAX = Column(Float)
    DISCOUNT_RATE = Column(Float)
    DISCOUNT_AMT = Column(Float)
    SERVICE_CHARGE = Column(Float)
    TOTAL_AMOUNT = Column(Float) #Done
    CUS_NAME = Column(String)
    DISC_TYPE = Column(String)
    ITEM_DESC = Column(Integer)
    BILL_PRINTED = Column(Integer)
    STATUS = Column(String)
    Waiter = Column(String)
    ManualKot = Column(Integer)
    EntryTime = Column(DateTime, default=datetime.utcnow)
    Insert_Synced = Column(Boolean)
    KotPrinted = Column(Boolean)
    KotResubmitted = Column(Boolean)
    ReKotPrinted = Column(Boolean)
    CUS_ID = Column(Integer)
    CUS_PHONE = Column(String)
    SupplimetaryAmount = Column(Float)
    MachineName = Column(String)
    Location = Column(String)
    SCRate = Column(Float)
    VatRate = Column(Float)


class TempOrder2(Base):
    __tablename__ = "TEMP_ORDER_2"

    AutoID = Column(Integer, primary_key=True, index=True)
    KOT_NO = Column(Integer)
    SLNO = Column(Integer)
    MENU_ID = Column(Integer)
    MENU_NAME = Column(String)
    MENU_TYPE = Column(Integer)
    QUANTITY = Column(Float)
    PRICE = Column(Float)
    AMOUNT = Column(Float)
    INCLUDEVAT = Column(Float)
    INCLUDESC = Column(Float)
    PromotionID = Column(Integer)
    PromotionPercent = Column(Float)
    Cat_ID = Column(Integer)
    Insert_Synced = Column(Boolean)
    SupplimetaryAmt = Column(Float)
    TaxRate = Column(Integer)

class CustomerInfo(Base):
    __tablename__ = "CUSTOMER_INFO"

    CUS_ID = Column(Integer, primary_key=True, index=True)
    CardNo = Column(String)
    CUS_NAME = Column(String)
    ADDRESS1 = Column(String)
    ADDRESS2 = Column(String)
    OPENNING_BALANCE = Column(Float)
    PHONE_NO = Column(String)
    MOBILE_NO = Column(String)
    FAX_NO = Column(String)
    EMAIL_ID = Column(String)
    ParentID = Column(Integer)
    LR = Column(String)
    CorporateAccID = Column(Integer)
    AccId = Column(Integer)
    SourceID = Column(Integer)

class WaiterInfo(Base):
    __tablename__ = "Waiter_Info"

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String)
    Remarks = Column(String)
    
class SaleMaster(Base):
    __tablename__ = "SALE_MASTER"

    ORDER_NUMBER = Column(Integer, primary_key=True, index=True)
    MEMO_NO = Column(Integer)
    FOR_PERSONS = Column(Integer)
    SALE_TYPE = Column(String)
    ORDER_DATE = Column(DateTime)
    SUBTOTAL = Column(Float)
    VAT = Column(Float)
    SERVICE_CHARGE = Column(Float)
    DISCOUNT_AMT = Column(Float)
    TOTAL_AMOUNT = Column(Float)
    PAID_AMOUNT = Column(Float)
    DUE_AMOUNT = Column(Float)
    PAYMENT_METHOD = Column(String)
    PAYMENT_MEDIA = Column(String)
    MACHINE_OF = Column(String)
    VID = Column(Integer)
    PAIDVID = Column(Integer)
    CUS_ID = Column(Integer)
    USERID = Column(String)
    PRICE_PER = Column(Float)
    CARDVID = Column(Integer)
    ID = Column(Integer)
    TABLENO = Column(String)
    WAITER = Column(String)
    KOT_NO = Column(Integer)
    EntryTime = Column(DateTime)
    ManualKOT = Column(String)
    InsertType = Column(String)
    SupplimetaryAmount = Column(Float)
    ComplementaryAmt = Column(Float)
    CusName = Column(String)
    
class Promotion(Base):
    __tablename__ = "PromotionDetails"
    
    PromotionID = Column(Integer,primary_key=True, index=True)
    MenuID = Column(Integer)
    DiscountPercent = Column(Float)
    

class Voucher(Base):
    __tablename__ = "Voucher"
    
    Vid= Column(Integer,primary_key=True)
    VDate= Column(DateTime)
    VType = Column(Integer)
    VNO= Column(String)
    Posted= Column(String)  # Assuming Posted is a boolean flag
    UserId= Column(String)
    Status= Column(Integer)
    Particulars= Column(String)
    Location= Column(Integer)
    LastUpdated= Column(DateTime)
    
class MenuCategory(Base):
    __tablename__ = "MENUCATEGORY"
    ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String)

class MenuItem(Base):
    __tablename__ = "MENUITEM"
    MENU_ID = Column(Integer, primary_key=True, index=True)
    MENU_NAME = Column(String)
    QUANTITY = Column(Float)
    QUNIT = Column(String)
    PRICE = Column(Float)
    UNIT = Column(String)
    CAT_ID = Column(Integer, ForeignKey("MENUCATEGORY.ID"))
    SUB_ID = Column(Integer)
    NOTE = Column(String)
    ITEM_TYPE = Column(Integer)
    MenuCode = Column(String)
    IsVAT = Column(Boolean)
    IsDiscount = Column(Boolean)
    IsSupplimentary = Column(Boolean)

class SubCategory(Base):
    __tablename__ = "SUBCATEGORY"
    SUB_ID = Column(Integer, primary_key=True, index=True)
    NAME = Column(String)
    CAT_ID = Column(Integer, ForeignKey("MENUCATEGORY.ID"))


class UserInfo(Base):
    __tablename__ = "UserInfo"
    UserID = Column(Integer, primary_key=True, index=True)
    UserName = Column(String)
    FullName = Column(String)
    SetPassword = Column(String)
    UserType = Column(String)
    Status = Column(Boolean)
    BackdateEntry = Column(Boolean)
    
class TableInfo(Base):
    __tablename__ = 'TableInfo'
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    tblType = Column(String)
    tblStatus = Column(String)



# -- Drop the existing ID column constraint if there is any
# ALTER TABLE [dbo].[Waiter_Info] DROP CONSTRAINT IF EXISTS [DF_Waiter_Info_ID];

# -- Alter the ID column to be an identity column
# ALTER TABLE [dbo].[Waiter_Info]
# DROP COLUMN ID;

# ALTER TABLE [dbo].[Waiter_Info]
# ADD ID INT IDENTITY(1,1) NOT NULL;


# ALTER TABLE [dbo].[Waiter_Info] DROP CONSTRAINT [PK_Waiter_Info];

# ALTER TABLE [dbo].[Waiter_Info] DROP COLUMN ID;

# ALTER TABLE [dbo].[Waiter_Info]
# ADD ID INT IDENTITY(1,1) NOT NULL;

# ALTER TABLE [dbo].[Waiter_Info]
# ADD CONSTRAINT [PK_Waiter_Info] PRIMARY KEY (ID);
