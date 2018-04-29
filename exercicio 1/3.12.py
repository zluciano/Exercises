import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.penup()

alex.stamp()


for i in range(0, 12):
    alex.forward(100)
    alex.pendown()
    alex.forward(10)
    alex.penup()
    alex.forward(15)
    alex.stamp()
    alex.back(125)
    alex.left(30)

turtle.mainloop()