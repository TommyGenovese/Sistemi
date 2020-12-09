#es sull'algoritmo di diff-hellman
import socket
import math
import random
import config

Ip_server = "127.0.0.1"
PORT= 6000

def is_prime(n):

    #n is the prime number to find out
    bruteforce_numbers = []
    for i in range (2,int(math.sqrt(n) + 1)):
        bruteforce_numbers.append(i)

    for number in bruteforce_numbers:
        if n != number and n % number == 0:
            return 0

    return 1

def client():
    g = config.g
    N = config.N 
    
    print(f"g={config.g}, N={config.N}")      
    

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((Ip_server, PORT))
    a = random.randint(1, config.N-1)
    print(f"a = {a}")
    A = str((g**a)%N)
    cli.sendall(A.encode())

    B = cli.recv(4096).decode()
    B = int(B)

    Ks = (B**a)%N
    print (f"numero: {Ks}")

    cli.close()

if __name__ == "__main__":
    client()