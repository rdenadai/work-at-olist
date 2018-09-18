import os
import dj_database_url
from peewee import *
from .settings import CONFIG

# Database Connection
# ---------------
db_conn = None
if CONFIG.DATABASE_TYPE == 'sqlite':
    db_conn = SqliteDatabase(CONFIG.DATABASE_CONN)
elif CONFIG.DATABASE_TYPE == 'psql':
    conn = dj_database_url.parse(CONFIG.DATABASE_CONN)
    data = {
        'user': conn['USER'],
        'password': conn['PASSWORD'],
        'host': conn['HOST'],
        'port': conn['PORT'],
    }
    db_conn = PostgresqlDatabase(conn['NAME'], **data)
