import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('127.0.0.1', 6004))
    
    data, addr = server.recvfrom(1024)
    text = data.decode()
    result = "Palindrome" if text == text[::-1] else "Not a Palindrome"
    server.sendto(result.encode(), addr)
    server.close()

if __name__ == '__main__':
    start_server()
