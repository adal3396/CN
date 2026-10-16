import socket
import threading

clients = []

def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            # Broadcast message to all other clients
            for client in clients:
                if client != client_socket:
                    client.send(message)
        except:
            break
            
    client_socket.close()
    clients.remove(client_socket)
    print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen()
    print("[SERVER STARTED] Multi-user chat server is listening on port 5555...")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
