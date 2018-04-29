import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

for i in range(0, 6):
    alex.forward(100)
    alex.left(360/6)

turtle.mainloop()