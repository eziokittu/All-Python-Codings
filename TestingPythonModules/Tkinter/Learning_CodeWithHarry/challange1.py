from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk
import os

app = Tk()

# Defining the title
titleLabelFont = font.Font(size = 72)
titleLabel = Label(bg = "#93e6d1", fg="black", font = titleLabelFont, relief = RIDGE, text = "--- Photo Album ---")

# Defining all the images
image_directory = "D:/Coding Stuff, Editing/Visual Studio Python Codings/TestingPythonModules/Tkinter/Assets/image"
images_filenames_list = os.listdir(image_directory)

images = []
photos = []
photoLabels = []

for i in range(0,len(images_filenames_list)):
    images.append(Image.open(image_directory + images_filenames_list[i]))
    photos.append(ImageTk.PhotoImage(images[i]))
    photoLabels.append(Label(image = photos[i]))

# Displaying all in the screen
titleLabel.grid(row=0,column=0,columnspan=3)
photoLabels[0].grid(row=1,column=0)
photoLabels[1].grid(row=1,column=1)
photoLabels[2].grid(row=1,column=2)
photoLabels[3].grid(row=2,column=0)
photoLabels[4].grid(row=2,column=1)

# Tkinter main loop
app.mainloop()