import socket

server_ip = "192.168.0.118" 
server_ip_personal = "192.168.0.119"
port = 7000
file = open('marvel.jpg', 'wb')


def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.bind((server_ip_personal,port))
    s.listen()
    c,address = s.accept()

    raw_data = c.recv(4096)

    while(raw_data):
        file.write(l)
        raw_data=c.recv(4096)
    
    file.close()
    c.close()


if __name__ == "__main__":
    server()