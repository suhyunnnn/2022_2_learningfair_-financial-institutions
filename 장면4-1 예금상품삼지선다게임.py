quotes = [["요구불 예금이란?","수시로 입금과 출금이 자유로운 예금을 말한다"],
                ["정기 예금이란?", "목돈을 넣어두고 이자를 받아 돈을 불리는 예금을 말한다"],
                   [ "정기 적금이란?","매달 정해진 금액을 저축하며 돈을 불리는 상품을 말한다"]]
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



