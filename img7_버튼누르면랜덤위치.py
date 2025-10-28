import tkinter as tk
from tkinter import PhotoImage
import random

root = tk.Tk()
root.title("랜덤 위치 이미지 (한 장만)")
root.geometry("500x500")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=20)

img = None  # 전역 변수

# 이미지 파일 리스트
image_list = ["image1.png", "image2.png", "image3.png"]

def draw_image_random_position():
    global img
    canvas.delete("all")  # 이전 이미지 모두 삭제

    # 랜덤으로 이미지 선택
    image_index = random.randint(0, len(image_list) - 1)
    img = PhotoImage(file=image_list[image_index])

    # 랜덤 위치 생성 (캔버스 안에서)
    x = random.randint(0, 400 - img.width())
    y = random.randint(0, 400 - img.height())

    # 캔버스에 이미지 그리기
    canvas.create_image(x, y, anchor=tk.NW, image=img)

# 버튼 생성
btn = tk.Button(root, text="랜덤 위치 이미지", command=draw_image_random_position)
btn.pack()

# 처음 이미지 표시
draw_image_random_position()

root.mainloop()
