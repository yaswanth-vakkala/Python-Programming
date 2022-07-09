import turtle
import random

w = turtle.Screen()
w.title("turtle graphics")
w.bgcolor("light cyan")
colors = ['red', 'blue', 'cyan', 'purple', 'black', 'grey', 'orange', 'yellow']

turtle = turtle.Turtle()
turtle.pensize(5)
turtle.speed(0)
for x in range(50):
    rcolor = random.randrange(0, len(colors))
    turtle.color(colors[rcolor],colors[random.randrange(0, len(colors))])
    r1= random.randrange(-350, 350)
    r2 = random.randrange(-350, 350)
    turtle.penup()
    turtle.setpos((r1, r2))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(random.randrange(0, 80))
    turtle.end_fill()

'''
turtle = turtle.Turtle()
turtle.color('red', 'green')
turtle.pensize(5)

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.color('yellow', 'black')
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
'''