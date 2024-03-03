from ...gameCore.utils.gameRound import GameRound


class State:
    Idle = 1
    StartPlayer = 2
    start_game = 3
    CalculateResults = 4
    StopPlayers = 5
    NextRound = 6
    ForwardMsg = 7


class SharedData:
    def __init__(self):
        self.socket = None
        self.stopFlag = False
        self.state = State.Idle
        self.msg = None
        self.clients = {}
        self.isConnectionMonitor = True

        # Variables related to game
        self.maxNumberOfRounds = 0
        self.roundNumber = -1
        self.rounds = {}
        self.roundStatus = {}

    def init_data(self):
        self.socket = None
        self.stopFlag = False
        self.state = State.Idle
        self.msg = None
        self.clients = {}
        self.isConnectionMonitor = True

        # Variables related to game
        self.maxNumberOfRounds = 0
        self.roundNumber = -1
        self.rounds = {}
        self.roundStatus = {}

    def next_round(self, first, second):
        self.roundNumber += 1
        if self.roundNumber >= self.maxNumberOfRounds:
            return False
        else:
            self.rounds[self.roundNumber] = GameRound(
                first, second)
            return True

    def get_current_round(self):
        return self.rounds[self.roundNumber]

    def get_last_round(self):
        return self.rounds[self.roundNumber - 1]

# rounds is a dict
# roundNumber:GameRound
# 1:{P1:gameRound, P2:gameRound}
# 2:{P1:gameRound, P2:gameRound}
