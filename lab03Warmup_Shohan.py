# Shohan Ramesh - program to draw the first letter of my name.

import turtle


def drawPicture(theTurtle):

    ''' Draw a simple square using a turtle '''

    theTurtle.forward(100)

    theTurtle.left(90)

    theTurtle.forward(100)

    theTurtle.left(90)

    theTurtle.forward(100)

    theTurtle.left(90)

    theTurtle.forward(100)

    theTurtle.left(90)   
     



myTurtle = turtle.Turtle()  # Create a new Turtle object

drawPicture(myTurtle)   # make the new Turtle draw the shape

# initializes two turtle objects
turtle1 = turtle.Turtle()

turtle2 = turtle.Turtle()

#sets the two turtle positions

turtle1.setpos(-50, -50)

turtle2.setpos(200, 100)

#moves turtle one forward

turtle1.forward(100)

#turns turtle two left ninety degrees and moves it forward

turtle2.left(90)

turtle2.forward(100)