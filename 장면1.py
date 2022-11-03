from tkinter import *

    
window = Tk()
window.title("장면1")
window.resizable(False, False)

canvas = Canvas(window, width=500, height=700, bg="blue")
canvas.pack()

img1=PhotoImage(file="수뭉.png")
canvas.create_image(230, 440, image=img1)


#레이블
label1 = Label(window, text="입금/출금" , font=("Arial", 24, "bold"), fg="white", bg="navy")
label1.place(x =180 , y = 55)
label2 = Label(window, text="↪입금/출금 시스템에 온 걸 환영해\n이용할 시스템을 골라줘!",font=("Arial", 20, "bold"), fg="white", bg="navy")
label2.place(x = 50, y = 500)

#버튼
button1 = Button(text = "출금", font=("Arial", 20),bg="beige")
button1.place(x = 130, y = 580)
button2 = Button(text = "입금", font=("Arial", 20),bg="beige")
button2.place(x = 290, y = 580)
      




window.mainloop()

