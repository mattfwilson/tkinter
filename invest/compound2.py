import tkinter as tk

principal = 0

def btn_cmd(obj, labelText):

    global principal

    print("aVarOutside: " + str(principal))
    principal = obj.get()
    labelText.set(obj.get())
    print("Entry: " + obj.get())

def main():

    root = tk.Tk()
    root.title('Compound Calculatorer 1.0')

    input_text = tk.Entry(root)
    input_text.pack()

    lblTextVar = tk.StringVar()
    lbl = tk.Label(root, textvariable=lblTextVar)
    lbl.pack()

    calc_btn = tk.Button(text="Calculate", command=lambda obj = input_text : btn_cmd(obj, lblTextVar))
    calc_btn.pack()

    root.mainloop()

if __name__ == '__main__':
    main()