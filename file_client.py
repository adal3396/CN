import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))
    
    filename = input("Enter the filename to request from server: ")
    client.send(filename.encode())
    
    response = client.recv(4096).decode()
    print("\n--- Response from Server ---")
    print(response)
    
    client.close()

if __name__ == "__main__":
    start_client()
