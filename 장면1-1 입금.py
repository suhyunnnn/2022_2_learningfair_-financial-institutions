from tkinter import *
import time



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
        print("DEBUG: Third Tapped")


    elif function_Count == 3:
        fourthButtonTapped()
        print("DEBUG: Fourth Tapped")

    elif function_Count == 4:
        fifthButtonTapped()
        print("DEBUG: Fifth Tapped")

    elif function_Count == 5:
        sixthButtonTapped()
        print("DEBUG: Sixth Tapped")

    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1


def firstButtonTapped():
    label2.config(text ="↪당신의 계좌잔액을 입력하세요")
    label4.config(text = entry1.get(), fg="yellow")
    label4.place(x = 320, y =155)
    
    
def secondButtonTapped():
    label2.config(text = "↪입금할 금액을 입력하세요")
    label6.config(text = entry1.get(),fg="yellow")
    label6.place(x = 335, y =255)
                
    

def thirdButtonTapped():
    time.sleep(1)
    label8.config(text = entry1.get(),fg="yellow")
    label8.place(x = 340, y =355)
    label2.config(text = "↪입금이 완료되었습니다")
    label2.place(x = 100, y = 500)
    entry1.destroy()
    button1.config(text = "계좌잔액 확인하기")
    button1.place(x = 150, y = 570)

def fourthButtonTapped():
    
    bank_balance=int(label6.cget("text"))
    deposit=int(label8.cget("text"))
    
    plus = (bank_balance + deposit)
    
    label6.config(text = plus)
    label8.config(text = "0")
    label2.config(text = "↪입금 후 당신의 계좌잔액은\n"+ str(label6.cget("text")) + "(만)원 입니다")
    label2.place(x = 70, y = 500)
    button1.config(text = "시스템 종료")
    button1.place(x = 180, y = 580)

def fifthButtonTapped():
     window.destroy()




   





window = Tk()
window.title("입금")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1=PhotoImage(file="수뭉.png")
canvas.create_image(150, 440, image=img1)


#레이블
label1 = Label(window, text="입금" , font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x =210 , y = 55)
label2 = Label(window, text="↪당신의 계좌번호를 입력하세요",
                       font=("Arial", 20, "bold"), fg="white", bg="navy")
label2.place(x = 65, y = 500)
label3 = Label(window, text= "계좌번호", font=("Arial", 18, "bold"), fg="white", bg="blue")
label3.place(x = 330, y = 125)
label4 = Label(window, text= "", font=("Arial", 18, "bold"), fg="blue", bg="blue")
label4.place(x = 330, y = 155)
label5 = Label(window, text= "계좌잔액", font=("Arial", 18, "bold"), fg="white", bg="blue")
label5.place(x = 330, y = 225)
label6 = Label(window, text= "", font=("Arial", 18, "bold"), fg="blue", bg="blue")
label6.place(x = 330, y = 255)
label7 = Label(window, text= "입금금액", font=("Arial", 18, "bold"), fg="white", bg="blue")
label7.place(x = 330, y = 325)
label8 = Label(window, text= "", font=("Arial", 18, "bold"), fg="blue", bg="blue")
label8.place(x = 330, y = 355)





#엔트리
entry1 = Entry()
entry1.place(x =90, y = 560, width=280, height=40)

#버튼
button1 = Button(window, text = "입력", font=("Arial", 15, "bold"), fg="yellow", bg="navy",
                          command = button1_function)
button1.place(x = 385, y = 558)










window.mainloop()
