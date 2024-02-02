class PlayerGame():
    def __init__(self) -> None:
        self.move = 0
        self.score = 0


class GameRound():
    def __init__(self, first, second) -> None:
        self.gameObject = {}
        self.gameObject[first] = PlayerGame()
        self.gameObject[second] = PlayerGame()

    def updateMove(self, player, move):
        self.gameObject[player].move = move

    def getMove(self, player):
        return self.gameObject[player].move

    def updateScore(self, player, score):
        self.gameObject[player].score = score

    def __repr__(self):
        l = self.gameObject.values()
        return f'1- {l[0].move} {l[0].score}; 2- {l[1].move} {l[1].move}'

# {p1:PlayerGame, p2:PlayerGame}
