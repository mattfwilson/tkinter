import tkinter as tk

principal = 0

def btn_cmd(obj, labelText):

    global principal

    if int(obj.get()) > 10000:
        print("Principal: " + str(principal))
        principal = obj.get()
        labelText.set(obj.get())
        print(f'You have {obj.get()} in principal and it is greater than 10000!')
    else:
        print(f'You have {obj.get()} in principal and it is lower than 10000...')

def main():

    root = tk.Tk()
    root.title('Compound Calculatorer 1.0')

    input_principal = tk.Entry(root)
    input_principal.pack()

    lblTextVar = tk.StringVar()
    lbl = tk.Label(root, textvariable=lblTextVar)
    lbl.pack()

    calc_btn = tk.Button(text="Calculate", command=lambda obj = input_principal : btn_cmd(obj, lblTextVar))
    calc_btn.pack()

    root.mainloop()

if __name__ == '__main__':
    main()