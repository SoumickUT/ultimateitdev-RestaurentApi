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




