import turtle

wn = turtle.Screen()

alex = turtle.Turtle()
alex.left(72)

for i in range(0, 5):
    alex.forward(100)
    alex.right(180-36)

turtle.mainloop()