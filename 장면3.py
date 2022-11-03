from tkinter import *



global function_Count
function_Count = 0

def button1_function():
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

         
        

        

    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1



def firstButtonTapped():
    label1.config(text="카드의 종류에는 신용카드,체크카드,\n제휴카드가 있어요.")
    label1.place(x = 30, y = 480)
    
    button1.config(text="각 카드의 개념을 알려줘!")
    button1.place(x=88, y=570)


def secondButtonTapped():
    label1.config(text = "신용카드는 카드대금 지급을\n 은행이 보증하여 \n일정 기간 뒤에 지급할 수 있도록 하는, \n신용 판매 제도에 이용되는 카드에요.")
    label1.place(x = 15, y = 480)

    button1.config(text = "체크카드는??")
    button1.place(x = 145, y = 620)

def thirdButtonTapped():
    label1.config(text = "체크카드는 직불 카드와 신용 카드의\n기능이 혼합된 카드에요\n 카드예금 계좌잔액 내에서 사용하며\n신용도에 따라 예금 잔액이 없어도\n50만원 내에서 신용 거래가 가능하답니다.",
                                                font=("Arial", 17, "bold")  )
    label1.place(x = 40, y = 480)
    
    button1.config(text = "제휴카드는?")
    button1.place(x = 160, y = 640)

def fourthButtonTapped():
    label1.config(text = "제휴카드는 신용카드의 기능에\n신분증이나 각종 회원증 기능이 추가되어\n여러가지 용도로 사용할 수 있는 카드에요\n제휴카드는 카드할인이나\n 서비스 혜택을 받을 수 있답니다.",
                                      font=("Arial", 17, "bold"))
    label1.place(x = 40, y = 480)

    button1.config(text = "그렇구나! 고마워")
    button1.place(x = 130, y = 630)

def fifthButtonTapped():
      
      label1.config(text = "카드의 개념을 이용한\n간단한 게임을 준비했어요\n플레이 해보시겠어요?")
      label1.place(x = 110, y = 500)

      button1.config(text = "응 해볼래!")
      button1.place(x= 170, y = 600)

      
def sixthButtonTapped():
      label1.config(text = "게임으로 이동중입니다..")
      label1.place(x = 110, y = 530)

      button1.destroy()

      
      



    

window = Tk()
window.title("장면3")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()




img1=PhotoImage(file="수뭉.png")
canvas.create_image(230, 430, image=img1)




label1=Label(window,
                   text="카드의 종류가 궁금하세요?",
                   font=("Arial", 20, "bold"))
label1.place(x = 80, y = 510)

label2=Label(window, text=" 카드의 종류",  font=("Arial", 24, "bold"), fg="white", bg="navy")
label2.place(x =160 , y = 50)


button1=Button(window,
                       text="↪응! 궁금해",
                       font=("Arial", 20, "bold"),
                       bg="beige",
                       command = button1_function)
button1.place(x = 170, y = 570)


window.mainloop()


