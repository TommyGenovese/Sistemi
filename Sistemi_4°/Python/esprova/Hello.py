import turtle
import time

giocatori = []

for i in range(0,10):
    giocatori[i]= turtle.Turtle()
    giocatori[i].forward(10*i)
    time.sleep(1)

