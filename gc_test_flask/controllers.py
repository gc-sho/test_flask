from flask import jsonify, request, abort
from flask import Blueprint
from gc_test_flask.models import User, MongoModel
# This line has to be here, otherwise we will get import error
api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/', methods=['GET'])
def hello_world(): 
    users = (User({
                "name": "Nenad",
                "dev": True
            })).save()
    print 'users %r' % users
    return jsonify({ 'bravo': 'gotovo neverovatno kako si ovo napravio!' }), 200