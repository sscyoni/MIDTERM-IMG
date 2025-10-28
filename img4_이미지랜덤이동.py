from tkinter import *
import random  # 랜덤 좌표 생성을 위해 import

root = Tk()
canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

def draw_images_random():
    global img1, img2, img3, item1, item2, item3
    img1 = PhotoImage(file="파일경로1")
    img2 = PhotoImage(file="파일경로2")
    img3 = PhotoImage(file="파일경로3")

    # 랜덤 좌표 생성 (캔버스 안에서 이미지가 완전히 들어오도록)
    x1 = random.randint(0, canvas_width - img1.width())
    y1 = random.randint(0, canvas_height - img1.height())

    x2 = random.randint(0, canvas_width - img2.width())
    y2 = random.randint(0, canvas_height - img2.height())

    x3 = random.randint(0, canvas_width - img3.width())
    y3 = random.randint(0, canvas_height - img3.height())

    # 이미지 배치
    item1 = canvas.create_image(x1, y1, anchor=NW, image=img1)
    item2 = canvas.create_image(x2, y2, anchor=NW, image=img2)
    item3 = canvas.create_image(x3, y3, anchor=NW, image=img3)

# 버튼을 눌러 이미지를 다시 랜덤 위치로 이동
def move_images_random():
    canvas.coords(item1,
                  random.randint(0, canvas_width - img1.width()),
                  random.randint(0, canvas_height - img1.height()))
    canvas.coords(item2,
                  random.randint(0, canvas_width - img2.width()),
                  random.randint(0, canvas_height - img2.height()))
    canvas.coords(item3,
                  random.randint(0, canvas_width - img3.width()),
                  random.randint(0, canvas_height - img3.height()))

draw_images_random()

btn = Button(root, text="이미지 이동", command=move_images_random)
btn.pack()

root.mainloop()
