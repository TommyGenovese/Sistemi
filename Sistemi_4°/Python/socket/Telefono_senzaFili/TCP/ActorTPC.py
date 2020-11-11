import socket
IpAddress = '192.168.0.119' #0.0.0.0
port = 7000
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv.listen()
cn, address = srv.accept()
print("Connected to", address)
#ricezione del messaggio
data = cn.recv(8036)
print(f"msg from client: {data}")

cn.close()

#inviare

server_Ip = '192.168.0.118' #Karni
server_port = 7000

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#invio del messaggio
cli.sendto(data.encode(),(server_Ip,server_port))



msg = input("testo del messaggio:")
cli.sendto(msg.encode(),(server_Ip,server_port))

data = cli.recv(4096)

cli.close()