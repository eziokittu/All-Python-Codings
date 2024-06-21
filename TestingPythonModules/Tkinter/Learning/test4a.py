from tkinter import *

def app_puzzle():
    puzzle = Tk()
    puzzle.minsize(400,300)
    def p():
        print(1)
    b1 = Button(puzzle, text="press", command=p).pack()

    puzzle.mainloop()