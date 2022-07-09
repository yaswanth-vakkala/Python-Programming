import turtle

w = turtle.Screen()
w.title("turtle graphics")
w.bgcolor("light grey")

a1 = turtle.Turtle()
a1.pensize(5)
a1.shape('arrow')
a1.color("black")
a1.forward(100)
a1.left(90)
a1.forward(100)
a1.left(90)
#a1.penup()
a1.color('green')
a1.forward(100)
a1.left(90)
#a1.pendown()
a1.forward(100)
a1.left(90)

turtle = turtle.Turtle()
turtle.setx(-200)
turtle.pensize(2)
turtle.color('blue')
turtle.speed(2000)

for r in range(26):
    turtle.left(r)
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)

turtle.setx(-200)
turtle.sety(200)
turtle.pensize(1)
turtle.color('red')
turtle.speed(100)

for r in range(26):
    turtle.left(r)
    for i in range(3):
        turtle.forward(60)
        turtle.left(120)
