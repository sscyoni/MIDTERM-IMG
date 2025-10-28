from tkinter import *
root = Tk()

canvas = Canvas(root,width=200,height=300)
canvas.pack()

img = PhotoImage(file = "")
canvas . create_image(100,50,anchor = NW,image = img)