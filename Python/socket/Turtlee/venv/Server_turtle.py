import turtle
import socket
import time
IpAddress = '0.0.0.0'
port = 5004

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

srv.bind((IpAddress, port))
GIOCMAX=3
porte = []
for i in range(0,3):
    porte.append(0)

print(porte)


sally= turtle.Turtle()
sally.color('red')
sandy= turtle.Turtle()
sandy.color('blue')
sammy = turtle.Turtle()
sammy.color('green')

while (True):

    # ottengo il movimento (w,a,s,d) e l'address
    mov, address = srv.recvfrom(8036)
    movimento = mov.decode().split("=")
    movimento[1] = float(movimento[1])

    for i in range(0,3):
        if(porte[i]==0 and porte[0]!=address[1] and porte[1]!=address[1]):
            porte[i]= address[1]
            break

    if(porte[0]==address[1]):
        if (movimento[0] == "w" or movimento[0] == "W"):
            sally.forward(movimento[1])
        if (movimento[0] == "S" or movimento[0] == "s"):
            sally.backward(movimento[1])
        if (movimento[0] == "a" or movimento[0] == "A"):
            sally.left(movimento[1])
        if (movimento[0] == "d" or movimento[0] == "D"):
            sally.right(movimento[1])

    if (porte[1] == address[1]):
        if (movimento[0] == "w" or movimento[0] == "W"):
            sandy.forward(movimento[1])
        if (movimento[0] == "S" or movimento[0] == "s"):
            sandy.backward(movimento[1])
        if (movimento[0] == "a" or movimento[0] == "A"):
            sandy.left(movimento[1])
        if (movimento[0] == "d" or movimento[0] == "D"):
            sandy.right(movimento[1])

    if (porte[2] == address[1]):
        if (movimento[0] == "w" or movimento[0] == "W"):
            sammy.forward(movimento[1])
        if (movimento[0] == "S" or movimento[0] == "s"):
            sammy.backward(movimento[1])
        if (movimento[0] == "a" or movimento[0] == "A"):
            sammy.left(movimento[1])
        if (movimento[0] == "d" or movimento[0] == "D"):
            sammy.right(movimento[1])

    print(f"il giocatore {address[1]} fa: {movimento[0]} di {movimento[1]}")


srv.close()