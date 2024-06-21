from tkinter import *

app = Tk()

app.geometry("600x400")

myFrame = Frame(app, borderwidth=5, bg="pink")
myLabel1 = Label(myFrame, text="This text is inside a frame", bg="red",fg ="white")

myFrame.pack(side = LEFT, fill="y")
myLabel1.pack()

app.mainloop()