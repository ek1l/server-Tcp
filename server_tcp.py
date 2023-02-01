import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("127.0.0.1", 7799))
    server.listen(5)
    print("Listening...")

    client_socket, address = server.accept()
    print("Received from:" + address[0])
    while true:

        data= client_socket.recv(1024).decode()
        print(data)
        client_socket.send(input("Mensagem: ").encode())

    server.close()
except Exception as error:
    print('Erro ', error)
    server.close()
