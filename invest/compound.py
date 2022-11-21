import tkinter as tk

root = tk.Tk()

root.title('Compount Interest Calculator')
root.geometry('350x100')

base_principal = 0
int_rate = tk.IntVar()

txt = tk.Entry(root)
txt.pack()

def btn_cmd(obj):

    #use global variable
    global base_principal

    #modify it with what's written in Entry widget
    base_principal = obj.get()

    #modify lblTextVar, which is essentially modifying Label's text as lblTextVar is its textvariable
    principal_num.set(obj.get())

    #print what's inside Entry
    print("Entry: " + obj.get())

def calc_int():
    principal = base_principal.get()
    interest = int_rate.get()

    print(f'Your principal is: {principal}.')
    print(f'Your interest rate is: {interest}.')

    base_principal.set('')
    int_rate.set('')

principal_num = tk.StringVar()
principal_entry = tk.Entry(root, textvariable=principal_num)
principal_entry.pack()

submit_btn = tk.Button(root, text="Calculate", command=lambda obj = txt : btn_cmd(obj))
submit_btn.pack()

# principal_label.grid(row=0, column=0)
# principal_entry.grid(row=0, column=1)
# interest_label.grid(row=1, column=0)
# interest_entry.grid(row=1, column=1)
# submit_button.grid(row=2, column=1)

root.mainloop()