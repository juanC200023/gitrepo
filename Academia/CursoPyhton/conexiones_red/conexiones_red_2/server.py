#!/usr/bin/env python3
import socket
import threading
import pdb # debugging

class ClientTrhead(threading.Thread):

    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] Nuevo cliente conectado:{client_addr}")

    def run(self):

        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            # pdb.set_trace() # Breakpoint

            if message.strip() == 'bye':
                break

            print(f"\n[+] Mensaje enviado por el cliente {message.strip()}")
            self.client_sock.send(data)

        print(f"\n[!] Cliente {self.client_addr} deconectado")
        self.client_sock.close()

HOST = 'localhost'
PORT = 1234



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((HOST, PORT))

    print(f"\n[+] En espera de conexiones entrantes...")

    while True:

        server_socket.listen()
        client_sock, client_addr = server_socket.accept()
        new_thread = ClientTrhead(client_sock, client_addr)
        new_thread.start() # run()


