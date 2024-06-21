# A simple form fill that collects user info
# from a simple GUI and stores in a file.
# made with Tkniter Python Module
from tkinter import *
import tkinter.font as font
from tkinter.messagebox import showerror, showwarning, showinfo

directory = "D:\Coding Stuff, Editing\Visual Studio Python Codings\MyProjects\Assets/"
fileName = "FormFill_Tkinter_Data.txt"

def App():
    # app is defined
    app = Tk()

    # defining my app variables
    appWidth, appWidth_min, appWidth_max = 500, 360, 700
    appHeight, appHeight_min, appHeight_max = 500, 300, 700
    app.geometry(str(appWidth) + "x" + str(appHeight))
    app.minsize(appWidth_min, appHeight_min)
    app.maxsize(appWidth_max, appHeight_max)

    # gets the data and stores it in file
    def getData(listofentries, *listofdata):
        import datetime as dt
        currentDate = dt.datetime.now()

        for i in range(0,len(listofdata)):
            email_TopLevelDomain = [".com",".in",".org",".net"]
            email_hasTLD = False
            if (listofdata[i].get()==""):
                showerror(title="Error", message="No field can be empty")
                return 0
            elif i==1:
                for j in email_TopLevelDomain:
                    if j in listofdata[1].get():
                        email_hasTLD = True
                        break
                if (email_hasTLD==False):
                    showerror(title="Error", message="Not a valid email")
                    return 0
            elif i==2:
                if len(listofdata[2].get())<=3:
                    showerror(title="Error", message="Password is too short [minimum is 4 characters]")
                    return 0

        currentFile = open(directory + fileName,"at+")
        currentFile.write("[" + currentDate.strftime("%m/%d/%Y,%H:%M:%S") + "] ")
        for i in range(0,len(listofdata)):
            currentFile.write(listofdata[i].get())
            if i==len(listofdata)-1:
                currentFile.write("\n")
            else:
                currentFile.write(" ")
        currentFile.close()

        showinfo(title="Successful", message="Your input is successful")

        ResetEntries(listofentries)

    # resets the entry fields after submit is clicked
    def ResetEntries(listofentries):
        for i in range(0, len(listofentries)):
            listofentries[i].delete(0, END)

    # Font
    def applyFont(_size, *args):
        if len(args)==0:
            return font.Font(size = _size)
        else:
            return font.Font(family=args[0], size=_size, weight=args[1])    

    # Widgets and related variables
    # f=frame, l=label, d=data, b=button, e=entry, numbers and names accordingly
    f1 = Frame(app, padx=5,pady=5,borderwidth = 5, relief = RIDGE, background = "white")
    l1_f1_name = Label(f1, text="Enter your name : ", font = applyFont(12))
    l2_f1_email = Label(f1, text="Enter your email : ", font = applyFont(12))
    l3_f1_password = Label(f1, text="Enter a password : ", font = applyFont(12))
    # Variable classes in tkinter
    # BooleanVar, DoubleVar, IntVar, StringVar
    d1_f1 = StringVar()
    d2_f1 = StringVar()
    d3_f1 = StringVar()

    e1_f1 = Entry(f1, textvariable=d1_f1, borderwidth=4, relief = SUNKEN, font = applyFont(12), insertofftime=750)
    e1_f1.insert(0, "Enter your name")
    e2_f1 = Entry(f1, textvariable=d2_f1, borderwidth=4, relief = SUNKEN, font = applyFont(12), insertofftime=750)
    e2_f1.insert(0, "Enter an email")
    e3_f1 = Entry(f1, textvariable=d3_f1, borderwidth=4, relief = SUNKEN, font = applyFont(12), insertofftime=750, show='*')
    #e3_f1.insert(0, "Enter a password") #does not work as expected (obviously)

    b1_f1 = Button(f1, text="Submit",background="#a5ceee", activebackground="#5cb2f5", font = applyFont(16), 
        command=lambda: getData([e1_f1, e2_f1, e3_f1], *[d1_f1, d2_f1, d3_f1]) )

    # Displaying Widgets on screen
    f1.pack(side = TOP, expand = True)
    l1_f1_name.grid(row=0, column=0)
    l2_f1_email.grid(row=1, column=0)
    l3_f1_password.grid(row=2, column=0)
    e1_f1.grid(row=0, column=1, columnspan=2)
    e2_f1.grid(row=1, column=1, columnspan=2)
    e3_f1.grid(row=2, column=1, columnspan=2)
    b1_f1.grid(row=3, column=2, columnspan=2, pady=5, ipadx=20, ipady=5)

    # main loop for the app running
    app.mainloop()

if __name__ == "__main__":
    App()