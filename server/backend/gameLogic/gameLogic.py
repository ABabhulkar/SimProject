
import json
import logging
import os
from ..gameLogic.IGameLogic import IGameLogic

# logger to log things in code
logger = logging.getLogger(" game_logic ")


def setup_logger():
    """
    logger for gameLogic
    """
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


class GameLogic(IGameLogic):
    """Game logic implementation

    Args:
        IGameLogic (Interface): Interface for the game logic api
    """

    def __init__(self, root_path=None) -> None:
        """
        Args:
            root_path: The path to the directory to search for executable files. Defaults to None.
        """
        super().__init__()
        setup_logger()
        self.max_num_of_rounds = 0
        if root_path is None:
            self.root = os.getcwd()
            # TODO: Remove after dev
            self.root = '/mnt/d/Projects/PythonWS/SimProject/test/resources'

    def process_rounds(self, rounds_json):
        """
        Processes the given JSON data, updates the score for each round based on the
        provided table, and calculates the total score for P1 and P2.

        Args:
            json_data: The JSON data to process.

        Returns:
            A dictionary containing the updated JSON data and the total scores for P1 and P2.
        """

        score_table = {
            (0, 0): (3, 3),
            (0, 1): (0, 5),
            (1, 0): (5, 0),
            (1, 1): (1, 1),
        }

        processed_data = {}
        total_score_p1 = 0
        total_score_p2 = 0

        for round_id, round_data in rounds_json.items():
            processed_data[round_id] = round_data.copy()
            p1_move = processed_data[round_id]["gameRound"]["P0"]["move"]
            p2_move = processed_data[round_id]["gameRound"]["P1"]["move"]

            p1_score, p2_score = score_table[(p1_move, p2_move)]
            processed_data[round_id]["gameRound"]["P0"]["score"] = p1_score
            processed_data[round_id]["gameRound"]["P1"]["score"] = p2_score
            total_score_p1 += p1_score
            total_score_p2 += p2_score

        return processed_data, {"P0": total_score_p1, "P1": total_score_p2}

    def calculate_result(self, rounds_json: json) -> None:
        """
        Sames the results in DB and calculates final score for the game

        Args:
            rounds_json (json): dict of moves by all players
        """
        logger.debug('calculate result')
        data = json.loads(rounds_json)
        _, total_scores = self.process_rounds(data)

        # TODO: Save the rounds in a NoSQL db
        logger.info(f'Scores:{total_scores}')

    def get_file_names(self) -> list:
        """
        This function takes a path as an argument and returns a list of all executable files from 
        that path.

        Returns:
            A list of all executable files in the given path.
        """
        if not os.path.exists(self.root):
            raise ValueError(f"No dir: {self.root}")

        executable_files = []
        for filename in os.listdir(self.root):
            file_path = os.path.join(self.root, filename)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                executable_files.append(file_path)

        return executable_files

    def get_rounds_num(self) -> int:
        """
        Getter for number of rounds

        Returns:
            int: max number of rounds set for this game
        """
        return self.max_num_of_rounds
