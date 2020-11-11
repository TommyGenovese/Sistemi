import socket

IpAddress = '192.168.88.106'
port = 6000

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((IpAddress, port))

while(True):

    #invio del messaggio
    msg = input("testo del messaggio:")
    msg = msg.encode()
    cli.send(msg)

    #ricezione messaggio di conferma
    data = cli.recv(8036)
    print(data.decode())

cli.close()