import socket 
import threading

IpAddress = 'localhost'
port = 6006

ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser.bind((IpAddress, port))

print(f"\n Server connesso  {IpAddress}: {port}")

def cliente(conn, ind_cli):
    while(True):
        data= conn.recv(4096)

        if(data.decode == "!Stop"):
            break

        print(str(ind_cli) + ":    " + data.decode())

        conn.sendall(data)

    ser.close()

clienti = []
while(True):
    ser.listen()
    conn, ind_cli = ser.accept()
    clienti.append(threading.Thread(target = cliente, args=(conn, ind_cli)))
    clienti[-1].start()
    for i in clienti:
        i.join()
    

