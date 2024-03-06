from functools import wraps
import json
import os
from flask import jsonify, request, make_response
import jwt
import requests
from jwt.exceptions import DecodeError
from src import app


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({'error': 'Authorization token is missing'}), 401
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user_id = data['user_id']
        except DecodeError:
            return jsonify({'error': 'Authorization token is invalid'}), 401
        return f(current_user_id, *args, **kwargs)

    return decorated


@app.route('/auth', methods=['POST'])
def authenticate_user():
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Unsupported Media Type', 'code': 2}), 415
    username = request.json.get('username')
    password = request.json.get('password')

    # TODO sc-64: Get users from database
    user = {'username': '', 'password': ''}
    response = make_response(jsonify({'message': 'Login failed', 'code': 2}))

    if user['username'] == username and user['password'] == password:
        token = jwt.encode(
            {'user_id': user['id']}, app.config['SECRET_KEY'], algorithm="HS256")
        response = make_response(
            jsonify({'message': 'Login successful', 'code': 1}))
        response.set_cookie('token', token)

    return response, 200
