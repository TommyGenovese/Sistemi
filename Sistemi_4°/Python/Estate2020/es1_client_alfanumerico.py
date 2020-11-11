import socket

IpAddress = 'localhost'
port = 5004

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))

while(True):

    #invio del messaggio
    msg = input("testo del messaggio:")
    cli.send(msg.encode())

    #si può interrompere il collegamento digitando '!stop'
    if str(msg) == "!stop":
            break
    
    #ricezione messaggio di conferma
    data = cli.recv(4096)
    print("msg : " + data.decode())

cli.close()