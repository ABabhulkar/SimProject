class State:
    Idle = 1
    StartPlayer = 2
    StartGame = 3
    CalculateResults = 4
    End = 5


class SharedData:
    def __init__(self):
        self.socket = None
        self.stopFlag = False
        self.state = State.Idle
        self.msg = None
