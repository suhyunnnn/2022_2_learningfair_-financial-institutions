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
        

    else:
        print("DEBUG: 다른 기능 넣어주기")

    function_Count += 1

def firstButtonTapped():
    label2.config(text="↪금리는 이자율이야\n쉽게 말해 원금에 대한 이자의 비율이지\n이자율은 이자/원금 x 100으로\n구할 수 있어")
    label2.place(x = 15, y = 500)

    button1.place(x =210, y = 640)

def secondButtonTapped():
    label2.config(text="↪이자의 계산 방법에는 단리와 복리가 있어\n단리는 원금에 대해서만 이자를 계산하는 방법이고\n복리는 원금에 대한 이자뿐 아니라\n이자에 대한 이자까지 합쳐 계산하는 방법이야", font=("Arial", 16, "bold"))
    label2.place(x = 13, y =500)
    
    button1.place(x =200, y = 620)

def thirdButtonTapped():
    label2.config(text = "↪그러면 금리를 계산하러 가볼래?", font=("Arial", 20, "bold"))
    label2.place(x = 50, y = 530)
    button1.config(text = "계산하러 가기")
    button1.place(x = 150, y = 600)

def fourthButtonTapped():
      label2.config(text = "어떤 계산기를 쓸래?")
      label2.place(x = 120, y = 520)
      button1.destroy()
      button2 = Button(text = "단리계산기", font=("Arial", 20),bg="beige")
      button2.place(x = 70, y = 580)
      button3 = Button(text = "복리계산기", font=("Arial", 20),bg="beige")
      button3.place(x = 270, y = 580)
      




window = Tk()
window.title("장면2")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1=PhotoImage(file="수뭉.png")
canvas.create_image(230, 440, image=img1)

#레이블
label1 = Label(window, text="금리계산" , font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x =180 , y = 55)
label2 = Label(window, text="↪금리계산 시스템에 온 걸 환영해\n우선 금리의 개념에 대해 설명해줄게!",font=("Arial", 20, "bold"), fg="white", bg="navy")
label2.place(x = 35, y = 520)


#버튼
button1 =Button(text="다음", font=("Arial", 20),bg="beige", command = button1_function)
button1.place(x =210, y = 600)






window.mainloop()




















