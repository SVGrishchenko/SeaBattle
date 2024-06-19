from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

root = Tk()
root.title('Sea Battle')
root.resizable(width=False, height=False)
canvas = Canvas(root, width=900, height=500,highlightthickness=0)
canvas.grid(row=0, column=2,padx=10, pady=10, ipadx=0, ipady=0,)
Map1Pl = [[0 for x in range(10)] for y in range(10)]
Map2Pl = [[0 for x in range(10)] for y in range(10)]
Buttons1Pl = [[0 for x in range(10)] for y in range(10)]
Buttons2Pl = [[0 for x in range(10)] for y in range(10)]
InBattleShip1PL = 20
InBattleShip2PL = 20

CoordsShips_1PL = [[] for y in range(10)]
CoordsShips_2PL = [[] for y in range(10)]
for i in range(10):
    CoordsShips_1PL[i] = []
    CoordsShips_2PL[i] = []

def GetShipNumber(typeShip, numberShip):
    if typeShip==4:
        return 0;
    if typeShip==3:
        return numberShip;
    if typeShip==2:
        return 2+numberShip;
    if typeShip==1:
        return 5+numberShip;

def GetShipLenByNumber(shipNumber):
    if shipNumber == 0:
        return 4;
    if shipNumber >= 1 and shipNumber <= 2:
        return 3;
    if shipNumber >= 3 and shipNumber <= 5:
        return 2;
    else:
        return 1;


def PrintMap(pl):
    for i in range(10):
        for j in range(10):
            if pl==1:
                print(str(Map1Pl[i][j])[0], end=" ")
            else:
                print(str(Map2Pl[i][j])[0], end=" ")
        print()
    print()

def Coords0ShipValid(coords0, len,pl):
    x = coords0 % 10
    y = coords0 // 10
    if y < 0 or y > 9 or x < 0 or  (x + len - 1) > 9:
        return False
    for i in range(len):
        if pl==1:
            if GetMapXY(x+i,  y,1) != False:
                return False
        else:
            if GetMapXY(x+i,  y,2) != False:
                return False
    return True

def PosShip(coords, len,pl,typeShip,NumderShip):
    x = coords % 10
    y = coords // 10
    for i in range(len):
        SetMapXY(x+i, y-1, None, pl)
        SetMapXY(x+i, y, True, pl)
        SetMapXY(x+i, y+1, None, pl)
        ListKilled(x, y, i, typeShip, NumderShip, pl)
    for i in range(3):
        SetMapXY(x-1,  y-1+i, None,pl)
        SetMapXY(x+len, y-1+i, None,pl)

def SetMapXY(x,y,value, pl):
    if(x>=0 and x<10 and y>=0 and y<10):
        if pl == 1:
            Map1Pl[y][x] = value
        else:
            Map2Pl[y][x] = value

def GetMapXY(x,y,pl):
    if pl==1:
        return Map1Pl[y][x]
    else:
        return Map2Pl[y][x]
def MainMenu():
    global BackG, gm_fr, gm_fr2,BackG_picture,gm_fr_picture,gm_fr2_picture,Ship4_picture,Ship4,InBattleShip2PL,InBattleShip1PL
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
    btnNextPlayer.place_forget()
    btnGoToBattleWithFriends.place_forget()

    for i in range(100):
        Map1Pl[i // 10][i % 10] = False
        Map2Pl[i // 10][i % 10] = False

    Entry4Ship.place_forget()
    Enter4Ship.place_forget()
    Entry4Ship.delete(0, END)
    btnBackMainMenuFromBattle.place_forget()
    LabelWhoStep.place_forget()

    InBattleShip1PL = 20
    InBattleShip2PL = 20

    for x in range(10):
        CoordsShips_1PL[x]=[]
        CoordsShips_2PL[x]=[]
        for y in range(10):
            (Buttons1Pl[x][y]).fire=0
            (Buttons2Pl[x][y]).fire=0
            Buttons1Pl[x][y].config(state='normal',image=FonIm)
            Buttons2Pl[x][y].config(state='normal',image=FonIm)
            Buttons1Pl[x][y].place_forget()
            Buttons2Pl[x][y].place_forget()
            Map1Pl[x][y]=False
            Map2Pl[x][y]=False

def DefPlayWithFriends(pl):
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
    Pole_picture = canvas.create_image(150, 230,image = Pole)


    btnBackMainMenu.place(x=600,y=430)

    Entry4Ship.place(x=600,y=350)
    Enter4Ship.place(x=785,y=345)
    if pl==1:
        Enter4Ship.config(text='enter', command=lambda: Pos4Ship(1))
    else:
        Enter4Ship.config(text='enter', command=lambda: Pos4Ship(2))
        btnNextPlayer.place_forget()
        Entry4Ship.delete(0,END)


def Coords(type):
    global coords,coordsX,coordsY
    if type=='ship':
        coords += 11
        coordsX = 97 + (coords % 10) * 37.5
        coordsY = 19 + (coords // 10) * 39.75
    if type=='btn':
        coordsX = 64.5 + (coords % 10) * 37.5
        coordsY = 67 + (coords // 10) * 39.75
    if type=='btn2':
        coordsX = 514 + (coords % 10) * 37.5
        coordsY = 67 + (coords // 10) * 39.75
def Pos4Ship(pl):
    global coords,Ship4_picture,Ship4, coordsX, coordsY,RedCross, RedCross_picture
    coords = int(Entry4Ship.get())
    coords = coords-11
    if(Coords0ShipValid(coords, 4,pl) ):
        PosShip(coords,4,pl,4,1)
        canvas.delete(Ship4_picture)
        Ship4 = ImageTk.PhotoImage(Ship4Im)
        Coords('ship')
        Ship4_picture = canvas.create_image(coordsX,coordsY, image= Ship4)
        PrintMap(pl)
        Enter4Ship.config(command=lambda: Pos1Ship(4,pl))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")



def Pos3Ship(v,pl):
    global coords,Ship3_picture_1,Ship3, coordsX, coordsY,RedCross, RedCross_picture, Ship3_picture_2,Ship2_picture
    coords = int(Entry4Ship.get())
    coords = coords-11
    if(Coords0ShipValid(coords, 3,pl) ):
        PosShip(coords,3,pl,3,v)
        Coords('ship')
        coordsX= coordsX-20
        if v==1:
            Enter4Ship.config(command=lambda: Pos3Ship(2,pl))
            canvas.delete(Ship3_picture_1)
            Ship3_picture_1 = canvas.create_image(coordsX, coordsY, image=Ship3)
        else:
            Enter4Ship.config(command=lambda: Pos2Ship(1,pl))
            canvas.delete(Ship3_picture_2)
            Ship3_picture_2 = canvas.create_image(coordsX, coordsY, image=Ship3)
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    PrintMap(1)



def Pos2Ship(v,pl):
    global coords,Ship2_picture,Ship2, coordsX, coordsY,Ship2_picture_2,Ship2_picture_3
    coords = int(Entry4Ship.get())
    coords = coords-11
    if(Coords0ShipValid(coords, 2,pl) ):
        PosShip(coords,2,pl,2,v)
        Coords('ship')
        coordsX= coordsX-40
        if v==1:
            canvas.delete(Ship2_picture)
            Ship2_picture = canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos2Ship(2,pl))
        if v==2:
            canvas.delete(Ship2_picture_2)
            Ship2_picture_2 = canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos2Ship(3,pl))
        if v==3:
            canvas.delete(Ship2_picture_3)
            Ship2_picture_3= canvas.create_image(coordsX,coordsY, image= Ship2)
            Enter4Ship.config(command=lambda: Pos1Ship(1,pl))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    PrintMap(1)


def Pos1Ship(v,pl):
    global coords,Ship1_picture,Ship1, coordsX, coordsY,Ship1_picture_2,Ship1_picture_3,Ship1_picture_4
    coords = int(Entry4Ship.get())
    coords = coords-11
    if(Coords0ShipValid(coords, 1,pl) ):
        PosShip(coords,1,pl,1,v)
        Coords('ship')
        coordsX= coordsX-60
        if coords%10==0:
            coordsX=420
            if coords//10==2:
                coordsY=67
            if coords//10==3:
                coordsY=106
            if coords//10==4:
                coordsY=146
            if coords//10==5:
                coordsY=188
            if coords//10==6:
                coordsY=230
            if coords//10==7:
                coordsY=270
            if coords//10==8:
                coordsY=310
            if coords//10==9:
                coordsY=350
            if coords//10==10:
                coordsY=395
            if coords//10==11:
                coordsY=435
        if v==1:
            canvas.delete(Ship1_picture)
            Ship1_picture = canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(2,pl))
        if v==2:
            canvas.delete(Ship1_picture_2)
            Ship1_picture_2 = canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(3,pl))
        if v==3:
            canvas.delete(Ship1_picture_3)
            Ship1_picture_3= canvas.create_image(coordsX,coordsY, image= Ship1)
            Enter4Ship.config(command=lambda: Pos1Ship(4,pl))
        if v==4:
            canvas.delete(Ship1_picture_4)
            Ship1_picture_4= canvas.create_image(coordsX,coordsY, image= Ship1)
            Entry4Ship.place_forget()
            Enter4Ship.place_forget()
            if pl==1:
                btnNextPlayer.place(x=600,y=350)
            if pl==2:
                btnGoToBattleWithFriends.place(x=600,y=430)
            #Enter4Ship.config(command=lambda: Pos2Ship(3))
    else:
        messagebox.showerror("Помилка", "Сюди неможливо поставити корабель, бо він не вміщяеться в рядку"
                                        "або туди заборонено ставити")
    PrintMap(1)


def defGoToBattleWithFriends():
    global Pole_picture1Pl,Pole_picture2Pl,coords
    Pole_picture2Pl = canvas.create_image(600, 230, image=Pole)
    Pole_picture1Pl = canvas.create_image(150, 230, image=Pole)
    btnGoToBattleWithFriends.place_forget()
    btnBackMainMenu.place_forget()
    for x in range(10):
        for y in range(10):
            coords=x*10+y
            Coords('btn')
            Buttons1Pl[x][y].place(x=coordsX, y=coordsY)
    for x in range(10):
        for y in range(10):
            coords=x*10+y
            Coords('btn2')
            Buttons2Pl[x][y].place(x=coordsX, y=coordsY)
    LabelWhoStep.config(image=StepNone)
    LabelWhoStep.place(x=440,y=232)


def DefFire(pl,x,y):
    global InBattleShip1PL,InBattleShip2PL
    if pl==1:
        if Map1Pl[x][y]==True:
            Map1Pl[x][y]='W'
            Buttons1Pl[x][y].config( image=CrossIm,state='disabled')
            (Buttons1Pl[x][y]).fire = 1
            InBattleShip1PL = InBattleShip1PL-1
            LabelWhoStep.config(image=Step1PL)
            CheckKilled(x, y, pl)
            if InBattleShip1PL==0:
                ShowSurvivalShip()
                messagebox.showinfo('Перемога','Переміг 2 гравець')
                btnBackMainMenuFromBattle.place(x=420,y=463)
        else:
            NextStep(pl)
            (Buttons1Pl[x][y]).fire = 1
            Buttons1Pl[x][y].config(image=BlackDot ,state='disabled')
    if pl==2:
        if Map2Pl[x][y]==True:
            Map2Pl[x][y]='W'
            Buttons2Pl[x][y].config( image=CrossIm,state='disabled')
            InBattleShip2PL = InBattleShip2PL-1
            (Buttons2Pl[x][y]).fire = 1
            LabelWhoStep.config(image=Step2PL)
            if InBattleShip2PL==0:
                ShowSurvivalShip()
                messagebox.showinfo('Перемога','Переміг 1 гравець')
            CheckKilled(x,y,pl)
        else:
            NextStep(pl)
            (Buttons2Pl[x][y]).fire = 1
            Buttons2Pl[x][y].config(image=BlackDot ,state='disabled')


def ListKilled(x,y,i,typeShip,NumderShip,pl):
    shipNumber = GetShipNumber(typeShip,NumderShip)
    if pl==1:
        CoordsShips_1PL[shipNumber].append((x + i, y))
        print(CoordsShips_1PL[shipNumber])
    if pl==2:
         CoordsShips_2PL[shipNumber].append((x + i, y))
         print(CoordsShips_2PL[shipNumber])


def CheckKilled(x,y,pl):
    if pl==1:
        for i in range(10):
            if(y,x) in CoordsShips_1PL[i]:
                CoordsShips_1PL[i].remove((y, x))
                if len(CoordsShips_1PL[i]) == 0:
                    x1 = FindFirstPos(x, y, pl)
                    PosDotButtons(x, x1, GetShipLenByNumber(i), pl)
    else:
        for i in range(10):
            if (y, x) in CoordsShips_2PL[i]:
                CoordsShips_2PL[i].remove((y, x))
                if len(CoordsShips_2PL[i]) == 0:
                    x1 = FindFirstPos(x, y, pl)
                    PosDotButtons(x, x1, GetShipLenByNumber(i), pl)
def FindFirstPos(y,x, pl):
    pos = x
    while True:
        if pl==1:
            if pos == 0:
                return pos
            if Map1Pl[y][pos-1] == None:
                return pos
            if Map1Pl[y][pos-1] == 'W':
                pos = pos -1
            else:
                print('error')
                return pos
        else:
            if pos == 0:
                return pos
            if Map2Pl[y][pos-1] == None:
                return pos
            if Map2Pl[y][pos-1] == 'W':
                pos = pos -1
            else:
                print('error')
                return pos


def PosDotButtons(y, x, len,pl):
    for i in range(len):
            SetBtnXY(y-1, x+i, pl)
            SetBtnXY(y+1, x+i, pl)
    for i in range(3):
            SetBtnXY(y-1+i, x-1,pl)
            SetBtnXY(y-1+i, x+len,pl)

def SetBtnXY(y,x, pl):
    if(x>=0 and x<10 and y>=0 and y<10):
        if pl == 1:
            (Buttons1Pl[y][x]).fire = 1
            Buttons1Pl[y][x].config(image=BlackDot ,state='disabled')
        else:
            Buttons2Pl[y][x].config(image=BlackDot ,state='disabled')
            (Buttons2Pl[y][x]).fire = 1

def NextStep(pl):
    if pl==1:
        for x in range(10):
            for y in range(10):
                Buttons1Pl[x][y].config(state='disabled')
                LabelWhoStep.config(image=Step2PL)
                if (Buttons2Pl[x][y]).fire == 0:
                    Buttons2Pl[x][y].config(state='normal')
                else:
                    Buttons2Pl[x][y].config(state='disabled')
    if pl==2:
        for x in range(10):
            for y in range(10):
                Buttons2Pl[x][y].config(state='disabled')
                LabelWhoStep.config(image=Step1PL)
                if (Buttons1Pl[x][y]).fire == 0:
                    Buttons1Pl[x][y].config(state='normal')
                else:
                    Buttons2Pl[x][y].config(state='disabled')


def ShowSurvivalShip():
    for x in range(10):
        for y in range(10):
            if Map1Pl[x][y]==True:
                Buttons1Pl[x][y].config(image=BlueCross)
            if Map2Pl[x][y]==True:
                Buttons2Pl[x][y].config(image=BlueCross)

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
CrossIm = CrossIm.resize((40,40))
CrossIm = ImageTk.PhotoImage(CrossIm)

FonIm = Image.open('SeaBattle_Images/fon.png')
FonIm = FonIm.resize((25,25))
FonIm = ImageTk.PhotoImage(FonIm)

BlackDot = Image.open('SeaBattle_Images/BlackDot.png')
BlackDot = BlackDot.resize((50,50))
BlackDot = ImageTk.PhotoImage(BlackDot)

StepNone = Image.open('SeaBattle_Images/Green_triangle_None.png')
StepNone = StepNone.resize((40,40))
StepNone = ImageTk.PhotoImage(StepNone)

Step1PL = Image.open('SeaBattle_Images/Green_triangle_1Pl.png')
Step1PL = Step1PL.resize((40,40))
Step1PL = ImageTk.PhotoImage(Step1PL)

Step2PL = Image.open('SeaBattle_Images/Green_triangle_2Pl.png')
Step2PL = Step2PL.resize((40,40))
Step2PL = ImageTk.PhotoImage(Step2PL)

BlueCross = Image.open('SeaBattle_Images/Blue_cross.png')
BlueCross = BlueCross.resize((50,50))
BlueCross = ImageTk.PhotoImage(BlueCross)

PL = Image.open('SeaBattle_Images/Pole.jpg')
PL = PL.resize((550,450))
for x in range(10):
    for y in range(10):
        Buttons1Pl[x][y] = Button(image=FonIm,height=25, width=25,command=lambda x1=x, y1=y: DefFire(1,x1,y1))
        (Buttons1Pl[x][y]).fire = 0
        Buttons2Pl[x][y] = Button(image=FonIm, height=25, width=25,command=lambda x2=x, y2=y: DefFire(2,x2,y2) )
        (Buttons2Pl[x][y]).fire = 0

btnPlayWithFriends=Button(text='Грати з друзями',width=17,height=3,command=lambda: DefPlayWithFriends(1))
btnBackMainMenu = Button(text='Назад в меню',width=30,height=5,command=MainMenu)
Enter4Ship = Button(text='enter', command=lambda: Pos4Ship(1))
btnNextPlayer = Button(text='Наступний гравець',width=30,height=5,command=lambda: DefPlayWithFriends(2))
btnGoToBattleWithFriends = Button(text='В бій!',width=30,height=5,command=defGoToBattleWithFriends)
btnBackMainMenuFromBattle = Button(text='Назад в меню',width=12,height=3,command=MainMenu)

Entry4Ship = Entry(width=30)

LabelWhoStep = Label(image=StepNone, bg='white')



MainMenu()



root.mainloop()