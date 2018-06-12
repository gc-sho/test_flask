from flask import jsonify, request, abort
from flask import Blueprint
from utils import encrypt_pass, check_insert_user_data, check_object_id_validation
from gc_test_flask.models import UserMongo as User, MongoModel
from serializers import UserCreateSerializer, UserUpdateSerializer, UserShowSerializer
from gc_test_flask.gateways import MongoDBGateway
# This line has to be here, otherwise we will get import error
api_v1 = Blueprint('api_v1', __name__)
import json
db_gateway = MongoDBGateway()

@api_v1.route('/', methods=['GET'])
def hello_world(): 
    return jsonify({ 'bravo': 'gotovo neverovatno kako si ovo napravio!' }), 200

# create user or get list of users
@api_v1.route('/user', methods=['POST'])
def create_user():
    if request.method == 'POST':
        request_json = request.get_json()
        # Required fields
        check, err = check_insert_user_data(request_json)
        # Handle user error
        if err:
            return jsonify({ 'message', err }), 400

        check['password'] = encrypt_pass(check['password'])

        # get data from body and add it to a model
        user = User(UserCreateSerializer.to_format(check))
        user_id, err = db_gateway.save(user.collection, user)
        if err:
            return jsonify({ 'message': err }), 404
        # just for the sake of returning newly created user model 
        where, err = check_object_id_validation(user_id)
        if err:
            return jsonify({ 'message': err }), 404
        
        db_gateway.load(user.collection, where)
        return jsonify({'success': user_id}), 200

@api_v1.route('/user/<id_user>', methods=['GET', 'POST'])
def get_update_user(id_user):
    if request.method == 'GET':
        # user default state
        user = User(UserCreateSerializer.to_format(dict()))

        where, err = check_object_id_validation(id_user)
        if err:
            return jsonify({ 'message': err }), 404

        user, err = db_gateway.load(user.collection, where)
        if err:
            return jsonify({ 'message': err }), 404
        
        return jsonify(UserShowSerializer.to_web(user)), 200

    if request.method == 'POST':
        request_json = request.get_json()
        # Required fields
        check, err = check_insert_user_data(request_json)
        # Handle user error
        if err:
            return jsonify({ 'message', err }), 400

        where, err = check_object_id_validation(id_user)
        if err:
            return jsonify({ 'message': err }), 404

        # get data from body and add it to a model
        user = User(UserUpdateSerializer.to_format(check))

        data, err = db_gateway.update(user.collection, where, user)

        if err:
            return jsonify({ 'message': err }), 404

        return jsonify({'success': 'Successfully updated user.'}), 200