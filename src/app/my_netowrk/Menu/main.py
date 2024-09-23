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


def get_all_menu(db: Session):
    # Use parameterized queries to prevent SQL injection
    query = text(f"""
        SELECT [MENU_ID]
              ,[MENU_NAME]
              ,[QUANTITY]
              ,[QUNIT]
              ,[PRICE]
              ,[UNIT]
              ,[CAT_ID]
              ,[SUB_ID]
              ,[NOTE]
              ,[ITEM_TYPE]
              ,[MenuCode]
              ,[IsVAT]
              ,[IsDiscount]
              ,[IsSupplimentary]
        FROM [Res_Halditest_Db].[dbo].[MENUITEM]
    """)
    
    # Execute the query with parameter binding
    result = db.execute(query)
    
    # Fetch all results
    data = result.fetchall()
    
    # Convert result to a list of dictionaries for better usability
    menu_items = []
    for row in data:
        menu_item = {
            'MENU_ID': row[0],
            'MENU_NAME': row[1],
            'QUANTITY': row[2],
            'QUNIT': row[3],
            'PRICE': row[4],
            'UNIT': row[5],
            'CAT_ID': row[6],
            'SUB_ID': row[7],
            'NOTE': row[8],
            'ITEM_TYPE': row[9],
            'MenuCode': row[10],
            'IsVAT': row[11],
            'IsDiscount': row[12],
            'IsSupplimentary': row[13]
        }
        menu_items.append(menu_item)
    
    return menu_items

def get_menu(db: Session, CAT_ID: int, SUB_ID: int):
    # Use parameterized queries to prevent SQL injection
    query = text(f"""
        SELECT [MENU_ID]
              ,[MENU_NAME]
              ,[QUANTITY]
              ,[QUNIT]
              ,[PRICE]
              ,[UNIT]
              ,[CAT_ID]
              ,[SUB_ID]
              ,[NOTE]
              ,[ITEM_TYPE]
              ,[MenuCode]
              ,[IsVAT]
              ,[IsDiscount]
              ,[IsSupplimentary]
        FROM [Haldi].[dbo].[MENUITEM]
        WHERE [CAT_ID] = :cat_id AND [SUB_ID] = :sub_id;
    """)
    
    # Execute the query with parameter binding
    result = db.execute(query, {'cat_id': CAT_ID, 'sub_id': SUB_ID})
    
    # Fetch all results
    data = result.fetchall()
    
    # Convert result to a list of dictionaries for better usability
    menu_items = []
    for row in data:
        menu_item = {
            'MENU_ID': row[0],
            'MENU_NAME': row[1],
            'QUANTITY': row[2],
            'QUNIT': row[3],
            'PRICE': row[4],
            'UNIT': row[5],
            'CAT_ID': row[6],
            'SUB_ID': row[7],
            'NOTE': row[8],
            'ITEM_TYPE': row[9],
            'MenuCode': row[10],
            'IsVAT': row[11],
            'IsDiscount': row[12],
            'IsSupplimentary': row[13]
        }
        menu_items.append(menu_item)
    
    return menu_items

