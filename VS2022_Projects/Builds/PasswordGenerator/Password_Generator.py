'''Project - Password Generator
Tkinter used as UI'''

from tkinter import *
from tkinter import messagebox
import MyResources as m

def ShowIfPasswordIsGood(state):
    if state==6:
        messagebox.showerror("error", "Invalid Characters present in the password !")
    elif state==1:
        messagebox.showwarning("info", "Your password is good")
    elif state==2:
        messagebox.showwarning("warning", "Your password must contain numbers.")
    elif state==3:
        messagebox.showwarning("warning", "Your password must contain special characters.")
    elif state==4:
        messagebox.showwarning("warning", "Your password must contain atleast 1 upper/lower case letter.")
    elif state==5:
        messagebox.showerror("error", "The password length needs to be between 8 to 20 characters long !")

def ShowPassword(str):
    passwordEntry2.delete(0, END)
    passwordEntry2.insert(0,str)

def OnClickCopyPassword(copy): # this piece of code is mostly copied
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(copy)  # Change INFO_TO_COPY to the name of your data source
    clip.destroy()
    if len(copy)==0:
        messagebox.showwarning("warning", "The entry field is empty")
    elif " " in copy:
        messagebox.showerror("error", "INVALID character (spaces and some other special characters not allowed)")
    else:
        messagebox.showinfo("info", "The password has successfully been copied to clipboard")

root = Tk()
root.minsize(600,400)
root.title("Password Generator (Made by EZIOKITTU)")

l1 = Label(root, text="Password Generator - Check if your password is strong / generate a strong password",
    font=("Consolas",16),justify="center",bg="white",fg="black")
l1.grid(row=0,column=0, columnspan=3)

# password that is being checked
myPassword1 = StringVar()
passwordEntry1 = Entry(root, textvariable=myPassword1,
    font=("Consolas",28),justify="center",width=30,bg="white",fg="blue")
passwordEntry1.insert(0, "Type your password:")
passwordEntry1.grid(row=1,column=0, columnspan=2)

b1 = Button(root, text="Check Password Strength", command=lambda:ShowIfPasswordIsGood(m.CheckPasswordStrength(myPassword1.get(),0)),
    font=("Calibri",18),justify="center",bg="#b4ff48",fg="black")
b1.grid(row=1,column=2, columnspan=1)

btnCopy1 = Button(root, text="Copy to clipboard", command=lambda:OnClickCopyPassword(myPassword1.get()),
    font=("Calibri",18),justify="center",bg="#30dade",fg="black")
btnCopy1.grid(row=1,column=3, columnspan=1)

# password that is being generated
myPassword2 = StringVar()
newPassword = ""
b2 = Button(root, text="Generate Strong Password", command=lambda:ShowPassword(m.GenerateStrongPassword()),
    font=("Calibri",18),justify="center",bg="#e8eb75",fg="black")
b2.grid(row=2,column=0, columnspan=1)
passwordEntry2 = Entry(root, textvariable=myPassword2,
    font=("Consolas",28),justify="center",width=30,bg="white",fg="blue")
passwordEntry2.insert(0, "<-- click to generate")
passwordEntry2.grid(row=2,column=1, columnspan=2)

btnCopy2 = Button(root, text="Copy to clipboard", command=lambda:OnClickCopyPassword(myPassword2.get()),
    font=("Calibri",18),justify="center",bg="#30dade",fg="black")
btnCopy2.grid(row=2,column=3, columnspan=1)

root.mainloop()