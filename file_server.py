import socket
import os
import multiprocessing

def handle_client(client_socket):
    pid = os.getpid()
    try:
        filename = client_socket.recv(1024).decode().strip()
        print(f"[PID {pid}] Request received for file: {filename}")
        
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename, 'r') as f:
                content = f.read()
            response = f"[SERVER PID: {pid}] File Found:\n{content}"
        else:
            response = f"[SERVER PID: {pid}] Error: File '{filename}' does not exist on server."
            
        client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(5)
    print("Concurrent File Server is running on port 8888...")

    while True:
        client_socket, addr = server.accept()
        # Use multiprocessing to handle concurrent clients and get distinct PIDs
        process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        process.start()
        client_socket.close() # Parent closes its reference to client socket

if __name__ == "__main__":
    start_server()
