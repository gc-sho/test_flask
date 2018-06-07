import hmac
import hashlib
import base64
from bson import ObjectId
from bson.errors import InvalidId
from gc_test_flask import application

def encrypt_pass(hash_string):
    digest = hmac.new(application.config['PASS_SECRET'], hash_string, hashlib.sha256).digest()
    sha_signature = base64.b64encode(digest).decode()
    return sha_signature

def check_insert_user_data(data):
  if not 'name' in data and not 'email' in data and not 'password' in data:
      return None, 'Bad request'

  return data, None

def check_object_id_validation(id):
    try:
        where = {"_id": ObjectId(id)}
        return where, None
    except (InvalidId):
        return None, 'Not found'