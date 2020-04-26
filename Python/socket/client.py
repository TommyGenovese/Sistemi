import socket

ip = 'localhost'
port = 5004

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    #ricezione del messaggio
    raw_data = cli.recv(4096)

    if str(raw_data,encoding="ascii") == "$stop":
        break
    print('msg del client:' + str(raw_data))

    #invio del messaggio
    msg = input("inserisci il messaggio da inviare:")
    cli.sendto(msg.encode(),(ip,port))
    if str(msg) == "$stop":
        break


cli.close()