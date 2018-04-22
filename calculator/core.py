#!/usr/bin/env python3
from Tkinter import *
import math

# gerer operateurs specifiques python : ** et ^

class Window:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # TEXT AREA
        self.textarea = Entry(master, font=('Verdana',40), width=10)
        self.textarea.grid(row=0, column=0, columnspan=5)
        # CLEAR BUTTON
        self.clear = Button(master, command=lambda:self.clearEntry(), text='C', width=5, height=4).grid(row=0, column=5)
        # NUMBERS
        self.numbers = {}
        self.numbers[0] = Button(master, command=lambda:self.printEntry(7), text=7, width=5, height=4)
        self.numbers[1] = Button(master, command=lambda:self.printEntry(8), text=8, width=5, height=4)
        self.numbers[2] = Button(master, command=lambda:self.printEntry(9), text=9, width=5, height=4)
        for i in range(0,3):
            self.numbers[i].grid(row=1,column=i)
        self.numbers[3] = Button(master, command=lambda:self.printEntry(4), text=4, width=5, height=4)
        self.numbers[4] = Button(master, command=lambda:self.printEntry(5), text=5, width=5, height=4)
        self.numbers[5] = Button(master, command=lambda:self.printEntry(6), text=6, width=5, height=4)
        for i in range(3,6):
            self.numbers[i].grid(row=2,column=i-3)
        self.numbers[6] = Button(master, command=lambda:self.printEntry(1), text=1, width=5, height=4)
        self.numbers[7] = Button(master, command=lambda:self.printEntry(2), text=2, width=5, height=4)
        self.numbers[8] = Button(master, command=lambda:self.printEntry(3), text=3, width=5, height=4)
        for i in range(6,9):
            self.numbers[i].grid(row=3,column=i-6)
        self.numbers[9] = Button(master, command=lambda:self.printEntry(0), text=0, width=5, height=4)
        self.numbers[9].grid(row=4, column=1)
        # LETTERS (FOR BASE 16)
        self.letters = {}
        self.letters[0] = Button(master, command=lambda:self.printEntry('a'), text='a', width=5, height=4)
        self.letters[1] = Button(master, command=lambda:self.printEntry('b'), text='b', width=5, height=4)
        self.letters[2] = Button(master, command=lambda:self.printEntry('c'), text='c', width=5, height=4)
        self.letters[3] = Button(master, command=lambda:self.printEntry('d'), text='d', width=5, height=4)
        self.letters[4] = Button(master, command=lambda:self.printEntry('e'), text='e', width=5, height=4)
        self.letters[5] = Button(master, command=lambda:self.printEntry('f'), text='f', width=5, height=4)
        for i in range(0,3):
            self.letters[i].grid(row=i+1,column=3)
        for i in range(3,6):
            self.letters[i].grid(row=i-2,column=4)
        [self.letters[x].config(state="disabled") for x in self.letters]
        # SYMBOLS
        self.symbols = {}
        self.symbols[0] = Button(master, command=lambda:self.operation('/'), text="/", width=5, height=4, bg='burlywood3')
        self.symbols[1] = Button(master, command=lambda:self.operation('*'), text="x", width=5, height=4, bg='burlywood3')
        self.symbols[2] = Button(master, command=lambda:self.operation('-'), text="-", width=5, height=4, bg='burlywood3')
        self.symbols[3] = Button(master, command=lambda:self.operation('+'), text="+", width=5, height=4, bg='burlywood3')
        self.symbols[4] = Button(master, command=lambda:self.operation('='), text="=", width=5, height=4, bg='coral1')
        self.symbols[4].grid(row=4, column=2)
        for i in range(4):
            self.symbols[i].grid(row=i+1, column=5)
        # ADVANCED FUNCTIONS
        self.functions = {}
        self.functions[0] = Button(master, command=lambda:self.printEntry('sin('), text="sin", width=5, height=4, bg='tan3').grid(row=0, column=6)
        self.functions[1] = Button(master, command=lambda:self.printEntry('cos('), text="cos", width=5, height=4, bg='tan3').grid(row=1, column=6)
        self.functions[2] = Button(master, command=lambda:self.printEntry('tan('), text="tan", width=5, height=4, bg='tan3').grid(row=2, column=6)
        self.functions[3] = Button(master, command=lambda:self.printEntry('^'), text="^", width=5, height=4, bg='tan3').grid(row=4, column=3)
        self.functions[4] = Button(master, command=lambda:self.printEntry('e('), text="e", width=5, height=4, bg='tan3').grid(row=4, column=4)
        self.functions[5] = Button(master, command=lambda:self.printEntry('3.14159265359'), text="PI", width=5, height=4, bg='tan3').grid(row=3, column=6)
        self.functions[6] = Button(master, command=lambda:self.printEntry('log('), text="log", width=5, height=4, bg='tan3').grid(row=4, column=6)
        # BASES
        self.bases = {}
        self.bases[0] = Button(master, command=lambda:self.changeBase('2'), text="B2", width=5, height=4, bg='tan4').grid(row=0, column=8)
        self.bases[1] = Button(master, command=lambda:self.changeBase('4'), text="B4", width=5, height=4, bg='tan4').grid(row=1, column=8)
        self.bases[1] = Button(master, command=lambda:self.changeBase('8'), text="B8", width=5, height=4, bg='tan4').grid(row=2, column=8)
        self.bases[2] = Button(master, command=lambda:self.changeBase('10'), text="B10", width=5, height=4, bg='tan4').grid(row=3, column=8)
        self.bases[3] = Button(master, command=lambda:self.changeBase('16'), text="B16", width=5, height=4, bg='tan4').grid(row=4, column=8)
        # self.bases[4] = Button(master, command=lambda:self.operation('**'), text="**", width=5, height=4, bg='wheat2').grid(row=4, column=5)

        self.divZero = False
        self.newOperation = True
        self.firstNumber = None
        self.secondNumber = None
        self.base = 10
        self.result = None
        self.symbol = None

    def clearEntry(self):
        self.textarea.delete(0, END)
        self.firstNumber = None
        self.secondNumber = None
        self.result = None
        self.symbol = None

    def printEntry(self, number):
        val = self.textarea.get()
        # if val.isalpha():     # if "Division par zero" (a modifier a cause de base 16)
        #     self.textarea.delete(0, END)
        #     self.textarea.insert(0, str(number))
        # else:
        self.textarea.delete(0, END)
        self.textarea.insert(0, val+str(number))


    def operation(self, symbol):
        # self.firstNumber = str(self.firstNumber).replace(" ", "")
        if self.symbol == None:         # very first operation
            self.symbol = symbol
        if self.newOperation == True:   # new operation
            if self.isFloat(self.textarea.get().replace(" ", "")):
                self.firstNumber = float(self.textarea.get().replace(" ", ""))
            else:
                self.firstNumber = self.trigo()
            self.textarea.delete(0, END)
            self.newOperation = False
        else:
            if self.isFloat(self.textarea.get()):
                self.secondNumber = float(self.textarea.get().replace(" ", ""))
            else:
                self.secondNumber = self.trigo()
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
            # Advanced operations
                # print(self.textarea.split("("))
                # Result
        self.symbol = symbol
        if self.symbol=='=':
            self.printResult()

    def trigo(self):
        for i in self.textarea.get():
            if i == '(':
                function = self.textarea.get().split("(")
                n = float(function[1])
                if function[0] == 'sin':
                    return math.sin(math.radians(n))
                elif function[0] == 'cos':
                    return math.cos(math.radians(n))
                elif function[0] == 'tan':
                    return math.tan(math.radians(n))
                elif function[0] == 'e':
                    return math.exp(n)
                elif function[0] == 'log':
                    return math.log(n, 10)
            elif i == '^':
                function = self.textarea.get().split("^")
                return math.pow(float(function[0]), float(function[1]))


    def printResult(self):
        if self.divZero==False:
            print(1)
            self.result = self.firstNumber
            self.textarea.insert(0, self.result)
        else:
            self.textarea.insert(0, "Division par zero impossible")
            # self.newOperation = True
            self.divZero = False
        self.newOperation = True
        self.symbol = None

    def changeBase(self, base):
        if self.base == None:
            self.base = base
        else:
            if base == '2':
                ([self.numbers[x].config(state="disabled") if x!=9 and x!=6 else self.numbers[x].config(state="normal") for x in self.numbers])
                ([self.letters[x].config(state="disabled") for x in self.letters])
            if base == '4':
                ([self.numbers[x].config(state="disabled") if x<6 else self.numbers[x].config(state="normal") for x in self.numbers])
                ([self.letters[x].config(state="disabled") for x in self.letters])
            if base == '8':
                ([self.numbers[x].config(state="disabled") if x==1 or x==2 else self.numbers[x].config(state="normal") for x in self.numbers])
                ([self.letters[x].config(state="disabled") for x in self.letters])
            if base == '10':
                ([self.numbers[x].config(state="normal") for x in self.numbers if x<6])
                ([self.letters[x].config(state="disabled") for x in self.letters])
            if base == '16':
                ([self.numbers[x].config(state="normal") for x in self.numbers])
                ([self.letters[x].config(state="normal") for x in self.letters])
            self.convertBase(self.base, base)
            self.base = base

    def convertBase(self, curBase, newBase):
        # from superior base to inferior base:
        # current number % newBase = unit
        # current number / newBase = ten
        ten = float(self.textarea.get()) % float(newBase)
        unit = float(self.textarea.get()) / float(newBase)
        self.textarea.delete(0, END)
        self.textarea.insert(0, str(unit)+str(ten))

    def isFloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def isInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = Tk()
    my_gui = Window(root)
    root.mainloop()
