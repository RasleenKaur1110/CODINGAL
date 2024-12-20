from tkinter import *
window = Tk()
window.title("Tkinter Window")
window.geometry("400x200")
greetings = Label(text= "Hi Everyone", fg= "black", bg="white" )
button = Button(text = "Click me", bg= "black", fg= "white")
entry = Entry(fg= "yellow", bg= "blue", width= 50)
greetings.pack()
button.pack()
entry.pack()

frame = Frame(master= window, relief= RAISED, borderwidth= 5)
frame.pack()
label = Label(master= frame, text= "Sample Frame")
label.pack()

textbox = Text(fg= "green", bg= "yellow")
textbox.pack()
window.mainloop()