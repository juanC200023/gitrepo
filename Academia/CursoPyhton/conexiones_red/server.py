#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_address = ('localhost', 1234)
server_socket.bind(sever_address) #me pongo en escucha por el puerto 1234
#Limitar el limite de conexiones
server_socket.listen(1)

while True:

    client_socket, client_address = server_socket.accept()
    data = client_socket.recv(1024)

    print(f"\n[+] Mensaje recibido del cliente: {data.decode()}")
    print(f"\n[+] Informacion del cliente que se ha comunicado con nosotros: {client_address}")

    client_socket.sendall(f"Un saludo cra\n".encode())
    client_socket.close()
