# I can say your name in turtle graphics

import turtle
import tkSimpleDialog

t = turtle.Pen()
turtle.bgcolor("black")
t.pencolor("green")
your_name =tkSimpleDialog.askstring('what is your name?', 'enter in your name')
t.write("hi " + your_name, font=("times", int(15)))
t.right(90)
for x in range (10):
    t.penup()
    t.forward(30)
    t.pendown()
    t.write("hi " + your_name, font = ("times",int(15)))
    t.penup()
    t.pendown()
t.penup()
t.forward(30)
t.pendown()
t.write("did i say your name too many times?", font = ("times", int(15)))

q = raw_input("press close to exit")
