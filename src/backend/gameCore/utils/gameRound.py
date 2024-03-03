class PlayerGame():
    def __init__(self) -> None:
        self.move = 0
        self.score = 0

    def __dict__(self):
        return {
            "move": int(self.move),
            "score": int(self.score)
        }


class GameRound:
    def __init__(self, first, second) -> None:
        self.gameObject = {first: PlayerGame(), second: PlayerGame()}

    def update_move(self, player, move):
        self.gameObject[player].move = move

    def get_move(self, player):
        return self.gameObject[player].move

    def update_score(self, player, score):
        self.gameObject[player].score = score

    def __repr__(self):
        l = self.gameObject.values()
        return f'1- {l[0].move} {l[0].score}; 2- {l[1].move} {l[1].move}'

    def __dict__(self):
        return {
            "gameRound": {
                player: player_obj.__dict__() for player, player_obj in self.gameObject.items()
            }
        }

# {p1:PlayerGame, p2:PlayerGame}
