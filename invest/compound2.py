import tkinter as tk

root = tk.Tk()

principal = 0

def btn_cmd(obj):

    #use global variable
    global principal
    #print its unmodified value
    print("aVarOutside: " + str(principal))
    #modify it with what's written in Entry widget
    principal = obj.get()

    #modify lblTextVar, which is essentially modifying Label's text as lblTextVar is its textvariable
    lblTextVar.set(obj.get())

    #print what's inside Entry
    print("Entry: " + obj.get())

txt = tk.Entry(root)
txt.pack()

lblTextVar = tk.StringVar()
lbl = tk.Label(root, textvariable=lblTextVar)
lbl.pack()

btn = tk.Button(text="Calculate", command=lambda obj = txt : btn_cmd(obj))
btn.pack()

root.mainloop()