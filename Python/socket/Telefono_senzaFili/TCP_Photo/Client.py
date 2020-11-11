import socket

server_ip = "192.168.0.118" 
server_ip_personal = "192.168.0.119"
port = 7000

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((server_ip,port))

print(data)
 #data = "Error: Traceback send failed"
c.sendall(data.encode())
c.close()

file = open('marvel.jpg','rb')
raw_data = file.read(1024)
while (raw_data):
       s.send(raw_data)
       raw_data = f.read(1024)
f.close()
s.close      