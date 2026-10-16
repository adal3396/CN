import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            print("\n[SERVER CLOSED] Connection lost.")
            client_socket.close()
            sys.exit()

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))
    
    name = input("Enter your chat name: ")
    
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    while True:
        msg = input()
        if msg.lower() == 'exit':
            break
        full_msg = f"{name}: {msg}"
        client.send(full_msg.encode())

    client.close()

if __name__ == "__main__":
    start_client()
