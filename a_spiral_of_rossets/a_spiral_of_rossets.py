
import turtle
import tkSimpleDialog
t = turtle.Pen()
t.speed(0)
t.penup()
turtle.bgcolor ("black")

sides = tkSimpleDialog.askinteger("number of circles", "enter in how many circles do you want  (1 - 8)")
colors = ["red", "orange", "yellow", "pink", "purple", "blue", "green", "salmon" ]
t.width(2)
for x in range(100):

    t.forward((x*4))
    position = t.position()
    heading = t.heading()
    print(position, heading)

    for y in range(sides):
        t.pendown()
        t.pencolor(colors[y%sides])
        t.circle(x/5)
        t.right(360/sides)
        t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides + 2)
q = quit()