import subprocess


class ClientTask:
    def __init__(self, name, dir) -> None:
        self.name = name
        self.dir = dir
        self.socket = None
        self.startHandler = False

    def startApp(self):
        # TODO: This function should start the application with proper arguments
        subprocess.call([f'python3 {self.dir}', f'{self.name}'])
        NotImplemented
