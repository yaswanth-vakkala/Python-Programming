from tkinter import *

main = Tk(className="Calculator")
# main.minsize(345,450)
# main.maxsize(345,450)
mainHeight = main.winfo_height()
mainWidth = main.winfo_width()

def createButton(text):
    return Button(main,text=text,width=11,height=2)

e = Entry(main,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

one = createButton("1")
two = createButton("2")
three = createButton("3")
four = createButton("4")
five = createButton("5")
six = createButton("6")
seven = createButton("7")
eight = createButton("8")
nine = createButton("9")
zero = createButton("0")
clear = createButton("C")
add = createButton("+")
subtract = createButton("-")
multiply = createButton("x")
divide = createButton("/")
equals = createButton("=")

one.grid(row=0,column=0)
two.grid(row=0,column=1)
three.grid(row=0,column=2)
add.grid(row=0,column=3)
four.grid(row=1,column=0)
five.grid(row=1,column=1)
six.grid(row=1,column=2)
subtract.grid(row=1,column=3)
seven.grid(row=2,column=0)
eight.grid(row=2,column=1)
nine.grid(row=2,column=2)
multiply.grid(row=2,column=3)
zero.grid(row=3,column=0)
clear.grid(row=3,column=1)
equals.grid(row=3,column=2)
divide.grid(row=3,column=3)



main.mainloop()