import socket
import threading
from time import sleep

# Function to handle each client's communication
def handle_client(client_socket, client_addr):
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

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5002))
    server_socket.listen(5)
    server_socket.settimeout(1)
    print("Server is listening for incoming connections...")

    clients = []
    count = 0
    stop = False
    while count<11:
        try:
            client_socket, client_addr = server_socket.accept()
            print(f"Connected to {client_addr}")

            clients.append(client_socket)

            # Start a new thread to handle each client
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_addr))
            client_thread.start()
        except TimeoutError:
            NotImplemented
        
        count+=1
        sleep(1)
        
    stop = True
    sleep(1)
