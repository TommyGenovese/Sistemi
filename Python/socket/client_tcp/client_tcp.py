import socket

IpAddress = 'localhost'
port = 5004

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cli.connect(IpAddress, port)

while(True):

    #invio del messaggio
    msg = input("testo del messaggio:")
    cli.send(msg)

    #si può interrompere il collegamento digitando '$stop'
    #if str(msg) == "$stop":
    #    break
    if str(msg) == "$stop":
            break
    
    #ricezione messaggio di conferma
    data = cli.recv(8036)
    print(data.decode())

cli.close()