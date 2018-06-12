from models import UserMongo as User
from gc_test_flask.utils import check_object_id_validation
from pymongo.errors import ConnectionFailure


class MongoDBGateway(object):

    def save(self, collection, data):
        # Check for result
        res = collection.find_one({"email": data['email']})
        if not res:
            return collection.insert(data), None

        return None, 'User already exists'
            
    def update(self, collection, where, data):
        try:
            res = collection.find_one_and_update(where, {'$set': data})
            if not res:
                return None, 'Not found'
            return res, None
        except ConnectionFailure:
            return None, 'DB Connection failed'
        
    def load(self, collection, where):
        if where:
            # gets results
            try:
                res = collection.find_one(where)      
                if not res:
                    return None, 'Not found'
                return res, None          
            except ConnectionFailure:
                return None, 'DB Connection failed'
        else:
            return None, 'Please provide required attributes'

    def remove(self, _id, collection):
        if _id:
            where, err = check_object_id_validation(_id)            
            if err: 
                return None, 'Bad request', 400
            try:
                collection.remove(where)
            except ConnectionFailure:
                return None, 'DB Connection failed'
            