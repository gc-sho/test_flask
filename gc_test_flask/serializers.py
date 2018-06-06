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


class UserUpdateSerializer(object):
    @staticmethod
    def to_format(data):
        DEFAULT_USER = userDefault(data)
        DEFAULT_USER['_id'] = data.get('_id')
        return DEFAULT_USER