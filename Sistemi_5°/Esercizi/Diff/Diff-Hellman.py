#es sull'algoritmo di diff-hellman
import socket
import config
import math
import random

Ip_server = "127.0.0.1"
PORT= 6000

def server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind((Ip_server, PORT))
    srv.listen()
    conn, _ = srv.accept()
    print("nuova connessione")

    A = conn.recv(4096).decode()
    A = int(A)
    b = random.randint(1, config.N-1)
    print(f"b = {b}")
    Ks = (A**b)%config.N
    print(f"numero scelto: {Ks}")
    B = str((config.g**b)%config.N)

    conn.sendall(B.encode())
    srv.close()

if __name__ == "__main__":
    server()