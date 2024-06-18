from tkinter import *
import os
import random
from PIL import Image, ImageTk
x=8
y=4
Aboba=[(x,y),(3,4)]
Aboba.remove(Aboba[1])
Aboba.remove(Aboba[0])
print(len(Aboba))
root = Tk()
root.title('Test')
root.geometry("300x400+600+200")
root.resizable(width=False, height=False)
money = 0

Rn = ['a','b','c','d','e','a2','b2','c2','d2','e2']


def PushBtn():
    global money,b
    b=15
    money+=1
    LabelMoney.config(text='Грошей:'+str(money), font=('Comic Sans MS', 15))
    b = b%10
    print(b)


LabelMoney = Label(text='Грошей:'+str(money), font=('Comic Sans MS', 15))


ImageButton = Image.open('SeaBattle_Images/red-cross.png')
ImageButton = ImageButton.resize((100 ,100))
ImageButton = ImageTk.PhotoImage(ImageButton)
btnImageButton = Button(image = ImageButton,command=PushBtn,text='onlinedddddd',state='disabled')
# btnImageButton.image = ImageButton

LabelMoney.place(x=100,y=50)
btnImageButton.place(x=90,y=150)
root.mainloop()

# a=1
# b=1
# print(a)
# print(b)
# for i in range(999998):
#     new=a+b
#     if i//2==i/2:
#         a=new
#     else:
#         b=new
#     print('\n'+str(new))

# import random, time
# d = 40
# while True:
#     a = random.randint(1,200)
#     c = random.randint(1,2)
#     b = a / 100
#     print(b)
#     if c == 1:
#         d = d + b
#     else:
#         d = d - b
#     format(d)
#     print(format(d, '.2f'))  # Вывод: 13.95. ...
#     time.sleep(0.1)

#print(10//1.33333)



# money = 1000
# AllCrypto = 242
# HaveDollar = 10
# my_file = open('Txt_Shop/save_1.txt', 'r+')
# #my_file.writelines(str(money)+'\n'+str(AllCrypto)+'\n'+str(HaveDollar))
# #my_file.close()
# with open('Txt_Shop/save_1.txt') as file:
#     try:
#       money = int((file.readline()).replace('\n',''))
#       AllCrypto = int((file.readline()).replace('\n',''))
#       HaveDollar = int((file.readline()).replace('\n', ''))
#     except:
#         pass


# print(money)
# print(AllCrypto)
# print(HaveDollar)


# n, m = map(int, input().split())
# find = False
#
# for f in range(n, m + 1):
#     sn = sum(i for i in range(1, f // 2 + 1) if f % i == 0)
#     if sn <= f or sn > m:
#         continue
#     sm = sum(i for i in range(1, sn // 2 + 1) if sn % i == 0)
#     if sm == f:
#         print(sm, sn)
#         find = True
#
# if not find:
#     print('Absent')


