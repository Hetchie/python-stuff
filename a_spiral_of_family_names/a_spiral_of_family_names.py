# a spiral of family names
awnser = raw_input("want to see a spiral? yes or no\n")
if awnser == "yes":
    print "working..."

    import turtle
    import tkSimpleDialog
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor ("black")
    colors = ["pink", "green", "red", "brown", "salmon", "yellow", "gold", "silver", "blue", "purple"]

    family = []
    name = tkSimpleDialog.askstring("family name", "enter in a name, or press [ENTER] to end")

    while name != "":
        family.append(name)
        name = tkSimpleDialog.askstring("family name", "enter in a name, or press [ENTER] to end")


    for x in range(100):
        t.penup()
        t.forward(x*5)
        position = t.position()
        heading = t.heading()
        print (position, heading)

        for y in range(len(family)):
            t.pendown()
            t.width(x/20)
            t.pencolor(colors[y%len(family)%10])
            t.write(family[y%len(family)], font = ("arial",  int((x + 4)/4), "bold"))
            t.right(360 / len(family))
            t.penup()
            t.forward (x//2)
        t.setx(position[0])
        t.sety(position[1])
        t.setheading(heading)
        t.left(360 / len(family) + 3)

else:
    print"thanks for visiting!"