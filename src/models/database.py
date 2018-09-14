from peewee import *
from ..app import application


db = None
if application.config.get('DATABASE_TYPE') == 'sqlite':
    db = SqliteDatabase(application.config.get('DATABASE_CONN'))
elif application.config.get('DATABASE_TYPE') == 'psql':
    db = PostgresqlDatabase(application.config.get('DATABASE_CONN'))
