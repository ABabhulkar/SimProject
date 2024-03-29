from flask import request, jsonify, make_response

from .. import db
from .. import sk
from ..app import app
from ..models.game import Game

class CoreController:

    @staticmethod
    def list_all_games():
        game_entries = Game.query.all()
        response = []
        for game in game_entries: response.append(game.toDict())
        return jsonify(response)


    @staticmethod
    def retrieve_game(game_id):
        response = Game.query.get(game_id).toDict()
        return jsonify(response)

