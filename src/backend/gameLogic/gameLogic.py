
import logging
from gameLogic.IGameLogic import IGameLogic

# logger to log things in code
logger = logging.getLogger(" game_logic ")


def setup_logger():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


class GameLogic(IGameLogic):

    def __init__(self) -> None:
        super().__init__()
        setup_logger()

    def calculate_result(self, rounds: dict) -> None:
        logger.debug('calculate result')

    def get_file_names(self):
        NotImplemented
