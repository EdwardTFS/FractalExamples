import turtle

def koch_fract(turtle, divis, size):
    if divis == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(turtle, divis - 1, size / 3)
            turtle.left(angle)


t = turtle.Turtle()
t.hideturtle()
t.speed(0)

for i in range(3):
    koch_fract(t, 5, 300.0)
    t.left(-120)

turtle.mainloop()