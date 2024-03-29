from flask import request

from ..app import app
from ..controllers.core import CoreController

core_controller = CoreController()


@app.route("/core/games/<game_id>", methods=['GET'])
def get_game_by_id(game_id):
    if request.method == 'GET':
        return core_controller.retrieve_game(game_id)
    else:
        return 'Method is Not Allowed'


@app.route("/core/games", methods=['GET'])
def list_games():
    if request.method == 'GET':
        return core_controller.list_all_games()
    else:
        return 'Method is Not Allowed'
