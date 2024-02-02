from time import sleep
from gameCore.gameCore import GameCore

from gameLogic.gameLogic import GameLogic


def main():
    # This is dir for the test application
    P1_dir = '/mnt/d/Projects/PythonWS/SimProject/ClientTemplate/src/clientApp.py'
    P2_dir = '/mnt/d/Projects/PythonWS/SimProject/ClientTemplate/src/clientApp.py'
    gameLogic = GameLogic()
    gameCore = GameCore(gameLogic)
    gameCore.execute(P1_dir, P2_dir)


if __name__ == "__main__":
    main()
