from tkinter import *
import time



global function_Count
function_Count = 0

def button1_function():
    global function_Count
    
    if function_Count == 0:
        firstButtonclick()
        print("DEBUG: First Tapped")

    elif function_Count == 1:
        secondButtonclick()
        print("DEBUG: Second Tapped")

    elif function_Count == 2:
        thirdButtonclick()
        print("DEBUG : Third Tapped")

    elif function_Count == 3:
         fourthButtonclick()
         print("DEBUG : Fourth Tapped")

    elif function_Count == 4:
         fifthButtonclick()
         print("DEBUG : Fifth Tapped")

    elif function_Count == 5:
         sixthButtonclick()
         print("DEBUG : Sixth Tapped")

    elif function_Count == 6:
         sixthButtonclick()
         print("DEBUG : Sixth Tapped")

    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1

def firstButtonclick():
    button2.destroy()
    label1.config(text = "예금",font=("Arial", 25, "bold"),fg="black", bg="beige")
    label1.place(x = 210, y = 55)
    label2.config(text = "↪예금상품은 크게 요구불 예금과\n저축성 예금으로 구분할 수 있어",font=("Arial", 20, "bold"), fg="white", bg="navy")
    label2.place(x = 60, y = 500)
    button1.config(text = "다음")
    button1.place(x = 215, y = 600)


def secondButtonclick():
    label2.config(text = "↪요구불 예금은\n 수시로 입금과 출금이 자유로운\n예금을 말해")
    label2.place(x = 50, y = 500)
    button1.place(x = 215, y = 620)

    
   
def thirdButtonclick():
    label2.config(text = "↪다음으로, 저축성 예금은\n이자 수입을 주된 목적으로 하는 예금이야\n저축성 예금은\n정기예금과 정기적금으로 구분할 수 있어", font=("Arial", 19, "bold"), fg="white", bg="navy")
    label2.place(x = 20, y = 500)
    button1.place(x = 215, y = 630)

    
    
    
def fourthButtonclick():
    label2.config(text = "↪쉽게 말해 정기 예금은 목돈을 넣어두고\n이자를 받아 돈을 불리는 상품이고\n 정기적금은 매달 정해진 금액을\n저축하며 돈을 불리는 상품이야")
    label2.place(x = 25, y = 500)
    button1.config(text = "그렇구나!", font=("Arial", 17))
    button1.place(x = 190, y = 640)
    

def fifthButtonclick():
    label2.config(text = "↪이제 예금 상품에 대한 설명이 끝났어!\n에금상품의 개념을 이용한\n간단한 게임을 준비해봤는데\n플레이 해볼래?", font=("Arial", 18, "bold"))
    label2.place(x = 40, y = 490)
    button1.config(text = "응 해볼래", font=("Arial", 18),bg="beige")
    button1.place(x = 280, y = 620)
    button3=Button(text = "아니 안할래", font=("Arial", 18),bg="beige", command = button3_function)
    button3.place(x = 80, y = 620)

def sixthButtonclick():
    window.destroy()

    


def button2_function():
    global function_Count
    
    if function_Count == 0:
        firstButtonTapped()
        print("DEBUG: First Tapped")

    elif function_Count == 1:
        secondButtonTapped()
        print("DEBUG: Second Tapped")

    elif function_Count == 2:
        thirdButtonTapped()
        print("DEBUG : Third Tapped")

    elif function_Count == 3:
         fourthButtonTapped()
         print("DEBUG : Fourth Tapped")

    elif function_Count == 4:
         fifthButtonTapped()
         print("DEBUG : Fifth Tapped")

    elif function_Count == 5:
         sixthButtonTapped()
         print("DEBUG : Sixth Tapped")
         
    elif function_Count == 6:
         seventhButtonTapped()
         print("DEBUG : Seventh Tapped")

    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1

def firstButtonTapped():
    button1.destroy()
    label1.config(text = "증권",font=("Arial", 25, "bold"),fg="black", bg="beige")
    label1.place(x = 210, y = 55)
    label2.config(text = "↪증권투자는 크게 직접투자상품과\n간접투자상품으로 구분할 수 있어",font=("Arial", 20, "bold"), fg="white", bg="navy")
    label2.place(x = 60, y = 500)
    button2.config(text = "다음")
    button2.place(x = 215, y = 600)

def secondButtonTapped():
    label2.config(text = "↪직접투자상품의 종류에는 주식과 채권이 있어\n주식은 기업이 사업 자금 조달을 위해\n투자자로부터 돈을 얻고 그 증표를 발행하는 것을 말해\n따라서 주식은 회사의 소유권의 일부를\n투자자에게 준다는 증표야" ,font=("Arial", 15, "bold"))
    label2.place(x = 8, y = 500)
    button2.place(x = 210, y = 630)

def thirdButtonTapped():
    label2.config(text ="↪채권은 자금을 필요로 하는\n정부나 기업 등이 다수의 사람으로부터 돈을 빌리면서\n상환 일시, 지급 이자액 등을 약속하는 증서를 말해")
    label2.place(x = 10, y = 510)
    button2.place(x = 210, y = 620)

def fourthButtonTapped():
    label2.config(text = "↪다음으로 간접 투자 상품에 해당하는 펀드는\n투자자가 금융 기관에 돈을 맡기고\n대신 투자하도록 하는 상품이야\n뮤추얼 펀드 등의 종류가 있어")
    label2.place(x = 45, y = 510)
    button2.place(x = 210, y = 625)

def fifthButtonTapped():
     label2.config(text = "↪이외의 다른 금융상품에는\n방카슈랑스라고 하는 상품이 있어\n방카슈랑스란 은행 등의 금융 기관이\n보험 회사와 제휴하여 중개사 자격으로\n보험 상품을 함께 판매하는 금융 상품을 말해")
     button2.place(x = 210, y = 640)

def sixthButtonTapped():
    label2.config(text = "↪이제 증권 투자 상품에 대한 설명이 끝났어!\n증권투자의 개념을 이용한\n간단한 게임을 준비해봤는데\n플레이 해볼래?", font=("Arial", 18, "bold"))
    label2.place(x = 15, y = 500)
    button2.config(text = "응 해볼래", font=("Arial", 18),bg="beige")
    button2.place(x = 280, y = 630)
    button4 = Button(text = "아니 안할래",font=("Arial", 18),bg="beige", command = button4_function)
    button4.place(x = 80, y = 630)

def seventhButtonTapped():
    window.destroy()


def button3_function() :
    window.destroy()

def button4_function() :
    window.destroy()
         




      
window = Tk()
window.title("장면4")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1=PhotoImage(file="수뭉.png")
canvas.create_image(230, 440, image=img1)

#레이블
label1 = Label(window, text="다양한 금융상품" , font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x =140 , y = 55)
label2 = Label(window, text="↪다양한 금융 상품 코너에 온 걸 환영해\n준비한 금융 상품에는 예금과 증권이 있어\n어떤 게 궁금해?",font=("Arial", 19, "bold"), fg="white", bg="navy")
label2.place(x = 20, y = 500)


#버튼
button1 = Button(text="예금", font=("Arial", 20),bg="beige", command = button1_function)
button1.place(x =130, y = 610)
button2 = Button(text = "증권",  font=("Arial", 20),bg="beige", command = button2_function)
button2.place(x =300, y = 610)






window.mainloop()
