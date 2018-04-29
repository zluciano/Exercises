import turtle

def draw_star(turtle):
    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")

draw_star(alex)

turtle.mainloop()