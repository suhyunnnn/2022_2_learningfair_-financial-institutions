quotes = [["주식이란?","기업이 사업 자금 조달을 위해\n투자자로부터 돈을 얻고 그 증표를 발행하는 것을 말한다"],
                ["채권이란?", "자금을 필요로 하는 정부나 기업 등이\n다수의 사람으로부터 돈을 빌리면서\n상환 일시, 지급 이자액 등을 약속하는 증서를 말한다"],
                   [ "펀드란?","투자자가 금융 기관에 돈을 맡기고\n대신 투자하도록 하는 상품을 말한다"],
                      ["방카슈랑스란?", "은행 등의 금융 기관이\n보험 회사와 제휴하여 중개사 자격으로\n보험 상품을 함께 판매하는 금융 상품을 말한다"]]
answer = 0


#문제 생성
def next_question():
    global answer

    for i in range(4):
        buttons[i].config(fg = "white", bg = "navy")
        
    multi_choice = random.sample(quotes, 4)
    answer = random.randint(0,3)
    cur_question = multi_choice[answer][0]

    question_label.config(text = cur_question)

    for i in range(4):
        buttons[i].config(text = multi_choice[i][1])


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
window.title("증권투자게임")
window.resizable(False, False)
window.config(padx=50, pady=200, bg="blue")
    


#레이블
question_label = Label(window, width=20, height=2, text="test",
                                 font=("나눔바른펜", 25, "bold"), fg="yellow", bg="blue")
question_label.pack(pady=30)

#버튼
buttons = []
for i in range(4):
     btn = Button(window, text=f"{i}번", width=43, height=3, font=("나눔바른펜", 15, "bold"),
                         fg="white", bg="navy", command = lambda idx=i: check_answer(idx))
     btn.pack()
     buttons.append(btn)

next_button = Button(window, text  = "다음 문제", width=20, height=2,
                                font=("나눔바른펜", 15, "bold"), fg="yellow", bg = "navy", command =next_question)
next_button.pack(pady = 30)


next_question()


window.mainloop()
