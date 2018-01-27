 # a spirsl of spirals

import turtle
import tkSimpleDialog
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor ("black")

sides = tkSimpleDialog.askinteger("number of sides", "enter in how many sides you want  (1 - 8)")
colors = ["red", "orange", "yellow", "pink", "purple", "blue", "green", "salmon" ]

for x in range(100):

    t.forward((x*4))
    position = t.position()
    heading = t.heading()
    print(position, heading)

    for y in range(int(x/2)):
        t.pendown()
        t.pencolor(colors[y%sides])
        t.forward(2*y)
        t.right(360/sides - 2)
        t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides + 2)