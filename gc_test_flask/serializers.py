def userDefault(data):
    return {
        'name': data['name'],
        'city': data['city'],
        'state': data['state'],
        'email': data['email'],
        'address': data['address'],
        'password': data['password']
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
            'name': data['name'],
            'city': data['city'],
            'state': data['state'],
            'email': data['email'],
            'address': data['address']
        }

class UserUpdateSerializer(object):
    @staticmethod
    def to_format(data):
        DEFAULT_USER = userDefault(data)
        del DEFAULT_USER['password']
        return DEFAULT_USER