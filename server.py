
import socket
import threading

MAX_CLIENTS = 5
client_sockets = [None] * MAX_CLIENTS

def handle_client(client_socket, index):
    print(f"Thread started for client {index}")
    while True:
        try:
            # Receive data from client
            data = client_socket.recv(128).decode()
            if not data:
                break
            print(f"Client {index} sent: {data}")
            # encode message and send it back to client
            client_socket.sendall(data.encode())
            # close conections if client sends 'quit'
            if data == "quit":
                break
        except socket.error as e:
            print(f"Error receiving data from client {index}: {e}")
            break
    client_socket.close()
    print(f"Connection with client {index} closed.")

def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 27000))
        server_socket.listen(MAX_CLIENTS)
    except socket.error as e:
        print(f"Error setting up server: {e}")
        return

    print("Server started. Waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        index = next((i for i, v in enumerate(client_sockets) if v is None), None)
        if index is not None:
            # create a thread for the client
            client_sockets[index] = client_socket
            thread = threading.Thread(target=handle_client, args=(client_socket, index))
            thread.start()
        else:
            print("Server full. Connection refused.")
            client_socket.sendall("Server full".encode())
            client_socket.close()

if __name__ == "__main__":
    main()
