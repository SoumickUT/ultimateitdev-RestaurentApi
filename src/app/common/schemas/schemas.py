
from pydantic import BaseModel,EmailStr, HttpUrl
from sqlalchemy import BIGINT, BigInteger, orm
from typing import Optional,Union,Set
from datetime import datetime, time, timedelta,date
from sqlalchemy.sql.schema import Column
from datetime import datetime

from typing import List



#####################################


# class UserCreate(BaseModel):
#     username: str
#     email: EmailStr

# class UserUpdate(BaseModel):
#     username: Optional[str]
#     email: Optional[EmailStr]

# class User(BaseModel):
#     id: int
#     username: str
#     email: EmailStr

#     class Config:
#         orm_mode = True

# class RoleBase(BaseModel):
#     name: str
#     permissions: List[str]

# class RoleCreate(RoleBase):
#     pass

# class Role(RoleBase):
#     id: int

#     class Config:
#         orm_mode = True


# class RoleUpdate(BaseModel):
#     name: Optional[str] = None
#     permissions: Optional[List[str]] = None

# class CommunityMemberCreate(BaseModel):
#     user_id: int
#     community_id: int  # Add this field
#     roles: List[int]

# class CommunityMember(BaseModel):
#     id: int
#     user_id: int
#     community_id: int
#     joined_at: datetime
#     roles: List[int]

#     class Config:
#         orm_mode = True


# class CommunityBase(BaseModel):
#     community_id: str
#     name: str
#     description: str
#     admin_id: int

# class CommunityCreate(CommunityBase):
#     pass

# class Community(CommunityBase):
#     id: int
#     admin: User
#     members: List[CommunityMember]

#     class Config:
#         orm_mode = True



# class UserBase(BaseModel):
#     userId: str
#     username: str
#     email: EmailStr

#     class Config:
#         orm_mode = True


# class CommunityMembersBase(BaseModel):
#     userId: str
#     username: str
#     email: EmailStr
#     roles: List[str]
#     joinedAt: datetime

#     class Config:
#         orm_mode = True

# class CommunityBase(BaseModel):
#     communityId: str
#     name: str
#     description: str
#     createdAt: datetime
#     admin: UserBase
#     members: List[CommunityMembersBase]
#     roles: List[RoleBase]

#     class Config:
#         orm_mode = True


# class Communitys(CommunityBase):
#     id: str

#     class Config:
#         orm_mode = True


# from typing import List, Optional
# from pydantic import BaseModel
# from datetime import datetime

# class UserSchema(BaseModel):
#     userId: int
#     username: str
#     email: str

#     class Config:
#         orm_mode = True

# class RoleSchema(BaseModel):
#     roleId: int
#     name: str
#     permissions: List[str]

#     class Config:
#         orm_mode = True

# class CommunityMemberSchema(BaseModel):
#     userId: int
#     username: str
#     email: str
#     roles: List[int]
#     joinedAt: datetime

#     class Config:
#         orm_mode = True

# class CommunitySchema(BaseModel):
#     communityId: str
#     name: str
#     description: str
#     createdAt: datetime
#     admin: UserSchema
#     members: List[CommunityMemberSchema]
#     roles: List[RoleSchema]

#     class Config:
#         orm_mode = True

class TempOrderBase(BaseModel):
    KOT_NO: Optional[int] = None
    TABLE_CODE: Optional[str] = None
    FOR_PERSONS: Optional[int] = None
    ORDER_TYPE: Optional[str] = None
    ATTENDANT: Optional[str] = None
    ORDER_DATE: Optional[datetime] = None
    START_TIME: Optional[str] = None
    SUBTOTAL: Optional[float] = None
    SALES_TAX: Optional[float] = None
    DISCOUNT_RATE: Optional[float] = None
    DISCOUNT_AMT: Optional[float] = None
    SERVICE_CHARGE: Optional[float] = None
    TOTAL_AMOUNT: Optional[float] = None
    CUS_NAME: Optional[str] = None
    DISC_TYPE: Optional[str] = None
    ITEM_DESC: Optional[int] = None
    BILL_PRINTED: Optional[int] = None  # Adjusted for bit type
    STATUS: Optional[str] = None
    Waiter: Optional[str] = None
    ManualKot: Optional[bool] = None  # Adjusted for bit type
    EntryTime: Optional[datetime] = None
    Insert_Synced: Optional[bool] = None  # Adjusted for bit type
    KotPrinted: Optional[bool] = None  # Adjusted for bit type
    KotResubmitted: Optional[bool] = None  # Adjusted for bit type
    ReKotPrinted: Optional[bool] = None  # Adjusted for bit type
    CUS_ID: Optional[int] = None
    CUS_PHONE: Optional[str] = None
    SupplimetaryAmount: Optional[float] = None
    MachineName: Optional[str] = None
    Location: Optional[str] = None
    SCRate: Optional[float] = None
    VatRate: Optional[float] = None

class TempOrderCreate(TempOrderBase):
    pass

class TempOrder(TempOrderBase):
    MEMO_NO: int

    class Config:
        orm_mode = True



# Pydantic models for request bodies
class OrderItem(BaseModel):
    KOT_NO: int
    SLNO: int
    MENU_ID: int
    MENU_NAME: str
    MENU_TYPE: int
    QUANTITY: float
    PRICE: float
    AMOUNT: float
    INCLUDEVAT: float
    INCLUDESC: float
    PromotionID: int
    PromotionPercent: float
    Cat_ID: int
    Insert_Synced: bool
    SupplimetaryAmt: float
    TaxRate: int

class CustomerInfoBase(BaseModel):
    CardNo: str
    CUS_NAME: str
    ADDRESS1: str
    ADDRESS2: str
    OPENNING_BALANCE: float
    PHONE_NO: str
    MOBILE_NO: str
    FAX_NO: str
    EMAIL_ID: str
    ParentID: int
    LR: str
    CorporateAccID: int
    AccId: int
    SourceID: int

class WaiterInfoBase(BaseModel):
    Name: str
    Remarks: str

class OrderBase(BaseModel):
    KOT_NO: int
    TABLE_CODE: str
    FOR_PERSONS: int
    ORDER_TYPE: str
    ATTENDANT: str
    ORDER_DATE: datetime
    START_TIME: str
    SUBTOTAL: float
    SALES_TAX: float
    DISCOUNT_RATE: float
    DISCOUNT_AMT: float
    SERVICE_CHARGE: float
    TOTAL_AMOUNT: float
    CUS_NAME: str
    DISC_TYPE: str
    ITEM_DESC: int
    BILL_PRINTED: int
    STATUS: str
    Waiter: str
    ManualKot: int
    EntryTime: datetime
    Insert_Synced: bool
    KotPrinted: bool
    KotResubmitted: bool
    ReKotPrinted: bool
    CUS_ID: int
    CUS_PHONE: str
    SupplimetaryAmount: float
    MachineName: str
    Location: str
    SCRate: float
    VatRate: float
    orderItems: List[OrderItem]
    customerInfo: List[CustomerInfoBase]
    # waiterInfo: List[WaiterInfoBase]



class SaleMasterBase(BaseModel):
    MEMO_NO: Optional[int]
    FOR_PERSONS: Optional[int]
    SALE_TYPE: Optional[str]
    ORDER_DATE: Optional[datetime]
    SUBTOTAL: Optional[float]
    VAT: Optional[float]
    SERVICE_CHARGE: Optional[float]
    DISCOUNT_AMT: Optional[float]
    TOTAL_AMOUNT: Optional[float]
    PAID_AMOUNT: Optional[float]
    DUE_AMOUNT: Optional[float]
    PAYMENT_METHOD: Optional[str]
    PAYMENT_MEDIA: Optional[str]
    MACHINE_OF: Optional[str]
    VID: Optional[int]
    PAIDVID: Optional[int]
    CUS_ID: Optional[int]
    USERID: Optional[str]
    PRICE_PER: Optional[float]
    CARDVID: Optional[int]
    ID: Optional[int]
    TABLENO: Optional[str]
    WAITER: Optional[str]
    KOT_NO: Optional[int]
    EntryTime: Optional[datetime]
    ManualKOT: Optional[str]
    InsertType:Optional[str]
    SupplimetaryAmount:Optional[float]
    ComplementaryAmt:Optional[float]
    CusName:Optional[str]
   

class SaleMasterCreate(SaleMasterBase):
    pass

class SaleMasterUpdate(SaleMasterBase):
    pass

class SaleMaster(SaleMasterBase):
    ID: int

    class Config:
        orm_mode = True

class Promotion(BaseModel):
    PromotionID: int
    MenuID: int
    DiscountPercent: float
    

class UserInfoBase(BaseModel):
    UserName: str
    FullName: str
    SetPassword: str
    UserType: str
    Status: bool
    BackdateEntry: bool

class UserInfoCreate(UserInfoBase):
    pass

class UserInfoSchema(UserInfoBase):
    UserID: int

    class Config:
        orm_mode = True