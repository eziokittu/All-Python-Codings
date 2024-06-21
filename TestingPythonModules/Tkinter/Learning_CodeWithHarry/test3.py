from tkinter import *
from PIL import Image, ImageTk
import random as r

app = Tk()

app_width = 800
app_height = 600
app.geometry(str(app_width) + "x" + str(app_height))
app.minsize(350, 150)
app.maxsize(1024,768)

# Episode 5
#label1 = Label(text="Learning Tkinter Python from 'CodeWithHarry' YT")
#label1.pack()

# Episode 6
def ChangeImage(a):
    image2 = Image.open("TestingPythonModules\Tkinter\Assets\image5.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    photoLabel1 = Label(text="Image created", image = photo2)
    photoLabel1.pack()

photoLabel= []
image = Image.open("TestingPythonModules\Tkinter\Assets\image1.jpg")
photo = ImageTk.PhotoImage(image)
photoLabel = Label(image = photo)
photoLabel.pack()

b1 = Button(app, text="Change image", command=lambda:ChangeImage(r.randint(1,5))).pack()
# Episode

app.mainloop()