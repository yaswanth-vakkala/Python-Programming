import turtle
import random
from turtle import *

a = turtle.Turtle()
a.speed(0)
a.width(5)
a.shape('turtle')
colors = ['red', 'blue', 'cyan', 'purple', 'black', 'grey', 'orange', 'yellow', 'dark blue', 'green', 'violet', 'pink']

def up():
    a.color(colors[random.randrange(0, len(colors))])
    a.setheading(90)
    a.forward(100)

def down():
    a.color(colors[random.randrange(0, len(colors))])
    a.setheading(270)
    a.forward(100)

def left():
    a.color(colors[random.randrange(0, len(colors))])
    a.setheading(180)
    a.forward(100)

def right():
    a.color(colors[random.randrange(0, len(colors))])
    a.setheading(0)
    a.forward(100)

turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()