import socket
import os

def main():
    ip_address = socket.gethostbyname(socket.gethostname())

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((ip_address, 80))
    server_socket.listen(1)

    with open("home.html", "r") as f:
        home_html = f.read()

    while True:
        client_socket, address = server_socket.accept()

        client_socket.sendall(home_html.encode())

        client_socket.close()

if __name__ == "__main__":
    main()
