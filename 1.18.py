#!user/bin/python3

import turtle

turtle.showturtle()


def drawAngle(length, angle):
    turtle.forward(length)
    turtle.right(angle)
    turtle.forward(length)


x = 1
while(x <= 5):
    drawAngle(50, 144)
    x = x + 1

turtle.done()
