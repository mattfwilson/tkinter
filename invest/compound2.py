import tkinter as tk

principal = 0

def main():

    root = tk.Tk()
    root.title('Calculatorer')

    txt = tk.Entry(root)
    txt.pack()

    lblTextVar = tk.StringVar()
    lbl = tk.Label(root, textvariable=lblTextVar)
    lbl.pack()

    btn = tk.Button(text="Calculate", command=lambda obj = txt : btn_cmd(obj, lblTextVar))
    btn.pack()

    root.mainloop()

def btn_cmd(obj, labelText):

    global principal

    print("aVarOutside: " + str(principal))
    principal = obj.get()
    labelText.set(obj.get())
    print("Entry: " + obj.get())

if __name__ == '__main__':
    main()