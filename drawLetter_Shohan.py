
#Shohan Ramesh - program to draw the first letter of my name.
import turtle


def drawS(theTurtle):
    """draws an S using the turtle object"""

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

