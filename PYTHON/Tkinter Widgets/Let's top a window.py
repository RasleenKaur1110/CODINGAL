from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main Window")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Toplevel Window")
    
    label_top = Label(top, text="This is a toplevel window")
    label_top.pack()

label_root = Label(root, text="This is the root window")
btn = Button(root, text="Click here to open another window", command=topwin)

label_root.pack()
btn.pack()

root.mainloop()

