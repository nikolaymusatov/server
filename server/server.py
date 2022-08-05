import socket


def start_server():
    try:
        server = socket.create_server(('', 2000))
        server.listen(10)
        print("Listening to localhost:2000")
        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n"
            client_socket.send(headers.encode('utf-8') + data.encode('utf-8'))
            client_socket.shutdown(socket.SHUT_RDWR)
    except KeyboardInterrupt:
        server.close()


if __name__ == '__main__':
    start_server()
