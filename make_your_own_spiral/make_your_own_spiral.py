# make your own spiral

import turtle
import tkSimpleDialog
t = turtle.Pen()
turtle.bgcolor ("black")
t.speed(0)
colors = ["red", "blue", "green", "orange", "yellow", "purple", "gold", "pink"]
sides = tkSimpleDialog.askinteger ("number of sides",
                                  "enter in how many sides you want 1-8" )

for x in range (360):
    t.pencolor (colors [x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
q=input("press close to exit")