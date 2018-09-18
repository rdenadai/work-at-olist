import os
import sys
import logging
from .database import db_conn
from .models.models import Telephone, Call, Bill
from .settings import DevelopmentConfig, ProductionConfig

# Configuration
# ---------------
# Import configuration depending on the environment
if os.environ.get('PYTHONHOME', None):
    config = ProductionConfig()
else:
    config = DevelopmentConfig()

if config.DEBUG:
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info('Sync database structure...')
db_conn.create_tables([Telephone, Call, Bill])
logging.info('Sync ended...')
