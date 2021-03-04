import string
from random import choices


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_DOMAIN = 'localhost.localdomain'
    SECRET_KEY = ''.join(choices(string.printable, k=50))


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SERVER_NAME = 'wools.cc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod.db'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SERVER_NAME = '127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

