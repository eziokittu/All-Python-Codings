from tkinter import *

# ------ Lessons ------
# just like pygame - root = Tk(); root.mainloop(); --- these two lines are must
# everything in Tkinter is a WIDGET
# pack() and grid() does not work together

root = Tk()

def getdate():
    '''Function to give a time stamp'''
    import datetime
    return datetime.datetime.now()

# Creating an Input field widget
e = Entry(width = 100,borderwidth=5, bg="grey", fg="black")
e.grid(row=0,column=0)
e.insert(0, "Enter your name : ")

# Creating a Label Widget
myLabel1 = Label(root, text = "Hello World !").grid(row = 0, column = 1)
myLabel2 = Label(root, text = "CSGO").grid(row = 0, column = 2)
myLabel3 = Label(root, text = "pubg").grid(row = 1, column = 0)
myLabel4 = Label(root, text = "srgjrbgiwrg").grid(row = 1, column = 1)

# Creating a button widget
def myClick():
    t = e.get()
    if t == "Enter your name : ":
        t = ""
    myLabel=Label(root, text="["+ str(getdate()) + "] " + "Hello "+ t)
    myLabel.grid()
myButton1 = Button(root, text="Click me!", command=myClick, fg="green", bg="#444444")
myButton1.grid(row = 1, column = 2)

root.mainloop()