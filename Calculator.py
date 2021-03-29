from tkinter import *

root = Tk()
root.title("Calculator")

FirstNumber = 0
Signal = None
Answer = "Unused"
i = 0

Number1 = Entry(root, width = 45, borderwidth = 0)
Number1.grid(row = 0,column=0, columnspan = 3, padx = 10, pady = 10)
Number2 = Entry(root, width = 45, borderwidth = 5)
Number2.grid(row = 1,column=0, columnspan = 3, padx = 10, pady = 10)

def Add():
    global Result
    Result = float(FirstNumber) + float(Number2.get())
    Number2.delete(0, END)
    Number2.insert(0, Result)

def Minus():
    global Result
    Result = float(FirstNumber) - float(Number2.get())
    Number2.delete(0, END)
    Number2.insert(0, Result)

def Multiply():
    global Result
    Result = float(FirstNumber) * float(Number2.get())
    Number2.delete(0, END)
    Number2.insert(0, Result)

def Divide():
    global Result
    Result = float(FirstNumber) / float(Number2.get())
    Number2.delete(0, END)
    Number2.insert(0, Result)

def button_click(number):

    current = Number1.get()
    Number1.delete(0, END)
    Number1.insert(0, str(current) + str(number))

    current = Number2.get()
    Number2.delete(0, END)
    Number2.insert(0, str(current) + str(number))

def button_clear():
    Number1.delete(0, END)
    Number2.delete(0, END)
    global FirstNumber
    global Signal
    global Answer
    global i
    FirstNumber = 0
    Signal = None
    Answer = "Unused"
    i = 0

def button_operation(signal):
    global Result
    global i

    if (i != 0):
        Number1.delete(0, END)
        Number1.insert(0, Result)
       
    i += 1

    global Signal
    global FirstNumber

    FirstNumber = Number1.get()
    Number1.delete(0, END)
    Number2.delete(0, END)
    Signal = signal
    Number1.insert(0, str(FirstNumber) + " " + str(signal) + " ")

def equal():
    if(str(Signal) == "+"):
        Add()

    elif(str(Signal) == "-"):
        Minus()

    elif(str(Signal) == "X"):
        Multiply()

    elif(str(Signal) == "/"):
        Divide()


button0 = Button(root, text="0", padx = 90, pady = 20, command = lambda: button_click(0), bg="#272829", fg="white")
button1 = Button(root, text="1", padx = 40, pady = 20, command = lambda: button_click(1), bg="#272829", fg="white")
button2 = Button(root, text="2", padx = 40, pady = 20, command = lambda: button_click(2), bg="#272829", fg="white")
button3 = Button(root, text="3", padx = 40, pady = 20, command = lambda: button_click(3), bg="#272829", fg="white")
button4 = Button(root, text="4", padx = 40, pady = 20, command = lambda: button_click(4), bg="#272829", fg="white")
button5 = Button(root, text="5", padx = 40, pady = 20, command = lambda: button_click(5), bg="#272829", fg="white")
button6 = Button(root, text="6", padx = 40, pady = 20, command = lambda: button_click(6), bg="#272829", fg="white")
button7 = Button(root, text="7", padx = 40, pady = 20, command = lambda: button_click(7), bg="#272829", fg="white")
button8 = Button(root, text="8", padx = 40, pady = 20, command = lambda: button_click(8), bg="#272829", fg="white")
button9 = Button(root, text="9", padx = 40, pady = 20, command = lambda: button_click(9), bg="#272829", fg="white")

buttonDot = Button(root, text=".", padx = 40, pady = 20, command = lambda: button_click("."), bg="#272829", fg="white")

buttonEqual = Button(root, text="=", padx = 39, pady = 20, command = equal, bg="#272829", fg="white")

buttonClear = Button(root, text="C", padx = 39, pady = 20, command = button_clear, bg="#272829", fg="white")

PlusButton = Button(root, text="+", padx = 39, pady = 20, bg="#272829", fg="white", command=lambda: button_operation("+"))
MinusButton = Button(root, text="-", padx = 39, pady = 20, bg="#272829", fg="white", command=lambda: button_operation("-"))
MultiButton = Button(root, text="X", padx = 39, pady = 20, bg="#272829", fg="white", command=lambda: button_operation("X"))
DivButton = Button(root, text="/", padx = 39, pady = 20, bg="#272829", fg="white", command=lambda: button_operation("/"))

button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button1.grid(row = 4, column = 0)
button2.grid(row = 4, column = 1)
button3.grid(row = 4, column = 2)
button0.grid(row = 5, column = 0, columnspan = 2)
buttonDot.grid(row = 6, column = 0)
buttonEqual.grid(row = 6, column = 1)
buttonClear.grid(row = 6, column = 2)

PlusButton.grid(row = 2, column = 4)
MinusButton.grid(row = 3, column = 4)
MultiButton.grid(row = 4, column = 4)
DivButton.grid(row = 5, column = 4)

root.mainloop()