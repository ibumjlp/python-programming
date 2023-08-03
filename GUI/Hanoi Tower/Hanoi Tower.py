from tkinter import *
import time

#กำหนด interface
game = Tk()
game.title("Hanoi Tower by Julla")
game.minsize(500,300)
game.maxsize(500,300)

#ใส่พื้นหลัง
ph = PhotoImage(file="เสา.png")
bg = Canvas(game,width=500,height=300)
bg.pack()
bg.create_image(0,0,anchor=NW,image=ph)

#สร้างชั้น
L1 = Label(game,text="111",height=1,bg="violetred1",fg="violetred1")
L2 = Label(game,text="22222",height=1,bg="firebrick1",fg="firebrick1")
L3 = Label(game,text="3333333",height=1,bg="orangered2",fg="orangered2")
##L4 = Label(game,text="444444444",height=1,bg="yellow2",fg="yellow2")
##L5 = Label(game,text="55555555555",height=1,bg="mediumspringgreen",fg="mediumspringgreen")
##L6 = Label(game,text="6666666666666",height=1,bg="mediumturquoise",fg="mediumturquoise")
##L7 = Label(game,text="777777777777777",height=1,bg="royalblue3",fg="royalblue3")
##L8 = Label(game,text="88888888888888888",height=1,bg="purple",fg="purple")
##L9 = Label(game,text="9999999999999999999",height=1,bg="black",fg="black")

ชื่อเกม = Label(game,text="Hanoi Tower",font="JasmineUPC 26 bold italic")
ชื่อเกม.place(x=165,y=-5)

ข้อความ = Label(game,text="ใส่จำนวนชั้น",font="Arial 13")
ข้อความ.place(x=130,y=43)

#รับ input จำนวนชั้น
ชั้น = IntVar()
ช่อง = Entry(game,width=3,textvariable=ชั้น)
ช่อง.place(x=230,y=45)

#ตำแหน่ง
l1 = int(89)
l2 = int(83)
l3 = int(77)
Y1 = int(260)
Y2 = int(240)
Y3 = int(220)
B = int(150)
C = int(300)

#ปุ่มสร้าง
def make():
    global mov
    mov = 7
    N = ชั้น.get()
##    if N == 1:
##        L5.place(x=600,y=180)
##        L4.place(x=600,y=160)
##        L3.place(x=600,y=140)
##        L2.place(x=600,y=120)
##        L1.place(x=l1,y=Y1)
##    elif N == 2:
##        L5.place(x=600,y=180)
##        L4.place(x=600,y=160)
##        L3.place(x=600,y=140)
##        L2.place(x=l2,y=Y1)
##        L1.place(x=l1,y=Y2)
    if N == 3:
##        L5.place(x=600,y=180)
##        L4.place(x=600,y=160)
        L3.place(x=l3,y=Y1)
        L2.place(x=l2,y=Y2)
        L1.place(x=l1,y=Y3)
##    elif N == 4:
##        L5.place(x=600,y=180)
##        L4.place(x=l4,y=Y1)
##        L3.place(x=l3,y=Y2)
##        L2.place(x=l2,y=Y3)
##        L1.place(x=l1,y=Y4)
##    elif N == 5:
##        L5.place(x=l5,y=Y1)
##        L4.place(x=l4,y=Y2)
##        L3.place(x=l3,y=Y3)
##        L2.place(x=l2,y=Y4)
##        L1.place(x=l1,y=Y5)
##    elif N == 6:
##        L6.place(x=59,y=260)
##        L5.place(x=65,y=240)
##        L4.place(x=71,y=220)
##        L3.place(x=77,y=200)
##        L2.place(x=83,y=180)
##        L1.place(x=89,y=160)
##    elif N == 7:
##        L7.place(x=53,y=260)
##        L6.place(x=59,y=240)
##        L5.place(x=65,y=220)
##        L4.place(x=71,y=200)
##        L3.place(x=77,y=180)
##        L2.place(x=83,y=160)
##        L1.place(x=89,y=140)
##    elif N == 8:
##        L8.place(x=47,y=260)
##        L7.place(x=53,y=240)
##        L6.place(x=59,y=220)
##        L5.place(x=65,y=200)
##        L4.place(x=71,y=180)
##        L3.place(x=77,y=160)
##        L2.place(x=83,y=140)
##        L1.place(x=89,y=120)
##    elif N == 9:
##        L9.place(x=41,y=260)
##        L8.place(x=47,y=240)
##        L7.place(x=53,y=220)
##        L6.place(x=59,y=200)
##        L5.place(x=65,y=180)
##        L4.place(x=71,y=160)
##        L3.place(x=77,y=140)
##        L2.place(x=83,y=120)
##        L1.place(x=89,y=100)
    else :
        เกิน = Label(game,text="ใส่ได้เฉพาะเลข 3 เท่านั้น")
        เกิน.place(x=195,y=72)
    finish.place(x=600,y=150)
สร้าง = Button(game,text="สร้าง",font="Arial 12",command=make)
สร้าง.place(x=270,y=39)

#ปุ่ม Reset
def Reset():
##    L9.place(x=600,y=260)
##    L8.place(x=600,y=240)
##    L7.place(x=600,y=220)
##    L6.place(x=600,y=200)
##    L5.place(x=600,y=180)
##    L4.place(x=600,y=160)
    global mov
    mov = 8
    finish.place(x=600,y=150)
    L3.place(x=600,y=140)
    L2.place(x=600,y=120)
    L1.place(x=600,y=100)
รี = Button(game,text="รีเซ็ต",font="Arial 12",command=Reset)
รี.place(x=315,y=39)

#ปุ่มต่อไป
mov = 7
def move():
        global mov
        X = ชั้น.get()
        if X == 3:
            if mov == 7:
                L1.place(x=l1+C,y=Y1)
                mov = mov-1
            elif mov == 6:
                L2.place(x=l2+B,y=Y1)
                mov = mov-1
            elif mov == 5:
                L1.place(x=l1+B,y=Y2)
                mov = mov-1
            elif mov == 4:
                L3.place(x=l3+C,y=Y1)
                mov = mov-1
            elif mov == 3:
                L1.place(x=l1,y=Y1)
                mov = mov-1
            elif mov == 2:
                L2.place(x=l2+C,y=Y2)
                mov = mov-1
            elif mov == 1:
                L1.place(x=l1+C,y=Y3)
                mov = mov-1
            elif mov == 0:
                finish.place(x=200,y=150)
finish = Label(game,text="FINISH",font="Arial 26 bold",fg="red")            
ต่อไป = Button(game,text="ต่อไป",font="Arial 12",command=move)
ต่อไป.place(x=358,y=39)

game.mainloop()

#ตัวอย่าง code recursive
##def hanoi (n,A,B,C):
##    if n == 1:
##        print("Move disc %s from %s to %s" %(n,A,B))
##        print(A,B,C)
##    else:
##        hanoi(n-1,A,C,B)
##        print("Move disc %s from %s to %s" %(n,A,B))
##        print(A,B,C)
##        hanoi(n-1,C,B,A)
##numb = int(input("How many discs : "))
##number = numb
##a = "A"
##b = "B"
##c = "C"
##print(a,b,c)
##hanoi(number,a,b,c)
