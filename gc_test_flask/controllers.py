from flask import jsonify, request, abort
from flask import Blueprint
# This line has to be here, otherwise we will get import error
api_v1 = Blueprint('api_v1', __name__)

@api_v1.route('/', methods=['GET'])
def hello_world(): 
    return jsonify({ 'bravo': 'gotovo neverovatno kako si ovo napravio!' }), 200