import os
from os.path import expanduser
import errno

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import APISpec, Swagger
from pymongo import MongoClient
import logging

# Initialize Flask instance
application = Flask(__name__)
# Loading gc-lite-client configuration
application.config.from_object('gc_test_flask.config.BaseConfig')

# Initialize Swagger documentation
swag = Swagger(application, template_file='api_docs/gc.yaml')

# Initialize MongoDB
mongo_client = MongoClient(application.config['MONGO_PATH'], application.config['MONGO_PORT'])
mongo_db = mongo_client[application.config['MONGO_DB']]

# Initialize PostgreSQL
postgres_db = SQLAlchemy(application)

# Register the blueprint and import the controllers
from gc_test_flask.controllers import api_v1
application.register_blueprint(api_v1, url_prefix='/api/v1')