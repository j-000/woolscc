import string
from random import choices

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_DOMAIN = 'localhost.localdomain'
    # SERVER_NAME = 'joservices'
    SERVER_NAME = '127.0.0.1:5000'
    SECRET_KEY = ''.join(choices(string.printable, k=50))


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_data.db'

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_data.db'

