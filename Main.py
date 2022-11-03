from tkinter import *
import time

       

      


def button1_function() :
      button1.destroy()
      button2.destroy()
      button3.destroy()
      button4.destroy()
      label1.config( text="↪입.출금 시스템으로 이동중입니다..", font=("Arial", 20, "bold"),
                                       fg="white", bg="navy")
      label1.place(x=50, y=500)


def button2_function() :
      button1.destroy()
      button2.destroy()
      button3.destroy()
      button4.destroy()
      label1.config( text="↪금리계산 시스템으로 이동중입니다..", font=("Arial", 20, "bold"),
                                       fg="white", bg="navy")
      label1.place(x=30, y=500)





def button3_function() :
      button1.destroy()
      button2.destroy()
      button3.destroy()
      button4.destroy()
      label1.config( text="↪카드의 종류시스템으로 이동중입니다..", font=("Arial", 20, "bold"),
                                       fg="white", bg="navy")
      label1.place(x=10, y=500)
      
   
      
def button4_function() :
      button1.destroy()
      button2.destroy()
      button3.destroy()
      button4.destroy()
      label1.config( text="↪다양한 금융상품 시스템으로\n이동중입니다..", font=("Arial", 20, "bold"),
                                       fg="white", bg="navy")
      label1.place(x=70, y=500)

           


window = Tk()
window.title("상명금융원")
window.resizable(False, False) #윈도우크기고정

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1= PhotoImage(file="수뭉.png")
canvas.create_image(230,440, image=img1)
 

   
           
#레이블 : 문자 표현
label1 = Label(window, text="상명금융원", font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x=165, y=45)



#버튼 : 버튼 누르기
button1 = Button(text="입금/출금", font=("Arial", 20), bg="beige", command = button1_function)
button1. place(x=80, y=500)

button2 = Button(text="금리계산", font=("Arial", 20),bg="beige" , command = button2_function)
button2. place(x=280, y=500) 

button3 = Button(text="카드 종류", font=("Arial", 20),bg="beige" , command = button3_function)
button3. place(x=80, y=600)

button4 = Button(text="금융상품", font=("Arial", 20),bg="beige" , command = button4_function)
button4. place(x=280, y=600)


 




window.mainloop()





