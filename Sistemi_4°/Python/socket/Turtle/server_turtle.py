import turtle
import socket
import time
IpAddress = 'localhost'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress,port))
IpGioc=[]
giocatore = "giocatore"

while(True):
    #ottengo il movimento (w,a,s,d) e l'address
    movimento, address = srv.recvfrom(8036)
    movimento= movimento.split("=")
    #movimento:    x=n

    #controllo se c'è un nuovo giocatore
    for i in len(IpGioc):
        if(address != IpGioc):
            IpGioc.append(address)
            if i==0:
                sally = turtle.Turtle()
            if i==1:
                sandy = turtle.Turtle()
            if i==2:
                sasha = turtle.Turtle()
    
    #controllo chi ha inviato il comando
    for i in len(IpGioc):
        if(IpGioc[i]== address):
            if(movimento[0] == "w" or movimento[0] == "W"):
                sally.forward(movimento[1])
            if(movimento[0] == "S" or movimento[0] == "s"):
                sally.backward(movimento[1])
            if(movimento[0] == "a" or movimento[0] == "A"):
                sally.left(movimento[1])
            if(movimento[0] == "d" or movimento[0] == "D"):
                sally.right(movimento[1])

        



    
