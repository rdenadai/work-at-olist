import os


class Config:
    DEBUG = True
    TESTING = True
    DATABASE_TYPE = 'sqlite'
    DATABASE_CONN = 'localhost.db'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    TESTING = True
    DATABASE_TYPE = 'psql'
    DATABASE_CONN = os.environ.get('DATABASE_URL')
