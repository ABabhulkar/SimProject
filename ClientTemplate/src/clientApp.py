import socket
import sys
import threading
import logging
import time
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
# logger to log things in code
logger = logging.getLogger(" clientApp ")


def setup_logger():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


def monitor_communication(_name, _data, _event):
    while True:
        # Check if the event is set by worker2
        if _event.is_set():
            with lock:
                if _data.stopFlag:
                    # Reset the event after performing specific work
                    event.clear()
                    break

        with lock:
            sock = _data.socket

        try:
            data = sock.recv(1024)
            if not data:
                break

            with lock:
                _data.msg = data.decode()
                _data.state = State.DataReceived
            logger.debug(f"-> {_name}: {data.decode()}")
            _event.set()
        except TimeoutError:
            NotImplemented


class ClientApp():
    def __init__(self):
        self.count = 0
        self.stop_thread = False
        self.monitor_thread1 = None
        self.name = None
        setup_logger()
        # Create a socket
        self.app_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, timeout=10):
        # Connect to the server (app1) on localhost and port 5002
        start_time = time.time()
        while True:
            try:
                self.app_sock.settimeout(1)
                self.app_sock.connect(('localhost', 5002))
                logger.debug("Connected to the server!")
                return True
            except socket.error as e:
                logger.debug(f"{e}")

                # Check if the timeout has been reached
                elapsed_time = time.time() - start_time
                if elapsed_time >= timeout:
                    logger.error(
                        f"Timeout ({timeout} seconds) reached. Unable to connect.")
                    return None

                # Sleep for a short duration before attempting to connect again
                time.sleep(1)

    def _handleMsg(self, line):
        parts = line.strip().split(':')
        if len(parts) == 2:
            key, value = parts[0], parts[1]
            # TODO :filter based on own name and respond on other names
            if key.startswith('P') and value.isdigit():
                generateReply(int(value), self._sendReply)

        # TODO :Repeat start are not allowed
        elif line.strip() == 'start':
            generateReply(-1, self._sendReply)

        elif line.strip() == 'end':
            return -1

        return None

    def _stopServer(self):
        with lock:
            shared_data.stopFlag = True
            event.set()

        if self.monitor_thread1:
            self.monitor_thread1.join()

        # TODO: wait for all threads to stop
        self._disconnectServer()

    def _disconnectServer(self):
        NotImplemented

    def _sendReply(self, replay):
        if self.name is not None:
            message = f"{self.name}:{replay}"
            logger.info(f'<-{message}')
            self.app_sock.sendall(message.encode())
        else:
            logger.error("Application name is empty")

    def execute(self, name):
        started = True
        self.name = name

        # -------------start-----------------
        # TODO: maybe move this section to connection state
        is_Connected = self._connectToServer()

        if is_Connected:
            with lock:
                shared_data.socket = self.app_sock
                shared_data.stopFlag = False
                shared_data.state = State.Idle
                state = shared_data.state

            # Start threads to monitor communication in both directions
            self.monitor_thread1 = threading.Thread(
                target=monitor_communication, args=(name, shared_data, event,))
            self.monitor_thread1.start()
        else:
            logger.info("Exit code")
            state = State.End
        # -------------end-----------------

        while started:
            match state:
                case State.Idle:
                    # TODO: figure out way to go in connection mode if disconnected
                    if event.is_set():
                        with lock:
                            state = shared_data.state
                            # Reset the event after updating state
                            event.clear()
                case State.DataReceived:
                    with lock:
                        msg = shared_data.msg
                    result = self._handleMsg(msg)
                    if result == -1:
                        state = State.End
                    else:
                        state = State.Idle

                case State.End:
                    started = False

        self._stopServer()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app_num = sys.argv[1]
    else:
        app_num = "clientApp"

    app = ClientApp()
    app.execute(app_num)
