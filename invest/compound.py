import tkinter as tk

root = tk.Tk()

root.title('Compount Interest Calculator')
root.geometry('350x100')

base_principal = tk.IntVar()
int_rate = tk.IntVar()

def calc_int():
    principal = base_principal.get()
    interest = int_rate.get()

    print(f'Your principal is: {principal}.')
    print(f'Your interest rate is: {interest}.')

    base_principal.set('')
    int_rate.set('')

principal_label = tk.Label(root, text='Principal Amount ($):', anchor='w')
principal_entry = tk.Entry(root, textvariable=base_principal,)

interest_label = tk.Label(root, text='Interest Rate (%):', anchor='w')
interest_entry = tk.Entry(root, textvariable=int_rate)

submit_button = tk.Button(root, text='Calculate', command='submit')

principal_label.grid(row=0, column=0)
principal_entry.grid(row=0, column=1)
interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1)
submit_button.grid(row=2, column=1)

root.mainloop()