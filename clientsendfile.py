from socket import socket, AF_INET, SOCK_STREAM
import argparse

HOST = "192.168.100.34"
PORT = 10000

parser = argparse.ArgumentParser()
parser.add_argument('save', type=str)

parser.add_argument('send', type=str)

args = parser.parse_args()

def main():
    with socket(AF_INET, SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        with open(args.save, "rb") as file:
            f = file.read()
            client_socket.sendall(bytes([len(args.send)]) +  args.send.encode() + f)



if __name__ == '__main__':
    main()
