from flask import request

from ..app import app
from ..controllers.user import UserController
from ..utils.jwt_token import token_required

user_controller = UserController(app)


@app.route("/user", methods=['GET', 'POST'])
def list_create_accounts():
    if request.method == 'GET':
        return user_controller.list_all_users()
    if request.method == 'POST':
        return user_controller.create_user()
    else:
        return 'Method is Not Allowed'


@app.route("/user/<username>", methods=['GET', 'PUT', 'DELETE'])
@token_required
def retrieve_update_destroy_accounts(user_id, username):
    if request.method == 'GET':
        return user_controller.retrieve_users(username)
    if request.method == 'PUT':
        return user_controller.update_user(username)
    if request.method == 'DELETE':
        return user_controller.delete_user(username)
    else:
        return 'Method is Not Allowed'


@app.route('/auth', methods=['POST'])
def authenticate_user():
    return user_controller.login()
