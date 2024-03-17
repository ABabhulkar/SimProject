from functools import wraps
from flask import request, jsonify
from jwt.exceptions import DecodeError
import jwt

from .. import sk


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401
        try:
            data = jwt.decode(
                token, sk, algorithms=["HS256"])
            print(data)
            current_user_id = data['user_id']
        except DecodeError:
            return jsonify({'error': 'Authorization token is invalid'}), 401
        return f(current_user_id, *args, **kwargs)

    return decorated
