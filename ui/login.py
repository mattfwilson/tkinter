import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry('600x400')

def login():
    print(entry1)
    print(entry27)

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20,
    padx=100,
    fill='both',
    expand='True',)

label = ctk.CTkLabel(master=frame, text='Login System', justify='right')
label.pack(pady=12, padx=100)

entry1 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Username')
entry1.pack(pady=12, padx=0)

entry2 = ctk.CTkEntry(master=frame, width=200, placeholder_text='Password')
entry2.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, width=100, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me?')
checkbox.pack(pady=12, padx=10)

root.mainloop()