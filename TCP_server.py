import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5004))
    server.listen(1)
    conn, addr = server.accept()
    
    text = conn.recv(1024).decode()
    result = str(len(text))
    conn.send(result.encode())
    
    conn.close()
    server.close()

if __name__ == '__main__':
    start_server()
