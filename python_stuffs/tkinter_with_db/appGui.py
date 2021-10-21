from tkinter import *

root = Tk()

mylabel = Label(root, text="hi")
mylabel1 = Label(root, text="world")

mylabel.grid(row=0, column=0)
mylabel1.grid(row=1,column=5)

root.mainloop()
