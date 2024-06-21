from tkinter import *
from PIL import ImageTk, Image

assets_directory = 'TestingPythonModules\Tkinter\Assets'
app_width = 800
app_height = 600
pictureFrame_width = 790
pictureFrame_height = 540
appControlsFrame_width = 790
appControlsFrame_height = 50

def button_changeImage(nextImage):
    global image_label
    global image_number
    global button_goLeft
    global button_goRight

    image_label.grid_forget()
    if nextImage:
        image_number = image_number + 1
    else:
        image_number = image_number - 1
    
    image_label = Label(pictureFrame, image = images[image_number])
    button_goLeft = Button(appControlsFrame, bg = "#2ade39", activebackground = "#1dab29", padx = button_padX, pady = button_padY, text="< back <", command = lambda: button_changeImage(False))
    button_goRight = Button(appControlsFrame, bg = "#2ade39", activebackground = "#1dab29", padx = button_padX, pady = button_padY, text="> next >", command = lambda: button_changeImage(True))

    image_label.pack(fill = Y,side = BOTTOM, expand = True)
    button_goLeft.grid(row=0, column=0)
    button_goRight.grid(row=0, column=2)

root = Tk()

root.geometry(str(app_width)+"x"+str(app_height))

# Creating a picture Frame
pictureFrame = Frame(root, bg = "#fcc0f5")

# All Images
image1 = ImageTk.PhotoImage(Image.open(assets_directory + "\image1.jpg"))
image2 = ImageTk.PhotoImage(Image.open(assets_directory + "\image2.jpg"))
image3 = ImageTk.PhotoImage(Image.open(assets_directory + "\image3.jpg"))
image4 = ImageTk.PhotoImage(Image.open(assets_directory + "\image4.jpg"))
image5 = ImageTk.PhotoImage(Image.open(assets_directory + "\image5.jpg"))
images = [image1, image2, image3, image4, image5]
image_number = 2
image_label = Label(pictureFrame, image = images[image_number])
image_label.pack(fill = Y,side = BOTTOM, expand = True)

# Creating a app controls Frame
appControlsFrame = Frame(root, bg = "#000055")

# Creating Buttons
button_padX = 108
button_padY = 14
button_goLeft = Button(appControlsFrame, bg = "#2ade39", activebackground = "#1dab29", padx = button_padX, pady = button_padY, text="< back <", command = lambda: button_changeImage(False))
button_goRight = Button(appControlsFrame, bg = "#2ade39", activebackground = "#1dab29", padx = button_padX, pady = button_padY, text="> next >", command = lambda: button_changeImage(True))
button_quit = Button(appControlsFrame, bg = "#b51018", activebackground = "#ff0000", padx = button_padX, pady = button_padY, text="QUIT", command = root.quit)

# Drawing on screen
pictureFrame.place(width = pictureFrame_width, height = pictureFrame_height, x=5, y=5)
appControlsFrame.place(width = appControlsFrame_width, height = appControlsFrame_height, x=5, y=5+pictureFrame_height)
button_goLeft.grid(row=0, column=0)
button_goRight.grid(row=0, column=2)
button_quit.grid(row=0, column=1)

root.mainloop()