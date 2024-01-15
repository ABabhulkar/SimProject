import socket
import sys
import threading
from sharedData import State
from sharedData import SharedData
from time import sleep

from strategy import generateReply

# Create an instance of SharedData
shared_data = SharedData()
# Create a lock
lock = threading.Lock()
# Create an event
event = threading.Event()


def monitor_communication(num, _data, _event):
    while True:
        # Check if the event is set by worker2
        if _event.is_set():
            with lock:
                if _data.stopFlag:
                    # Reset the event after performing specific work
                    event.clear()
                    break

        with lock:
            stop = _data.stopFlag
            sock = _data.socket

        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received in app{num}: {data.decode()}")
        except TimeoutError:
            NotImplemented

        # TODO: set the state based on received command
        with lock:
            _data.state = State.End
            # Set event after state update.
            _event.set()


class ClientApp():
    def __init__(self):
        self.count = 0
        self.stop_thread = False
        # Create a socket
        self.app_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, name):
        # Connect to the server (app1) on localhost and port 5001
        self.app_sock.connect(('localhost', 5002))
        self.app_sock.settimeout(1)

        # TODO: add error handling here

        with lock:
            shared_data.socket = self.app_sock
            shared_data.stopFlag = False

        # Start threads to monitor communication in both directions
        self.monitor_thread1 = threading.Thread(
            target=monitor_communication, args=(name, shared_data, event,))
        self.monitor_thread1.start()

    def execute(self, name):
        started = True

        # self._connectToServer(name)

        with lock:
            shared_data.state = State.Idle
            state = shared_data.state

        while started:
            match state:
                case State.Idle:
                    if event.is_set():
                        with lock:
                            state = shared_data.state
                            # Reset the event after updating state
                            event.clear()

                case State.StartAsPlayer1:
                    generateReply(-1, self._sendReply)
                    state = State.Idle

                case State.MoveReceived:
                    # TODO: Read receivedMove this is temp fix
                    generateReply(1, self._sendReply)
                    state = State.Idle

                case State.End:
                    started = False

        self._stopServer()

    def _stopServer(self):
        with lock:
            shared_data.stopFlag = True
            event.set()

        self.monitor_thread1.join()
        # wait for all threads to stop
        self._disconnectServer()

    def _disconnectServer(self):
        NotImplemented

    def _sendReply(self, replay):
        message = f"P1:{replay}"
        self.app_sock.sendall(message.encode())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app_num = sys.argv[1]
    else:
        app_num = 0
        print("Hello, world!")

    # TODO: do error handling here
    app = ClientApp()
    app.execute(app_num)
