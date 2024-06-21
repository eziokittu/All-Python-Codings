from tkinter import *
import test4a

app = Tk()
app.title("My app")
app.minsize(800,600)

def open_puzzle():
    test4a.app_puzzle()
b1 = Button(app, text="open puzzle app", command=open_puzzle).pack()

app.mainloop()

