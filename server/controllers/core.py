from flask import request, jsonify, make_response

from .. import db
from .. import sk
from ..app import app
from ..models.game import Game
from ..models.game_history import GameHistory


class CoreController:

    @staticmethod
    def list_all_games():
        game_entries = Game.query.all()
        response = []
        for game in game_entries:
            response.append(game.toDict())
        return jsonify(response)

    @staticmethod
    def retrieve_game(game_id):
        response = Game.query.get(game_id).toDict()
        return jsonify(response)

    @staticmethod
    def run_game(game_id, iterations) -> None:
        '''
        This function will run the files against one another and save results

        :param game_id: To get all relevant data from db
        :param iterations: Number of rounds that should happen
        :return:
        '''

        game = Game.query.get(game_id)
        root_path = app.config.get("PD_GAME_FILE_PATH")

        from server.backend.gameLogic.gameLogic import GameLogic
        from server.backend.gameCore.gameCore import GameCore
        game_logic = GameLogic(result_metric=game.result_metric, root_path=root_path)
        game_logic.max_num_of_rounds = iterations

        # Run for selected game
        GameCore(game_logic).execute()

        if game_logic.total_scores is not None:
            game_history = GameHistory(
                game_id=game_id,
                round_score=game_logic.total_scores,
            )

            db.session.add(game_history)
            db.session.commit()
