import logging
import socket
import subprocess
import threading
from time import sleep

from backend.clientTask import ClientTask
from backend.utils.sharedData import SharedData, State

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


def handle_client(client_socket, client_addr):
    # This is a thread run function which should be invoked per client
    client = ClientTask()

    global clients
    global stop
    client_socket.settimeout(1)
    while True:
        if stop == True:
            break
        try:
            data = client_socket.recv(1024)
        except TimeoutError:
            NotImplemented
        if not data:
            break
        logger.debug(f"Received from {client_addr}: {data.decode()}")

        # Send the received data to all other clients
        for client in clients:
            if client != client_socket:
                try:
                    client.sendall(data)
                except Exception as e:
                    # print(f"Error sending data to {client.getpeername()}: {e}")
                    # client.close()
                    clients.remove(client)

    client_socket.close()


def monitor_connection_events(server_socket):
    # This is a thread function which monitors the connection events for the clients
    # and stores the handlers while starting separate thread per client to monitor
    # data reception and transmission events.
    server_socket.settimeout(5)
    while True:
        with lock:
            if not shared_data.isConnectionMonitor:
                break
        try:
            client_socket, client_addr = server_socket.accept()
            logger.info(f"Connected to {client_addr}")

            # TODO: Figure out how to save the client socket into specific client
            # clients.append(client_socket)

            # Start a new thread to handle each client
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, client_addr))
            client_thread.start()
        except TimeoutError:
            logger.error('Server connection timeout')


class GameCore:
    def __init__(self) -> None:
        self._socket = None
        self._numOfClients = 2
        self._timeout = 1
        self._port = 5002
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _startServer(self):
        self._socket.bind(('localhost', self._port))
        self._socket.listen(self._numOfClients)
        self._socket.settimeout(self._timeout)
        logger.info("Server is listening for incoming connections...")

        self.monitorConnection = threading.Thread(
            target=handle_client, args=(self._socket,))
        with lock:
            shared_data.isConnectionMonitor = True
        self.monitorConnection.start()
        # TODO: Add error handling here in case of error return false
        return True

    def _stopServer(self):
        # here we want to close all the open connection and threads
        self._socket.close()
        logger.info("Server stopped.")

    def _stateMachine(self, client1_dir, client2_dir):
        with lock:
            shared_data.state = State.Idle
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
                    with lock:
                        if client1_dir is not None:
                            P1 = ClientTask('P1', client1_dir)
                            shared_data.clients[P1.name] = P1
                        if client2_dir is not None:
                            P2 = ClientTask('P2', client2_dir)
                            shared_data.clients[P2.name] = P2

                        # Iterating over player to start processes
                        for key, value in shared_data.clients.items():
                            logger.debug(f"player: {key}")
                            value.startApp()

                    # TODO: wait for both players to connect
                    state = State.StartGame

                case State.StartGame:
                    with lock:
                        NotImplemented
                    # TODO: Select player 1 and start the game by sending command 'start'
                    state = State.CalculateResults

                case State.CalculateResults:
                    # TODO: stop players and calculate final results.
                    state = State.Idle

                case State.End:
                    break

    def execute(self, client1_dir, client2_dir):
        # start server
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
    P1_dir = ''
    gameCore = GameCore()
    gameCore.execute(P1_dir, P1_dir)
