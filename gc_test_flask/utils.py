import hmac
import hashlib
import base64
from gc_test_flask import application

def encrypt_pass(hash_string):
    digest = hmac.new(application.config['PASS_SECRET'], hash_string, hashlib.sha256).digest()
    sha_signature = base64.b64encode(digest).decode()
    return sha_signature