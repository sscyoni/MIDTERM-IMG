import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("이미지 변경 예제")
root.geometry("400x400")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=20)

img = None  # 전역 변수
image_index = 0  # 현재 이미지 번호

# 이미지 파일 리스트
image_list = ["image1.png", "image2.png", "image3.png"]

def draw_image():  #힌트코드
    global img
    img = PhotoImage(file=image_list[image_index])
    canvas.create_image(0, 0, anchor=tk.NW, image=img)

# 다음 이미지로 바꾸는 함수
def next_image():
    global image_index
    if image_index < len(image_list) - 1:  # 마지막 이미지가 아니면
        image_index += 1
        draw_image()

# 버튼 생성
btn = tk.Button(root, text="다음 이미지", command=next_image)
btn.pack()


#키 눌러서 바꿀려면 root.bind("<Right>", next_image) 코드 사용
# 처음 이미지 표시
draw_image()

root.mainloop()

