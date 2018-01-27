import turtle
import tkSimpleDialog
import random

t = turtle.Pen()
t.speed(0)
turtle.bgcolor ("black")
number_of_circles = tkSimpleDialog.askinteger("number of circles", "enter in how many cicles you want (1 - 360)")
for x in range(number_of_circles):
    t.pencolor("red")
    t.circle(100)
    t.left(360/number_of_circles)
    t.pencolor("yellow")
    t.circle(50)
    t.left(360/number_of_circles)
q = raw_input("press q to exit")
