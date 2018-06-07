def userDefault(data):
    return {
        'name': data.get('name'),
        'city': data.get('city'),
        'state': data.get('state'),
        'email': data.get('email'),
        'address': data.get('address'),
        'password': data.get('password')
    }

class UserCreateSerializer(object):
    @staticmethod
    def to_format(data):
        DEFAULT_USER = userDefault(data)
        return DEFAULT_USER

class UserShowSerializer(object):
    @staticmethod
    def to_web(data):
        return {
            'name': data.get('name'),
            'city': data.get('city'),
            'state': data.get('state'),
            'email': data.get('email'),
            'address': data.get('address')
        }

class UserUpdateSerializer(object):
    @staticmethod
    def to_format(data):
        DEFAULT_USER = userDefault(data)
        del DEFAULT_USER['password']
        return DEFAULT_USER