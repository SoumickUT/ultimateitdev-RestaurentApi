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
from sqlalchemy import text
from src.app.common.properties import properties
import json

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





# def get_menucategory(db: Session):
#     # Use parameterized queries to prevent SQL injection
#     query = text(f"""
#       SELECT 
#        [ID]
#       ,[NAME]
#       FROM [Res_Halditest_Db].[dbo].[MENUCATEGORY]

#     """)

def get_menucategory(db: Session):
    # Use parameterized queries to prevent SQL injection
    query = text("""
      SELECT 
        ID,
        NAME
      FROM MENUCATEGORY
    """)
    
    
    # Execute the query with parameter binding
    result = db.execute(query)
    
    # Fetch all results
    data = result.fetchall()
    
    # Convert result to a list of dictionaries for better usability
    menu_items = []
    for row in data:
        menu_item = {
            'CAT_ID': row[0],
            'NAME': row[1]
        }
        menu_items.append(menu_item)
    
    return menu_items



def get_category(category_id: int, db: Session):
    category = db.query(models.MenuCategory).filter(models.MenuCategory.ID == category_id).first()
    
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    menu_items = db.query(models.MenuItem).filter(models.MenuItem.CAT_ID == category_id).all()
    sub_categories = db.query(models.SubCategory).filter(models.SubCategory.CAT_ID == category_id).all()

    # Construct the JSON response
    response = {
        "category": {
            "CAT_ID": category.ID,
            "NAME": category.NAME,
            "menu": [
                {
                    "MENU_ID": item.MENU_ID,
                    "MENU_NAME": item.MENU_NAME,
                    "QUANTITY": item.QUANTITY,
                    "QUNIT": item.QUNIT,
                    "PRICE": item.PRICE,
                    "UNIT": item.UNIT,
                    "CAT_ID": item.CAT_ID,
                    "SUB_ID": item.SUB_ID,
                    "NOTE": item.NOTE,
                    "ITEM_TYPE": item.ITEM_TYPE,
                    "MenuCode": item.MenuCode,
                    "IsVAT": item.IsVAT,
                    "IsDiscount": item.IsDiscount,
                    "IsSupplimentary": item.IsSupplimentary
                }
                for item in menu_items
            ],
            "submenu": [
                {
                    "SUB_ID": sub.SUB_ID,
                    "NAME": sub.NAME,
                    "CAT_ID": sub.CAT_ID
                }
                for sub in sub_categories
            ]
        }
    }

    return response

# def get_category(category_id: int, db: Session):
#     query = text("""
#         SELECT 
#             c.ID as CAT_ID,
#             c.NAME,
#             (
#                 SELECT 
#                     MENU_ID,
#                     MENU_NAME,
#                     QUANTITY,
#                     QUNIT,
#                     PRICE,
#                     UNIT,
#                     CAT_ID,
#                     SUB_ID,
#                     NOTE,
#                     ITEM_TYPE,
#                     MenuCode,
#                     IsVAT,
#                     IsDiscount,
#                     IsSupplimentary
#                 FROM MENUITEM mi
#                 WHERE mi.CAT_ID = c.ID
#                 FOR JSON PATH
#             ) AS menu,
#             (
#                 SELECT 
#                     SUB_ID,
#                     NAME,
#                     CAT_ID
#                 FROM SUBCATEGORY sc
#                 WHERE sc.CAT_ID = c.ID
#                 FOR JSON PATH
#             ) AS submenu
#         FROM MENUCATEGORY c
#         WHERE c.ID = 1
#         FOR JSON PATH, ROOT('category');

#     """)

#     result = db.execute(query, {"category_id": category_id}).fetchone()

#     if not result:
#         raise HTTPException(status_code=404, detail="Category not found")

#     # Inspect the raw SQL result
#     raw_result = result[0]
#     print("Raw SQL Result:", raw_result)

#     # Attempt to fix common JSON formatting issues
#     sanitized_result = raw_result.replace('\r', '').replace('\n', '').replace('\\', '\\\\').replace('"', '\"')

#     try:
#         # Convert the SQL result to JSON
#         result_json = json.loads(sanitized_result)
#     except json.JSONDecodeError as e:
#         # Log the exact position of the error
#         error_position = e.pos
#         snippet = sanitized_result[max(0, error_position-50):error_position+50]
#         print(f"Error at position {error_position}: {snippet}")
#         raise HTTPException(status_code=500, detail=f"Error parsing JSON: {e.msg}")

#     return result_json
