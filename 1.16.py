#!usr/bin/python3

'''
exercise 1.16
'''

import turtle


def drawCircle():
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()


turtle.showturtle()
turtle.penup()
turtle.goto(50, 50)
drawCircle()
turtle.goto(50, -50)
drawCircle()
turtle.goto(-50, 50)
drawCircle()
turtle.goto(-50, -50)
drawCircle()
turtle.done()
