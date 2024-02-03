from time import sleep
from gameCore.gameCore import GameCore

from gameLogic.gameLogic import GameLogic


def main():
    # This is dir for the test application
    gameLogic = GameLogic()
    gameCore = GameCore(gameLogic)
    gameCore.execute()


if __name__ == "__main__":
    main()
