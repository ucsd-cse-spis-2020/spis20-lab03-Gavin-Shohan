import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.
       :return: a tuple containing the Turtle and the Screen
       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()
   
    
    hurricaneFile = "data/franklin.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)

        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator

        next(pointreader)

        # Moves the turtle to start of hurricane. In seperate for loop to reduce overhead. Couldn't figure out how to read csv file without for loop.
        for row in pointreader:
            t.hideturtle()
            t.penup()
            t.setpos(float(row[3]),float(row[2])) 
            t.showturtle()
            t.pendown()
            print("Date:", row[0], "Time:", row[1])   
            break
        

        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            cCheck = categoryCheck(float(row[4]))


            #executes based on category of the hurricane
            if (cCheck == 0):
                t.pencolor("white")
                t.pensize(1)
            elif (cCheck == 1):
                t.pencolor("blue")
                t.write("1", False, align="center")
                t.pensize(2)
                
            elif (cCheck == 2):
                t.pencolor("green")
                t.write("2", False, align="center")
                t.pensize(4)
                
            elif (cCheck == 3):
                t.pencolor("yellow")
                t.write("3", False, align="center")
                t.pensize(6)
               
            elif (cCheck == 4):
                t.pencolor("orange")
                t.write("4", False, align="center")
                t.pensize(8)
                
            elif (cCheck == 5):
                t.pencolor("red")
                t.write("5", False, align="center")
                t.pensize(11)
                
            # Hurricane tracing
            t.setpos(float(row[3]),float(row[2]))  

            #defaulting pensize for writing numbers
            t.pensize(2)
              

            print("Date:", row[0], "Time:", row[1])



    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img

def categoryCheck(windSpeed):
    """ returns a hurricane category number based on wind speed """

    if(windSpeed < 74):
        return 0
    elif (74 <= windSpeed < 96):
        return 1
    elif (96 <= windSpeed < 111):
        return 2
    elif (111 <= windSpeed < 130):
        return 3
    elif (130 <= windSpeed < 157):
        return 4
    elif (windSpeed >= 157):
        return 5
        


# Feel free to add "helper" functions here


if __name__ == "__main__":
    bg=irma()

""" 

for replit testing

def infinity():
    while 1 == 1:  
        turtle.forward(100)
        turtle.backward(100)

infinity() 

"""
