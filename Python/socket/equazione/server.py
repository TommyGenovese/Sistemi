import socket
IpAddress = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))

while(True):
    #invio del messaggio
    #msg = input("inserisci il messaggio da inviare:")
    #srv.sendto(msg.encode(),(IpAddress,port))
    #if str(msg) == "$stop":
    #    break

    #ricezione del messaggio
    data, address = srv.recvfrom(8036)
    print(f"msg from client: {data}")
    
    #invio messaggio di conferma
    if data:
        sent = srv.sendto(data, address)
        print (f"sent {data} bytes back to {IpAddress}")

    raw_data, address = srv.recvfrom(4096)   #saving data and address 

    if(data.decode()[1:] == "$stop"): 
        break

    equation = eval(data.decode()[0:])  #compute the equation excluting initial 'b'

    print( str(address) + "msg: " + raw_data.decode()[0:] + " = " + str(equation))    

    srv.sendto(str(equation).encode(), address) 

srv.close()