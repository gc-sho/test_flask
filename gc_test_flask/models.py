from gc_test_flask import mongo_db, postgres_db
from bson import ObjectId

class MongoModel(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

class UserMongo(MongoModel):    
    collection = mongo_db['User']

# Postgresql models

class UserSQL(postgres_db.Model):
    id = postgres_db.Column(postgres_db.Integer, primary_key=True)
    name = postgres_db.Column(postgres_db.String(80), unique=True, nullable=False)
    email = postgres_db.Column(postgres_db.String(120), unique=True, nullable=False)
    city = postgres_db.Column(postgres_db.String(40), default='', nullable=False)
    state = postgres_db.Column(postgres_db.String(40), default='', nullable=False)
    address = postgres_db.Column(postgres_db.String(40), default='', nullable=False)
    password = postgres_db.Column(postgres_db.String(140), unique=True, nullable=False)

    def __init__(self, email, name, city, state, address, password):
        self.name = name
        self.email = email
        self.city = city
        self.state = state
        self.address = address
        self.password = password

    def __str__(self):
        return 'id: %s | name: %s | email: %s | city: %s | state: %s | address: %s' % (self.id, self.name, self.email, self.city, self.state, self.address)

    def as_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'city': self.city,
            'state': self.state,
            'address': self.address
        }