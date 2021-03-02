from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig, DevelopmentConfig
from dotenv import load_dotenv
import os
from flask_marshmallow import Marshmallow


load_dotenv(dotenv_path='.')
HOST = 'http://127.0.0.1'

app = Flask(__name__)
CORS(app, resources={"/": {"origins": "*"}})


if os.getenv('ENV') == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

api = Api(app)

db = SQLAlchemy(app=app)

ma = Marshmallow(app)