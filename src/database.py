import os
import dj_database_url
from peewee import *
from .settings import DevelopmentConfig, ProductionConfig

# Configuration
# ---------------
# Import configuration depending on the environment
if os.environ.get('PYTHONHOME', None):
    config = ProductionConfig()
else:
    config = DevelopmentConfig()

# Database Connection
# ---------------
db_conn = None
if config.DATABASE_TYPE == 'sqlite':
    db_conn = SqliteDatabase(config.DATABASE_CONN)
elif config.DATABASE_TYPE == 'psql':
    conn = dj_database_url.parse(config.DATABASE_CONN)
    data = {
        'user': conn['USER'],
        'password': conn['PASSWORD'],
        'host': conn['HOST'],
        'port': conn['PORT'],
    }
    db_conn = PostgresqlDatabase(conn['NAME'], **data)
