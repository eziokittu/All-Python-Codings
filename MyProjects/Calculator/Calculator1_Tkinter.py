from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Calculator - by Bodhisatta (Using Tkinter in Python)")
root.geometry("306x483")

# defining some global variables
answer = ""
text_insert_position = 0
text_needsToBeCleared = False

# Text Size
myFont = font.Font(size=30)

# Defining some other functions
def calculation_usingBODMAS(s):
    # this function calculates the full equation inside of string and return another string which is the output
    global text_needsToBeCleared
    no_of_operator = 0

    if s[0] in ["+","X","/"]:
        return "ERROR"
    else:
        # assigning some variables
        text_needsToBeCleared = True
        num1 = 0
        num1_filled = False
        num1_float = 0
        num2 = 0
        num2_float = 0
        op = ""

        # loop to iterate the string
        for i in s:
            # getting the opertor
            if i in ["+","-","X","/"]:
                no_of_operator += 1
                op = i
                num1_filled = True

            # getting first number
            elif num1_filled == False:
                if i=="." and num1_float==0:
                    num1_float +=1
                elif i=="." and num1_float>0:
                    return "ERROR"
                elif num1_float == 0:
                    num1 = num1*10 + int(i)
                else:
                    num1 += int(i)/pow(10, num1_float)
                    num1_float+=1

            # getting the second number
            elif num1_filled == True:
                if i=="." and num2_float==0:
                    num2_float += 1
                elif i=="." and num2_float>0:
                    return "ERROR"
                elif num2_float == 0:
                    num2 = num2*10 + int(i)
                else:
                    num2 += int(i)/pow(10, num2_float)
                    num2_float+=1
        
        # Calculation done here
        if no_of_operator>1:
            return "ERROR"
        if op == "+":
            return "{:.3f}".format(num1+num2)
        if op == "-":
            return "{:.3f}".format(num1-num2)
        if op == "X":
            return "{:.3f}".format(num1*num2)
        if op == "/":
            return "{:.3f}".format(num1/num2)

# Creating an Input field widget
e = Entry(width = 15,borderwidth=5, font = font.Font(size=20), bg="grey", fg="black")
e.grid(row=0,column=0,columnspan=4, padx=10, pady=10)

# defining button functions
def button_func_click(a):
    global text_insert_position
    global text_needsToBeCleared
    global answer

    if text_needsToBeCleared==True:
        button_func_clear()

    text_needsToBeCleared = False

    # action if operator is clicked
    if a in ["+","-","X","/"]:
        print("operator clicked , answer is --- "+ answer)
        e.insert(text_insert_position, str(answer + a))
        text_insert_position+=len(answer)+1

    # action if numbers or dot is clicked
    else:
        e.insert(text_insert_position, a)
        text_insert_position+=1
        answer = ""

def button_func_equals():
    global text_insert_position
    global answer
    text_insert_position=0
    txt = ""

    try:
        if len(e.get())>0:
            answer = calculation_usingBODMAS(e.get())
            try:
                print("Current answer is --- "+ answer)
            except:
                print("Current answer is --- NONE")
            txt = e.get() + " = " + answer
            if answer == "ERROR":
                answer = ""
    except:
        txt = "ERROR"
    
    e.delete(0,END)
    e.insert(0,txt)
    text_needsToBeCleared = True

def button_func_clear():
    global answer
    global text_insert_position
    e.delete(0,END)
    text_insert_position=0

# Creating all the button widgets
button_1 = Button(root, text="1", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(1))
button_2 = Button(root, text="2", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(2))
button_3 = Button(root, text="3", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(3))
button_4 = Button(root, text="4", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(4))
button_5 = Button(root, text="5", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(5))
button_6 = Button(root, text="6", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(6))
button_7 = Button(root, text="7", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(7))
button_8 = Button(root, text="8", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(8))
button_9 = Button(root, text="9", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(9))
button_0 = Button(root, text="0", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click(0))
button_add = Button(root, text="+", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click("+"))
button_sub = Button(root, text="-", padx=10,pady=0, font = font.Font(size = 34), background="white", activebackground="#57b1c9", command=lambda: button_func_click("-"))
button_mul = Button(root, text="X", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click("X"))
button_div = Button(root, text="/", padx=10,pady=0, font = font.Font(size = 34), background="white", activebackground="#57b1c9", command=lambda: button_func_click("/"))
button_dot = Button(root, text=". ", padx=10,pady=5, font = myFont, background="white", activebackground="#57b1c9", command=lambda: button_func_click("."))
button_equals = Button(root, text="=", padx=10,pady=5, font = myFont, bg="green", activebackground="#28ff03", command=lambda: button_func_equals())
button_clear = Button(root, text="CLEAR", padx=30,pady=5, font = myFont, bg="#cf137a", activebackground="#ff0000", command=lambda: button_func_clear())

# putting all the buttons on screen using grid
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_add.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_mul.grid(row=3,column=3)
button_dot.grid(row=4,column=0,columnspan=1)
button_0.grid(row=4,column=1)
button_div.grid(row=4,column=3)
button_clear.grid(row=5,column=0,columnspan=3)
button_equals.grid(row=5,column=3,columnspan=1)

# Running the Tkinter main loop
root.mainloop()