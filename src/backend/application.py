from src.backend.gameCore.gameCore import GameCore

from src.backend.gameLogic.gameLogic import GameLogic


class Application:
    """_summary_
    """

    def __init__(self) -> None:
        self.game_logic = GameLogic()

    def start_game(self, num_iterations: int) -> None:
        """
        This is dir for the test application

        Args:
            num_iterations (int): _description_
        """
        self.game_logic.max_num_of_rounds = num_iterations
        gameCore = GameCore(self.game_logic)
        gameCore.execute()
