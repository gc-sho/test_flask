import os
from os.path import expanduser
import errno

from flask import Flask, jsonify
from flasgger import APISpec, Swagger
from pymongo import MongoClient
import logging

# Initialize Flask instance
application = Flask(__name__)
# Loading gc-lite-client configuration
application.config.from_object('gc_test_flask.config.BaseConfig')

if not os.path.exists(os.path.dirname(application.config['GC_LOG_DIR'])):
    try:    
        os.makedirs(os.path.dirname(application.config['GC_LOG_DIR']))
    except OSError as exc: # Guard against race condition
    # Please take in considiration topic below before changing this part of the code
    # https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output#12517490
        if exc.errno != errno.EEXIST:
            raise

# Initialize Swagger documentation
swag = Swagger(application, template_file='api_docs/gc.yaml')

# Initialize MongoDB
mongo_client = MongoClient(application.config['MONGO_PATH'], application.config['MONGO_PORT'])
mongo_db     = mongo_client[application.config['MONGO_DB']]

# Initialize global loger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(application.config['GC_LOG_DIR'])
file_handler.setLevel(logging.DEBUG)

formater = logging.Formatter(application.config['FORMAT'])
file_handler.setFormatter(formater)

logger.addHandler(file_handler)

# Register the blueprint and import the controllers
from gc_test_flask.controllers import api_v1
application.register_blueprint(api_v1, url_prefix='/api/v1')