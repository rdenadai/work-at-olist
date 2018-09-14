import os


class Config:
    DEBUG = True
    TESTING = True
    DATABASE_TYPE = 'sqlite'
    DATABASE_CONN = 'localhost.db'
    CORS_HEADERS = 'Content-Type'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    TESTING = True
    DATABASE_TYPE = 'psql'
    DATABASE_CONN = os.environ.get('DATABASE_URL')
