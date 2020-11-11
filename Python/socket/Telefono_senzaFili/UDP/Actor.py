import socket
IpAddress = '192.168.0.119' #0.0.0.0
port = 7000
while(True):
    srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    srv.bind((IpAddress,port))

    #ricezione del messaggio
    print("attesa:")
    data, address = srv.recvfrom(4096)
    data= data.decode()
    print(f"msg from client: {data}") 

    srv.close()

    #inviare

    server_Ip = '192.168.0.118' #Karni
    server_port = 7000

    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #invio del messaggio
    cli.sendto(data.encode(),(server_Ip,server_port))

    data = cli.recv(4096)

    cli.close()