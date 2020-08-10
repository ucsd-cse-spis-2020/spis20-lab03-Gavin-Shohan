"""

1. What is the “anonymous turtle”?

A Turtle that python initializes automatically when no turtle object is created but turtle methods are being used. Used mostly when only one turtle is required for a program.

2. In the code below, what is the difference between turtle and Turtle()?

myTurtle = turtle.Turtle()

drawPicture(myTurtle)   

turtle is the library being called while Turtle() is the method that is initializing the turtle object.

Imagine that I have a turtle in a variable named myTurtle. What line of code will change that turtle’s y-position to 100?

myTurtle.sety(100)


"""

import turtle


def drawS(theTurtle,size):
    """draws an S using the turtle object. The size parameter is an integer that represents the scale factor of the letter"""

    theTurtle.penup()
    theTurtle.setpos(50,50)
    theTurtle.pendown()

    theTurtle.left(90)

    for x in range(1,27):
        theTurtle.forward(10*size)
        theTurtle.left(10)

    theTurtle.forward(10)

    for x in range(1,27):
        theTurtle.forward(10*size)
        theTurtle.right(10)

myTurtle = turtle.Turtle()

drawS(myTurtle,0.5)

