import socket
import threading
import json

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start(self):
        server = threading.Thread(target=self.run_server)
        server.start()

    def run_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Node running on {self.host}:{self.port}")
        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = json.loads(data.decode('utf-8'))
            self.handle_message(message)
        client_socket.close()

    def handle_message(self, message):
        print(f"Received message: {message}")
        # Implement message handling (e.g., new transactions, block proposals)

node = Node('127.0.0.1', 5000)
node.start()
