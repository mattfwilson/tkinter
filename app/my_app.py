from tkinter import *
from PIL import ImageTk, Image

def main():
    root = Tk()
    root.title('The App of Matt')
    root.iconbitmap('smile.ico')

    my_img = ImageTk.PhotoImage(Image.open('images/matt.png'))
    my_label = Label(image=my_img)
    my_label.pack()

    button_quit = Button(root, text='Exit', command=root.quit)
    button_quit.pack()

    root.mainloop()

if __name__ == '__main__':
    main()