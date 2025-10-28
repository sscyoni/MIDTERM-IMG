import tkinter as tk
from tkinter import PhotoImage
import random  # 랜덤 선택을 위해 추가

root = tk.Tk()
root.title("랜덤 이미지 예제")
root.geometry("400x400")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=20)

img = None  # 전역 변수

# 이미지 파일 리스트
image_list = ["image1.png", "image2.png", "image3.png"]

def draw_image_random():
    global img
    # 랜덤으로 이미지 선택
    image_index = random.randint(0, len(image_list) - 1)
    img = PhotoImage(file=image_list[image_index])
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

# 버튼 생성
btn = tk.Button(root, text="랜덤 이미지", command=draw_image_random)
btn.pack()

# 처음 이미지 표시 (랜덤으로)
draw_image_random()

root.mainloop()
