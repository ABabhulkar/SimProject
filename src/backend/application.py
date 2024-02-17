from time import sleep
from src.backend.gameCore.gameCore import GameCore

from src.backend.gameLogic.gameLogic import GameLogic


class Application:
    def __init__(self) -> None:
        self.gameLogic = GameLogic()

    def startGame(self, num_iterations: int) -> None:
        # This is dir for the test application
        self.gameLogic.maxNumOfRounds = num_iterations
        gameCore = GameCore(self.gameLogic)
        gameCore.execute()
