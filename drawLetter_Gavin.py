#Gavin Yuan - drawing first initial
import turtle


def drawG(theTurtle):
    """draws an G using the turtle"""

    theTurtle.penup()
    theTurtle.setpos(0,0)
    theTurtle.left(90)
    for x in range(0,63):
        if (x>9):
            theTurtle.pendown()
        theTurtle.left(5)
        theTurtle.forward(10)
    
    theTurtle.left(45)
    theTurtle.forward(79)
    theTurtle.left(90)
    theTurtle.forward(99)
    


myTurtle = turtle.Turtle()

drawG(myTurtle)

notMyTurtle=turtle.Turtle()

#notMyTurtle.penup()
#notMyTurtle.setpos(100,0)

drawG(notMyTurtle)
