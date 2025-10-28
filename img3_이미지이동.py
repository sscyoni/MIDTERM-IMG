from tkinter import *

root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()

def draw_images():
    global img1, img2, img3, item1
    img1 = PhotoImage(file="파일경로1")
    img2 = PhotoImage(file="파일경로2")
    img3 = PhotoImage(file="파일경로3")
    
    item1 = canvas.create_image(50, 50, anchor=NW, image=img1)
    canvas.create_image(200, 150, anchor=NW, image=img2)
    canvas.create_image(350, 300, anchor=NW, image=img3)

def move_image():
    canvas.coords(item1, 300, 50)

draw_images()

btn = Button(root, text="이미지 이동", command=move_image)
btn.pack()

root.mainloop()