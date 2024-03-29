import sys
from .gameCore.gameCore import GameCore

from .gameLogic.gameLogic import GameLogic


class Application:
    """_summary_
    """

    def __init__(self, root_path) -> None:
        # TODO read this value from db
        r = {}
        self.game_logic = GameLogic(result_metric=r, root_path=root_path)

    def start_game(self, num_iterations: int) -> None:
        """
        This is dir for the test application

        Args:
            num_iterations (int): _description_
        """
        self.game_logic.max_num_of_rounds = num_iterations

        # Run for selected game
        GameCore(self.game_logic).execute()

        if self.game_logic.total_scores is not None:
            # TODO: Save the rounds in a NoSQL db
            pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_iterations = sys.argv[1]
    application = Application(root_path=None)
    application.start_game(int(num_iterations))
