import logging
import socket
import threading
from time import sleep

# logger to log things in code
logger = logging.getLogger(" clientAppTest ")


def setup_logger():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)


def handle_client(client_socket, client_addr):
    # Function to handle each client's communication
    global clients
    global stop
    client_socket.settimeout(1)
    while True:
        if stop == True:
            break
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            logger.debug(f"Received from {client_addr}: {data.decode()}")
        except TimeoutError:
            NotImplemented

        # Send the received data to all other clients
        for client in clients:
            if client != client_socket:
                try:
                    client.sendall(data)
                except Exception as e:
                    logger.error(
                        f"Error sending data to {client.getpeername()}: {e}")
                    # client.close()
                    # clients.remove(client)

    client_socket.close()


def start_server(soc):
    soc.bind(('localhost', 5002))
    soc.listen(1)
    soc.settimeout(10)
    logger.info("Server is listening for incoming connections...")

    # wait for client to connect
    try:
        client_socket, client_addr = soc.accept()
        logger.info(f"Connected to {client_addr}")

        clients.append(client_socket)

        # Start a new thread to handle each client
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_addr))
        client_thread.start()
        return True
    except TimeoutError:
        logger.error('Server connection timeout')
        return False


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_logger()
    stop = False
    clients = []
    result = start_server(server_socket)

    # TODO: Make testing automated
    # - User should put test inputs in array and run test
    # - Test should wait for connection
    # - once connected test should send test data with delay

    if result:
        while True:
            _in = input()
            try:
                for client in clients:
                    try:
                        client.sendall(_in.encode())
                    except Exception as e:
                        logger.error(
                            f"Error sending data to {client.getpeername()}: {e}")
            except TimeoutError:
                logger.error('Server connection timeout')

            if _in == 'end':
                break
    stop = True
    sleep(1)
