import turtle

def drawG(theTurtle):
    theTurtle.left(90)
    for x in range(0,100):
        theTurtle.left(10)
        theTurtle.forward(10)
        
myTurtle = turtle.Turtle()

drawG(myTurtle)


def infinity():
    turtle.penup()
    turtle.hideturtle()
    while (1==1):
        turtle.forward(10) 
        turtle.backward(10) 
infinity()