import os
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig, DevelopmentConfig
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app, resources={"/": {"origins": "*"}})

load_dotenv()

if os.getenv('ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

api = Api(app)

db = SQLAlchemy(app=app)

ma = Marshmallow(app)