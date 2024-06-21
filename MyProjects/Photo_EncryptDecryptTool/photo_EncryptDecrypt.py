from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import ImageTk,Image
#import photo_EncryptDecrypt as ped
import photo_browsefiles as pbf

def getPhotoPath():
    global path
    path = pbf.browseFiles()
    print(path)
    try:
        img = PhotoImage(file=path)
        panel = Label(root, image=img)
        panel.grid(row=3,column=3,padx=10,pady=10)
        print("path -- ", path)
    except:
        l=Label(root,text="Image cannot be opened (Image is encrypted)")
        l.grid(row=0,column=0,padx=10,pady=10)
        print(2)

def EncryptDecrypt(path, key):
    try:
        # take path of image as a input
        # path = input(r'Enter path of Image : ')

        # taking encryption key as input
        # key = int(input('Enter Key for encryption of Image : '))

        # print path of image file and encryption key that
        # we are using
        print('The path of file : ', path)
        print('Key for encryption : ', key)

        # open file for reading purpose
        fin = open(path, 'rb')

        # storing image data in variable "image"
        image = fin.read()
        fin.close()

        # converting image into byte array to
        # perform encryption easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        fin = open(path, 'wb')

        # writing encrypted data in image
        fin.write(image)
        fin.close()

        messagebox.showinfo("Encrytion / Decryption", "This image is now encrypted / decrypted")
    except Exception:
        messagebox.showerror("Error in Encryption / Decryption", "ERROR : No photo selected")
        print('Error caught : ', Exception.__name__)

root=Tk()

path = "NOPATH" #D:/Bodhisatta_CST_2019to2022/fbus1.JPG
key = 22

btn_EncryptDecrypt = Button(root, text="Encrypt / Decrypt", command=lambda:EncryptDecrypt(path, key))
button_explore = Button(root, text = "Browse Files", command=lambda:getPhotoPath())
button_exit = Button(root, text = "Exit", command = exit)
btn_EncryptDecrypt.grid(row=2,column=0)
button_explore.grid(row=1,column=0)
button_exit.grid(row=1,column=1)

root.mainloop()