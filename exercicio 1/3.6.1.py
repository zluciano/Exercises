import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

for i in range(0, 3):
    alex.forward(100)
    alex.left(360/3)

turtle.mainloop()