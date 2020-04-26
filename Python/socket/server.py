import socket

ip = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((ip,port))

while(True):
    
    #ricezione del messaggio
    raw_data = srv.recv(4096)
    if str(raw_data,encoding="ascii") == "$stop":
        break
    print('msg del client:' + str(raw_data))


    #invio del messaggio
    msg = input("inserisci il messaggio da inviare:")
    srv.sendto(msg.encode(),(ip,port))
    if str(msg) == "$stop":
        break

srv.close()