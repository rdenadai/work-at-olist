import os
import dj_database_url
from flask import Flask
from peewee import *
from .controllers.principal import principal
from .controllers.api import api
from .settings import DevelopmentConfig, ProductionConfig


# Start the flask app
application = Flask(__name__)

# Configuration
# ---------------
# Import configuration depending on the environment
if os.environ.get('PYTHONHOME', None):
    application.config.from_object(ProductionConfig)
else:
    application.config.from_object(DevelopmentConfig)

# Models
# ---------------
# Database connection
db_conn = None
if application.config.get('DATABASE_TYPE') == 'sqlite':
    db_conn = SqliteDatabase(application.config.get('DATABASE_CONN'))
elif application.config.get('DATABASE_TYPE') == 'psql':
    conn = dj_database_url.parse(application.config.get('DATABASE_CONN'))
    data = {
        'user': conn['USER'],
        'password': conn['PASSWORD'],
        'host': conn['HOST'],
        'port': conn['PORT'],
    }
    db_conn = PostgresqlDatabase(conn['NAME'], **data)

# Controllers
# ---------------
# Register the apps blueprint endpoints
application.register_blueprint(principal)
application.register_blueprint(api)
