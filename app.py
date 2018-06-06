from gc_test_flask import application

if __name__ == '__main__':
    application.run(application.config['HOST'],  application.config['PORT'])