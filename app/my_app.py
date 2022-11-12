from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('My First App')
root.iconbitmap('smile.ico')

my_img = ImageTk.PhotoImage(Image.open('images/matt.png'))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text='Exit', command=root.quit)
button_quit.pack()

root.mainloop()