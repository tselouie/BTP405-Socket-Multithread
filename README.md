# Python Client-Server Application

This repository contains a simple Python client-server application that demonstrates basic network communication using sockets and multi-threading to handle multiple clients.

## Overview

The application consists of two main scripts:

- `client.py`: A client program that connects to the server, sends messages, and receives responses.
- `server.py`: A server program that listens for connections from clients, receives messages, echoes them back to the client, and supports multiple client connections using threading.

### Server

To start the server, run:

```bash
python server.py
```

The server will start on `localhost` (127.0.0.1) at port `27000` and will listen for incoming client connections.

### Client

To connect a client to the server, run:

```bash
python client.py
```

After running the client script, you will be prompted to enter messages to send to the server. Type your message and press enter. The server will echo the message back. To exit, type `exit` and press enter.

## Implementation Details

### Server

- It listens on port `27000` and can handle up to 5 simultaneous client connections.
- Each client is handled in a separate thread, where the server receives a message and sends it back (echoes).

### Client

- The client establishes a connection to the server at `127.0.0.1:27000`.
- It sends messages entered by the user to the server and prints the server's response.
- The client will disconnect and exit when the user types `exit`.
