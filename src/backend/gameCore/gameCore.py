import logging
import socket
import threading
from time import sleep
from typing import Callable

from gameCore.clientTask import ClientTask
from gameCore.utils.sharedData import SharedData, State
from gameLogic.IGameLogic import IGameLogic

PLAYER1 = 'P1'
PLAYER2 = 'P2'

# Create an instance of SharedData
shared_data = SharedData()
# Create a lock
lock = threading.Lock()
# Create an event
event = threading.Event()

# logger to log things in code
logger = logging.getLogger(" game_core ")

# TODO: check if game specific functions can be removed from this file and make it an interface


def setup_logger():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


def monitor_connection_events(server_socket):
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
                target=ClientTask.handle_connection, args=(client_socket, client_addr, lock, shared_data, event, logger))
            client_thread.start()
            clientCount += 1
            if clientCount == 2:
                with lock:
                    shared_data.state = State.StartGame
                event.set()
                sleep(1)
                # TODO: Wait hear for the connection of both sides
                logger.debug(f'Closing Monitor')
                break
        except TimeoutError:
            logger.error('Server connection timeout')


class GameCore:
    def __init__(self, game_logic: IGameLogic) -> None:
        self._socket = None
        self._numOfClients = 2
        self._timeout = 1
        self._port = 5002
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        setup_logger()
        logger.debug("Init done")
        self.game_logic = game_logic

    def __startServer(self):
        # Connects to socket and return true. return false in case of error
        try:
            self._socket.bind(('localhost', self._port))
            self._socket.listen(self._numOfClients)
            self._socket.settimeout(self._timeout)
            logger.info("Server is listening for incoming connections...")

            # Start thread to monitor client connections
            self.monitorConnection = threading.Thread(
                target=monitor_connection_events, args=(self._socket,))
            with lock:
                shared_data.isConnectionMonitor = True
            self.monitorConnection.start()
            return True
        except socket.error as e:
            logger.error('Server connection error')
        return False

    def __stopServer(self):
        # here we want to close all the open connection and threads
        self._socket.close()
        logger.info("Server stopped.")

    def __stateMachine(self, client1_dir, client2_dir):
        with lock:
            shared_data.state = State.StartPlayer
            state = shared_data.state

        while True:
            match state:
                case State.Idle:
                    with lock:
                        if event.is_set():
                            # l = shared_data.roundStatus.values()
                            # if all(val == True for val in l) and len(l) != 0:
                            #     state = State.NextRound
                            if shared_data.roundStatus.get(PLAYER1, False) and shared_data.roundStatus.get(PLAYER2, False):
                                state = State.NextRound
                            elif shared_data.roundStatus.get(PLAYER1, False) and not shared_data.roundStatus.get(PLAYER2, True):
                                state = State.ForwardMsg
                            else:
                                state = shared_data.state
                                shared_data.state = State.Idle
                            # Reset the event after updating state
                            event.clear()

                case State.StartPlayer:
                    logger.debug(f'Entered state: StartPlayer')
                    with lock:
                        if client1_dir is not None:
                            P1 = ClientTask(PLAYER1, client1_dir)
                            shared_data.clients[P1.name] = P1
                        if client2_dir is not None:
                            P2 = ClientTask(PLAYER2, client2_dir)
                            shared_data.clients[P2.name] = P2

                        # Iterating over player to start processes
                        for key, value in shared_data.clients.items():
                            logger.debug(f"Start player: {key}")
                            value.startApp(logger)
                    state = State.Idle

                # TODO: check if we can move the logic of following lines to some other class
                case State.StartGame:
                    logger.debug(f'Entered state: StartGame')
                    with lock:
                        shared_data.maxNumberOfRounds = 10
                        shared_data.roundStatus[PLAYER1] = False
                        shared_data.roundStatus[PLAYER2] = False
                        result = shared_data.nextRound(PLAYER1, PLAYER2)
                        if result:
                            shared_data.clients[PLAYER1].sendCommand('start')
                            state = State.Idle

                case State.NextRound:
                    logger.debug(f'Entered state: NextRound')
                    with lock:
                        shared_data.roundStatus[PLAYER1] = False
                        shared_data.roundStatus[PLAYER2] = False
                        result = shared_data.nextRound(PLAYER1, PLAYER2)
                        if result:
                            shared_data.clients[PLAYER1].forwardMove(
                                shared_data.getLastRound().getMove(PLAYER2))
                            state = State.Idle
                        else:
                            state = State.CalculateResults

                case State.ForwardMsg:
                    logger.debug(f'Entered state: Forward')
                    with lock:
                        shared_data.clients[PLAYER2].forwardMove(
                            shared_data.getCurrentRound().getMove(PLAYER1))
                        state = State.Idle

                case State.CalculateResults:
                    logger.debug(f'Entered state: CalculateResults')
                    for key, value in shared_data.clients.items():
                        value.sendCommand('end')
                    if self.game_logic:
                        with lock:
                            self.game_logic.calculate_result(
                                shared_data.rounds)
                    state = State.End

                case State.End:
                    # Iterating over player to start processes
                    for key, value in shared_data.clients.items():
                        # value.socket.close()
                        NotImplemented
                    logger.error(f'Entered state: End')
                    break

    def execute(self, client1_dir, client2_dir):
        logger.debug(f'Started execution')
        result = self.__startServer()

        if result:
            # Init complete now start normal operations.
            self.__stateMachine(client1_dir, client2_dir)
        else:
            return False

        # Game complete
        self.__stopServer()
        return True
