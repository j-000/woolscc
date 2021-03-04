import os
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
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

db = SQLAlchemy(app=app)

ma = Marshmallow(app)