from models import User
from bson import ObjectId

class MongoDBGateway(object):
    def __init__(self, collection):
        self.collection = collection        

    def save(self, data, _id):
        if not _id:            
            return self.collection.insert(data)
        else:
            return self.collection.update(
                { "_id": ObjectId(_id) }, data)

    def reload(self, _id, model):
        if _id:
            # gets results
            result = self.collection.find_one({"_id": ObjectId(_id)})
            result['_id'] = str(_id)
            model.update(result)

    def remove(self, data, model):
        if data._id:
            self.collection.remove({"_id": ObjectId(data._id)})
            # todo check
            model.clear()