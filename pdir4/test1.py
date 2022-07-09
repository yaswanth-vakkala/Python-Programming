from tkinter import *

main = Tk()
main.title("Calculator")

e = Entry(main,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

def clear():
    e.delete(0, END)

button_1 = Button(main, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = Button(main, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = Button(main, text="3", padx=40, pady=20, command=lambda: click(3))
button_4 = Button(main, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = Button(main, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = Button(main, text="6", padx=40, pady=20, command=lambda: click(6))
button_7 = Button(main, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = Button(main, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = Button(main, text="9", padx=40, pady=20, command=lambda: click(9))
button_0 = Button(main, text="0", padx=40, pady=20, command=lambda: click(0))
button_add = Button(main, text="+", padx=40, pady=20, command=add)
button_equal = Button(main, text="=", padx=40, pady=20, command=equal)
button_clear = Button(main, text="Clear", padx=130, pady=20, command=clear)

button_subtract = Button(main, text="-", padx=40, pady=20, command=subtract)
button_multiply = Button(main, text="*", padx=40, pady=20, command=multiply)
button_divide = Button(main, text="/", padx=40, pady=20, command=divide)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)

button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

button_clear.grid(row=6,columnspan=3)

main.mainloop()