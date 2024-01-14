class State:
    Idle = 1
    StartAsPlayer1 = 2
    MoveReceived = 3
    End = 4


class SharedData:
    def __init__(self):
        self.socket = None
        self.stopFlag = False
        self.state = State.Idle
        self.msg = None
