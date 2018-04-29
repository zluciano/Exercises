import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
wdth = 1
tess.width(wdth)

# The next functions are our "event handlers".
def h1():
   tess.color("red")

def h2():
   tess.color("green")

def h3():
   tess.color("blue")

def h4():
    global wdth
    wdth += 0.1
    tess.width(wdth)

def h5():
    global wdth
    if wdth >= 1.1:
        wdth -= 0.1
    tess.width(wdth)

def h6():
    tess.forward(20)

def h7():
    tess.back(20)

def h8():
    tess.right(30)

def h9():
    tess.left(30)

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "r")
wn.onkey(h2, "g")
wn.onkey(h3, "b")
wn.onkey(h4, "Up")
wn.onkey(h5, "Down")
wn.onkey(h6, "w")
wn.onkey(h7, "s")
wn.onkey(h8, "d")
wn.onkey(h9, "a")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()