from tkinter import *
# from tkinter.ttk import Frame, Button, Entry, Style

# create a window

# create event handling


class Calculator(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        self.init_calculator()

    def init_calculator(self):
        self.master.title("Calculator")

        # create buttons in grid
        # 1.number and dot; 2.operation; 3.result and clear

        # 1st Row to display
        entry = Entry(width=40)
        entry.grid(row=0, columnspan=4)

        # 2nd Row: Clear as C or EC, Back
        ec = Button(text='EC/C', width=20)
        ec.grid(row=1, column=0, columnspan=2)
        back = Button(text='Back', width=20)
        back.grid(row=1, column=2, columnspan=2)

        # 3rd Row: 7, 8, 9 , +
        num7 = Button(text='7', width=10)
        num7.grid(row=2, column=0)
        num8 = Button(text='8', width=10)
        num8.grid(row=2, column=1)
        num9 = Button(text='9', width=10)
        num9.grid(row=2, column=2)
        op_add = Button(text='+', width=10)
        op_add.grid(row=2, column=3)

        # 4th Row: 4, 5, 6, -
        num4 = Button(text='4', width=10)
        num4.grid(row=3, column=0)
        num5 = Button(text='5', width=10)
        num5.grid(row=3, column=1)
        num6 = Button(text='6', width=10)
        num6.grid(row=3, column=2)
        op_sub = Button(text='-', width=10)
        op_sub.grid(row=3, column=3)

        # 5th Row: 1, 2, 3, *
        num1 = Button(text='1', width=10)
        num1.grid(row=4, column=0)
        num2 = Button(text='2', width=10)
        num2.grid(row=4, column=1)
        num3 = Button(text='3', width=10)
        num3.grid(row=4, column=2)
        op_mul = Button(text='*', width=10)
        op_mul.grid(row=4, column=3)

        # 6th Row: 0, ., =, /
        op_dot = Button(text='.', width=10)
        op_dot.grid(row=5, column=0)
        num0 = Button(text='0', width=10)
        num0.grid(row=5, column=1)
        op_equal = Button(text='=', width=10)
        op_equal.grid(row=5, column=2)
        op_div = Button(text='/', width=10)
        op_div.grid(row=5, column=3)

    # add functions to display numbers and calculate the result
    def clear(self):
        return True

    def back(self):
        return True

    def numbers(self):
        return True

    def operations(self):
        return True

root = Tk()
app = Calculator(root)
root.mainloop()