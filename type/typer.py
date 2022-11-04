from tkinter import *

root = Tk()

# label1 = Label(root, text='Welcome to Typer')
# label2 = Label(root, text='We are all plebs in this world.')

# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, 'Enter your name')

def myClick():
    hello = 'Hello, ' + entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

button1 = Button(root, text='Submit', padx=50, pady=20, command=myClick)
button1.pack()

root.mainloop()
