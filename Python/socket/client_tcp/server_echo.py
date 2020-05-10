import socket
IpAddress = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.listen()
cn, address = srv.accept()
print("Connected to", address)

while(True):
    
    #ricezione del messaggio
    data = cn.recv(8036)
    print(f"msg from client: {data}")
    
    #invio messaggio di conferma
    if not data or data.decode()[1:] == "$stop":
        break
    cn.send(data)

cn.close()