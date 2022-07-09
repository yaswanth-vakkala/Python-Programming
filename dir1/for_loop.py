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

r = int(input("Enter no of rows: "))
for i in range(r):
    for j in range(i):
        print("#", end="")
    print() # to come to new line

s = input("Input the word you want to translate: ")
translation = ""
for l in s:
    if l.lower() in "aeiou":
        if l.isupper():
            translation = translation + "J"
        else:
            translation = translation + "j"
    else:
        translation = translation + l
print(translation)