import tkinter as tk

root = tk.Tk()

aVarOutside = 'asd'
def btn_cmd(obj):

    #use global variable
    global aVarOutside
    #print its unmodified value
    print("aVarOutside: " + aVarOutside)
    #modify it with what's written in Entry widget
    aVarOutside = obj.get()

    #modify lblTextVar, which is essentially modifying Label's text as lblTextVar is its textvariable
    lblTextVar.set(obj.get())

    #print what's inside Entry
    print("Entry: " + obj.get())

txt = tk.Entry(root)
txt.pack()

lblTextVar = tk.StringVar()
lbl = tk.Label(root, textvariable=lblTextVar)
lbl.pack()

btn = tk.Button(text="Submit", command=lambda obj = txt : btn_cmd(obj))
btn.pack()

root.mainloop()