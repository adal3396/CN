import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = input("Enter a string: ")
    client.sendto(text.encode(), ('127.0.0.1', 6004))
    
    data, _ = client.recvfrom(1024)
    print(f"Result: {data.decode()}")
    client.close()

if __name__ == '__main__':
    start_client()
