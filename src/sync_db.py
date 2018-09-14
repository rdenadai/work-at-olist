import logging
import sys
from .app import application, db_conn
from .models.models import Telephone, Call, Bill

if application.config.get('DEBUG', False):
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info('Sync database structure...')
db_conn.create_tables([Telephone, Call, Bill])
logging.info('Sync ended...')
