import socket
import sys
import threading
from time import sleep


def monitor_communication(num, sock, stop):
    while True:
        if stop():
            break
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Received in app{num}: {data.decode()}")
        except TimeoutError:
            NotImplemented


def app():
    if len(sys.argv) > 1:
        app_num = sys.argv[1]
    else:
        print("Hello, world!")

    count = 0
    stop_thread = False
    # Create a socket
    app_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (app1) on localhost and port 5001
    app_sock.connect(('localhost', 5002))
    app_sock.settimeout(1)
    # Start threads to monitor communication in both directions
    monitor_thread1 = threading.Thread(
        target=monitor_communication, args=(app_num, app_sock, lambda: stop_thread))
    monitor_thread1.start()

    while count < 10:
        message = f"app{app_num} alive:{count}"
        app_sock.sendall(message.encode())

        sleep(1)
        count += 1

    stop_thread = True
    monitor_thread1.join()


if __name__ == "__main__":
    app()
