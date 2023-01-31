from socket import socket, AF_INET, SOCK_STREAM

HOST = "localhost"
PORT = 10000

def main():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        connection, address = server_socket.accept()
        print(f"accepted connection from {address}")

        with connection:
            data = connection.recv(2048)
            print(f"received: {data}")
            connection.sendall(data)

if __name__ == '__main__':
    main()
