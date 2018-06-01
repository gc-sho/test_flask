import os
from os.path import expanduser

class BaseConfig(object):
    HOST = '127.0.0.1'
    PORT = 8080
    DEBUG = True
    TESTING = False

    # Tmp directory is the directory that we keep our files that we will cleanup later
    DB_PATH = 'gc_test_flask/db/gc-test-flask.db'
    TMP_PATH = 'gc_test_flask/tmp/.tmp-mnemo'
    VERIFY_PATH = 'gc_test_flask/tmp/.verify'
    
    TMP_DIR_PATH = 'gc_test_flask/tmp'
    DB_DIR_PATH = 'gc_test_flask/db'

    # Mongo conf
    MONGO_PATH = 'localhost',
    MONGO_PORT = 27017;
    MONGO_DB   = 'test_flask'

    # Sqlite3 configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/gc-test-flask.db'
    # I set this to suppress some boring
    # deprecation warning :)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Address limit starts from 0, our limit is 100
    ADDRESS_LIMIT = 100
    GENERATE_NEW_ADDRESS_LIMIT = 5
    INITAL_ADDRESSES_LIMIT = 5
    # Transactions
    MIN_SEND_AMOUNT = 0.001
    GTOSHI_PER_BYTE = 100
    # Block explorer production
    BLO_BASE_URL = 'https://a1v2738bcd.gamecredits.org/api'

    # Logging information
    FORMAT = "[%(asctime)s] %(message)s"
    
    # TODO: Is it really platform independent?
    # https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python#4028943
    GC_LOG_DIR = os.path.join(expanduser('~'), 'GcLogs/gc_test.log')

class TestingConfig(BaseConfig):
    TESTING = True
    DEBUG = True