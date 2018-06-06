from flask import jsonify, request, abort
from flask import Blueprint
from gc_test_flask.models import User, MongoModel
from serializers import UserCreateSerializer
from gc_test_flask.gateways import MongoDBGateway
# This line has to be here, otherwise we will get import error
api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/', methods=['GET'])
def hello_world(): 
    return jsonify({ 'bravo': 'gotovo neverovatno kako si ovo napravio!' }), 200

# create user or get list of users
@api_v1.route('/user', methods=['GET', 'POST'])
def get_create_user():
    if request.method == 'GET':
        return jsonify({'user': 'user data'}), 200
    if request.method == 'POST':
        
        # get data from body and add it to a model
        user = User(UserCreateSerializer.to_format(request.get_json()))
        # TODO hash password

        # save to mongo
        mongoDBGateway = MongoDBGateway(user.collection)
        userID = mongoDBGateway.save(user, None)
        # just for the sake of returning newly created user model 
        mongoDBGateway.reload(userID, user)
        return jsonify({'success': user}), 200

@api_v1.route('/user/<id_user>', methods=['GET', 'POST'])
def get_update_user(id_user):
    if request.method == 'GET':
        # user default state
        user = User(UserCreateSerializer.to_format(dict()))

        mongoDBGateway = MongoDBGateway(user.collection)
        mongoDBGateway.reload(id_user, user)
        
        return jsonify({'user': user}), 200
    if request.method == 'POST':
        # TODO update user
        return jsonify({'success': 'Successfully updated user.'}), 200