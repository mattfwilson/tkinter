import tkinter as tk

root = tk.Tk()
root.geometry("250x120")
root.title('Calculatorer 2.0')
principal_label = 0

def show_principal(obj):
    global principal_label

    print("Default: " + str(principal_label))
    print("Entry: " + obj.get())

    #modify it with what's written in Entry widget
    principal_label = obj.get()

    #modify principal, which is essentially modifying Label's text as principal is its textvariable
    principal.set(obj.get())

entry = tk.Entry(root)
entry.pack()
entry.place(x=40, y=35)

submit = tk.Button(text="Submit", command=lambda obj=entry : show_principal(obj))
submit.pack()
submit.place(x=170, y=32)

principal = tk.StringVar()
prince_label = tk.Label(root, textvariable=principal)
prince_label.pack(padx=10, pady=40, side=tk.BOTTOM)

root.mainloop()