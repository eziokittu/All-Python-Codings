from tkinter import *

app = Tk()

app.geometry("400x600")

myFrame = Label(bg="white")
myLabel = Label(myFrame, text="Press here", bg="white", fg="red")
myButton = Button(myFrame, bg="blue", fg="white", text="READY")

myFrame.pack(side=BOTTOM, anchor="s", padx = 100, pady = 100 )
myLabel.grid(row=0, column=0)
myButton.grid(row=1, column=0)

# Tkinter main loop
app.mainloop()