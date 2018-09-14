import os


class Config:
    DEBUG = True
    TESTING = True
    DATABASE_TYPE = 'sqlite'
    DATABASE = 'localhost.db'


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    TESTING = True
    DATABASE_TYPE = 'psql'
    DATABASE = os.environ.get('DATABASE_URL')
