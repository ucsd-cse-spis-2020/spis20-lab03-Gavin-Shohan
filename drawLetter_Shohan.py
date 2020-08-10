import turtle

def drawS(theTurtle):

    theTurtle.penup()
    theTurtle.setpos(50,50)
    theTurtle.pendown()

    theTurtle.left(90)

    for x in range(1,27):
        theTurtle.forward(10)
        theTurtle.left(10)

    theTurtle.forward(10)

    for x in range(1,27):
        theTurtle.forward(10)
        theTurtle.right(10)

myTurtle = turtle.Turtle()

drawS(myTurtle)

