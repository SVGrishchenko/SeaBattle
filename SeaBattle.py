from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

root = Tk()
root.title('Sea Battle')
root.resizable(width=False, height=False)
canvas = Canvas(root, width=900, height=500,highlightthickness=0)
canvas.grid(row=0, column=2,padx=10, pady=10, ipadx=0, ipady=0,)
PL1 = []

for i in range(100):
    PL1.append(False)

# PL2Line1 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line2 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line3 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line4 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line5 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line6 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line7 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line8 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line9 =[False,False,False,False,False,False,False,False,False,False]
# PL2Line10 =[False,False,False,False,False,False,False,False,False,False]



def MainMenu():
    global BackG, gm_fr, gm_fr2,BackG_picture,gm_fr_picture,gm_fr2_picture,Ship4_picture,Ship4
    btnBackMainMenu.place_forget()

    BackG = ImageTk.PhotoImage(Bg)
    BackG_picture = canvas.create_image(-10, -3, image=BackG)

    gm_fr = ImageTk.PhotoImage(gm_sol)
    gm_fr_picture = canvas.create_image(220, 250, image=gm_fr)

    gm_fr2 = ImageTk.PhotoImage(gm_sol)
    gm_fr2_picture = canvas.create_image(250, 248, image=gm_fr2)

    Ship4 = ImageTk.PhotoImage(Ship4Im)
    Ship4_picture = canvas.create_image(800, 100, image=Ship4)

    btnPlayWithFriends.place(x=180,y=150)
    canvas.delete(Ship4_picture)


def DefPlayWithFriends():
    global Ship4,Ship4_picture,Ship3,Ship3_picture_1,Ship2,Ship2_picture,Ship1,Ship1_picture,Ship3_picture_2,FrS
    global Ship2_picture_2,Ship2_picture_3,Ship1_picture_2 ,Ship1_picture_3 ,Ship1_picture_4,Pole,Pole_picture
    canvas.delete(gm_fr_picture,gm_fr2_picture,BackG_picture)
    btnPlayWithFriends.place_forget()

    Ship4 = ImageTk.PhotoImage(Ship4Im)
    Ship4_picture = canvas.create_image(670, 50, image=Ship4)


    Ship3 = ImageTk.PhotoImage(Ship3Im)
    Ship3_picture_1 = canvas.create_image(560, 130, image=Ship3)
    Ship3_picture_2 = canvas.create_image(760, 130, image=Ship3)


    Ship2 = ImageTk.PhotoImage(Ship2Im)
    Ship2_picture = canvas.create_image(520, 200, image=Ship2)
    Ship2_picture_2 = canvas.create_image(670, 200, image=Ship2)
    Ship2_picture_3 = canvas.create_image(820, 200, image=Ship2)


    Ship1 = ImageTk.PhotoImage(Ship1Im)
    Ship1_picture = canvas.create_image(500, 250, image=Ship1)
    Ship1_picture_2 = canvas.create_image(620, 250, image=Ship1)
    Ship1_picture_3 = canvas.create_image(740, 250, image=Ship1)
    Ship1_picture_4 = canvas.create_image(850, 250, image=Ship1)

    Pole = ImageTk.PhotoImage(PL)
    Pole_picture = canvas.create_image(170,230,image = Pole)

    btnBackMainMenu.place(x=600,y=430)

    Entry4Ship.place(x=600,y=350)
    Enter4Ship.place(x=785,y=345)




def Coords():
    global coords,coordsX,coordsY
    coords += 11
    if coords % 10 == 1:
        coordsX = 145
    if coords % 10 == 2:
        coordsX = 185
    if coords % 10 == 3:
        coordsX = 220
    if coords % 10 == 4:
        coordsX = 260
    if coords % 10 == 5:
        coordsX = 300
    if coords % 10 == 6:
        coordsX = 335
    if coords % 10 == 7:
        coordsX = 375
    if coords % 10 == 8:
        coordsX = 410
    if coords % 10 == 9:
        coordsX = 445
    if coords // 10 == 1:
        coordsY = 60
    if coords // 10 == 2:
        coordsY = 102
    if coords // 10 == 3:
        coordsY = 144
    if coords // 10 == 4:
        coordsY = 186
    if coords // 10 == 5:
        coordsY = 223
    if coords // 10 == 6:
        coordsY = 262
    if coords // 10 == 7:
        coordsY = 302
    if coords // 10 == 8:
        coordsY = 344
    if coords // 10 == 9:
        coordsY = 386
    if coords // 10 == 10:
        coordsY = 428

def SetPL(x,y, value):
    if(x < 0 or x > 9 or y < 0 or y > 9):
        return
    PL1[coords + i + 10] = None

def Pos4Ship():
    global coords,Ship4_picture,Ship4, coordsX, coordsY,RedCross, RedCross_picture
    coords = int(Entry4Ship.get())
    coords = coords-11
    if (coords+3)//10==coords//10 and PL1[coords]!=None and PL1[coords+1]!=None and PL1[coords+2]!=None and PL1[coords+3]!=None:
        for i in range(4):
            PL1[coords+i] = True
            try:
                PL1[coords+i+10] =None
            except:
                 pass
            if coords//10!=0:
                try:
                    PL1[coords + i - 10] = None
                except:
                    pass
        if coords%10 !=0:
            PL1[coords-1] = None
            try:
                PL1[coords-1+10] = None
            except:
                pass
            if coords // 10 != 0:
                try:
                    PL1[coords-1-10] = None
                except:
                    pass
        if (coords+4) % 10 != 0:
            PL1[coords+4] = None
            try:
                PL1[coords+4+10] = None
            except:
                pass
            try:
                PL1[coords+4-10] = None
            except:
                pass
        canvas.delete(Ship4_picture)
        Ship4 = ImageTk.PhotoImage(Ship4Im)
        Coords()
        Ship4_picture = canvas.create_image(coordsX,coordsY, image= Ship4)
        print(PL1)
        Enter4Ship.config(command=lambda: Pos3Ship(1))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")



def Pos3Ship(v):
    global coords,Ship3_picture_1,Ship3, coordsX, coordsY,RedCross, RedCross_picture, Ship3_picture_2,Ship2_picture
    coords = int(Entry4Ship.get())
    coords = coords-11
    if (coords+2)//10==coords//10 and PL1[coords]!=None and PL1[coords+1]!=None and PL1[coords+2]!=None:
        for i in range(3):
            PL1[coords+i] = True
            try:
                PL1[coords+i+10] =None
            except:
                pass
            try:
                PL1[coords + i - 10] = None
            except:
                pass
        if coords%10 !=0:
            PL1[coords-1] = None
            try:
                PL1[coords-1+10] = None
            except:
                pass
            try:
                PL1[coords-1-10] = None
            except:
                pass
        if (coords+3) % 10 != 0:
            PL1[coords+3] = None
            try:
                PL1[coords+3+10] = None
            except:
                pass
            try:
                PL1[coords+3-10] = None
            except:
                pass
        Coords()
        coordsX= coordsX-20
        if v==1:
            Enter4Ship.config(command=lambda: Pos3Ship(2))
            canvas.delete(Ship3_picture_1)
            Ship3_picture_1 = canvas.create_image(coordsX, coordsY, image=Ship3)
        else:
            Enter4Ship.config(command=lambda: Pos2Ship(1))
            canvas.delete(Ship3_picture_2)
            Ship3_picture_2 = canvas.create_image(coordsX, coordsY, image=Ship3)
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    print(PL1)



def Pos2Ship(v):
    global coords,Ship2_picture,Ship2, coordsX, coordsY,Ship2_picture_2,Ship2_picture_3
    coords = int(Entry4Ship.get())
    coords = coords-11
    if (coords+1)//10==coords//10 and PL1[coords]!=None and PL1[coords+1]!=None:
        for i in range(2):
            PL1[coords+i] = True
            try:
                PL1[coords+i+10] =None
            except:
                pass
            try:
                PL1[coords + i - 10] = None
            except:
                pass
        if coords%10 !=0:
            PL1[coords-1] = None
            try:
                PL1[coords-1+10] = None
            except:
                pass
            try:
                PL1[coords-1-10] = None
            except:
                pass
        if (coords+2) % 10 != 0:
            PL1[coords+2] = None
            try:
                PL1[coords+2+10] = None
            except:
                pass
            try:
                PL1[coords+2-10] = None
            except:
                pass
        Coords()
        coordsX= coordsX-40
        if v==1:
            canvas.delete(Ship2_picture)
            Ship2_picture = canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos2Ship(2))
        if v==2:
            canvas.delete(Ship2_picture_2)
            Ship2_picture_2 = canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos2Ship(3))
        if v==3:
            canvas.delete(Ship2_picture_3)
            Ship2_picture_3= canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos1Ship(1))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    print(PL1)


def Pos1Ship(v):
    global coords,Ship1_picture,Ship1, coordsX, coordsY,Ship1_picture_2,Ship1_picture_3,Ship1_picture_4
    coords = int(Entry4Ship.get())
    coords = coords-11
    if PL1[coords]==False:
        PL1[coords] = True
        try:
            PL1[coords+10] =None
        except:
            pass
        try:
            PL1[coords - 10] = None
        except:
                pass
        if coords%10 !=0:
            PL1[coords-1] = None
            try:
                PL1[coords-1+10] = None
            except:
                pass
            try:
                PL1[coords-1-10] = None
            except:
                pass
        if (coords+1) % 10 != 0:
            PL1[coords+2] = None
            try:
                PL1[coords+2+10] = None
            except:
                pass
            try:
                PL1[coords+2-10] = None
            except:
                pass
        Coords()
        coordsX= coordsX-20
        if v==1:
            canvas.delete(Ship1_picture)
            Ship1_picture = canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(2))
        if v==2:
            canvas.delete(Ship1_picture_2)
            Ship1_picture_2 = canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(3))
        if v==3:
            canvas.delete(Ship1_picture_3)
            Ship1_picture_3= canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(4))
        if v==4:
            canvas.delete(Ship1_picture_4)
            Ship1_picture_4= canvas.create_image(coordsX,coordsY, image= Ship1)
            #Enter4Ship.config(command=lambda: Pos2Ship(3))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    print(PL1)



Bg = Image.open('SeaBattle_Images/photo_2024-05-12_16-58-46.jpg')
Bg = Bg.resize((1900,1500))

gm_sol = Image.open('SeaBattle_Images/png-transparent-business-man-drawing-cartoon-business-man-child-hand-people.jpg')
gm_sol = gm_sol.resize((100 ,100))

Ship4Im = Image.open('SeaBattle_Images/Ship4.png.')
Ship4Im = Ship4Im.resize((160,50))

Ship3Im = Image.open('SeaBattle_Images/Ship3.png')
Ship3Im = Ship3Im.resize((130,60))

Ship2Im = Image.open('SeaBattle_Images/Ship2.png')
Ship2Im = Ship2Im.resize((80,45))

Ship1Im = Image.open('SeaBattle_Images/Ship1.png')
Ship1Im = Ship1Im.resize((45,30))

CrossIm = Image.open('SeaBattle_Images/red-cross.png')
CrossIm = CrossIm.resize((50,50))

PL = Image.open('SeaBattle_Images/Pole.jpg')
PL = PL.resize((550,450))

btnPlayWithFriends=Button(text='Грати з друзями',width=17,height=3,command=DefPlayWithFriends)
btnBackMainMenu = Button(text='Назад в меню',width=30,height=5,command=MainMenu)
Enter4Ship = Button(text='enter', command=Pos4Ship)

Entry4Ship = Entry(width=30)



MainMenu()



root.mainloop()