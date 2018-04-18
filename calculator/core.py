#!/usr/bin/env python3
from Tkinter import *

# gerer operateurs specifiques python : ** et ^

class Window:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # TEXT AREA
        self.textarea = Entry(master, width=25)
        self.textarea.grid(row=0, column=0, columnspan=3)
        # NUMBERS
        self.numbers = {}
        self.numbers[0] = Button(master, command=lambda:self.printNumber(7), text=7, width=5, height=4).grid(row=1, column=0)
        self.numbers[1] = Button(master, command=lambda:self.printNumber(8), text=8, width=5, height=4).grid(row=1, column=1)
        self.numbers[2] = Button(master, command=lambda:self.printNumber(9), text=9, width=5, height=4).grid(row=1, column=2)
        self.numbers[3] = Button(master, command=lambda:self.printNumber(4), text=4, width=5, height=4).grid(row=2, column=0)
        self.numbers[4] = Button(master, command=lambda:self.printNumber(5), text=5, width=5, height=4).grid(row=2, column=1)
        self.numbers[5] = Button(master, command=lambda:self.printNumber(6), text=6, width=5, height=4).grid(row=2, column=2)
        self.numbers[6] = Button(master, command=lambda:self.printNumber(1), text=1, width=5, height=4).grid(row=3, column=0)
        self.numbers[7] = Button(master, command=lambda:self.printNumber(2), text=2, width=5, height=4).grid(row=3, column=1)
        self.numbers[8] = Button(master, command=lambda:self.printNumber(3), text=3, width=5, height=4).grid(row=3, column=2)
        self.numbers[9] = Button(master, command=lambda:self.printNumber(0), text=0, width=5, height=4).grid(row=4, column=1)
        # SYMBOLS
        self.symbols = {}
        self.symbols[0] = Button(master, command=lambda:self.operation('/'), text="/", width=5, height=4).grid(row=1, column=4)
        self.symbols[1] = Button(master, command=lambda:self.operation('*'), text="x", width=5, height=4).grid(row=2, column=4)
        self.symbols[2] = Button(master, command=lambda:self.operation('-'), text="-", width=5, height=4).grid(row=3, column=4)
        self.symbols[3] = Button(master, command=lambda:self.operation('+'), text="+", width=5, height=4).grid(row=4, column=4)
        self.symbols[4] = Button(master, command=lambda:self.operation('='), text="=", width=5, height=4).grid(row=4, column=2)

        self.divZero = False
        self.newOperation = True
        self.firstNumber = None
        self.secondNumber = None
        self.result = None
        self.symbol = None

    def printNumber(self, number):
        val = self.textarea.get()
        print(val)
        if val.isalpha():
            self.textarea.delete(0, END)
            self.textarea.insert(0, str(number))
        else:
            self.textarea.delete(0, END)
            self.textarea.insert(0, val+str(number))

    def operation(self, symbol):
        if self.symbol == None:
            self.symbol = symbol
        if self.newOperation == True:
            self.firstNumber = int(self.textarea.get())
            self.textarea.delete(0, END)
            self.newOperation = False
            return
        else:
            self.secondNumber = int(self.textarea.get())
            self.textarea.delete(0, END)
            if self.symbol=='/':
                if self.secondNumber==0:
                    self.divZero = True         # raise exception error
                else:
                    self.firstNumber /= self.secondNumber
            if self.symbol=='*':
                self.firstNumber *= self.secondNumber
            if self.symbol=='-':
                self.firstNumber -= self.secondNumber
            if self.symbol=='+':
                self.firstNumber += self.secondNumber
            self.symbol = symbol
            if self.symbol=='=':
                if self.divZero==False:
                    self.result = self.firstNumber
                    self.textarea.insert(0, self.result)
                else:
                    self.textarea.insert(0, "Division par zero impossible")
                    # self.newOperation = True
                    self.divZero = False
                self.newOperation = True
                self.symbol = None
        print(self.firstNumber)

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()
