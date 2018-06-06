from gc_test_flask import mongo_db
from bson import ObjectId

class MongoModel(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

class User(MongoModel):    
    collection = mongo_db['User']