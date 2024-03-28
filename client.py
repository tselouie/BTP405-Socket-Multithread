import socket
import random

def main():
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return
    host = '127.0.0.1'
    port = 27000
    try:
        client_socket.connect((host, port))
    except socket.error as e:
        print(f"Failed to connect to server: {e}")
        client_socket.close()
        return

    print("Connected to the server. Type 'exit' to quit.")
    while True:
        message = input("Enter message to send or 'exit' to quit: ")
        if message == 'exit':
            break
        print(f"Sending: {message}")
        try:
            # Send message to server
            client_socket.sendall(message.encode())
            # Receive echo'd response from server
            response = client_socket.recv(128).decode()
            print(f"Received: {response}")
        except socket.error as e:
            print(f"Error sending or receiving data: {e}")
            break

    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
