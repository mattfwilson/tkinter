import tkinter as tk
 
root = tk.Tk()
root.geometry("300x170")

principal_input = tk.Text(root, height = 1, width = 25)
l = tk.Label(root, text = "Principal amount:")
l.config(font =("Courier", 12))
 
principal = 0
 
b1 = tk.Button(root, text = "Submit",)
b2 = tk.Button(root, text = "Exit", command = root.destroy)
 
l.pack()
principal_input.pack()
b1.pack()
b2.pack()
 
principal_input.insert(tk.END, principal)
tk.mainloop()