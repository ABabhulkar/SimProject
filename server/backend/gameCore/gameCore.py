import json
import logging
import socket
import threading
from time import sleep
from typing import Callable

from ..gameCore.clientTask import ClientTask
from ..gameCore.utils.sharedData import SharedData, State
from ..gameLogic import IGameLogic

PLAYER0 = 'P0'
PLAYER1 = 'P1'

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
    """Logger for game core context
    """
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


def monitor_connection_events(server_socket):
    """
    This is a thread function which monitors the connection events for the clients
    and stores the handlers while starting separate thread per client to monitor
    data reception and transmission events.

    Args:
        server_socket (_type_): _description_
    """

    server_socket.settimeout(5)
    client_count = 0
    while True:
        with lock:
            if not shared_data.isConnectionMonitor:
                break
        try:
            logger.debug('Monitoring for Client %d', client_count)
            client_socket, client_addr = server_socket.accept()
            logger.info("Connected to %s", client_addr)

            # Start a new thread to handle each client
            client_thread = threading.Thread(
                target=ClientTask.handle_connection,
                args=(client_socket, client_addr, lock, shared_data, event, logger))
            client_thread.start()
            client_count += 1
            if client_count == 2:
                with lock:
                    shared_data.state = State.start_game
                event.set()

                sleep(1)
                logger.debug('Closing Monitor')
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
        self.game_logic = game_logic
        with lock:
            shared_data.init_data()
        logger.debug("Init done")

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
            logger.error('Server connection error: %s', e)
        return False

    def __stopServer(self):
        # here we want to close all the open connection and threads
        self._socket.close()
        logger.info("Server stopped.")

    def __startPlayers(self) -> bool:
        logger.debug('Entered state: StartPlayer')
        algo_list = self.game_logic.get_file_names()

        if len(algo_list) == 2:
            clients = {}
            for index, item in enumerate(algo_list):
                player = ClientTask(index, item)
                clients[player.name] = player

            with lock:
                shared_data.clients = clients

            for key, value in clients.items():
                logger.debug('Start Player: %s', key)
                value.startApp(logger)

    def __stateMachine(self):
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
                            if shared_data.roundStatus.get(PLAYER0, False) and shared_data.roundStatus.get(PLAYER1, False):
                                state = State.NextRound
                            elif shared_data.roundStatus.get(PLAYER0, False) and not shared_data.roundStatus.get(PLAYER1, True):
                                state = State.ForwardMsg
                            else:
                                state = shared_data.state
                                shared_data.state = State.Idle
                            # Reset the event after updating state
                            event.clear()

                case State.StartPlayer:
                    self.__startPlayers()
                    state = State.Idle

                # TODO: check if we can move the logic of following lines to some other class
                case State.start_game:
                    logger.debug('Entered state: start_game')
                    with lock:
                        shared_data.maxNumberOfRounds = self.game_logic.get_rounds_num()
                        shared_data.roundStatus[PLAYER0] = False
                        shared_data.roundStatus[PLAYER1] = False
                        result = shared_data.nextRound(PLAYER0, PLAYER1)
                        if result:
                            shared_data.clients[PLAYER0].sendCommand('start')
                            state = State.Idle

                case State.NextRound:
                    logger.debug('Entered state: NextRound')
                    with lock:
                        shared_data.roundStatus[PLAYER0] = False
                        shared_data.roundStatus[PLAYER1] = False
                        result = shared_data.nextRound(PLAYER0, PLAYER1)
                        if result:
                            shared_data.clients[PLAYER0].forwardMove(
                                shared_data.getLastRound().getMove(PLAYER1))
                            state = State.Idle
                        else:
                            state = State.StopPlayers

                case State.ForwardMsg:
                    logger.debug('Entered state: Forward')
                    with lock:
                        shared_data.clients[PLAYER1].forwardMove(
                            shared_data.getCurrentRound().getMove(PLAYER0))
                        state = State.Idle

                case State.StopPlayers:
                    # Iterating over player to start processes
                    for key, value in shared_data.clients.items():
                        value.sendCommand('end')
                    logger.info('Entered state: StopPlayers')
                    state = State.CalculateResults

                case State.CalculateResults:
                    logger.debug('Entered state: CalculateResults')
                    if self.game_logic:
                        with lock:
                            json_s = json.dumps(
                                shared_data.rounds, default=lambda o: o.__dict__())
                            self.game_logic.calculate_result(json_s)
                    break

    def execute(self):
        """Execute the game

        Returns:
            bool: true on success, false otherwise
        """
        logger.debug('Started execution')
        result = self.__startServer()

        if result:
            # Init complete now start normal operations.
            self.__stateMachine()
        else:
            return False

        # Game complete
        self.__stopServer()
        return True
