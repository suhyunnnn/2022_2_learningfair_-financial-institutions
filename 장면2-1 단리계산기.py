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
        print("DEBUG: FIfth Tapped")
        
    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1


def firstButtonTapped():
    label2.config(text ="↪이자율을 입력하세요")
    label4.config(text = entry1.get(), fg="yellow")
    label4.place(x = 320, y =155)
    
    

def secondButtonTapped():
    label2.config(text = "↪투자기한을 입력하세요")
    label6.config(text = entry1.get(),fg="yellow")
    label6.place(x = 335, y =255)
                
    

def thirdButtonTapped():    
    time.sleep(1)
    label8.config(text = entry1.get(),fg="yellow")
    label8.place(x = 340, y =355)
    label2.config(text = "↪계산이 완료되었습니다")
    label2.place(x = 100, y = 500)
    entry1.destroy()
    button1.config(text = str(label8.cget("text"))+"년 후 원리금 확인하기")
    button1.place(x = 140, y = 570)

    
def fourthButtonTapped():
    principal=float(label4.cget("text"))
    interest_rate=float(label6.cget("text"))
    years=int(label8.cget("text"))


    total = (principal * (1 + interest_rate/100 * years))
    label9 = Label(window, text="원리금", font=("Arial", 18, "bold"), fg="white", bg="blue")
    label9.place(x = 330, y = 425)
    label10 = Label(window, text=total, font=("Arial", 18, "bold"), fg="white", bg="blue")
    label10.place(x = 330, y = 475)
    label2.config(text = "↪ " + str(label8.cget("text"))+ "년 후 당신의 원리금은\n"+ str(label10.cget("text")) + "(만)원 입니다")
    label2.place(x = 80, y = 520)
    button1.config(text = "시스템 종료")
    button1.place(x = 180, y = 600)

def fifthButtonTapped():
    window.destroy()






window = Tk()
window.title("단리계산기")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1=PhotoImage(file="수뭉.png")
canvas.create_image(150, 440, image=img1)


#레이블
label1 = Label(window, text="단리계산기" , font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x =170 , y = 55)
label2 = Label(window, text="↪투자할 원금을 입력하세요",font=("Arial", 20, "bold"), fg="white", bg="navy")
label2.place(x = 65, y = 500)
label3 = Label(window, text= "원금", font=("Arial", 18, "bold"), fg="white", bg="blue")
label3.place(x = 330, y = 125)
label4 = Label(window, text= "", font=("Arial", 18, "bold"), fg="blue", bg="blue")
label4.place(x = 330, y = 155)
label5 = Label(window, text= "이자율(%)", font=("Arial", 18, "bold"), fg="white", bg="blue")
label5.place(x = 330, y = 225)
label6 = Label(window, text= "", font=("Arial", 18, "bold"), fg="blue", bg="blue")
label6.place(x = 330, y = 255)
label7 = Label(window, text= "투자기한(년)", font=("Arial", 18, "bold"), fg="white", bg="blue")
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
