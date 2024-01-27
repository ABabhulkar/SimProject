import logging
import socket
import subprocess
import threading
from time import sleep

from clientTask import ClientTask
from utils.sharedData import SharedData, State

# Create an instance of SharedData
shared_data = SharedData()
# Create a lock
lock = threading.Lock()
# Create an event
event = threading.Event()

# logger to log things in code
logger = logging.getLogger(" game_core ")


def setup_logger():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


def _parseMsg(line):
    parts = line.strip().split(':')
    if len(parts) == 2:
        key, value = parts[0], parts[1]
        if key.startswith('P') and value == "connected":
            return key, True
        elif key.startswith('P'):
            return value, False

    return None


def handle_client(client_socket, client_addr):
    # This is a thread run function which should be invoked per client
    stop = False
    name = ''
    client_socket.settimeout(1)
    while True:
        if stop == True:
            break
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            logger.debug(f"{client_addr[1]} {name}-> {data.decode()}")

            value, isAck = _parseMsg(data.decode())

            with lock:
                if isAck:
                    shared_data.clients[value].socket = client_socket
                    name = value
                else:
                    # Iterating over player to forward the massage
                    for key, value in shared_data.clients.items():
                        if key != name:
                            value.forwardMove(data)
                # TODO: Save the move.

        except TimeoutError:
            NotImplemented
    client_socket.close()


def monitor_connection_events(server_socket, _event):
    # This is a thread function which monitors the connection events for the clients
    # and stores the handlers while starting separate thread per client to monitor
    # data reception and transmission events.
    server_socket.settimeout(5)
    clientCount = 0
    while True:
        with lock:
            if not shared_data.isConnectionMonitor:
                break
        try:
            logger.debug(f'Monitoring for Client {clientCount}')
            client_socket, client_addr = server_socket.accept()
            logger.info(f"Connected to {client_addr}")

            # Start a new thread to handle each client
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, client_addr))
            client_thread.start()
            clientCount += 1
            if clientCount == 2:
                with lock:
                    shared_data.state = State.StartGame
                _event.set()
                sleep(1)
                # TODO: Wait hear for the connection of both sides
                logger.debug(f'Closing Monitor')
                break
        except TimeoutError:
            logger.error('Server connection timeout')


class GameCore:
    def __init__(self) -> None:
        self._socket = None
        self._numOfClients = 2
        self._timeout = 1
        self._port = 5002
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        setup_logger()
        logger.debug("Init done")

    def _startServer(self):
        # Connects to socket and return true. return false in case of error
        try:
            self._socket.bind(('localhost', self._port))
            self._socket.listen(self._numOfClients)
            self._socket.settimeout(self._timeout)
            logger.info("Server is listening for incoming connections...")

            # Start thread to monitor client connections
            self.monitorConnection = threading.Thread(
                target=monitor_connection_events, args=(self._socket, event))
            with lock:
                shared_data.isConnectionMonitor = True
            self.monitorConnection.start()
            return True
        except socket.error as e:
            logger.error('Server connection error')
        return False

    def _stopServer(self):
        # here we want to close all the open connection and threads
        self._socket.close()
        logger.info("Server stopped.")

    def _stateMachine(self, client1_dir, client2_dir):
        with lock:
            shared_data.state = State.StartPlayer
            state = shared_data.state

        while True:
            match state:
                case State.Idle:
                    if event.is_set():
                        with lock:
                            state = shared_data.state
                            # Reset the event after updating state
                            event.clear()

                case State.StartPlayer:
                    logger.debug(f'Entered state: StartPlayer')
                    with lock:
                        if client1_dir is not None:
                            P1 = ClientTask('P1', client1_dir)
                            shared_data.clients[P1.name] = P1
                        if client2_dir is not None:
                            P2 = ClientTask('P2', client2_dir)
                            shared_data.clients[P2.name] = P2

                        # Iterating over player to start processes
                        for key, value in shared_data.clients.items():
                            logger.debug(f"Start player: {key}")
                            value.startApp(logger)

                    state = State.Idle

                case State.StartGame:
                    logger.debug(f'Entered state: StartGame')
                    with lock:
                        shared_data.clients['P1'].sendCommand('start')
                    state = State.Idle

                case State.CalculateResults:
                    logger.debug(f'Entered state: CalculateResults')
                    # TODO: stop players and calculate final results.
                    state = State.Idle

                case State.End:
                    # TODO: Stop all threads hear
                    logger.debug(f'Entered state: End')
                    break

    def execute(self, client1_dir, client2_dir):
        logger.debug(f'Started execution')
        result = self._startServer()

        if result:
            # Init complete now start normal operations.
            self._stateMachine(client1_dir, client2_dir)
        else:
            return False

        # Game complete
        self._stopServer()
        return True


if __name__ == "__main__":

    # This is dir for the test application
    P1_dir = '/mnt/d/Projects/PythonWS/SimProject/ClientTemplate/src/clientApp.py'
    P2_dir = '/mnt/d/Projects/PythonWS/SimProject/ClientTemplate/src/clientApp.py'
    gameCore = GameCore()
    gameCore.execute(P1_dir, P2_dir)
