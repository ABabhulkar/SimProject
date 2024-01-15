import socket
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
        print(f"Received from {client_addr}: {data.decode()}")

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


class MainThread:
    def __init__(self) -> None:
        self._socket = None
        self._numOfClients = 2
        self._timeout = 1
        self._port = 5002

    def _startServer(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind(('localhost', self._port))
        self._socket.listen(self._numOfClients)
        self._socket.settimeout(self._timeout)
        # TODO: Add error handling here

    def _stopServer(self):
        # here we want to close all the open connection and threads
        NotImplemented

    def execute(self):
        # TODO: read dir to find which clients are present
        # start server
        self._startServer()
        # TODO: wait for clients to connect

        # Init complete now start normal operations.
        self._stateMachine()

        # Game complete
        self._stopServer()

    def _stateMachine(self):
        with lock:
            shared_data.state = State.Idle
            state = shared_data.state

        started = True

        while started:
            match state:
                case State.Idle:
                    if event.is_set():
                        with lock:
                            state = shared_data.state
                            # Reset the event after updating state
                            event.clear()

                case State.StartPlayer:
                    # TODO: Start players here
                    state = State.StartGame

                case State.StartGame:
                    # TODO: Select player 1 and start the game by sending command
                    state = State.CalculateResults

                case State.CalculateResults:
                    # TODO: stop players and calculate final results.
                    state = State.Idle

                case State.End:
                    started = False


if __name__ == "__main__":

    clients = []
    count = 0
    stop = False
    while count < 11:
        try:
            client_socket, client_addr = server_socket.accept()
            print(f"Connected to {client_addr}")

            clients.append(client_socket)

            # Start a new thread to handle each client
            client_thread = threading.Thread(
                target=handle_client, args=(client_socket, client_addr))
            client_thread.start()
        except TimeoutError:
            NotImplemented

        count += 1
        sleep(1)

    stop = True
    sleep(1)
