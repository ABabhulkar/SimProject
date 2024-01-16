class State:
    Idle = 1
    End = 4
    DataReceived = 5


class SharedData:
    def __init__(self):
        self.socket = None
        self.stopFlag = False
        self.state = State.Idle
        self.msg = None
