import turtle

sally = turtle.Turtle()
movimento= "w=90"
print(movimento)
movimento= movimento.split("=")
if(movimento[0] == "w" or movimento[0] == "W"):
    sally.forward(movimento[1])
if(movimento[0] == "S" or movimento[0] == "s"):
    sally.backward(movimento[1])
if(movimento[0] == "a" or movimento[0] == "A"):
    sally.left(movimento[1])
if(movimento[0] == "d" or movimento[0] == "D"):
    sally.right(movimento[1])

