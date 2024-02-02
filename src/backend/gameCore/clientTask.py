import os
import subprocess


class ClientTask:
    def __init__(self, name, dir) -> None:
        self.name = name
        self.dir = dir
        self.socket = None
        self.startHandler = False

    def startApp(self, logger):
        # This function should start the application with proper arguments
        if not os.path.isfile(self.dir):
            logger.info("Folder path does not exist.")
            return

        arguments = [self.name]  # Replace with your actual arguments
        # TODO: python should be removed as we will accept binary
        command = ['python3', self.dir] + arguments
        subprocess.Popen(command, stdout=subprocess.PIPE)
        logger.debug(f'command: {command}')

    def sendCommand(self, command):
        self.socket.sendall(command.encode())

    def forwardMove(self, move):
        msg = f'{self.name}:{move}'
        self.socket.sendall(msg.encode())

    @staticmethod
    def handle_connection(client_socket, client_addr, _lock, _shared_data, _event, _logger):
        # This is a thread run function which should be invoked per client
        name = ''
        client_socket.settimeout(1)
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                _logger.debug(f"{client_addr[1]} {name}-> {data.decode()}")

                value, isAck = ClientTask.parseMsg(data.decode())

                with _lock:
                    if isAck:
                        _shared_data.clients[value].socket = client_socket
                        name = value
                    else:
                        round = _shared_data.getCurrentRound()
                        round.updateMove(name, value)
                        _shared_data.roundStatus[name] = True
                        _event.set()
            except TimeoutError:
                NotImplemented
            except OSError as e:
                _logger.error(e)
                break
        client_socket.close()

    @staticmethod
    def parseMsg(line):
        # it returns the name if received connected
        # it returns move otherwise
        parts = line.strip().split(':')
        if len(parts) == 2:
            key, value = parts[0], parts[1]
            if key.startswith('P') and value == "connected":
                return key, True
            elif key.startswith('P'):
                return value, False
        return None
