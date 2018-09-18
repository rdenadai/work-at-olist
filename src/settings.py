import os


class Config:
    DEBUG = True
    TESTING = True
    DATABASE_TYPE = 'sqlite'
    DATABASE_CONN = 'localhost.db'
    CORS_HEADERS = 'Content-Type'
    URL = 'http://localhost:8000'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    TESTING = True
    DATABASE_TYPE = 'psql'
    DATABASE_CONN = os.environ.get('DATABASE_URL')
    URL = 'https://rdenadai-work-at-olist.herokuapp.com'


TARIF_VALUE = .09
STANDING_CHARGE = .36

# Configuration
# ---------------
# Import configuration depending on the environment
CONFIG = None
if os.environ.get('PYTHONHOME', None):
    CONFIG = ProductionConfig()
else:
    CONFIG = DevelopmentConfig()