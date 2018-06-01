from gc_test_flask import application

import atexit

if __name__ == '__main__':
    application.run(application.config['HOST'],  application.config['PORT'])