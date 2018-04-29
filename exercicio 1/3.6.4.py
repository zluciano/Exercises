import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

for i in range(0, 8):
    alex.forward(100)
    alex.left(360/8)

turtle.mainloop()