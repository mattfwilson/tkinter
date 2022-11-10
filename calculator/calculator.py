from tkinter import *

root = Tk()
root.title('Calculatorer')

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(num))

def func_clear():
    entry.delete(0, END)

def func_add():
    num1 = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(num1)
    entry.delete(0, END)

def func_subtract():
    num1 = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(num1)
    entry.delete(0, END)

def func_multiply():
    num1 = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(num1)
    entry.delete(0, END)

def func_divide():
    num1 = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(num1)
    entry.delete(0, END)

def func_equal():
    second_num = entry.get()
    entry.delete(0, END)

    if math == 'addition':
        entry.insert(0, f_num + int(second_num))
    elif math == 'subtraction':
        entry.insert(0, f_num - int(second_num))
    elif math == 'multiplication':
        entry.insert(0, f_num * int(second_num))
    elif math == 'division':
        entry.insert(0, f_num / int(second_num))

# define buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text='+', padx=40, pady=20, command=func_add)
button_subtraction = Button(root, text='-', padx=40, pady=20, command=func_subtract)
button_multiplication = Button(root, text='*', padx=40, pady=20, command=func_multiply)
button_division = Button(root, text='/', padx=40, pady=20, command=func_divide)
button_equal = Button(root, text='=', padx=140, pady=20, command=func_equal)
button_clear = Button(root, text='Clear', padx=30, pady=20, command=func_clear)

# put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
button_addition.grid(row=4, column=1)
button_subtraction.grid(row=4, column=2)

button_clear.grid(row=5, column=0)
button_multiplication.grid(row=5, column=1)
button_division.grid(row=5, column=2)

button_equal.grid(row=6, column=0, columnspan=3)

root.mainloop()