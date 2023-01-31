from socket import socket, AF_INET, SOCK_STREAM

HOST = "localhost"
PORT = 10000

def main():
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"test if works")
        data = client_socket.recv(2048)
        # print(f"received: {data}")

if __name__ == '__main__':
    main()
