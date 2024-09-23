from fastapi import FastAPI
from src.config.common.database import database
from src.config.common.database.database import engine
from src.app.common.models import models as service_student_user_model
from src.app.common.models import models 

from src.app.my_netowrk.community import community
from src.app.my_netowrk.order_details import order_details
from src.app.my_netowrk.promotion import promotion
from src.app.my_netowrk.Menu import menu
from src.app.my_netowrk.SubMenu import submenu
from src.app.my_netowrk.Tables import table
from src.app.my_netowrk.WaiterInfo import waiterinfo
from src.app.my_netowrk.MenuCategory import menucategory
from src.app.my_netowrk.auth.swag_auth import oauth 
from src.app.my_netowrk.Register import register 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



origins = [
    "http://student.user.ui.dev.eschooljourney.com:3000/", 
    "http://localhost:3000/",
    "localhost:3000"
]

app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   allow_origins=["*"])

get_db = database.get_db

service_student_user_model.Base.metadata.create_all(engine)

app.include_router(register.router)  
app.include_router(oauth.router)  
app.include_router(menucategory.router) 
app.include_router(menu.router)  
app.include_router(submenu.router) 
app.include_router(table.router)  
app.include_router(waiterinfo.router)   
app.include_router(community.router)  
app.include_router(order_details.router)  
app.include_router(promotion.router)  



 







