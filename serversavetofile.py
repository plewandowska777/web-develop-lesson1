from socket import socket, AF_INET, SOCK_STREAM


HOST = "localhost"
PORT = 10000


def main():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        connection, address = server_socket.accept()
        # print(f"accepted connection from {address}")

        with connection:
            data = connection.recv(2048)
            l = data[0]
            name = data[1:l+1]
            print(name)
            with open(name, "wb") as savefile:
                savefile.write(data[l+1:len(data)])





if __name__ == '__main__':
    main()
