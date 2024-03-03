import os
import subprocess


class ClientTask:
    def __init__(self, index: int, path: str) -> None:
        self.name = f'P{index}'
        self.path = path
        self.socket = None
        self.startHandler = False

    def start_app(self, logger):
        """This function should start the application with proper arguments

        Args:
            logger (_type_): Logger of context
        """
        if not os.path.isfile(self.path):
            logger.info("Folder path does not exist.")
            return

        arguments = [self.name]  # Replace with your actual arguments
        command = [self.path] + arguments
        subprocess.Popen(command, stdout=subprocess.PIPE)
        logger.debug(f'command: {command}')

    def send_command(self, command):
        self.socket.sendall(command.encode())

    def forward_move(self, move):
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

                value, isAck = ClientTask.parse_msg(data.decode())

                with _lock:
                    if isAck:
                        _shared_data.clients[value].socket = client_socket
                        name = value
                    else:
                        round = _shared_data.get_current_round()
                        round.update_move(name, value)
                        _shared_data.roundStatus[name] = True
                        _event.set()
            except TimeoutError:
                NotImplemented
            except OSError as e:
                _logger.error(e)
                break
        client_socket.close()

    @staticmethod
    def parse_msg(line):
        """
        It returns the name if received connected
        It returns move otherwise

        Args:
            line (_type_): _description_

        Returns:
            _type_: _description_
        """
        parts = line.strip().split(':')
        if len(parts) == 2:
            key, value = parts[0], parts[1]
            if key.startswith('P') and value == "connected":
                return key, True
            elif key.startswith('P'):
                return value, False
        return None, None
