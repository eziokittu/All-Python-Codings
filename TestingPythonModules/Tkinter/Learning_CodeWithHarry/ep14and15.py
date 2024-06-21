from tkinter import *

app = Tk()

myCanvasWidth = 500
myCanvasHeight = 300
app.title("Canvas and Events")
app.geometry(f"{myCanvasWidth}x{myCanvasHeight}")

# ------------------------Episode 14----------------------------

# # Creating a Canvas
# myCanvas = Canvas(app, width=myCanvasWidth, height=myCanvasHeight)
# myCanvas.pack()

# myCanvas.create_line(myCanvasWidth,0,0,myCanvasHeight)
# myCanvas.create_polygon(100,100,200,100,200,200,100,200, fill="red")
# myCanvas.create_oval(200,200,350,270, fill="gray")

# -------------------------Episode 15----------------------------
def ClickMe(event):
    print(f"You clicked the button at ({event.x},{event.y})")

# Creating a button
myButton = Button(app, text="Click Here")
myButton.pack()
myButton.bind("<Button-1>", ClickMe)
myButton.bind("<Double-1>", quit)

app.mainloop()