# Newspaper GUI
# have many png photos and txt files
from tkinter import *
from PIL import Image, ImageTk
import datetime as dt

def getNewsTilesImageAndDescriptionFromFile(n):
    global images
    global photos
    global newsTilesLabels
    global newsTilesImageLabels
    global newsTilesDescriptionLabels

    currentFile = NONE

    # getting text file
    newsTilesLabels.append(Label(newsFrame, bg="#9eb2f0", borderwidth = 2 ))
    currentFile =open(assets_directory + "exercise1_" + str(n+1) + ".txt", "r")
    newsTilesDescriptionLabels.append(Label(newsTilesLabels[n], text = currentFile.readlines(), wraplength=200, justify = CENTER))

    currentFile.close()

    # getting image
    images.append(Image.open(assets_directory + "exercise1_" + str(n+1) + ".jpg"))
    photos.append(ImageTk.PhotoImage(images[n]))
    newsTilesImageLabels.append(Label(newsTilesLabels[n], image = photos[n]))

app = Tk()

assets_directory = "D:\Coding Stuff, Editing\Visual Studio Python Codings\TestingPythonModules\Tkinter\Assets/"

# app features
app.title("Bawandar Times Newspaper")
app.attributes('-alpha', 0.9)
app.configure(background="#b0f2f1")
app_width = 800
app_height = 1000
app.geometry(str(app_width) + "x" + str(app_height))
app.minsize(350, 150)
#app.maxsize(1024,768)

# defining
headingFrame = Frame(app, borderwidth = 5, relief = RIDGE)
headingLabel = Label(headingFrame, font = "calibri 28 bold", text="Bawandar Times", bg="#d0f2e1")
currentDate = dt.date.today()
headingDatelabel = Label(headingFrame, text=currentDate, font = "calibri 18 bold")

newsFrame = Frame(app, borderwidth = 5, relief = RIDGE)
images = []
photos = []
newsTilesLabels = []
newsTilesImageLabels = []
newsTilesDescriptionLabels = []
gridRow = 0
gridColumn = 0

for i in range(0,6):
    getNewsTilesImageAndDescriptionFromFile(i)

# displaying 
headingFrame.pack()
headingLabel.grid(row=0)
headingDatelabel.grid(row=1)

newsFrame.pack()
for i in range(0,len(images)):
    gridRow = int(i/3)
    gridColumn = i % 3
    newsTilesLabels[i].grid(row=gridRow,column=gridColumn)
    newsTilesImageLabels[i].grid(row=0,column=0)
    newsTilesDescriptionLabels[i].grid(row=1,column=0)

app.update()

#Return and print the width of label widget
width1 = app.winfo_reqwidth()
width2 = app.winfo_width()
print("The width of the label is:", width1, "pixels")

# app running loop
app.mainloop()