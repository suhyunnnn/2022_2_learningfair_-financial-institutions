quotes = [["신용카드란?","카드대금 지급을 일정기간 뒤에 지급할 수 있도록 하는,\n 신용 판매 제도에 이용되는 카드"],
                ["체크카드란?", "직불 카드와 신용 카드의 기능이 혼합된 카드"],
                   [ "제휴카드란?","신용카드의 기능에 각종 기능이 추가돼\n 여러가지 용도로 사용할 수 있는 카드"]]
answer = 0


#문제 생성
def next_question():
    global answer

    for i in range(3):
        buttons[i].config(fg = "white", bg = "navy")
        
    multi_choice = random.sample(quotes, 3)
    answer = random.randint(0,2)
    cur_question = multi_choice[answer][0]

    question_label.config(text = cur_question)

    for i in range(3):
        buttons[i].config(text = multi_choice[i][1])

#정답 체크
def check_answer(idx):
    idx = int(idx)
    if answer == idx:
        buttons[idx].config(bg = "green")
        window.after(1000, next_question)
    else:
        buttons[idx].config(bg = "red")
        
        

from tkinter import *
import random

    
window = Tk()
window.title("예금상품게임")
window.resizable(False, False)
window.config(padx=50, pady=200, bg="blue")
    


#레이블
question_label = Label(window, width=20, height=2, text="test",
                                 font=("나눔바른펜", 25, "bold"), fg="yellow", bg="blue")
question_label.pack(pady=30)

#버튼
buttons = []
for i in range(3):
     btn = Button(window, text=f"{i}번", width=43, height=2, font=("나눔바른펜", 15, "bold"),
                         fg="white", bg="navy", command = lambda idx=i: check_answer(idx))
     btn.pack()
     buttons.append(btn)

next_button = Button(window, text  = "다음 문제", width=20, height=2,
                                font=("나눔바른펜", 15, "bold"), fg="yellow", bg = "navy", command =next_question)
next_button.pack(pady = 30)


next_question()


window.mainloop()
