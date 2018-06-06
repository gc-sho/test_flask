import os
from os.path import expanduser

class BaseConfig(object):
    HOST = '127.0.0.1'
    PORT = 8080
    DEBUG = True
    TESTING = False

    # Mongo conf
    MONGO_PATH = 'localhost'
    MONGO_PORT = 27017
    MONGO_DB   = 'test_flask'

    # hash pass
    PASS_SECRET = 'you_will_never_know'

    # Logging information
    FORMAT = "[%(asctime)s] %(message)s"
    
    # TODO: Is it really platform independent?
    # https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python#4028943
    GC_LOG_DIR = os.path.join(expanduser('~'), 'GcLogs/gc_test.log')

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True