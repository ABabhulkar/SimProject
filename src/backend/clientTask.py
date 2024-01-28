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
