import os
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_restful import Api

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import ProductionConfig, DevelopmentConfig
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per day"]
)

CORS(app, resources={"/": {"origins": "*"}})

load_dotenv()

if os.getenv('ENV') == 'production':
    app.config.from_object(ProductionConfig)
elif os.getenv('ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    raise NotImplementedError('ENV Variable not set.')

api = Api(app)

# TODO: put sqlite uri in an env var

engine = create_engine('sqlite:///data.db', convert_unicode=True,
connect_args={'check_same_thread': False})
db = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# May stop working...

ma = Marshmallow(app)