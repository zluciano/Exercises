import turtle

move_list = [(0, 50), (135, 70.7), (270, 35.35), (270, 35.35), (225, 50), (90, 50), (135, 70.7), (225, 50)]

wn = turtle.Screen()

alex = turtle.Turtle()

for (angle, step) in move_list:
    alex.left(angle)
    alex.forward(step)

wn.mainloop()