from gc_test_flask.session import remove_file
from gc_test_flask import application

import atexit

if __name__ == '__main__':
    # On force quit, remove session files
    atexit.register(remove_file, [application.config['TMP_PATH'], application.config['VERIFY_PATH']])
    application.run(application.config['HOST'],  application.config['PORT'])