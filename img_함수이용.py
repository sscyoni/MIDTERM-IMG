from tkinter import *
root = Tk()

canvas = Canvas(root,width=300,height=200)
canvas.pack()

def draw_image () :
    global img 
    img =PhotoImage(file="")
    canvas.create_image(50, 50, anchor=NW, image=img)

draw_image()
root.mainloop()