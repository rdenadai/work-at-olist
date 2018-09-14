import os
import urlparse
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
    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(application.config.get('DATABASE_CONN'))
    db_conn = PostgresqlDatabase({
        'name': url.path[1:],
        'user': url.username,
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    })

# Controllers
# ---------------
# Register the apps blueprint endpoints
application.register_blueprint(principal)
application.register_blueprint(api)
