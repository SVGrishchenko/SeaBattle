from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random
import os
from PIL import Image, ImageTk
money = 100000000
temp = 0
after_id = ''
current = 0
current2 = 0
count =0
count2 = 0
Cards = [2,3,4,5,6,7,8,9 , 10 , 11, 10, 10, 10] *4
random.shuffle(Cards)
Rayt = 0
k = 0
m = 0
TempOrend1Room = 0
AfterIdOrend1Room = ''
Orend1RoomChange = False
TempOrend2Room = 0
AfterIdOrend2Room = ''
Orend2RoomChange = False
Orend3RoomChange = False
TempOrend3Room = 0
AfterIdOrend3Room = ''
s3Room = 0
Orend1HouseChange = False
TempOrend1House  = 0
AfterIdOrend1House = ''
s1House = 0
VideoCard1House = False
MainingIn1House = False
MainingSetUp1House = False
FrameForMining1House = False
CanGoToBasement1Home = False
TempMaining1House = 0
AfterIdMaining1House = ''
Crypto1House = 0
Maining1HouseChange = False
ReadySellShopCoins = 0
VideoCard2House = False
FrameForMining2House = False
MainingIn2House = False
MainingSetUp2House = False
Orend2HouseChange = False
TempOrend2House = 0
AfterIdOrend2House = ''
s2House = 0
Maining2HouseChange = False
TempMaining2House = 0
Crypto2House = 0
Orend3HouseChange = False
VideoCard3House = False
FrameForMining3House = False
MainingIn3House =  False
MainingSetUp3House = False
Maining3HouseChange = False
TempOrend3House = 0
AfterIdOrend3House = ''
s3House = 0
Crypto3House = 0
TempMaining3House = 0
AfterIdMaining3House = ''
b = 0
TempCourseChangeShopCoins = 0
AfterIdCourseChangeShopCoins = ''
sCourseChangeShopCoins = 0
CoursShopCoins = 100
UpOrDown = 'xz'
MovementShopCoins = 0
WantBuyShopCoins = 0
SumBuyShopCoins = 0
ReadyCharity = 0
HaveShopCoins = 0
HaveDollar = 0
TempCourseChangeDollar = 0
AfterIdCourseChangeDollar = ''
sCourseChangeDollar = 0
CoursDollar = 30
UpOrDownDollar = 'xz'
MovementDollar = 0
WantBuyDollar = 0
SumBuyDollar = 0
Liters = [' а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'c',
          'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
FirstLeters = None
HaveSausage = 0
HaveCheese = 0
HaveThan = 0
HaveFlour = 0
HaveChocolate = 0
HaveCola = 0
HaveBread = 0
HaveOil = 0
HaveBowl = 0
HaveSalt = 0
HaveSalad = 0
HaveTomato = 0
HaveCucumber = 0
HaveCutSausage = 0
HaveCutCheese = 0
HaveCutChocolate = 0
HaveCutBread = 0
HaveCutSalad = 0
HaveCutTomato = 0
HaveCutCucumber = 0
HaveSalat = 0
HaveButerbrod = 0
ReadySellDollar = 0
PromoCodeAmogus = False
PromoCodeUpdate_dowN_BlockNot = False
PromoCodeSecret_Charity_SUS = False
PromoCodeAmogus2024 = False
PromoCodeFrog = False
PromoCodeAbyba = False
PromoCodeShop = False
HaveDollarInBedsideTable = 0
HaveMoneyInBedsideTable = 0
PromoCodeStop_Orend_3_House = False
PromoCodeMining_1House_lox_=False
PromoCodeStooopOrend_One_Room=False
MemeBedsideTable = False
PinCode = 0
MoneyOnBankCard = 0
PayInExchangeCenter = 'Money'
ProofPinCode = 0
PayInShop ='Money'
PromoDontHaveMoneyShop = False
PayInMarket = 'Money'
PayInCasino = 'Money'
PayInCharity = 'Money'
MoneyOnDeposit = 0
TempDeposit = 0
AfterIdDeposit = ''
AllTaxes = 0
TempTaxes = 0
AfterIdTaxes = ''
Taxes1Room=0
Taxes2Room=0
Taxes3Room=0
Taxes1House=0
Taxes2House=0
Taxes3House=0
Have1Room = False
Have2Room = False
Have3Room = False
Have1House = False
Have2House = False
Have3House = False
PayTaxes = 'Money'
NameSave1 = ''
NameSave2 = ''
NameSave3 = ''
NameSave4 = ''
HaveSave = 0
HaveBedSideTable = False
HaveBankCard = False
HaveStuffing = 0
HaveSpaghetti = 0
HaveCookSpaghetti = 0
HaveCutlet = 0
HaveSpaghettiWithCutlet = 0
NowSave=0
HaveStarCoinInApp =10
UpgradeStarCoin = 0.01
HaveStarCoin = 0
CoursStarCoin = 30
TempCourseChangeStarCoin = 0
AfterIdCourseChangeStarCoin = ''
sCourseChangeStarCoin = 0
UpOrDownStarCoin = 0
MovementStarCoin = 0
WantBuyStarCoin = 0
SumBuyStarCoin = 0
#Інтерфейс для гри магазин
#Налаштування вікна
def on_close():
    if messagebox.askokcancel("Вихід", 'Ви точно хочете вийти?'):
        Save_saves = open('Txt_Shop/save/save_saves_name.txt', 'r+')
        Save_saves.writelines(NameSave1+'\n'+NameSave2+'\n'+NameSave3+'\n'+NameSave4+'\n'+str(HaveSave))
        Save_saves.close()
        root.destroy()
root = Tk()
root.title('Shop')
root.geometry("300x400+600+200")
root.resizable(width=False, height=False)
root.attributes("-topmost",True)
root.protocol('WM_DELETE_WINDOW', on_close)
with open('Txt_Shop/save/save_saves_name.txt') as file:
     try:
       NameSave1 = (file.readline()).replace('\n','')
       NameSave2 = (file.readline()).replace('\n','')
       NameSave3 = (file.readline()).replace('\n', '')
       NameSave4 = (file.readline()).replace('\n', '')
       HaveSave = int((file.readline()).replace('\n', ''))
     except:
         pass

#Скріпти яку виконуються при натисканні кнопок
#Повертає на сторінку з кнопками Start і Help

def ReturnToStart():
    HelpLabel.place_forget()
    ButtonBack.place_forget()
    WelcomeTitle.place(x=-35, y=20)
    btnHelp.place(x=3, y=320)
    btnStart.place(x=160, y=320)
def Back():
    global money, HaveSausage, HaveCheese,HaveThan,HaveFlour,HaveChocolate, HaveCola, HaveBread,HaveOil,HaveBowl,HaveSalt,HaveSalad,HaveTomato, HaveCucumber
    global HaveCutSausage, HaveCutCheese, HaveCutChocolate, HaveCutBread,HaveCutSalad,HaveCutTomato,HaveCutCucumber, HaveSalat, HaveButerbrod
    if messagebox.askokcancel("Підтвердження.","Ви точно хочете почати все с початку? ваші продукти, ваші гроші ваша нерухомість і все інше не збережиться(зверху буде написано скільки у вас було грошей коли ви вийшли з гри і гра закриється)?"):
        # Howmuchmoney.config(state='normal')
        # Howmuchmoney.delete(0, END)
        # Howmuchmoney.config(state='readonly')
        WelcomeTitle.place(x=-35, y=20)
        btnStart.place(x=160, y=320)
        btnHelp.place(x=3, y=320)
        HelpLabel.place(x=400, y=20)
        ButtonBack.place(x=300,y=320)
        btnGoHome.place(x=0, y=2200)
        btnGoShop.place(x=160, y=2200)
        bthGoMarket.place(x=0, y=1000)
        btnGoCasino.place(x=160, y=1000)
        ListBuy.place(x=0, y=1800)
        ListCook.place(x=160, y=1800)
        Real_estate.place(x=0, y=2600)
        NextListMeinMenu.place(x=160, y=2600)
        Reset.place(x=5, y=3370)
        root.destroy()

#Відправляє тебе на сторінку Help
def Help():
    WelcomeTitle.place(x=300, y=20)
    btnStart.place(x= 300, y=320)
    btnHelp.place(x=300, y=320)
    HelpLabel.place(x=-30, y=20)
    ButtonBack.place(x=60, y=310)

#Початок гри
def Start():
    WelcomeTitle.place(x=300, y=20)
    btnStart.place(x= 300, y=320)
    btnHelp.place(x=300, y=320)
    LabelBeforeEnter.place(x=-35,y=20)
    btnSave.place(x=72,y=250)
    btnAddSave.place_forget()
    LabelSave1.place_forget()
    btnSaveIn1File.place_forget()
    btnUploadFrom1File.place_forget()
    btnDeleat1File.place_forget()
    LabelSave2.place_forget()
    btnSaveIn2File.place_forget()
    btnUploadFrom2File.place_forget()
    btnDeleat2File.place_forget()
    LabelSave3.place_forget()
    btnSaveIn3File.place_forget()
    btnUploadFrom3File.place_forget()
    btnDeleat3File.place_forget()
    LabelSave4.place_forget()
    btnSaveIn4File.place_forget()
    btnUploadFrom4File.place_forget()
    btnDeleat4File.place_forget()
    Lines1.place_forget()
    Lines2.place_forget()
    Lines3.place_forget()
    BackTo2ListMainMenu.place_forget()

    #if (messagebox.askyesno(title="Запит", message="Перенести дані?")):
        #print('sss')
def Enter():
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    LabelBeforeEnter.place(x=1000,y=1000)
    btnGoHome.place(x=0, y=22)
    btnGoShop.place(x=160, y=22)
    bthGoMarket.place(x=0, y=100)
    btnGoCasino.place(x=160, y=100)
    ListBuy.place(x=0, y=180)
    ListCook.place(x=160, y=180)
    Real_estate.place(x=0, y=260)
    NextListMeinMenu.place(x=160, y=260)
    Reset.place(x=5, y=337)
    tickCourseChangeShopCoins()
    tickCourseChangeDollar()
    tickCourseChangeStarCoin()
    btnSave.place_forget()
    BackTo2ListMainMenu.config(command=DefBackTo2ListMainMenu)
    BackTo2ListMainMenu.place_forget()
# def Clear():
#     Howmuchmoney.config(state='normal')
#     Howmuchmoney.delete(0, END)
#     Howmuchmoney.config(state='readonly')
#Пішов в магазин

def tickCourseChangeShopCoins():
    global TempCourseChangeShopCoins, AfterIdCourseChangeShopCoins, sCourseChangeShopCoins, CoursShopCoins, UpOrDown, MovementShopCoins
    AfterIdCourseChangeShopCoins = root.after(33333,tickCourseChangeShopCoins)
    FTempCourseChangeShopCoins = datetime.fromtimestamp(TempCourseChangeShopCoins).strftime('%M:%S')
    TempCourseChangeShopCoins +=1
    if TempCourseChangeShopCoins == 2:
        #print('aboba')
        TempCourseChangeShopCoins = 1
        TempCourseChangeShopCoins = 1
        UpOrDown = random.randint(1,2) # Якщо 1 то -      #Якщо 2 то +
        #print(UpOrDown)
        MovementShopCoins = random.randint(1,10)
        #print(MovementShopCoins)
        if UpOrDown == 1:
            CoursShopCoins = CoursShopCoins - MovementShopCoins
        else:
            CoursShopCoins = CoursShopCoins + MovementShopCoins
        if CoursShopCoins<=15:
            CoursShopCoins = CoursShopCoins + MovementShopCoins
        CourseCurrency.config(text='1 ShopCoin - ' + str(CoursShopCoins) + ' грн')


def tickCourseChangeDollar():
    global TempCourseChangeDollar, AfterIdCourseChangeDollar, sCourseChangeDollar, CoursDollar, UpOrDownDollar, MovementDollar
    AfterIdCourseChangeDollar = root.after(60000,tickCourseChangeDollar)
    FTempCourseChangeDollar = datetime.fromtimestamp(TempCourseChangeDollar).strftime('%M:%S')
    TempCourseChangeDollar +=1
    if TempCourseChangeDollar == 2:
        MovementDollar = random.randint(1, 300)
        UpOrDownDollar = random.randint(1, 2)
        MovementDollar = MovementDollar / 100
        sCourseChangeDollar = 1
        TempCourseChangeDollar = 1
        if UpOrDownDollar == 1:
            CoursDollar = CoursDollar +MovementDollar
        else:
            CoursDollar = CoursDollar - MovementDollar
        if CoursDollar<=5:
            CoursDollar = CoursDollar + MovementDollar
        format(CoursDollar)
        CourseCurrencyDollar.config(text='1 Доллар - ' + format(CoursDollar, '.2f') + ' грн')


def GoShop():
    ListCook.place(x=1000,y=1000)
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    Sausage.place(x=0, y =22)
    Than.place(x=160, y=22)
    Cheese.place(x=0, y=100)
    Flour.place(x=160, y=100)
    Chocolate.place(x=0, y=180)
    Cola.place(x=160, y= 180)
    Bread.place(x=0, y=260)
    NextListShop.place(x=160, y=260)
    BackMainMenu.place(x=2, y=340)
    BuyMoreProduct0.place_forget()
    BuyMoreProduct1.place_forget()
    BuyMoreProduct2.place_forget()
    BuyMoreProduct3.place_forget()
    BuyMoreProduct4.place_forget()
    BuyMoreProduct5.place_forget()
    BuyMoreProduct6.place_forget()
    BuyMoreProduct7.place_forget()
    BuyMoreProduct8.place_forget()
    BuyMoreProduct9.place_forget()
    BuyMoreProductEntr1.place_forget()
    BuyMoreProductClear1.place_forget()
    BuyMoreProductEntry.place_forget()
#Пішов до дому
def GoHome():
    global temp
    temp = 0
    NextListCut.place(x=1000, y=1000)
    CookSalat.place(x=1000,y=1000)
    CutSausage.place(x=0, y=2200)
    CutThan.place(x=160, y=2200)
    CutCheese.place(x=0, y=1000)
    CutFlour.place(x=160, y=1000)
    CutChocolate.place(x=0, y=1800)
    CutCola.place(x=160, y=1800)
    CutBread.place(x=0, y=2600)
    CutCucumber.place(x=160, y=2600)
    btnCut.place(x=1000,y=1000)
    ListCook.place(x=1000,y=1000)
    CookButerbrod.place(x=0, y=2200)
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    GoCook.place(x=75,y=100)
    GoSleep.place(x=75, y=160)
    btnBedsideTable.place(x=75, y=220)
    DoInHome.place(x=-15, y=-66)
    BackMainMenu.place(x=2, y=340)
    btnStartTaimer.place(x=1000,y=1000)
    LabelSleep.place(x=1000,y=1000)
    btnContinuetTaimer.place(x=25, y=2000)
    CutOil.place(x=0, y=2200)
    CutBowl.place(x=160, y=2200)
    CutSalt.place(x=0, y=1000)
    CutSalat.place(x=160, y=1000)
    CutTomato.place(x=0, y=1800)
    CutCucumber.place(x=160, y=1800)
    LabelMainingFarm1.place_forget()
    LabelMainingFarm2.place_forget()
    LabelMainingFarm3.place_forget()
    LabelMainingFarm4.place_forget()
    LabelMainingFarm5.place_forget()
    btnStartMining2House.place_forget()
    LabelTaimerMaining2House.place_forget()
    btnCanGoTOBasement2House.place_forget()
    btnStopTaimerMaining2House.place_forget()
    LabelMainingFarm6.place_forget()
    LabelMainingFarm7.place_forget()
    LabelHalfMainingFarm1.place_forget()
    NextListMaining2House.place_forget()
    LabelHouse2Interier2.place_forget()
    LabelHouse2Interier1.place_forget()
    NextListInterier2House.place_forget()
    DefHideMoreProduct()
    TimeSleep.place_forget()
    btnPutInTheBedsideTable.place_forget()
    btnTakeFromBedsideTable.place_forget()
    btnInformationAboutWhatInTheBedsideTable.place_forget()
    LabelInfoBedsideTable.place_forget()
    LabelPutInBedsideTableDollar.place_forget()
    LabelPutInBedsideTable.place_forget()
    EntryInfoDollarInBedsideTable.config(state='normal')
    EntryInfoMoneyInBedsideTable.config(state='normal')
    EntryInfoDollarInBedsideTable.delete(0, END)
    EntryInfoMoneyInBedsideTable.delete(0, END)
    EntryInfoDollarInBedsideTable.place_forget()
    EntryInfoMoneyInBedsideTable.place_forget()
    LabelInfoWhatInBedsideTable.place_forget()
    btnFry.place_forget()
    btnBoil.place_forget()
    btnCookIngredient.place_forget()
    btnCookSpaghettiWithCutlet.place_forget()
#Пішов на ринок
def GoMarket():
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    ListCook.place(x=1000,y=1000)
    SellButerbrod.place(x=0, y =22)
    BackMainMenu.place(x=2, y=340)
    SellSalat.place(x=160, y=22)
    btnSellSpaghettiWithCutlet.place(x=0,y=102)
#Пішов в казино
def GoKasino():
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    ListCook.place(x=1000, y=1000)
    btnmoney10.place(x=55, y=320)
    btnmoney11.place(x=55, y=160)
    btnmoney12.place(x=120, y=160)
    btnmoney13.place(x=185, y=160)
    btnmoney14.place(x=55, y=200)
    btnmoney15.place(x=120, y=200)
    btnmoney16.place(x=185, y=200)
    btnmoney17.place(x=55, y=240)
    btnmoney18.place(x=120, y=240)
    btnmoney19.place(x=185, y=240)
    btnmoneyEntr1.place(x=55, y=280)
    btnmoneyClear1.place(x=150, y=280)
    RateKasino.place(x=62, y=140)
    Rate.place(x=50,y=00)

def OneDigit (c):
    RateKasino.config(state='normal')
    RateKasino.insert(END, c)
    RateKasino.config(state='readonly')

def Enter1():
    global money
    global a
    global Rayt, ScoreYou
    if PayInCasino=='Money':
        if PayInCasino=='Money' and int(RateKasino.get()) <= money:
            Rayt = RateKasino.get()
            Rayt = int(Rayt)
            BackMainMenu.place(x=2, y=340)
            RateKasino.place(x=62, y=1000)
            btnmoney11.place(x= 55, y= 1000)
            btnmoney12.place(x= 120, y= 1000)
            btnmoney13.place(x= 185, y= 1000)
            btnmoney14.place(x= 55, y= 1000)
            btnmoney15.place(x= 120, y= 1000)
            btnmoney16.place(x=185, y=1000)
            btnmoney17.place(x= 55, y= 1000)
            btnmoney18.place(x= 120, y= 1000)
            btnmoney19.place(x= 185, y= 1000)
            btnmoneyEntr1.place(x= 55, y= 1000)
            btnmoneyClear1.place(x= 150, y= 1000)
            QuestionMoney.place(x=-10, y=1000)
            btnmoney10.place(x=55, y=3200)
            ScoreYou = Label(frame, text='У вас: ' + str(count) + ' очок', height=1, width=15, font='April 15', bg='white' )
            ScoreYou.place(x=65, y=210)
            GetCard.place(x=0,y=260)
            StopKasino.place(x=150,y=260)
            GetCard.config(state=NORMAL)
            StopKasino.config(state=NORMAL)
            Rate.place(x=1000,y=1000)
            return
        else:
            messagebox.askokcancel("Помилка",'Ти не можеш поставити більше ніж у тебе є')
    else:
        if PayInCasino == 'BankCard' and int(RateKasino.get()) <= MoneyOnBankCard and ProofPinCode==PinCode:
            Rayt = RateKasino.get()
            Rayt = int(Rayt)
            BackMainMenu.place(x=2, y=340)
            RateKasino.place(x=62, y=1000)
            btnmoney11.place(x= 55, y= 1000)
            btnmoney12.place(x= 120, y= 1000)
            btnmoney13.place(x= 185, y= 1000)
            btnmoney14.place(x= 55, y= 1000)
            btnmoney15.place(x= 120, y= 1000)
            btnmoney16.place(x=185, y=1000)
            btnmoney17.place(x= 55, y= 1000)
            btnmoney18.place(x= 120, y= 1000)
            btnmoney19.place(x= 185, y= 1000)
            btnmoneyEntr1.place(x= 55, y= 1000)
            btnmoneyClear1.place(x= 150, y= 1000)
            QuestionMoney.place(x=-10, y=1000)
            btnmoney10.place(x=55, y=3200)
            ScoreYou = Label(frame, text='У вас: ' + str(count) + ' очок', height=1, width=15, font='April 15', bg='white' )
            ScoreYou.place(x=65, y=210)
            GetCard.place(x=0,y=260)
            StopKasino.place(x=150,y=260)
            GetCard.config(state=NORMAL)
            StopKasino.config(state=NORMAL)
            Rate.place(x=1000,y=1000)
        else:
            messagebox.askokcancel("Помилка",'Ти не можеш поставити більше ніж у тебе є')
def Clear1():
    RateKasino.config(state='normal')
    RateKasino.delete(0, END)
    RateKasino.config(state='readonly')
#Кнопка в головне меню
def DefBackMainMenu():
    global count,count2
    count2 = 0
    count = 0
    TimeSleep.place(x=1000,y=1000)
    SellSalat.place(x=1000,y=1000)
    Cucumber.place(x=160, y=1800)
    BuyOil.place(x=0, y=2200)
    BuyBowl.place(x=160, y=2002)
    BuySalt.place(x=0, y=1000)
    BuySalat.place(x=160, y=1000)
    BuyTomato.place(x=0, y=1800)
    LabelCook.place(x=1000,y=1000)
    LabelListCook.place(x=1000,y=1000)
    ListCook.place(x=100,y=1000)
    GoCook.place(x=80,y=1000)
    GoSleep.place(x=80, y=2500)
    DoInHome.place(x=0, y=8500)
    Sausage.place(x=0, y =2200)
    Than.place(x=160, y=2200)
    Cheese.place(x=0, y=1000)
    Flour.place(x=160, y=1000)
    Chocolate.place(x=0, y=1800)
    Cola.place(x=160, y= 1800)
    Bread.place(x=0, y=2600)
    Cucumber.place(x=160, y=2600)
    BackMainMenu.place(x=0, y=3400)
    btnGoHome.place(x=0, y=22)
    btnGoShop.place(x=160, y=22)
    bthGoMarket.place(x=0, y=100)
    btnGoCasino.place(x=160, y=100)
    ListBuy.place(x=0, y=180)
    ListCook.place(x=160, y=180)
    Real_estate.place(x=0, y=260)
    NextListMeinMenu.place(x=160, y=260)
    Reset.place(x=5, y=337)
    NextListShop.place(x=160, y=3400)
    LabelBuy.place(x=55, y=3000)
    SellButerbrod.place(x=1000, y=1000)
    GetCard.place(x=1000,y=1000)
    StopKasino.place(x=1000,y=1000)
    ScoreYou.place_forget()
    RateKasino.config(state='normal')
    RateKasino.delete("0", END)
    RateKasino.config(state='readonly')
    Label1Room.place(x=-5, y=1000)
    Label2Room.place(x=150, y=1000)
    Label3Room.place(x=0, y=15000)
    LabelHouse1.place(x=150, y=15000)
    LabelHouse2.place(x=0, y=26000)
    NextListRealEstate.place(x=0, y=3300)
    LabelHouse3.place(x=1000,y=1000)
    MicroLabel1Room.place(x=1000, y=1000)
    Go1Room.place(x=1000, y=1000)
    Maining1Room.place(x=1000,y=1000)
    Buy1Room.place(x=1000,y=1000)
    Orend1Room.place(x=1000,y=1000)
    Sell1Room.place(x=1000,y=1000)
    Buy2Room.place(x=120, y=1220)
    MicroLabel2Room.place(x=1000, y=1000)
    Go2Room.place(x=1000, y=1000)
    BackMainMenu.place(x=1000, y=1000)
    Maining2Room.place(x=800, y=1750)
    Orend2Room.place(x=80, y=2100)
    Sell2Room.place(x=80, y=2650)
    LabelOrend2Room.place(x=1000,y=1000)
    Buy3Room.place(x=1000,y=1000)
    Go3Room.place_forget() # place(x=1000,y=1000)
    Maining3Room.place(x=1000,y=1000)
    Orend3Room.place(x=1000,y=1000)
    Sell3Room.place(x=1000,y=1000)
    MicroLabel3Room.place(x=1000,y=1000)
    MicroLabel1House.place(x=1000,y=1000)
    Go1House.place(x=1000,y=1000)
    Maining1House.place(x=1000,y=1000)
    Orend1House.place(x=1000,y=1000)
    Sell1House.place(x=1000,y=1000)
    Buy1House.place(x=1000,y=1000)
    Go2House.place_forget()
    MicroLabel2House.place_forget()
    Sell2House.place_forget()
    Orend2House.place_forget()
    Go2House.place_forget()
    Maining2House.place_forget()
    Buy2House.place_forget()
    Buy3House.place_forget()
    MicroLabel3House.place_forget()
    Go3House.place_forget()
    Maining3House.place_forget()
    Orend3House.place_forget()
    Sell3House.place_forget()
    LabelListCook.place_forget()
    YourBuy.place_forget()
    YourBuy.config(state='normal')
    YourBuy.delete(0,END)
    YourBuy2.place_forget()
    YourBuy2.config(state='normal')
    YourBuy2.delete(0, END)
    YourBuy3.place_forget()
    YourBuy3.config(state='normal')
    YourBuy3.delete(0, END)
    YourBuy4.place_forget()
    YourBuy4.config(state='normal')
    YourBuy4.delete(0, END)
    YourBuy5.place_forget()
    YourBuy5.config(state='normal')
    YourBuy5.delete(0, END)
    YourBuy6.place_forget()
    YourBuy6.config(state='normal')
    YourBuy6.delete(0, END)
    YourBuy7.place_forget()
    YourBuy7.config(state='normal')
    YourBuy7.delete(0, END)
    YourBuy8.place_forget()
    YourBuy8.config(state='normal')
    YourBuy8.delete(0, END)
    YourBuy9.place_forget()
    YourBuy9.config(state='normal')
    YourBuy9.delete(0, END)
    YourBuy10.place_forget()
    YourBuy10.config(state='normal')
    YourBuy10.delete(0, END)
    YourBuy11.place_forget()
    YourBuy11.config(state='normal')
    YourBuy11.delete(0, END)
    YourBuy12.place_forget()
    YourBuy12.config(state='normal')
    YourBuy12.delete(0, END)
    YourBuy13.place_forget()
    YourBuy13.config(state='normal')
    YourBuy13.delete(0, END)
    YourBuy14.place_forget()
    YourBuy14.config(state='normal')
    YourBuy14.delete(0, END)
    YourBuy15.place_forget()
    YourBuy15.config(state='normal')
    YourBuy15.delete(0, END)
    YourBuy16.place_forget()
    YourBuy16.config(state='normal')
    YourBuy16.delete(0, END)
    YourBuy17.place_forget()
    YourBuy17.config(state='normal')
    YourBuy17.delete(0, END)
    YourBuy18.place_forget()
    YourBuy18.config(state='normal')
    YourBuy18.delete(0, END)
    YourBuy19.place_forget()
    YourBuy19.config(state='normal')
    YourBuy19.delete(0, END)
    YourBuy20.place_forget()
    YourBuy20.config(state='normal')
    YourBuy20.delete(0, END)
    YourBuy21.place_forget()
    YourBuy21.config(state='normal')
    YourBuy21.delete(0, END)
    YourBuy22.place_forget()
    YourBuy22.config(state='normal')
    YourBuy22.delete(0, END)
    YourCook.place_forget()
    YourCook.config(state='normal')
    YourCook.delete(0, END)
    YourCook2.place_forget()
    YourCook2.config(state='normal')
    YourCook2.delete(0, END)
    YourCook3.place_forget()
    YourCook3.config(state='normal')
    YourCook3.delete(0, END)
    YourCook4.place_forget()
    YourCook4.config(state='normal')
    YourCook4.delete(0, END)
    YourCook5.place_forget()
    YourCook5.config(state='normal')
    YourCook5.delete(0, END)
    BuyMoreProduct0.place_forget()
    BuyMoreProduct1.place_forget()
    BuyMoreProduct2.place_forget()
    BuyMoreProduct3.place_forget()
    BuyMoreProduct4.place_forget()
    BuyMoreProduct5.place_forget()
    BuyMoreProduct6.place_forget()
    BuyMoreProduct7.place_forget()
    BuyMoreProduct8.place_forget()
    BuyMoreProduct9.place_forget()
    BuyMoreProductEntr1.place_forget()
    BuyMoreProductEntry.place_forget()
    BuyMoreProductClear1.place_forget()
    btnBedsideTable.place_forget()
    btnBuyStuff.place_forget()
    btnBuySpaghetti.place_forget()
    YourCook4.place_forget()
    YourCook3.place_forget()
    YourCook5.place_forget()
    btnSellSpaghettiWithCutlet.place_forget()
#Наступний лист в магазині
def NextListShop():
    BuyOil.place(x=0,y=22)
    BuyBowl.place(x=160,y=22)
    BuySalt.place(x=0,y=100)
    BuySalat.place(x=160,y=100)
    BuyTomato.place(x=0,y=180)
    Cucumber.place(x=160, y=180)
    NextListShop.place(x=1000,y=1900)
    Sausage.place(x=0, y =2200)
    Than.place(x=160, y=2200)
    Cheese.place(x=0, y=1000)
    Flour.place(x=160, y=1000)
    Chocolate.place(x=0, y=1800)
    Cola.place(x=160, y= 1800)
    Bread.place(x=0, y=2600)
    btnBuyStuff.place(x=0,y=260)
    btnBuySpaghetti.place(x=160,y=260)
#Багато кнопок на покупку чогось
def BuySausage():
    global money, HaveSausage, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів", message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)"))==False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSausage)
    else:
        if PayInShop=='Money' and money >= 200:
            money = money - 200
            HaveSausage = HaveSausage + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 200 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 200
                HaveSausage = HaveSausage + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefBuyMoreProduct(v):
    BuyMoreProductEntry.config(state='normal')
    BuyMoreProductEntry.insert(END, v)
    BuyMoreProductEntry.config(state='readonly')

def ClearMoreProduct():
    BuyMoreProductEntry.config(state='normal')
    BuyMoreProductEntry.delete(0, END)
    BuyMoreProductEntry.config(state='readonly')

def DefEnterMoreSausage():
    global money,HaveSausage, MoneyOnBankCard
    if PayInShop=='Money' and 200*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*200)
        HaveSausage = HaveSausage + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' ковбаси за '+ str(int(BuyMoreProductEntry.get())*200)+' грн')
        return
    if PayInShop=='BankCard' and  200*int(BuyMoreProductEntry.get())<=int(MoneyOnBankCard) and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 200)
        HaveSausage = HaveSausage + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' ковбаси за ' + str(
                                   int(BuyMoreProductEntry.get()) * 200) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')
def BuyCheese():
    global money, HaveCheese,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів", message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)"))==False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreCheese)
    else:
        if PayInShop=='Money' and money >= 120:
            money = money - 120
            HaveCheese = HaveCheese + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 200 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 120
                HaveCheese = HaveCheese + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreCheese():
    global money, HaveCheese,MoneyOnBankCard
    if PayInShop=='Money' and 120*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*120)
        HaveCheese = HaveCheese + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' сирів за '+ str(int(BuyMoreProductEntry.get())*120)+' грн')
        return
    if PayInShop=='BankCard' and  120*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 120)
        HaveCheese = HaveCheese + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' сирів за ' + str(
                                   int(BuyMoreProductEntry.get()) * 120) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')
def BuyThan():
    global money, HaveThan, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreThan)
    else:
        if PayInShop=='Money' and money >= 150:
            money = money - 150
            HaveThan = HaveThan + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >=150 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 150
                HaveThan = HaveThan + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreThan():
    global money, HaveThan, MoneyOnBankCard
    if PayInShop=='Money' and 150*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*150)
        HaveThan = HaveThan + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' ножів за '+ str(int(BuyMoreProductEntry.get())*150)+' грн')
        return
    if PayInShop=='BankCard' and  150*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 150)
        HaveThan = HaveThan + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' ножів за ' + str(
                                   int(BuyMoreProductEntry.get()) * 150) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code.')


def BuyFlour():
    global money, HaveFlour, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreFlour)
    else:
        if PayInShop=='Money' and money >= 80:
            money = money - 80
            HaveFlour = HaveFlour + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >=80 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 80
                HaveFlour = HaveFlour + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreFlour():
    global money, HaveFlour, MoneyOnBankCard
    if PayInShop=='Money' and 80*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*80)
        HaveFlour = HaveFlour + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' борошна за '+ str(int(BuyMoreProductEntry.get())*80)+' грн')
        return
    if PayInShop=='BankCard' and  80*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 80)
        HaveFlour = HaveFlour + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' борошна за ' + str(
                                   int(BuyMoreProductEntry.get()) * 80) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuyChocolate():
    global money, HaveChocolate, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreChocolate)
    else:
        if PayInShop == 'Money' and money >= 70:
            money = money - 70
            HaveChocolate = HaveChocolate + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 70 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 70
                HaveChocolate= HaveChocolate + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")


def DefEnterMoreChocolate():
    global money, HaveChocolate,MoneyOnBankCard
    if PayInShop=='Money' and 70*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*70)
        HaveChocolate = HaveChocolate + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' плиток шоколаду за '+ str(int(BuyMoreProductEntry.get())*70)+' грн')
        return
    if PayInShop=='BankCard' and  70*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 70)
        HaveChocolate = HaveChocolate + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' плиток шоколаду за ' + str(
                                   int(BuyMoreProductEntry.get()) * 70) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')


def BuyCola():
    global money, HaveCola,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreCola)
    else:
        if PayInShop == 'Money' and money >= 35:
            money = money - 35
            HaveCola = HaveCola + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 35 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 35
                HaveCola= HaveCola + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreCola():
    global money, HaveCola, MoneyOnBankCard
    if PayInShop=='Money' and 35*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*35)
        HaveCola = HaveCola + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' банок коли за '+ str(int(BuyMoreProductEntry.get())*35)+' грн')
        return
    if PayInShop=='BankCard' and  35*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 35)
        HaveCola = HaveCola + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' банок коли за ' + str(
                                   int(BuyMoreProductEntry.get()) * 35) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuyBread():
    global money, HaveBread,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreBread)
    else:
        if PayInShop == 'Money' and money >= 10:
            money = money - 10
            HaveBread = HaveBread + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 10 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 10
                HaveBread= HaveBread + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreBread():
    global money, HaveBread,MoneyOnBankCard
    if PayInShop=='Money' and 10*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*10)
        HaveBread = HaveBread + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' хлібин(-и) за '+ str(int(BuyMoreProductEntry.get())*10)+' грн')
        return
    if PayInShop=='BankCard' and  10*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 10)
        HaveBread = HaveBread + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' хлібин(-и) за ' + str(
                                   int(BuyMoreProductEntry.get()) * 10) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuyCucumber():
    global money, HaveCucumber, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreCucumber)
    else:
        if PayInShop == 'Money' and money >= 20:
            money = money - 20
            HaveCucumber = HaveCucumber + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 20 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 20
                HaveCucumber = HaveCucumber + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreCucumber():
    global money, HaveCucumber,MoneyOnBankCard
    if PayInShop=='Money' and 20*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*20)
        HaveCucumber = HaveCucumber + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' огірків за '+ str(int(BuyMoreProductEntry.get())*20)+' грн')
        return
    if PayInShop=='BankCard' and  20*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 20)
        HaveCucumber = HaveCucumber + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' огірків за ' + str(
                                   int(BuyMoreProductEntry.get()) * 20) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')



def Gosleep():
    LabelSleep.config(text='0:0:0')
    TimeSleep.place(x=90,y=50)
    LabelSleep.place(x=40, y=120)
    GoCook.place(x=75,y=700)
    btnBedsideTable.place_forget()
    GoSleep.place(x=75, y=2200)
    DoInHome.place(x=-15, y=550)
    BackMainMenu.place(x=2, y=3400)
    btnStartTaimer.place(x=25, y=200)
    btnGoHome.place(x=80, y=330)
def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = str(int(temp/3600))+":"+str(int((temp% 3600) / 60) ) + ":" + str(int(temp % 60))
    LabelSleep.configure(text=str(f_temp))
    temp += 1
def start_tick():
    btnGoHome.place(x=80, y=3300)
    btnStartTaimer.place(x=1000,y=1000)
    btnStopTaimer.place(x=25, y=200)
    tick()
def stop_tick():
    btnGoHome.place(x=80, y=330)
    btnStopTaimer.place(x=25, y=2000)
    btnContinuetTaimer.place(x=25, y=200)
    root.after_cancel(after_id)
def continue_tick():
    btnContinuetTaimer.place(x=25, y=2000)
    btnGoHome.place(x=80, y=3300)
    btnStopTaimer.place(x=25, y=200)
    tick()
def DefGoCook():
    btnGoHome.place(x=80, y=330)
    DoInHome.place(x=-15, y=550)
    GoCook.place(x=75, y=700)
    btnBedsideTable.place_forget()
    GoSleep.place(x=75, y=2200)
    BackMainMenu.place(x=2, y=3400)
    CookButerbrod.place(x=0, y =72)
    CookSalat.place(x=150, y=72)
    btnCookIngredient.place(x=0, y=22)
    btnCookSpaghettiWithCutlet.place(x=0,y=150)

def ListBuy():
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    LabelBuy.place(x=55,y=-3)
    BackMainMenu.place(x=2,y=340)
    ListCook.place(x=100, y=1000)
    #YourBuy.config(text='  Ковбаса:'+ str(HaveSausage) + '      Ніж:'+ str(HaveThan)+'      Сир:'+ str(HaveCheese)+
    #'\nБорошно:'+str(HaveFlour)+'          Шоколадка:' + str(HaveСhocolate)+
    #'\nКола:'+str(HaveCola)+'       Хліб:'+str(HaveBread)+'     Масло:'+str(HaveOil)+
    #'\nМиска: '+str(HaveBowl)+'      Сіль:'+str(HaveSalt)+'    Салат:'+str(HaveSalad)+
    #'\nПомідори:'+str(HaveTomato)+'    Огірок:'+str(HaveCucumber)+'\nШмат. Ковбаси:'+str(HaveCutSausage)+
    #'  Шмат. сиру:'+str(HaveCutCheese)+'\n Шмат. шок.:'+str(HaveCutСhocolate)+'  Шмат. хлібу:'+str(HaveCutBread)+
    #'\nШмат.Салату:'+str(HaveCutSalad)+'  Шмат. пом.:'+str(HaveCutTomato)+'\nШматок огірка:'+str(HaveCutCucumber)
    #              )
    YourBuy.place(x=5, y=60)
    YourBuy.insert(0,'Ковбаса: '+ str(HaveSausage))
    YourBuy.config(state='readonly')
    YourBuy2.place(x=155,y=60)
    YourBuy2.insert(0,'Ніж: '+ str(HaveThan))
    YourBuy2.config(state='readonly')
    YourBuy3.place(x=5, y=82)
    YourBuy3.insert(0, 'Сир: '+ str(HaveCheese))
    YourBuy3.config(state='readonly')
    YourBuy4.place(x=155, y=82)
    YourBuy4.insert(0, 'Борошно: '+str(HaveFlour))
    YourBuy4.config(state='readonly')
    YourBuy5.place(x=5, y=104)
    YourBuy5.insert(0, 'Шоколадка: ' + str(HaveChocolate))
    YourBuy5.config(state='readonly')
    YourBuy6.place(x=155, y=104)
    YourBuy6.insert(0, 'Кола: '+str(HaveCola))
    YourBuy6.config(state='readonly')
    YourBuy7.place(x=5, y=126)
    YourBuy7.insert(0, 'Хліб: '+str(HaveBread))
    YourBuy7.config(state='readonly')
    YourBuy8.place(x=155, y=126)
    YourBuy8.insert(0, 'Масло: '+str(HaveOil))
    YourBuy8.config(state='readonly')
    YourBuy9.place(x=5, y=148)
    YourBuy9.insert(0, 'Миска: '+str(HaveBowl))
    YourBuy9.config(state='readonly')
    YourBuy10.place(x=155, y=148)
    YourBuy10.insert(0, 'Сіль: '+str(HaveSalt))
    YourBuy10.config(state='readonly')
    YourBuy11.place(x=5, y=170)
    YourBuy11.insert(0, 'Салат: '+str(HaveSalad))
    YourBuy11.config(state='readonly')
    YourBuy11.place(x=5, y=170)
    YourBuy11.insert(0, 'Помідори:'+str(HaveTomato))
    YourBuy11.config(state='readonly')
    YourBuy12.place(x=155, y=170)
    YourBuy12.insert(0, 'Огірок:'+str(HaveCucumber))
    YourBuy12.config(state='readonly')
    YourBuy13.place(x=155, y=192)
    YourBuy13.insert(0, 'Шмат. Ковбаси:'+str(HaveCutSausage))
    YourBuy13.config(state='readonly')
    YourBuy14.place(x=5, y=214)
    YourBuy14.insert(0, 'Шмат. сиру:'+str(HaveCutCheese))
    YourBuy14.config(state='readonly')
    YourBuy15.place(x=155, y=214)
    YourBuy15.insert(0, 'Шмат. шок.:'+str(HaveCutChocolate))
    YourBuy15.config(state='readonly')
    YourBuy16.place(x=5, y=236)
    YourBuy16.insert(0, 'Шмат. хлібу:'+str(HaveCutBread))
    YourBuy16.config(state='readonly')
    YourBuy17.place(x=155, y=236)
    YourBuy17.insert(0, 'Шмат.Салату:'+str(HaveCutSalad))
    YourBuy17.config(state='readonly')
    YourBuy18.place(x=5, y=258)
    YourBuy18.insert(0, 'Шмат. пом.:'+str(HaveCutTomato))
    YourBuy18.config(state='readonly')
    YourBuy20.place(x=155, y=258)
    YourBuy20.insert(0, 'Шмат. ог.:'+str(HaveCutCucumber))
    YourBuy20.config(state='readonly')
    YourBuy19.place(x=5, y=192)
    YourBuy19.insert(0, 'Помідор: ' + str(HaveTomato))
    YourBuy19.config(state='readonly')
    YourBuy21.place(x=5, y=280)
    YourBuy21.insert(0, 'Пач.фаршу:'+str(HaveStuffing))
    YourBuy21.config(state='readonly')
    YourBuy22.place(x=155, y=280)
    YourBuy22.insert(0, 'Пач. спагетті:'+str(HaveSpaghetti))
    YourBuy22.config(state='readonly')
def cookButerbrot():
    global HaveCutCheese, HaveCutSausage, HaveCutBread, HaveButerbrod
    #if HaveCutSausage >= 2 and HaveCutBread >= 1 and HaveCutCheese>=2:
    if (messagebox.askyesno(title="Скільки приготувати",
                            message="Ви хочете приготувати 1 страву чи декілка(Так-1 страву Ні-декілька страв)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreButerbrot)
    else:
        if HaveCutSausage >= 2 and HaveCutBread >= 1 and HaveCutCheese >= 2:
            HaveButerbrod = HaveButerbrod + 1
            HaveCutSausage = HaveCutSausage - 2
            HaveCutCheese = HaveCutCheese - 2
            HaveCutBread = HaveCutBread - 1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на бутерброд вам потрібен 2 шматка ковбаси, 2 шматка сира і 1 шматок хліба)")

def DefEnterMoreButerbrot():
    global money, HaveButerbrod, HaveCutCheese, HaveCutSausage, HaveCutBread
    if HaveCutSausage >=int(BuyMoreProductEntry.get())*2 and HaveCutBread >=int(BuyMoreProductEntry.get()) and HaveCutCheese >=int(BuyMoreProductEntry.get())*2:
        HaveButerbrod = HaveButerbrod + int(BuyMoreProductEntry.get())
        HaveCutSausage = HaveCutSausage -  int(BuyMoreProductEntry.get())*2
        HaveCutCheese = HaveCutCheese -  int(BuyMoreProductEntry.get())*2
        HaveCutBread = HaveCutBread - int(BuyMoreProductEntry.get())*1
        DefHideMoreProduct()
        GoHome()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви приготували ' + BuyMoreProductEntry.get() + ' бутерброд(-ів) за ')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на бутерброд вам потрібен 2 шматка ковбаси, 2 шматка сира і 1 шматок хліба)")

def ListCook():
    LabelCook.place(x=55,y=18)
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    ListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    YourCook.place(x=5, y=60)
    YourCook.insert(0, 'Бутерброд: ' + str(HaveButerbrod))
    YourCook.config(state='readonly')
    YourCook2.place(x=155, y=60)
    YourCook2.insert(0, 'Салат: ' + str(HaveSalat))
    YourCook2.config(state='readonly')
    BackMainMenu.place(x=2, y=340)
    YourCook3.place(x=5, y=80)
    YourCook3.insert(0, 'Котлети: ' + str(HaveCutlet))
    YourCook3.config(state='readonly')
    YourCook4.place(x=155, y=80)
    YourCook4.insert(0, 'Спагеті: ' + str(HaveCookSpaghetti))
    YourCook4.config(state='readonly')
    YourCook5.place(x=5, y=100)
    YourCook5.insert(0, 'Спагеті з котлетою: ' + str(HaveSpaghettiWithCutlet))
    YourCook5.config(state='readonly')
def SellButterbrod():
    global money, HaveButerbrod, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете продати 1 бутерброд чи декілка(Так-1, Ні-декілька)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreButerbrotSell)
    else:
        if PayInMarket =='Money':
            if HaveButerbrod >= 1:
                if messagebox.askokcancel("Підтвердження", "Ви можете продати бутербод. Ви цього хочете?"):
                    money = int(money) + 120
                    HaveButerbrod = HaveButerbrod -1
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    return
        else:
            messagebox.askokcancel("Ой, сталася помилка.", "У вас немає бутерброду")
        if PayInMarket=='BankCard' and ProofPinCode==PinCode:
            if HaveButerbrod >= 1:
                if messagebox.askokcancel("Підтвердження", "Ви можете продати бутербод. Ви цього хочете?"):
                    MoneyOnBankCard = int(MoneyOnBankCard) + 120
                    HaveButerbrod = HaveButerbrod -1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","У вас немає бутерброду або ви не підтвердили Pin-Code")
def DefEnterMoreButerbrotSell():
    global money, HaveButerbrod, MoneyOnBankCard
    if HaveButerbrod >= int(BuyMoreProductEntry.get()) and PayInMarket=='Money':
        money = money + (int(BuyMoreProductEntry.get()) * 120)
        HaveButerbrod = HaveButerbrod - int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' бутерброд(-ів) ' + str(
                                   int(BuyMoreProductEntry.get()) * 120) + ' грн')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.","У вас немає стільки бутербродів")
    if HaveButerbrod>=int(BuyMoreProductEntry.get()) and PayInMarket=='BankCard' and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard + (int(BuyMoreProductEntry.get()) * 120)
        HaveButerbrod = HaveButerbrod - int(BuyMoreProductEntry.get())
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' бутербродів ' + str(
                                   int(BuyMoreProductEntry.get()) * 120) + ' грн')
def Cut():
    if HaveThan>=1:
        CookSalat.place(x=3000,y=1000)
        CookButerbrod.place(x=0, y=2200)
        btnCut.place(x=1000, y=1000)
        CutSausage.place(x=0 , y=22)
        CutThan.place(x=160 , y=22)
        CutCheese.place(x=0 , y=100)
        CutFlour.place(x=160 , y=100)
        CutChocolate.place(x=0 , y=180)
        CutCola.place(x=160, y=180)
        CutBread.place(x= 0, y=260)
        NextListCut.place(x= 160, y=260)
        BuyMoreProduct0.place_forget()
        BuyMoreProduct1.place_forget()
        BuyMoreProduct2.place_forget()
        BuyMoreProduct3.place_forget()
        BuyMoreProduct4.place_forget()
        BuyMoreProduct5.place_forget()
        BuyMoreProduct6.place_forget()
        BuyMoreProduct7.place_forget()
        BuyMoreProduct8.place_forget()
        BuyMoreProduct9.place_forget()
        BuyMoreProductEntr1.place_forget()
        BuyMoreProductClear1.place_forget()
        BuyMoreProductEntry.place_forget()
        btnFry.place_forget()
        btnBoil.place_forget()
    else:
        messagebox.askokcancel("Ой, сталася помилка.", 'Вам потрібен ніж')
def CutSausage():
    global HaveSausage, HaveCutSausage
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSausageCut)
    else:
        if HaveSausage >= 1:
            HaveCutSausage = HaveCutSausage+10
            HaveSausage = HaveSausage - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 10 шматків ковбаси")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')
def DefEnterMoreSausageCut():
    global HaveSausage, HaveCutSausage
    if int(BuyMoreProductEntry.get()) <= HaveSausage:
        HaveSausage = HaveSausage - int(BuyMoreProductEntry.get())
        HaveCutSausage = HaveCutSausage+int(BuyMoreProductEntry.get())*10
        Cut()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' ковбас(-а) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 10) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає ковбаси. Щоб вона з'явилися купіть її в магазині.")

def CutThan():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порізати')
def CutCheese():
    global HaveCheese, HaveCutCheese
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreCheeseCut)
    else:
        if HaveCheese >= 1:
            HaveCutCheese = HaveCutCheese + 10
            HaveCheese = HaveCheese - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 10 шматків сиру")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')

def DefEnterMoreCheeseCut():
    global HaveCheese, HaveCutCheese
    if int(BuyMoreProductEntry.get()) <= HaveCheese:
        HaveCheese = HaveCheese - int(BuyMoreProductEntry.get())
        HaveCutCheese = HaveCutCheese+int(BuyMoreProductEntry.get())*10
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' сир(-ів) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 10) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає ковбачи. Щоб вона з'явилися купіть її в магазині.")

def CutFlour():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порізати')
def CutChocolate():
    global HaveChocolate, HaveCutChocolate
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreChocolateCut)
    else:
        if HaveChocolate >= 1:
            HaveCutChocolate = HaveCutChocolate + 16
            HaveChocolate = HaveChocolate - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 16 квадратиків шоколадки")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')

def DefEnterMoreChocolateCut():
    global HaveChocolate, HaveCutChocolate
    if int(BuyMoreProductEntry.get()) <= HaveChocolate:
        HaveChocolate = HaveChocolate - int(BuyMoreProductEntry.get())
        HaveCutChocolate = HaveCutChocolate+int(BuyMoreProductEntry.get())*16
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' шоколадк(-у,-и) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 16) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає ковбачи. Щоб вона з'явилися купіть її в магазині.")

def CutCola():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порізати')
def CutCucumber():
    global HaveCucumber, HaveCutCucumber
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreCucumberCut)
    else:
        if HaveCucumber >= 1:
            HaveCutCucumber = HaveCutCucumber + 10
            HaveCucumber = HaveCucumber - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 10 овалів огірка")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')

def DefEnterMoreCucumberCut():
    global HaveCucumber, HaveCutCucumber
    if int(BuyMoreProductEntry.get()) <= HaveCucumber:
        HaveCucumber = HaveCucumber - int(BuyMoreProductEntry.get())
        HaveCutCucumber = HaveCutCucumber+int(BuyMoreProductEntry.get())*10
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' огір(-ок,-ків) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 10) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає ковбачи. Щоб вона з'явилися купіть її в магазині.")

def CutBread():
    global HaveBread, HaveCutBread
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreBreadCut)
    else:
        if HaveBread>=1:
            HaveCutBread = HaveCutBread + 5
            HaveBread = HaveBread - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 5 шматків хлібу")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')

def DefEnterMoreBreadCut():
    global HaveBread, HaveCutBread
    if int(BuyMoreProductEntry.get()) <= HaveBread:
        HaveBread = HaveBread - int(BuyMoreProductEntry.get())
        HaveCutBread = HaveCutBread+int(BuyMoreProductEntry.get())*5
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' хліб(-а,-ів) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 5) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає ковбачи. Щоб вона з'явилися купіть її в магазині.")

def BuyTomato():
    global money, HaveTomato,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreTomato)
    else:
        if PayInShop == 'Money' and money >= 20:
            money = money - 20
            HaveTomato = HaveTomato + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 20 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 20
                HaveTomato = HaveTomato + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "Мабуть у вас невистачає грошей. Щоб вони з'явилися пограйте в казино, або продайте, що у вас є")

def DefEnterMoreTomato():
    global money, HaveTomato, MoneyOnBankCard
    if PayInShop=='Money' and 20*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*20)
        HaveTomato = HaveTomato + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' помідорів за '+ str(int(BuyMoreProductEntry.get())*20)+' грн')
        return
    if PayInShop=='BankCard' and  20*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 20)
        HaveTomato = HaveTomato + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' помідорів за ' + str(
                                   int(BuyMoreProductEntry.get()) * 20) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')


def BuySalat():
    global money, HaveSalad, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSalad)
    else:
        if PayInShop == 'Money' and money >= 30:
            money = money - 30
            HaveSalad = HaveSalad + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 30 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 30
                HaveSalad = HaveSalad + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreSalad():
    global money, HaveSalad,MoneyOnBankCard
    if PayInShop=='Money' and 30*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*30)
        HaveSalad = HaveSalad + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' салатів за '+ str(int(BuyMoreProductEntry.get())*30)+' грн')
        return
    if PayInShop=='BankCard' and  30*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 30)
        HaveSalad = HaveSalad + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' салатів за ' + str(
                                   int(BuyMoreProductEntry.get()) * 30) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuySalt():
    global money, HaveSalt,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSalt)
    else:
        if PayInShop == 'Money' and money >= 20:
            money = money - 20
            HaveSalt = HaveSalt + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 20 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 20
                HaveSalt = HaveSalt + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreSalt():
    global money, HaveSalt, MoneyOnBankCard
    if PayInShop=='Money' and 20*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*20)
        HaveSalt = HaveSalt + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' солі за '+ str(int(BuyMoreProductEntry.get())*20)+' грн')
        return
    if PayInShop=='BankCard' and  20*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 20)
        HaveSalt = HaveSalt + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' солі за ' + str(
                                   int(BuyMoreProductEntry.get()) * 20) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuyBowl():
    global money, HaveBowl, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreBowl)
    else:
        if PayInShop == 'Money' and money >= 50:
            money = money - 50
            HaveBowl = HaveBowl + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 50 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 50
                HaveBowl = HaveBowl + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")

def DefEnterMoreBowl():
    global money, HaveBowl, MoneyOnBankCard
    if PayInShop=='Money' and 50*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*50)
        HaveBowl = HaveBowl + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' мисок за '+ str(int(BuyMoreProductEntry.get())*50)+' грн')
        return
    if PayInShop=='BankCard' and  50*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 50)
        HaveBowl = HaveBowl + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' мисок за ' + str(
                                   int(BuyMoreProductEntry.get()) * 50) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def BuyOil():
    global money, HaveOil,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreOil)
    else:
        if PayInShop == 'Money' and money >= 30:
            money = money - 30
            HaveOil = HaveOil + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 30 and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 30
                HaveOil = HaveOil + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.",
                                       "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)є")

def DefEnterMoreOil():
    global money, HaveOil, MoneyOnBankCard
    if PayInShop=='Money' and 30*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*30)
        HaveOil = HaveOil + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' олії за '+ str(int(BuyMoreProductEntry.get())*30)+' грн')
        return
    if PayInShop=='BankCard' and  30*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 30)
        HaveOil = HaveOil + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' олії за ' + str(
                                   int(BuyMoreProductEntry.get()) * 30) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')
        
def DefBuyStuffing():
    global money, HaveStuffing, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів", message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)"))==False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreStuffing)
    else:
        if PayInShop=='Money' and money >= 100:
            money = money - 100
            HaveStuffing = HaveStuffing + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 100 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 100
                HaveStuffing = HaveStuffing + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")


def DefEnterMoreStuffing():
    global money, HaveStuffing, MoneyOnBankCard
    if PayInShop=='Money' and 100*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*100)
        HaveStuffing = HaveStuffing + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' пачок фаршу за '+ str(int(BuyMoreProductEntry.get())*100)+' грн')
        return
    if PayInShop=='BankCard' and  100*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 100)
        HaveStuffing = HaveStuffing + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' пачок фаршу за ' + str(
                                   int(BuyMoreProductEntry.get()) * 100) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')



def DefBuySpaghetti():
    global money, HaveSpaghetti, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів", message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)"))==False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSpaghetti)
    else:
        if PayInShop=='Money' and money >= 40:
            money = money - 40
            HaveSpaghetti = HaveSpaghetti + 1
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        else:
            if PayInShop == 'BankCard' and MoneyOnBankCard >= 40 and ProofPinCode==PinCode:
                MoneyOnBankCard = MoneyOnBankCard - 40
                HaveSpaghetti = HaveSpaghetti + 1
            else:
                messagebox.askokcancel("Ой, сталася помилка.", "У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)")


def DefEnterMoreSpaghetti():
    global money, HaveSpaghetti, MoneyOnBankCard
    if PayInShop=='Money' and 40*int(BuyMoreProductEntry.get())<=money:
        money = money - (int(BuyMoreProductEntry.get())*40)
        HaveSpaghetti = HaveSpaghetti + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoShop()
        messagebox.askokcancel('Операція пройша успішно','Ви купили '+BuyMoreProductEntry.get()+' пачок спагеті за '+ str(int(BuyMoreProductEntry.get())*40)+' грн')
        return
    if PayInShop=='BankCard' and  40*int(BuyMoreProductEntry.get())<=MoneyOnBankCard and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard - (int(BuyMoreProductEntry.get()) * 40)
        HaveSpaghetti = HaveSpaghetti + int(BuyMoreProductEntry.get())
        GoShop()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви купили ' + BuyMoreProductEntry.get() + ' пачок спагеті за ' + str(
                                   int(BuyMoreProductEntry.get()) * 40) + ' грн')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки грошей або ви не підтвердили Pin-code. :(Promo DontHaveMoneyShop)')

def NextListCut():
    CookButerbrod.place(x=0, y=2200)
    btnCut.place(x=1000, y=1000)
    CutSausage.place(x=0, y=2200)
    CutThan.place(x=160, y=2200)
    CutCheese.place(x=0, y=1000)
    CutFlour.place(x=160, y=1000)
    CutChocolate.place(x=0, y=1800)
    CutCola.place(x=160, y=1800)
    CutBread.place(x=0, y=2600)
    NextListCut.place(x=1000,y=1000)
    CutOil.place(x=0, y=22)
    CutBowl.place(x=160, y=22)
    CutSalt.place(x=0, y=100)
    CutSalat.place(x=160, y=100)
    CutTomato.place(x=0, y=180)
    CutCucumber.place(x=160, y=180)
def CutTomato():
    global  HaveCutTomato, HaveTomato
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreTomatoCut)
    else:
        if HaveTomato >= 1:
            HaveCutTomato = HaveCutTomato + 10
            HaveTomato = HaveTomato - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 10 шматків помідору")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')

def DefEnterMoreTomatoCut():
    global HaveTomato, HaveCutTomato
    if int(BuyMoreProductEntry.get()) <= HaveTomato:
        HaveTomato= HaveTomato - int(BuyMoreProductEntry.get())
        HaveCutTomato = HaveCutTomato+int(BuyMoreProductEntry.get())*10
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви порізали ' + BuyMoreProductEntry.get() + ' помідор(-ів) і отримали ' + str(
                                   int(BuyMoreProductEntry.get()) * 10) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає грошеу. Щоб вони з'явилися пограйте в казино або бродайте продукти.")


def CutSalad():
    global  HaveCutSalad, HaveSalad
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSaladCut)
    else:
        if HaveSalad >= 1:
            HaveCutSalad = HaveCutSalad + 10
            HaveSalad = HaveSalad - 1
            messagebox.askokcancel("Дія виконана", "До ваших продуктів було додано 10 шматків помідору")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару')


def DefEnterMoreSaladCut():
    global HaveSalad, HaveCutSalad
    if int(BuyMoreProductEntry.get()) <= HaveSalad:
        HaveSalad = HaveSalad - int(BuyMoreProductEntry.get())
        HaveCutSalad = HaveCutSalad + int(BuyMoreProductEntry.get())*10
        Cut()
        messagebox.askokcancel('Операція пройша успішно',
                    'Ви порізали ' + BuyMoreProductEntry.get() + ' салату і  отримали ' + str(
                                       int(BuyMoreProductEntry.get()) * 10) + ' шматків')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                                   "Мабуть у вас невистачає ковбачи. Щоб вона з'явилися купіть її в магазині.")

def CutSalt():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порізати')
def CutBowl():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порімзати')
def CutOil():
    messagebox.askokcancel("Ой, сталася помилка.", 'Цей предмет неможливо порізати')
def CookSalat():
    global HaveSalat, HaveBowl, HaveCutTomato, HaveCutSalad, HaveSalt, HaveCutCucumber, HaveOil
    if (messagebox.askyesno(title="Скільки салатів",
                            message="Ви хочете приготувати 1 страву чи декілка(Так-1 страва Ні-декілька страв)")) == False:
            BtnBuyMoreProduct_And_HideAllBtnShop()
            BuyMoreProductEntr1.config(command=DefEnterMoreSalatCook)
    else:
        if HaveCutTomato >=10 and HaveCutSalad >=10 and HaveCutCucumber >=10 and HaveBowl >=1 and HaveSalt >=1 and HaveOil >=1:
            if messagebox.askokcancel("Підтвердження", "Ви можете проготувати салат. Ви цього хочете?"):
                HaveSalat = HaveSalat + 1
                HaveBowl = HaveBowl - 1
                HaveCutTomato = HaveCutTomato - 10
                HaveCutSalad = HaveCutSalad - 10
                HaveCutCucumber = HaveCutCucumber -10
                HaveSalt = HaveSalt - 1
                HaveOil = HaveOil - 1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на салат вам потрібна: миска,5 шматків помідору,10 листів салату,10 овалів огірку,масло і сіль)")

def DefEnterMoreSalatCook():
    global money, HaveCutTomato, HaveCutSalad, HaveCutCucumber, HaveBowl, HaveOil, HaveSalt, HaveSalat
    sfdsf = int(BuyMoreProductEntry.get())
    if HaveCutTomato >=sfdsf*10 and HaveCutSalad >=sfdsf*10 and HaveCutCucumber >=sfdsf*10 and HaveBowl >=sfdsf and HaveSalt >=sfdsf and HaveOil >=sfdsf:
        HaveCutTomato = HaveCutTomato - int(BuyMoreProductEntry.get())*10
        HaveCutSalad = HaveCutSalad - int(BuyMoreProductEntry.get())*10
        HaveCutCucumber = HaveCutCucumber - int(BuyMoreProductEntry.get())*10
        HaveBowl = HaveBowl - int(BuyMoreProductEntry.get())
        HaveSalt = HaveSalt - int(BuyMoreProductEntry.get())
        HaveOil = HaveOil - int(BuyMoreProductEntry.get())
        HaveSalat = HaveSalat + int(BuyMoreProductEntry.get())
        DefHideMoreProduct()
        DefGoCook()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви приготували ' + BuyMoreProductEntry.get() + ' салат(-ів)')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на салат треба 1 масло,1 сіль, 1 миска, 5 шматків помідору,5 шматків салату і 10 шматків огірка)")

def SellSalat():
    global money, HaveSalat,MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете купити 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSalatSell)
    else:
        if PayInMarket=='Money' and HaveSalat >= 1:
            if messagebox.askokcancel("Підтвердження", "Ви можете продати салат. Ви цього хочете?"):
                money = int(money) + 340
                HaveSalat = HaveSalat - 1
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                return
        else:
            messagebox.askokcancel("Ой, сталася помилка.","У вас немає салату")
        if PayInMarket=='BankCard' and HaveSalat>=1 and ProofPinCode==PinCode:
            if messagebox.askokcancel("Підтвердження", "Ви можете продати салат. Ви цього хочете?"):
                MoneyOnBankCard = int(MoneyOnBankCard) + 340
                HaveSalat = HaveSalat - 1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","У вас немає салату або ви не підтвердили Pin-Code")

def DefEnterMoreSalatSell():
    global money, HaveSalat,MoneyOnBankCard
    if HaveSalat>=int(BuyMoreProductEntry.get()) and PayInMarket=='Money':
        money = money + (int(BuyMoreProductEntry.get()) * 340)
        HaveSalat = HaveSalat - int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' салат(-ів) за' + str(int(BuyMoreProductEntry.get())*340) +'гривень')
        return
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки салатів(')
    if HaveSalat>=int(BuyMoreProductEntry.get()) and PayInMarket=='BankCard' and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard + (int(BuyMoreProductEntry.get()) * 340)
        HaveSalat = HaveSalat - int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' салат(-ів) за' + str(
                                   int(BuyMoreProductEntry.get()) * 340) + 'гривень')
    else:
        messagebox.askokcancel('Сталася помилка','У вас немає стільки салатів або ви не підтвердили Pin-Code (')
def GetCard():
    Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10] * 4
    global current, current2, count, count2, money, Rayt,k,m,ScoreYou, MoneyOnBankCard
    if count2 >= 15:
        current = Cards.pop()
        count += current
        ScoreYou.config(text='У вас: ' + str(count) + ' очок')
    # Якщо у бота не21,20,19,18,17 очок
    else:
        random.shuffle(Cards)
        current = Cards.pop()
        current2 = Cards.pop()
        count += current
        count2 += current2
        ScoreYou.config(text='У вас: ' + str(count) + ' очок')
        ScoreYou.place(x=65, y=210)
        # Умови що перевірити ти переміг чи програв
    if count > 21 and count2<=21:
        messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокFDV')
        if PayInCasino == 'Money':
            money = money - Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard - Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count2 > 21:
        messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокMMCX')
        if PayInCasino == 'Money':
            money = money + Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard + Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count2 == 21 and count!=count2:
        messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокPDBHGF')
        if PayInCasino == 'Money':
            money = money - Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard - Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count == 21 and count!=count2:
        messagebox.askokcancel("Результат гри",'Ви виграли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокZVXCHJV')
        if PayInCasino == 'Money':
            money = money + Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard + Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count2 == 21 and count!=21:
        messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокVV')
        if PayInCasino == 'Money':
            money = money - Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard - Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count2 > 21:
            messagebox.askokcancel("Результат гри", 'Ви зіграли в нічию. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. Ваша ставка повертаєтьсяGCDB')
            GetCard.config(state=DISABLED)
            StopKasino.config(state=DISABLED)
            return
    if count>21 or count2>21:
        if count > count2 and count <= 21:
                messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокERDF')
                if PayInCasino == 'Money':
                    money = money + Rayt
                if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                    MoneyOnBankCard = MoneyOnBankCard + Rayt
                GetCard.config(state=DISABLED)
                StopKasino.config(state=DISABLED)
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                return
        if count < count2 and count2 <= 21:
                messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокERF')
                if PayInCasino == 'Money':
                    money = money + Rayt
                if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                    MoneyOnBankCard = MoneyOnBankCard + Rayt
                GetCard.config(state=DISABLED)
                StopKasino.config(state=DISABLED)
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                return
    if count == 21:
        if count == count2:
            messagebox.askokcancel("Результат гри", 'Ви зіграли в нічию. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. Ваша ставка повертаєтьсяHJCB')
            GetCard.config(state=DISABLED)
            StopKasino.config(state=DISABLED)
            return
        else:
            messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокNBVC')
            if PayInCasino == 'Money':
                money = money + Rayt
            if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                MoneyOnBankCard = MoneyOnBankCard + Rayt
            GetCard.config(state=DISABLED)
            StopKasino.config(state=DISABLED)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            return
    
    #print(money)
def StopKasino():
    global count,count2,money,Rayt,MoneyOnBankCard
    # Перевіряє чи брати боту карту чи ні
    if count2 <= 16:
        while count2 <= 15:
            current2 = Cards.pop()
            count2 += current2
    if count2 > 21 and count <= 21:
        messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокVCBGF')
        if PayInCasino == 'Money':
            money = money + Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard + Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count > 21 and count2<=21:
        messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очокWQNLX')
        if PayInCasino == 'Money':
            money = money - Rayt
        if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
            MoneyOnBankCard = MoneyOnBankCard - Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    if count2 == 21:
        messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. Ваша ставка повертається. A')
        if PayInCasino=='Money':
            money = money - Rayt
        if PayInCasino=='BankCard' and ProofPinCode==PinCode:
            MoneyOnBankCard = MoneyOnBankCard - Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    if count > count2 and count <= 21:
        messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. B')
        if PayInCasino=='Money':
            money = money + Rayt
        if PayInCasino=='BankCard' and ProofPinCode==PinCode:
            MoneyOnBankCard= MoneyOnBankCard + Rayt
        GetCard.config(state=DISABLED)
        StopKasino.config(state=DISABLED)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        return
    else:
        if count < count2 and count2 <= 21:
            messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. C')
            if PayInCasino == 'Money':
                money = money - Rayt
            if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                MoneyOnBankCard= MoneyOnBankCard- Rayt
            GetCard.config(state=DISABLED)
            StopKasino.config(state=DISABLED)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            return
        else:
            if count > count2 and count <= 21:
                messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. D')
                if PayInCasino == 'Money':
                    money = money + Rayt
                if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                    MoneyOnBankCard= MoneyOnBankCard+ Rayt
                GetCard.config(state=DISABLED)
                StopKasino.config(state=DISABLED)
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                return
            else:
                if count < count2 and count2 <= 21:
                    messagebox.askokcancel("Результат гри",'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. E')
                    if PayInCasino == 'Money':
                        money = money + Rayt
                    if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                        MoneyOnBankCard= MoneyOnBankCard+ Rayt
                    GetCard.config(state=DISABLED)
                    StopKasino.config(state=DISABLED)
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    return
                if count < count2 and count2 < 21:
                    messagebox.askokcancel("Результат гри",'Ви програли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. F')
                    if PayInCasino == 'Money':
                        money = money - Rayt
                    if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                        MoneyOnBankCard = MoneyOnBankCard - Rayt
                    GetCard.config(state=DISABLED)
                    StopKasino.config(state=DISABLED)
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    return
                if count < count2 and count2 > 21:
                    messagebox.askokcancel("Результат гри", 'Ви перемогли. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. V')
                    if PayInCasino == 'Money':
                        money = money + Rayt
                    if PayInCasino == 'BankCard' and ProofPinCode == PinCode:
                        MoneyOnBankCard= MoneyOnBankCard+ Rayt
                    GetCard.config(state=DISABLED)
                    StopKasino.config(state=DISABLED)
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    return
                else:
                    messagebox.askokcancel("Результат гри", 'Ви зіграли в нічию. У вас було ' + str(count) + ' очок. У супротивника було ' + str(count2) + ' очок. Ваша ставка повертається.G')
                    
    GetCard.config(state=DISABLED)
    StopKasino.config(state=DISABLED)
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    
    #print(money)


def RealEstate():
    ListCook.place(x=1000, y=1000)
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    Reset.place(x=5, y=3370)
    Label1Room.place(x=-5, y=20)
    Label2Room.place(x=150,y=20)
    Label3Room.place(x=0,y=190)
    LabelHouse1.place(x=150,y=190)
    BackMainMenu.place(x=2, y=340)
    NextListRealEstate.place(x=0,y=330)
    Buy1Room.place(x=0,y=122)
    Buy2Room.place(x=150,y=122)
    Buy3Room.place(x=0, y=260)
    Buy1House.place(x=150,y=260)
    NextListRealEstate.config(command=DefNextListRealEstate)
    if Have1Room == True:
        Buy1Room.config(text='Керувати квартирою', command=DefSettings1Room)
    else:
        Buy1Room.config(text='Купити однокімнатну\nквартиру', command=DefBuy1Room)
    if Have2Room:
        Buy2Room.config(text='Керувати квартирою', command=DefSettings2Room)
    else:
        Buy2Room.config(text='Купити двокімнтану\nквартиру', command=DefBuy2Room)
    if Have3Room:
        Buy3Room.config(text='Керувати квартирою', command=DefSettings3Room)
    else:
        Buy3Room.config(text='Купити трьохкімнатну\nквартиру', command=DefBuy3Room)
    if Have1House:
        Buy1House.config(text='Керувати будинком', command=DefSettings1House)
    else:
        Buy1House.config(text='Купити одноповерховий\nбудинок', command=DefBuy1House)
    if Have2House:
        Buy2House.config(text='Керувати будинком', command=DefSettings2House)
    else:
        Buy2House.config(text='Купити двоповерховий\nбудинок', command=DefBuy2House)
    if Have3House:
        Buy3House.config(text='Керувати будинком', command=DefSettings3House)
    else:
        Buy3House.config(text='Купити хай-тег\nбудинок', command=DefBuy3House)



def DefNextListRealEstate():
    Buy2Room.place(x=120, y=1220)
    Label1Room.place(x=-5, y=2000)
    Label2Room.place(x=150, y=2000)
    Label3Room.place(x=0, y=19000)
    LabelHouse1.place(x=150, y=1900)
    NextListRealEstate.config(command=BackListRealEstate)
    LabelHouse2.place(x=-5, y=20)
    LabelHouse3.place(x=150,y=20)
    Buy1Room.place(x=1000,y=1000)
    Buy3Room.place(x=1000,y=1000)
    Buy1House.place(x=150, y=2600)
    Buy2House.place(x=0,y=108)
    Buy3House.place(x=150,y=108)

def BackListRealEstate():
    LabelHouse2.place(x=-5, y=2000)
    LabelHouse3.place(x=150, y=2000)
    Buy2Room.place(x=150, y=122)
    Label1Room.place(x=-5, y=20)
    Label2Room.place(x=150, y=20)
    Label3Room.place(x=0, y=190)
    LabelHouse1.place(x=150, y=190)
    Buy1Room.place(x=0,y=122)
    Buy3Room.place(x=0,y=260)
    Buy1House.place(x=150, y=260)
    NextListRealEstate.config(command=DefNextListRealEstate)
    Buy2House.place_forget()
    Buy3House.place_forget()
def DefBuy1Room():
    global money, HaveDollar,Have1Room, Go1Room,Maining1Room,Orend1Room,Sell1Room
    if (messagebox.askyesno(title="Запит", message="Ви будет купувати квартиру за долари чи за гривні? За доллари - "+ str(1000000//CoursDollar)+', а за '
                'гривні 1.000.00.Що оберете(так-за долари,ні - за гривні)')):
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба '+format(1000000/CoursDollar, '.2f') +' доларів, якщо ви готові натисніть ОК'):
            if HaveDollar >= 1000000//CoursDollar:
                HaveDollar=HaveDollar-1000000//CoursDollar
                Buy1Room.config(text='Керувати квартирою', command=DefSettings1Room)
                Have1Room = True
                Go1Room.config(text='Увійти в дім', width=20, height=3, command=DefGo1Room, state=NORMAL)
                Maining1Room.config(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
                Orend1Room.config(text='Здати в оренду', width=20, height=3, command=DefOrend1Room, state=NORMAL)
                Sell1Room.config(text='Продати квартиру', width=20, height=3, command=DefSell1Room, state=NORMAL)
            else:
                messagebox.askokcancel('Помилка','У вас невистачає доларів для купівлі квартири')
    else:
        if messagebox.askokcancel('Купівля квартири', 'Щоб купити квартиру вам треба 1.000.000 гривень, якщо ви готові натисніть ОК'):
            if money >= 1000000:
                money=money-1000000
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Buy1Room.config(text='Керувати квартирою', command=DefSettings1Room)
                Have1Room = True
                Go1Room.config(text='Увійти в дім', width=20, height=3, command=DefGo1Room, state=NORMAL)
                Maining1Room.config(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
                Orend1Room.config(text='Здати в оренду', width=20, height=3, command=DefOrend1Room, state=NORMAL)
                Sell1Room.config(text='Продати квартиру', width=20, height=3, command=DefSell1Room, state=NORMAL)
            else:
                messagebox.askokcancel('Помилка','У вас невистачає грошей для купівлі квартири')

def DefSettings1Room():
    Buy3Room.place(x=1000,y=1000)
    Label1Room.place(x=-5, y=2000)
    Label2Room.place(x=150, y=2000)
    Label3Room.place(x=0, y=19000)
    LabelHouse1.place(x=150, y=1900)
    NextListRealEstate.place(x=0, y=3300)
    Buy1Room.place(x=1000, y=1000)
    MicroLabel1Room.place(x=110, y=30)
    Go1Room.place(x=80, y=100)
    Maining1Room.place(x=80, y=155)
    Orend1Room.place(x=80, y=211)
    Sell1Room.place(x=80, y=265)
    Buy2Room.place(x=120, y=1220)
    Buy1House.place(x=1000,y=1000)
    if Orend1RoomChange == False:
        Sell1Room.config(state=NORMAL)
        Go1Room.config(state=NORMAL)
    else:
        Sell1Room.config(state=DISABLED)
        Go1Room.config(state=DISABLED)
def DefGo1Room():
        MicroLabel1Room.place(x=1000,y=1000)
        Go1Room.place(x=1000,y=1000)
        Label1RoomInterior.place(x=0,y=80)
        BackMainMenu.place(x=1000,y=1000)
        BackSettings1Room.place(x=2, y=340)
        Maining1Room.place(x=800, y=1750)
        Orend1Room.place(x=80, y=2100)
        Sell1Room.place(x=80, y=2650)


def DefBackSettings1Room():
    LabelBeforeOrend.place(x=-10, y=2000)
    BackSettings1Room.place(x=1000, y=1000)
    Label1RoomInterior.place(x=1000, y=1000)
    MicroLabel1Room.place(x=110, y=30)
    MicroLabel1Room.place(x=110, y=30)
    Go1Room.place(x=80, y=100)
    Maining1Room.place(x=80, y=155)
    Orend1Room.place(x=80, y=211)
    Sell1Room.place(x=80, y=265)
    BackMainMenu.place(x=2, y=340)
    btnStartOrend1Room.place(x=1000, y=1000)
    btnStopTaimerOrend1Room.place(x=55, y=2500)
    LabelOrend.place(x=20, y=1000)
    if Orend1RoomChange == False:
        Sell1Room.config(state=NORMAL)
        Go1Room.config(state=NORMAL)
    else:
        Sell1Room.config(state=DISABLED)
        Go1Room.config(state=DISABLED)
    if Have1Room == False:
        Go1Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend1Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell1Room.config(text='Це не баг, а фіча!', state=DISABLED)
def DefOrend1Room():
    LabelBeforeOrend.place(x=-10, y=15)
    MicroLabel1Room.place(x=1000,y=1000)
    Go1Room.place(x=1000,y=1000)
    BackMainMenu.place(x=1000,y=1000)
    BackSettings1Room.place(x=2, y=340)
    Maining1Room.place(x=800, y=1750)
    Orend1Room.place(x=80, y=2100)
    Sell1Room.place(x=80, y=2650)
    LabelOrend.place(x=0, y=240)
    if Orend1RoomChange == False:
        btnStartOrend1Room.place(x=55,y=280)
    else:
        btnStopTaimerOrend1Room.place(x=40,y=288)


def DefSell1Room():
    global money,Have1Room,Taxes1Room,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 700.000 гривень. Ви зходні?'):
        money=money+700000
        MicroLabel1Room.place(x=1000, y=1000)
        BackMainMenu.place(x=1000, y=1000)
        Maining1Room.place(x=800, y=1750)
        Orend1Room.place(x=80, y=2100)
        Sell1Room.place(x=80, y=2650)
        Go1Room.place(x=1000,y=1000)
        Label1Room.place(x=-5, y=20)
        Label2Room.place(x=150, y=20)
        Label3Room.place(x=0, y=190)
        LabelHouse1.place(x=150,y=190)
        BackMainMenu.place(x=2, y=340)
        NextListRealEstate.place(x=0, y=330)
        Buy1Room.config(text='Купити однокімнатну \n квартиру', command=DefBuy1Room)
        Buy1Room.place(x=0, y=122)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        Buy1Room.place(x=0, y=122)
        Buy2Room.place(x=150, y=122)
        Buy3Room.place(x=0, y=260)
        Buy1House.place(x=150, y=260)
        Have1Room = False
        AllTaxes = AllTaxes-Taxes1Room
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        Taxes1Room = 0
        btnPayTaxes1Room.config(text='Оплатити податки за\nоднокімнатну квартиру\n(' + str(Taxes1Room) + ' гривень)')

def DeftickOrend1Room():
    global TempOrend1Room, AfterIdOrend1Room, s1Room
    AfterIdOrend1Room = root.after(1000,DeftickOrend1Room)
    FTempOrend1Room = str(int(TempOrend1Room/3600))+":"+str(int((TempOrend1Room % 3600) / 60) ) + ":" + str(int(TempOrend1Room % 60))  #  datetime.fromtimestamp(3600000).strftime('%D:%H:%M:%S')
    LabelOrend.config(text=str(FTempOrend1Room))
    TempOrend1Room +=1
    s1Room = TempOrend1Room*20

def DefStartOrend1Room():
    global Orend1RoomChange
    Orend1RoomChange = True
    btnStartOrend1Room.place(x=1000,y=1000)
    btnStopTaimerOrend1Room.place(x=37,y=281)
    DeftickOrend1Room()

def DefStopOrend1Room(v):
    global temp, Orend1RoomChange, money, TempOrend1Room
    Orend1RoomChange = False
    temp = 0
    LabelOrend.config(text='0:0:0')
    btnStopTaimerOrend1Room.place(x=1000,y=1000)
    if v != 1:
        btnStartOrend1Room.place(x=55,y=280)
    else:
        btnStartOrend1Room.place_forget()
    root.after_cancel(AfterIdOrend1Room)
    z1Room = s1Room // 1200
    w1Room = z1Room * 1200
    money = money+w1Room
    TempOrend1Room = 0
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    messagebox.askokcancel('Підсумки здачі в оренду','За '+str(z1Room)+' хвилин здачі ви отримали '+str(w1Room)+' гривень.Промокод: StooopOrend_One-Room')

def DefBuy2Room():
        global money, HaveDollar,Have2Room
        if (messagebox.askyesno(title="Запит",message="Ви будет купувати квартиру за долари чи за гривні? За доллари - " + str(1500000 // CoursDollar) + ', а за ''гривні 1.500.00.Що оберете(так-за долари,ні - за гривні)')):
            if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба ' + format(1500000 / CoursDollar,'.2f') + ' доларів, якщо ви готові натисніть ОК'):
                if HaveDollar >= 1500000 // CoursDollar:
                    HaveDollar = HaveDollar - 1500000 // CoursDollar
                    Buy2Room.config(text='Керувати квартирою', command=DefSettings2Room)
                    Have2Room = True
                    Buy2Room.config(text='Купити двокімнатну \n квартиру', width=20, height=4, command=DefBuy2Room,state=NORMAL)
                    Go2Room.config(text='Увійти в дім', width=20, height=3, command=DefGo2Room, state=NORMAL)
                    Maining2Room.config(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
                    Orend2Room.config(text='Здати в оренду', width=20, height=3, command=DefOrend2Room, state=NORMAL)
                    Sell2Room.config(text='Продати квартиру', width=20, height=3, command=DefSell2Room, state=NORMAL)
                else:
                    messagebox.askokcancel('Помилка', 'У вас невистачає доларів для купівлі квартири')
        else:
            if messagebox.askokcancel('Купівля квартири',
                                      'Щоб купити квартиру вам треба 1.500.000 гривень, якщо ви готові натисніть ОК'):
                if money >= 1500000:
                    money = money - 1500000
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    Buy2Room.config(text='Керувати квартирою', command=DefSettings2Room)
                    Have2Room = True
                else:
                    messagebox.askokcancel('Помилка', 'У вас невистачає грошей для купівлі квартири')

def DefSettings2Room():
    Buy3Room.place(x=1000, y=1000)
    Label1Room.place(x=-5, y=2000)
    Label2Room.place(x=150, y=2000)
    Label3Room.place(x=0, y=19000)
    LabelHouse1.place(x=150, y=1900)
    NextListRealEstate.place(x=0, y=3300)
    Buy1Room.place(x=1000, y=1000)
    MicroLabel2Room.place(x=110, y=30)
    Go2Room.place(x=80, y=100)
    Maining2Room.place(x=80, y=155)
    Orend2Room.place(x=80, y=211)
    Sell2Room.place(x=80, y=265)
    Buy2Room.place(x=120, y=1220)
    btnStartOrend1Room.place(x=1000,y=1000)
    Buy1House.place(x=150, y=2600)
    if Orend2RoomChange == False:
        Sell2Room.config(state=NORMAL)
        Go2Room.config(state=NORMAL)
    else:
        Sell2Room.config(state=DISABLED)
        Go2Room.config(state=DISABLED)
def DefGo2Room():
        MicroLabel2Room.place(x=1000,y=1000)
        Go2Room.place(x=1000,y=1000)
        Label2RoomInterior.place(x=0,y=80)
        BackMainMenu.place(x=1000,y=1000)
        BackSettings2Room.place(x=2, y=340)
        Maining2Room.place(x=800, y=1750)
        Orend2Room.place(x=80, y=2100)
        Sell2Room.place(x=80, y=2650)
        NextInterier.place(x=150,y=280)


def DefBackSettings2Room():
    MicroLabel2Room.place(x=110, y=30)
    Go2Room.place(x=80, y=100)
    Maining2Room.place(x=80, y=155)
    Orend2Room.place(x=80, y=211)
    Sell2Room.place(x=80, y=265)
    NextInterier.place(x=1000,y=1000)
    BackInterier.place(x=1000,y=1000)
    Label2RoomInterior.place(x=1000,y=1000)
    Label2RoomInterior2.place(x=1000,y=1000)
    Label2RoomInterior3.place(x=1000,y=1000)
    LabelBeforeOrend2Room.place(x=-10, y=2000)
    BackSettings2Room.place(x=1000, y=1000)
    Label2RoomInterior.place(x=1000, y=1000)
    BackMainMenu.place(x=2, y=340)
    btnStartOrend2Room.place(x=1000, y=1000)
    btnStopTaimerOrend2Room.place(x=55, y=2500)
    LabelOrend.place(x=20, y=1000)
    NextInterier.config(command = DefNextListInterier1)
    if Orend2RoomChange == False:
        Sell2Room.config(state=NORMAL)
        Go2Room.config(state=NORMAL)
    else:
        Sell2Room.config(state=DISABLED)
        Go2Room.config(state=DISABLED)
    if Have2Room == False:
        Go2Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend2Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell2Room.config(text='Це не баг, а фіча!', state=DISABLED)

def DefOrend2Room():
    MicroLabel2Room.place(x=1000,y=1000)
    Go2Room.place(x=1000,y=1000)
    BackMainMenu.place(x=1000,y=1000)
    BackSettings2Room.place(x=2, y=340)
    Maining2Room.place(x=800, y=1750)
    Orend2Room.place(x=80, y=2100)
    Sell2Room.place(x=80, y=2650)
    LabelOrend2Room.place(x=0, y=240)
    LabelBeforeOrend2Room.place(x=-10, y=15)
    if Orend2RoomChange == False:
        btnStartOrend2Room.place(x=55,y=280)
    else:
        btnStopTaimerOrend2Room.place(x=40,y=288)


def DefSell2Room():
    global money,Have2Room,Taxes2Room,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 1.050.000 гривень. Ви зходні?'):
        money=money+1050000
        Buy1House.place(x=1000, y=1000)
        MicroLabel2Room.place(x=1000, y=1000)
        BackMainMenu.place(x=1000, y=1000)
        Maining2Room.place(x=800, y=1750)
        Orend2Room.place(x=80, y=2100)
        Sell2Room.place(x=80, y=2650)
        Go2Room.place(x=1000,y=1000)
        Label1Room.place(x=-5, y=20)
        Label2Room.place(x=150, y=20)
        Label3Room.place(x=0, y=190)
        LabelHouse1.place(x=150, y=260)
        LabelHouse1.place(x=150, y=190)
        BackMainMenu.place(x=2, y=340)
        NextListRealEstate.place(x=0, y=330)
        Buy1Room.place(x=0, y=122)
        Buy2Room.place(x=150, y=122)
        Buy3Room.place(x=0, y=260)
        Buy1House.place(x=150, y=260)
        Buy2Room.config(text='Купити двокімнатну \n квартиру', command=DefBuy1Room)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        AllTaxes = AllTaxes - Taxes2Room
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        Taxes2Room = 0
        btnPayTaxes2Room.config(text='Оплатити податки за\nдвокімнатну квартиру\n(' + str(Taxes2Room) + ' гривень)')
        Have2Room = False
        


def DeftickOrend2Room():
    global TempOrend2Room, AfterIdOrend2Room, s2Room
    AfterIdOrend2Room = root.after(1000,DeftickOrend2Room)
    FTempOrend2Room = str(int(TempOrend2Room/3600))+":"+str(int((TempOrend2Room % 3600) / 60) ) + ":" + str(int(TempOrend2Room % 60))
    LabelOrend2Room.config(text=str(FTempOrend2Room))
    TempOrend2Room +=1
    s2Room = TempOrend2Room*30

def DefStartOrend2Room():
    global Orend2RoomChange
    Orend2RoomChange = True
    btnStartOrend2Room.place(x=1000,y=1000)
    btnStopTaimerOrend2Room.place(x=37,y=281)
    DeftickOrend2Room()

def DefStopOrend2Room(v):
    global temp, Orend2RoomChange, money, TempOrend2Room
    Orend2RoomChange = False
    temp = 0
    LabelOrend2Room.config(text='0:0:0')
    btnStopTaimerOrend2Room.place(x=1000,y=1000)
    btnStartOrend2Room.place(x=55,y=280)
    root.after_cancel(AfterIdOrend2Room)
    if v != 1:
        btnStartOrend2Room.place(x=55,y=280)
    else:
        btnStartOrend2Room.place_forget()
    root.after_cancel(AfterIdOrend1Room)
    z2Room = s2Room // 1800
    w2Room = z2Room * 1800
    money = money+w2Room
    TempOrend2Room = 0
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    
    messagebox.askokcancel('Підсумки здачі в оренду','За '+str(z2Room)+' хвилин здачі ви отримали '+str(w2Room)+' гривень')

def DefNextListInterier1():
    Label2RoomInterior.place(x=1000,y=1000)
    Label2RoomInterior2.place(x=0,y=80)
    NextInterier.config(command=DefNextListInterier2)
    BackInterier.place(x=0,y=280)

def DefNextListInterier2():
    NextInterier.place(x=1000,y=1000)
    Label2RoomInterior3.place(x=0,y=80)
    Label2RoomInterior2.place(x=1000,y=1000)
    BackInterier.config(command=DefBackListInterier2)

def DefBackListInterier1():
    Label2RoomInterior.place(x=0, y=80)
    Label2RoomInterior2.place(x=1000,y=1000)
    NextInterier.config(command = DefNextListInterier1)
    BackInterier.place(x=1000,y=1000)

def DefBackListInterier2():
    Label2RoomInterior3.place(x=0, y=8000)
    Label2RoomInterior2.place(x=0, y=80)
    BackInterier.config(command=DefBackListInterier1)
    NextInterier.place(x=150, y=280)
    NextInterier.config(command=DefNextListInterier1)


def DefBuy3Room():
    global money, HaveDollar,Have3Room
    if (messagebox.askyesno(title="Запит",message="Ви будет купувати квартиру за долари чи за гривні? За доллари - " + str(2000000// CoursDollar) + ', а за ''гривні 2.000.00.Що оберете(так-за долари,ні - за гривні)')):
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба ' + format(2000000 / CoursDollar,'.2f') + ' доларів, якщо ви готові натисніть ОК'):
            if HaveDollar >= 2000000 // CoursDollar:
                HaveDollar = HaveDollar - 2000000 // CoursDollar
                Buy3Room.config(text='Керувати квартирою', command=DefSettings3Room)
                Have3Room = True
                Go3Room.config(text='Увійти в дім', state=NORMAL)
                Maining3Room.config(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
                Orend3Room.config(text='Здати в оренду', width=20, height=3, command=DefOrend3Room, state=NORMAL)
                Sell3Room.config(text='Продати квартиру', width=20, height=3, command=DefSell3Room, state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає доларів для купівлі квартири')
    else:
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба 2.000.000 гривень, якщо ви готові натисніть ОК'):
            if money >= 2000000:
                money = money - 2000000
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Buy3Room.config(text='Керувати квартирою', command=DefSettings3Room)
                Have3Room = True
                Go3Room.config(text='Увійти в дім', width=20, height=3,state=NORMAL)
                Maining3Room.config(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
                Orend3Room.config(text='Здати в оренду', width=20, height=3, command=DefOrend3Room, state=NORMAL)
                Sell3Room.config(text='Продати квартиру', width=20, height=3, command=DefSell3Room, state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає грошей для купівлі квартири')

def DefSettings3Room():
    Buy2Room.place(x=1000, y=1000)
    Buy3Room.place(x=1000, y=1000)
    Label1Room.place(x=-5, y=2000)
    Label2Room.place(x=150, y=2000)
    Label3Room.place(x=0, y=19000)
    LabelHouse1.place(x=150, y=1900)
    NextListRealEstate.place(x=0, y=3300)
    Buy1Room.place(x=1000, y=1000)
    MicroLabel3Room.place(x=110, y=30)
    Go3Room.place(x=80, y=100)
    Maining3Room.place(x=80, y=155)
    Orend3Room.place(x=80, y=211)
    Sell3Room.place(x=80, y=265)
    Buy3Room.place(x=120, y=1220)
    Buy1House.place(x=150, y=2600)
    if Orend3RoomChange == False:
        Sell3Room.config(state=NORMAL)
        Go3Room.config(state=NORMAL)
    else:
        Sell3Room.config(state=DISABLED)
        Go3Room.config(state=DISABLED)

def Go3RoomCommand(images):
    MicroLabel3Room.place_forget()
    Go3Room.place_forget()
    BackMainMenu.place_forget()
    Maining3Room.place_forget()
    Orend3Room.place_forget()
    Sell3Room.place_forget()

    BackSettings3Room.place(x=2, y=340)
    CurrentSlide.place(x=0, y=80)
    ImageSlider(images, 0)


def ImageSlider(images, pos):
    image = Image.open(images[pos])
    image = image.resize((300, 200))
    photo = ImageTk.PhotoImage(image)
    CurrentSlide.config(image=photo)
    CurrentSlide.image = photo

    BackSlide.config(command=lambda: ImageSlider(images, pos - 1))
    NextSlide.config(command=lambda: ImageSlider(images, pos + 1))

    count = len(images)

    if pos == 0:
        BackSlide.place_forget()
    else:
        BackSlide.place(x=2, y=280)

    if pos == count - 1:
        NextSlide.place_forget()
    else:
        NextSlide.place(x=150, y=280)


def DefBackSettings3Room():
    Buy2Room.place(x=1000,y=1000)
    NextSlide.place_forget()
    BackSlide.place_forget()
    CurrentSlide.place_forget()
    LabelBeforeOrend3Room.place(x=-10, y=2000)
    BackSettings3Room.place(x=1000, y=1000)
    BackMainMenu.place(x=2, y=340)
    MicroLabel3Room.place(x=110, y=30)
    Go3Room.place(x=80, y=100)
    Maining3Room.place(x=80, y=155)
    Orend3Room.place(x=80, y=211)
    Sell3Room.place(x=80, y=265)
    btnStartOrend3Room.place(x=1000, y=1000)
    btnStopTaimerOrend3Room.place(x=55, y=2500)
    LabelOrend3Room.place(x=20, y=1000)
    if Orend3RoomChange == False:
        Sell3Room.config(state=NORMAL)
        Go3Room.config(state=NORMAL)
    else:
        Sell3Room.config(state=DISABLED)
        Go3Room.config(state=DISABLED)
    if Have3Room == False:
        Go3Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend3Room.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell3Room.config(text='Це не баг, а фіча!', state=DISABLED)

def DefOrend3Room():
    LabelBeforeOrend3Room.place(x=-10, y=15)
    MicroLabel3Room.place(x=1000,y=1000)
    Go3Room.place_forget() # .place(x=1000,y=1000)
    BackMainMenu.place(x=1000,y=1000)
    BackSettings3Room.place(x=2, y=340)
    Maining3Room.place(x=800, y=1750)
    Orend3Room.place(x=80, y=2100)
    Sell3Room.place(x=80, y=2650)
    LabelOrend3Room.place(x=0, y=240)
    if Orend3RoomChange == False:
        btnStartOrend3Room.place(x=55,y=280)
    else:
        btnStopTaimerOrend3Room.place(x=40,y=288)


def DefSell3Room():
    global money,Have3Room,Taxes3Room,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 1.400.000 гривень. Ви зходні?'):
        money=money+1400000
        MicroLabel3Room.place(x=1000, y=1000)
        BackMainMenu.place(x=1000, y=1000)
        Maining3Room.place(x=800, y=1750)
        Orend3Room.place(x=80, y=2100)
        Sell3Room.place(x=80, y=2650)
        Go3Room.place_forget() # .place(x=1000,y=1000)
        Label1Room.place(x=-5, y=20)
        Label2Room.place(x=150, y=20) 
        Label3Room.place(x=0, y=190)
        LabelHouse1.place(x=150, y=190)
        BackMainMenu.place(x=2, y=340)
        NextListRealEstate.place(x=0, y=330)
        Buy1Room.place(x=0, y=122)
        Buy2Room.place(x=150, y=122)
        Buy3Room.place(x=0, y=260)
        Buy1House.place(x=150, y=260)
        Buy3Room.config(text='Купити трьохкімнатну \n квартиру', command=DefBuy3Room)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        Have3Room = False
        AllTaxes = AllTaxes - Taxes3Room
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        Taxes3Room = 0
        btnPayTaxes3Room.config(text='Оплатити податки за\nтрьохкімнатну квартиру\n(' + str(Taxes3Room) + ' гривень)')
        


def DeftickOrend3Room():
    global TempOrend3Room, AfterIdOrend3Room, s3Room
    AfterIdOrend3Room = root.after(1000,DeftickOrend3Room)
    FTempOrend3Room = str(int(TempOrend3Room/3600))+":"+str(int((TempOrend3Room % 3600) / 60) ) + ":" + str(int(TempOrend3Room % 60))
    LabelOrend3Room.config(text=str(FTempOrend3Room))
    TempOrend3Room +=1
    s3Room = TempOrend3Room*40

def DefStartOrend3Room():
    global Orend3RoomChange
    Orend3RoomChange = True
    btnStartOrend3Room.place(x=1000,y=1000)
    btnStopTaimerOrend3Room.place(x=37,y=281)
    DeftickOrend3Room()

def DefStopOrend3Room(v):
    global temp, Orend3RoomChange, money,TempOrend3Room
    Orend3RoomChange = False
    temp = 0
    LabelOrend3Room.config(text='0:0:0')
    btnStopTaimerOrend3Room.place(x=1000,y=1000)
    btnStartOrend3Room.place(x=55,y=280)
    root.after_cancel(AfterIdOrend3Room)
    if v != 1:
        btnStartOrend3Room.place(x=55,y=280)
    else:
        btnStartOrend3Room.place_forget()
    root.after_cancel(AfterIdOrend1Room)
    z3Room = s3Room // 2400
    w3Room = z3Room * 2400
    money = money+w3Room
    TempOrend3Room = 0
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    
    messagebox.askokcancel('Підсумки здачі в оренду','За '+str(z3Room)+' хвилин здачі ви отримали '+str(w3Room)+' гривень')



def DefBuy1House():
    global money, HaveDollar,Have1House
    if (messagebox.askyesno(title="Запит",message="Ви будет купувати квартиру за долари чи за гривні? За доллари - " + str(5000000// CoursDollar) + ', а за ''гривні 5.000.00.Що оберете(так-за долари,ні - за гривні)')):
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба ' + format(5000000 / CoursDollar,'.2f') + ' доларів, якщо ви готові натисніть ОК'):
            if HaveDollar >= 5000000 // CoursDollar:
                HaveDollar = HaveDollar - 5000000 // CoursDollar
                Buy1House.config(text='Керувати будинком', command=DefSettings1House)
                Have1House = True
                Go1House.config(text='Увійти в дім',state=NORMAL)
                Maining1House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend1House.config(text='Здати в оренду', state=NORMAL)
                Sell1House.config(text='Продати дім',state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає доларів для купівлі квартири')
    else:
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба 5.000.000 гривень, якщо ви готові натисніть ОК'):
            if money >= 5000000:
                money = money - 5000000
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Buy1House.config(text='Керувати будинком', command=DefSettings1House)
                Have1House = True
                Go1House.config(text='Увійти в дім', state=NORMAL)
                Maining1House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend1House.config(text='Здати в оренду', state=NORMAL)
                Sell1House.config(text='Продати дім', state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає грошей для купівлі квартири')

def DefSettings1House():
    Label1Room.place(x=-5, y=2000)
    Label2Room.place(x=150, y=2000)
    Label3Room.place(x=0, y=19000)
    LabelHouse1.place(x=150, y=1900)
    NextListRealEstate.place(x=0, y=3300)
    Buy1Room.place(x=1000, y=1000)
    Buy2Room.place(x=1000,y=1000)
    Buy3Room.place(x=1000,y=1000)
    Buy1House.place(x=1000,y=1000)
    MicroLabel1House.place(x=110, y=30)
    Go1House.place(x=80, y=100)
    Maining1House.place(x=80, y=155)
    Orend1House.place(x=80, y=211)
    Sell1House.place(x=80, y=265)
    if Orend1HouseChange == False:
        Sell1House.config(state=NORMAL)
        Go1House.config(state=NORMAL)
    else:
        Sell1House.config(state=DISABLED)
        Go1House.config(state=DISABLED)
def DefGo1House():
        MicroLabel1House.place(x=1000,y=1000)
        Go1House.place(x=1000,y=1000)
        Label1HouseInterior.place(x=0,y=80)
        BackMainMenu.place(x=1000,y=1000)
        BackSettings1House.place(x=2, y=340)
        Maining1House.place(x=800, y=1750)
        Orend1House.place(x=80, y=2100)
        Sell1House.place(x=80, y=2650)


def DefMaining1House():
    MicroLabel1House.place(x=1000, y=1000)
    Go1House.place(x=1000, y=1000)
    BackMainMenu.place(x=1000, y=1000)
    BackSettings1House.place(x=2, y=340)
    Maining1House.place(x=800, y=1750)
    Orend1House.place(x=80, y=2100)
    Sell1House.place(x=80, y=2650)
    LabelMaining1House.place(x=-5,y=22)
    BuyVideoCard1House.place(x=2, y=180)
    BuyFrameForMining1House.place(x=2, y=220)
    BuyMiner1House.place(x=2, y=260)
    BuyMainingSetUp1House.place(x=2, y=300)
    if VideoCard1House:
        BuyVideoCard1House.place(x=2, y=1800)
    if FrameForMining1House:
        BuyFrameForMining1House.place(x=2, y=2200)
    if MainingIn1House:
        BuyMiner1House.place(x=2, y=2600)
    if MainingSetUp1House:
        BuyMainingSetUp1House.place(x=2, y=3000)
    if VideoCard1House==True and FrameForMining1House==True and MainingIn1House==True and MainingSetUp1House==True:
        btnCanGoTOBasement1House.place(x=2,y=240)



def DefBackSettings1House():
    LabelBeforeOrend1House.place(x=-10, y=2000)
    BackSettings1House.place(x=1000, y=1000)
    Label1HouseInterior.place(x=1000, y=1000)
    MicroLabel1House.place(x=110, y=30)
    BackMainMenu.place(x=2, y=340)
    btnStartOrend1House.place(x=1000, y=1000)
    btnStopTaimerOrend1House.place(x=55, y=2500)
    LabelMaining1House.place(x=1000,y=1000)
    LabelOrend1House.place(x=20, y=1000)
    BuyVideoCard1House.place(x=2, y=1800)
    BuyFrameForMining1House.place(x=2, y=2200)
    BuyMiner1House.place(x=2, y=2600)
    BuyMainingSetUp1House.place(x=2, y=3000)
    Go1House.place(x=80, y=100)
    Maining1House.place(x=80, y=155)
    Orend1House.place(x=80, y=211)
    Sell1House.place(x=80, y=265)
    LabelMainingFarm1.place(x=-2, y=2000)
    LabelMainingFarm2.place(x=148, y=2000)
    LabelMainingFarm3.place(x=-2, y=950)
    LabelMainingFarm4.place(x=148, y=950)
    LabelMainingFarm5.place(x=75, y=1700)
    btnStartMining1House.place(x=2, y=3000)
    LabelTaimerMaining1House.place(x=1000,y=1000)
    btnCanGoTOBasement1House.place_forget()
    btnStopTaimerMaining1House.place_forget()
    if Orend1HouseChange == False:
        Sell1House.config(state=NORMAL)
        Go1House.config(state=NORMAL)
    else:
        Sell1House.config(state=DISABLED)
        Go1House.config(state=DISABLED)
    if Have1House == False:
        Go1House.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend1House.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell1House.config(text='Це не баг, а фіча!', state=DISABLED)
        Maining1House.config(text='Це не баг, а фіча!', state=DISABLED)

def DefOrend1House():
    LabelBeforeOrend1House.place(x=-10, y=20)
    MicroLabel1House.place(x=1000,y=1000)
    Go1House.place(x=1000,y=1000)
    BackMainMenu.place(x=1000,y=1000)
    BackSettings1House.place(x=2, y=340)
    Maining1House.place(x=800, y=1750)
    Orend1House.place(x=80, y=2100)
    Sell1House.place(x=80, y=2650)
    LabelOrend1House.place(x=0, y=240)
    if Orend1HouseChange == False:
        btnStartOrend1House.place(x=55,y=280)
    else:
        btnStopTaimerOrend1House.place(x=40,y=288)





def DefSell1House():
    global money, VideoCard1House, CanGoToBasement1Home, MainingSetUp1House, MainingIn1House,FrameForMining1House,Have1House,Taxes1House,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 3.500.000 гривень. Ви зходні?'):
        money=money+3500000
        try:
            DefStopMining1House(1)
        except:
            pass
        VideoCard1House = False
        CanGoToBasement1Home = False
        MainingIn1House = False
        MainingSetUp1House = False
        FrameForMining1House = False
        MicroLabel1House.place(x=1000, y=1000)
        BackMainMenu.place(x=1000, y=1000)
        Maining1House.place(x=800, y=1750)
        Orend1House.place(x=80, y=2100)
        Sell1House.place(x=80, y=2650)
        Go1House.place(x=1000,y=1000)
        Label1Room.place(x=-5, y=20)
        Label2Room.place(x=150, y=20)
        Label3Room.place(x=-5, y=190)
        LabelHouse1.place(x=150, y=190)
        BackMainMenu.place(x=2, y=340)
        NextListRealEstate.place(x=0, y=330)
        Buy1House.config(text='Купити одноповерховий \n будинок', command=DefBuy1House)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        Buy1Room.place(x=0, y=122)
        Buy2Room.place(x=150, y=122)
        Buy3Room.place(x=0, y=260)
        Buy1House.place(x=150, y=260)
        Have1House = False
        AllTaxes = AllTaxes - Taxes1House
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        Taxes1House = 0
        btnPayTaxes1House.config(text='Оплатити податки за\nодноповерховий будинок\n(' + str(Taxes1House) + ' гривень)')

def DeftickOrend1House():
    global TempOrend1House, AfterIdOrend1House, s1House
    AfterIdOrend1House = root.after(1000,DeftickOrend1House)
    FTempOrend1House = str(int(TempOrend1House/3600))+":"+str(int((TempOrend1House % 3600) / 60) ) + ":" + str(int(TempOrend1House % 60))
    LabelOrend1House.config(text=str(FTempOrend1House))
    TempOrend1House +=1
    s1House = TempOrend1House*100

def DefStartOrend1House():
    global Orend1HouseChange
    Orend1HouseChange = True
    btnStartOrend1House.place(x=1000,y=1000)
    btnStopTaimerOrend1House.place(x=37,y=281)
    DeftickOrend1House()

def DefStopOrend1House(v):
    global temp, Orend1HouseChange, money,TempOrend1House
    Orend1HouseChange = False
    temp = 0
    LabelOrend1House.config(text='0:0:0')
    btnStopTaimerOrend1House.place(x=1000,y=1000)
    btnStartOrend1House.place(x=55,y=280)
    root.after_cancel(AfterIdOrend1House)
    if v != 1:
        btnStartOrend1House.place(x=55,y=280)
    else:
        btnStartOrend1House.place_forget()
    root.after_cancel(AfterIdOrend1Room)
    z1House = s1House // 6000
    w1House = z1House * 6000
    money = money+w1House
    TempOrend1House = 0
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    
    messagebox.askokcancel('Підсумки здачі в оренду','За '+str(z1House)+' хвилин здачі ви отримали '+str(w1House)+' гривень')


def DefBuyVideoCard1House():
    global money, VideoCard1House, CanGoToBasement1Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 280000 грн на 20 відео карт?'):
        if money>=280000:
            money = money - 280000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            VideoCard1House = True
            BuyVideoCard1House.place(x=1000,y=1000)
            if FrameForMining1House and MainingIn1House and MainingSetUp1House and VideoCard1House:
                CanGoToBasement1Home = True
                btnCanGoTOBasement1House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка','У вас невистачає грошей, щоб купити це')
def DefBuyMainingSetUp1House():
    global money, MainingSetUp1House, CanGoToBasement1Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 2000 грн на налаштуванння цієї системи?'):
        if money>=2000:
            money = money - 2000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingSetUp1House = True
            BuyMainingSetUp1House.place(x=1000,y=1000)
            if FrameForMining1House and MainingIn1House and MainingSetUp1House and VideoCard1House:
                CanGoToBasement1Home = True
                btnCanGoTOBasement1House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка','У вас невистачає грошей, щоб купити це')
def DefBuyMiner1House():
    global money, MainingIn1House, CanGoToBasement1Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 30000 грн на майнер відео карт?'):
        if money>=30000:
            money = money - 30000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingIn1House = True
            BuyMiner1House.place(x=1000,y=1000)
            if FrameForMining1House and MainingIn1House and MainingSetUp1House and VideoCard1House:
                CanGoToBasement1Home = True
                btnCanGoTOBasement1House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка','У вас невистачає грошей, щоб купити це')

def DefBuyFrameForMining1House():
    global money,FrameForMining1House, CanGoToBasement1Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 10000 грн на каркас для відео карт'):
        if money>=10000:
            money = money - 10000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            FrameForMining1House = True
            BuyFrameForMining1House.place(x=1000,y=1000)
            if FrameForMining1House and MainingIn1House and MainingSetUp1House and VideoCard1House:
                CanGoToBasement1Home = True
                btnCanGoTOBasement1House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка','У вас невистачає грошей, щоб купити це')


def DefCanGoToBasement1Home():
    LabelMaining1House.place(x=1000,y=1000)
    btnCanGoTOBasement1House.place(x=1000,y=1000)
    LabelMainingFarm1.place(x=-2,y=20)
    LabelMainingFarm2.place(x=148,y=20)
    LabelMainingFarm3.place(x=-2,y=95)
    LabelMainingFarm4.place(x=148,y=95)
    LabelMainingFarm5.place(x=75,y=170)
    LabelTaimerMaining1House.place(x=10, y=260)
    if Maining1HouseChange:
        btnStopTaimerMaining1House.place(x=2, y=300)
    else:
        btnStartMining1House.place(x=2, y=300)


def DeftickMining1House():
    global TempMaining1House, AfterIdMaining1House, Crypto1House
    AfterIdMaining1House = root.after(1000,DeftickMining1House)
    FTempMining1House = str(int(TempMaining1House/3600))+":"+str(int((TempMaining1House % 3600) / 60) ) + ":" + str(int(TempMaining1House % 60))
    LabelTaimerMaining1House.config(text=str(FTempMining1House))
    TempMaining1House +=1
    Crypto1House = TempMaining1House*1

def DefStartMining1House():
    global Maining1HouseChange
    Maining1HouseChange = True
    btnStartMining1House.place(x=1000,y=1000)
    btnStopTaimerMaining1House.place(x=2,y=300)
    DeftickMining1House()

def DefStopMining1House(v):
    global temp, Maining1HouseChange, money, TempMaining1House, HaveShopCoins
    Maining1HouseChange = False
    temp = 0
    LabelTaimerMaining1House.config(text='0:0:0')
    btnStopTaimerMaining1House.place(x=1000,y=1000)
    root.after_cancel(AfterIdMaining1House)
    if v != 1:
        btnStartMining1House.place(x=2,y=300)
    else:
        btnStartMining1House.place_forget()
    TempMaining1House = 0
    messagebox.askokcancel('Підсумки майнингу. ','За час поки ви майнили ви отримали '+str(Crypto1House)+' ShopCoins Промокод:Mining_1HOUSE_lox_')
    HaveShopCoins = HaveShopCoins + Crypto1House
    #print(AllCrypto)




def DefBuy2House():
    global money, HaveDollar,Have2House
    if (messagebox.askyesno(title="Запит",message="Ви будет купувати квартиру за долари чи за гривні? За доллари - " + str(7500000 // CoursDollar) + ', а за ''гривні 7.500.00.Що оберете(так-за долари,ні - за гривні)')):
        if messagebox.askokcancel('Купівля квартири', 'Щоб купити квартиру вам треба ' + format(7500000 / CoursDollar,'.2f') + ' доларів, якщо ви готові натисніть ОК'):
            if HaveDollar >= 7500000 // CoursDollar:
                HaveDollar = HaveDollar - 7500000 // CoursDollar
                Buy2House.config(text='Керувати будинком', command=DefSettings2House)
                Have2House = True
                Go2House.config(text='Увійти в дім', state=NORMAL)
                Maining2House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend2House.config(text='Здати в оренду', state=NORMAL)
                Sell2House.config(text='Продати дім', state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає доларів для купівлі квартири')
    else:
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба 7.500.000 гривень, якщо ви готові натисніть ОК'):
            if money >= 7500000:
                money = money - 7500000
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Buy2House.config(text='Керувати будинком', command=DefSettings2House)
                Have2House = True
                Go2House.config(text='Увійти в дім', state=NORMAL)
                Maining2House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend2House.config(text='Здати в оренду', state=NORMAL)
                Sell2House.config(text='Продати дім', state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає грошей для купівлі квартири')

def DefSettings2House():
    LabelHouse3.place_forget()
    LabelHouse2.place_forget()
    Buy2House.place_forget()
    Buy3House.place_forget()
    MicroLabel2House.place(x=110, y=30)
    Go2House.place(x=80, y=100)
    Maining2House.place(x=80, y=155)
    Orend2House.place(x=80, y=211)
    Sell2House.place(x=80, y=265)
    NextListRealEstate.place_forget()
    if Orend2HouseChange == False:
        Sell2House.config(state=NORMAL)
        Go2House.config(state=NORMAL)
    else:
        Sell2House.config(state=DISABLED)
        Go2House.config(state=DISABLED)
def DefGo2House():
        MicroLabel2House.place_forget()
        Go2House.place_forget()
        LabelHouse2Interier1.place(x=0,y=80)
        BackMainMenu.place_forget()
        BackSettings2House.place(x=2, y=340)
        Maining2House.place_forget()
        Orend2House.place_forget()
        Sell2House.place_forget()
        NextListInterier2House.place(x=150, y=280)


def DefMaining2House():
    Go2House.place_forget()
    MicroLabel2House.place_forget()
    BackMainMenu.place_forget()
    BackSettings2House.place(x=2, y=340)
    Maining2House.place_forget()
    Orend2House.place_forget()
    Sell2House.place_forget()
    LabelMaining2House.place(x=-5,y=22)
    BuyVideoCard2House.place(x=2, y=180)
    BuyFrameForMining2House.place(x=2, y=220)
    BuyMiner2House.place(x=2, y=260)
    BuyMainingSetUp2House.place(x=2, y=300)
    if VideoCard2House:
        BuyVideoCard2House.place_forget()
    if FrameForMining2House:
        BuyFrameForMining2House.place_forget()
    if MainingIn2House:
        BuyMiner2House.place_forget()
    if MainingSetUp2House:
        BuyMainingSetUp2House.place_forget()
    if VideoCard2House and FrameForMining2House and MainingIn2House and MainingSetUp2House:
        btnCanGoTOBasement2House.place(x=2,y=240)



def DefBackSettings2House():
    #NextListMiningFarm2House.place_forget()
    LabelBeforeOrend2House.place_forget()
    BackSettings2House.place_forget()
    LabelHouse2Interier1.place_forget()
    LabelHouse2Interier2.place_forget()
    MicroLabel2House.place(x=110, y=30)
    BackMainMenu.place(x=2, y=340)
    btnStartOrend2House.place_forget()
    btnStopTaimerOrend2House.place_forget()
    LabelMaining2House.place_forget()
    LabelOrend2House.place_forget()
    BuyVideoCard2House.place_forget()
    BuyFrameForMining2House.place_forget()
    BuyMiner2House.place_forget()
    BuyMainingSetUp2House.place_forget()
    Go2House.place(x=80, y=100)
    Maining2House.place(x=80, y=155)
    Orend2House.place(x=80, y=211)
    Sell2House.place(x=80, y=265)
    LabelMainingFarm1.place_forget()
    LabelMainingFarm2.place_forget()
    LabelMainingFarm3.place_forget()
    LabelMainingFarm4.place_forget()
    LabelMainingFarm5.place_forget()
    btnStartMining2House.place_forget()
    LabelTaimerMaining2House.place_forget()
    btnCanGoTOBasement2House.place_forget()
    btnStopTaimerMaining2House.place_forget()
    LabelMainingFarm6.place_forget()
    LabelMainingFarm7.place_forget()
    LabelHalfMainingFarm1.place_forget()
    NextListMaining2House.place_forget()
    LabelHouse2Interier2.place_forget()
    LabelHouse2Interier1.place_forget()
    NextListInterier2House.place_forget()
    NextListInterier2House.config(command=DefNextListInterier2House, text='>>>>')
    if Orend2HouseChange == False:
        Sell2House.config(state=NORMAL)
        Go2House.config(state=NORMAL)
    else:
        Sell2House.config(state=DISABLED)
        Go2House.config(state=DISABLED)
    if Have2House == False:
        Go2House.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend2House.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell2House.config(text='Це не баг, а фіча!', state=DISABLED)
        Maining2House.config(text='Це не баг, а фіча!', state=DISABLED)
def DefOrend2House():
    LabelBeforeOrend2House.place(x=-10, y=20)
    MicroLabel2House.place_forget()
    Go2House.place_forget()
    BackMainMenu.place_forget()
    BackSettings2House.place(x=2, y=340)
    Maining2House.place(x=800, y=1750)
    Orend2House.place(x=80, y=2100)
    Sell2House.place(x=80, y=2650)
    LabelOrend2House.place(x=0, y=240)
    if Orend2HouseChange == False:
        btnStartOrend2House.place(x=55,y=280)
    else:
        btnStopTaimerOrend2House.place(x=40,y=288)





def DefSell2House():
    global money, VideoCard2House, CanGoToBasement2Home, MainingSetUp2House, MainingIn2House,FrameForMining2House,Have2House,Taxes2House,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 5.250.000 гривень. Ви зходні?'):
        try:
            DefStopMining2House(1)
        except:
            pass
        money=money+5250000
        VideoCard2House = False
        CanGoToBasement2Home = False
        MainingIn2House = False
        MainingSetUp2House = False
        FrameForMining2House = False
        MicroLabel2House.place_forget()
        BackMainMenu.place_forget()
        Maining2House.place_forget()
        Orend2House.place_forget()
        Sell2House.place_forget()
        Go2House.place_forget()
        Label1Room.place(x=-5, y=20)
        Label2Room.place(x=150, y=20)
        Label3Room.place(x=-5, y=190)
        LabelHouse1.place(x=150, y=190)
        BackMainMenu.place(x=2, y=340)
        NextListRealEstate.place(x=0, y=330)
        Buy2House.config(text='Купити двоповерховий \n будинок', command=DefBuy2House)
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        Buy1Room.place(x=0, y=122)
        Buy2Room.place(x=150, y=122)
        Buy3Room.place(x=0, y=260)
        Buy1House.place(x=150, y=260)
        Have2House = False
        AllTaxes = AllTaxes - Taxes2House
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        Taxes2House = 0
        btnPayTaxes2House.config(text='Оплатити податки за\nдвоповерховий будинок\n(' + str(Taxes2House) + ' гривень)')


def DeftickOrend2House():
    global TempOrend2House, AfterIdOrend2House, s2House
    AfterIdOrend2House = root.after(1000,DeftickOrend2House)
    FTempOrend2House = str(int(TempOrend2House/3600))+":"+str(int((TempOrend2House % 3600) / 60) ) + ":" + str(int(TempOrend2House % 60))
    LabelOrend2House.config(text=str(FTempOrend2House))
    TempOrend2House +=1
    s2House = TempOrend2House*150

def DefStartOrend2House():
    global Orend2HouseChange
    Orend2HouseChange = True
    btnStartOrend2House.place_forget()
    btnStopTaimerOrend2House.place(x=37,y=281)
    DeftickOrend2House()

def DefStopOrend2House(v):
    global temp, Orend2HouseChange, money, TempOrend2House
    Orend2HouseChange = False
    temp = 0
    LabelOrend2House.config(text='0:0:0')
    btnStopTaimerOrend2House.place(x=1000,y=1000)
    btnStartOrend2House.place(x=55,y=280)
    root.after_cancel(AfterIdOrend2House)
    if v != 1:
        btnStartOrend2House.place(x=55,y=280)
    else:
        btnStartOrend2House.place_forget()
    z2House = s2House // 9000
    w2House = z2House * 9000
    money = money+w2House
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    TempOrend2House = 0
    messagebox.askokcancel('Підсумки здачі в оренду','За '+str(z2House)+' хвилин здачі ви отримали '+str(w2House)+' гривень')


def DefBuyVideoCard2House():
    global money, VideoCard2House, CanGoToBasement2Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 420000 грн на 30 відео карт?'):
        if money>=420000:
            money = money - 420000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            VideoCard2House = True
            BuyVideoCard2House.place_forget()
            if FrameForMining2House and MainingIn2House and MainingSetUp2House and VideoCard2House:
                CanGoToBasement2Home = True
                btnCanGoTOBasement2House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')
def DefBuyMainingSetUp2House():
    global money, MainingSetUp2House, CanGoToBasement2Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 2000 грн на налаштуванння цієї системи?'):
        if money>=2000:
            money = money - 2000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingSetUp2House = True
            BuyMainingSetUp2House.place_forget()
            if FrameForMining2House and MainingIn2House and MainingSetUp2House and VideoCard2House:
                CanGoToBasement2Home = True
                btnCanGoTOBasement2House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')

def DefBuyMiner2House():
    global money, MainingIn2House, CanGoToBasement2Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 30000 грн на майнер відео карт?'):
        if money>=30000:
            money = money - 30000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingIn2House = True
            BuyMiner2House.place_forget()
            if FrameForMining2House and MainingIn2House and MainingSetUp2House and VideoCard2House:
                CanGoToBasement2Home = True
                btnCanGoTOBasement2House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')
def DefBuyFrameForMining2House():
    global money,FrameForMining2House, CanGoToBasement2Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 16000 грн на каркас для відео карт'):
        if money>=16000:
            money = money - 16000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            FrameForMining2House = True
            BuyFrameForMining2House.place_forget()
            if FrameForMining2House and MainingIn2House and MainingSetUp2House and VideoCard2House:
                CanGoToBasement2Home = True
                btnCanGoTOBasement2House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')

def DefCanGoToBasement2Home():
    LabelMaining2House.place_forget()
    btnCanGoTOBasement2House.place_forget()
    LabelMainingFarm1.place(x=-2,y=20)
    LabelMainingFarm2.place(x=148,y=20)
    LabelMainingFarm3.place(x=-2,y=95)
    LabelMainingFarm4.place(x=148,y=95)
    LabelMainingFarm5.place(x=-2,y=170)
    LabelMainingFarm6.place(x=148,y=170)
    NextListMaining2House.place(x=230, y=260)
    LabelTaimerMaining2House.place(x=10, y=260)
    if Maining2HouseChange:
        btnStopTaimerMaining2House.place(x=2, y=300)
    else:
        btnStartMining2House.place(x=2, y=300)


def DeftickMining2House():
    global TempMaining2House, AfterIdMaining2House, Crypto2House
    AfterIdMaining2House = root.after(1000,DeftickMining2House)
    FTempMining2House = str(int(TempOrend2House/3600))+":"+str(int((TempMaining2House % 3600) / 60) ) + ":" + str(int(TempMaining2House % 60))
    LabelTaimerMaining2House.config(text=str(FTempMining2House))
    TempMaining2House +=1
    Crypto2House = TempMaining2House*1.5

def DefStartMining2House():
    global Maining2HouseChange
    Maining2HouseChange = True
    btnStartMining2House.place(x=1000,y=1000)
    btnStopTaimerMaining2House.place(x=2,y=300)
    DeftickMining2House()

def DefStopMining2House(v):
    global temp, Maining2HouseChange, money, TempMaining2House, HaveShopCoins
    Maining2HouseChange = False
    temp = 0
    LabelTaimerMaining2House.config(text='0:0:0')
    btnStopTaimerMaining2House.place_forget()
    root.after_cancel(AfterIdMaining2House)
    if v != 1:
        btnStartMining2House.place(x=2,y=300)
    else:
        btnStartMining2House.place_forget()
    TempMaining2House = 0
    messagebox.askokcancel('Підсумки майнингу','За час поки ви майнили ви отримали '+str(Crypto2House)+' ShopCoins')
    HaveShopCoins = HaveShopCoins + Crypto2House
    #print(AllCrypto)

def DefNextListMaining2House():
    LabelMainingFarm1.place_forget()
    LabelMainingFarm2.place_forget()
    LabelMainingFarm3.place_forget()
    LabelMainingFarm4.place_forget()
    LabelMainingFarm5.place_forget()
    LabelMainingFarm6.place_forget()
    LabelMainingFarm7.place(x= -2, y =20)
    LabelHalfMainingFarm1.place(x=148, y=20)
    NextListMaining2House.place(x=0,y=260)
    NextListMaining2House.config(text='<<<<', command=DefBackListMaining2House)

def DefBackListMaining2House():
    LabelMainingFarm1.place(x=-2,y=20)
    LabelMainingFarm2.place(x=148,y=20)
    LabelMainingFarm3.place(x=-2,y=95)
    LabelMainingFarm4.place(x=148,y=95)
    LabelMainingFarm5.place(x=-2,y=170)
    LabelMainingFarm6.place(x=148,y=170)
    NextListMaining2House.place(x=230, y=260)
    LabelMainingFarm7.place_forget()
    LabelHalfMainingFarm1.place_forget()
    NextListMaining2House.config(text='>>>>', command=DefNextListMaining2House)


def DefNextListInterier2House():
    LabelHouse2Interier2.place(x=0,y=80)
    NextListInterier2House.place(x=0, y=280)
    NextListInterier2House.config(text='<<<<', command=DefBackInterier2House)

def DefBackInterier2House():
    LabelHouse2Interier1.place(x=0,y=80)
    NextListInterier2House.config(text='>>>>', command=DefNextListInterier2House)
    LabelHouse2Interier2.place_forget()
    NextListInterier2House.place(x=150, y=280)


def DefBuy3House():
    global money, HaveDollar,Have3House
    if (messagebox.askyesno(title="Запит",message="Ви будет купувати квартиру за долари чи за гривні? За доллари - " + str(10000000 // CoursDollar) + ', а за ''гривні 10.000.00.Що оберете(так-за долари,ні - за гривні)')):
        if messagebox.askokcancel('Купівля квартири', 'Щоб купити квартиру вам треба ' + format(10000000 / CoursDollar,'.2f') + ' доларів, якщо ви готові натисніть ОК'):
            if HaveDollar >= 10000000 // CoursDollar:
                HaveDollar = HaveDollar - 10000000 // CoursDollar
                Buy3House.config(text='Керувати будинком', command=DefSettings3House)
                Have3House = True
                Go3House.config(text='Увійти в дім', state=NORMAL)
                Maining3House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend3House.config(text='Здати в оренду', state=NORMAL)
                Sell3House.config(text='Продати дім', state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає доларів для купівлі квартири')
    else:
        if messagebox.askokcancel('Купівля квартири','Щоб купити квартиру вам треба 10.000.000 гривень, якщо ви готові натисніть ОК'):
            if money >= 10000000:
                money = money - 10000000
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Buy3House.config(text='Керувати будинком', command=DefSettings3House)
                Have3House = True
                Go3House.config(text='Увійти в дім', state=NORMAL)
                Maining3House.config(text='Майніти криптовалюту', state=NORMAL)
                Orend3House.config(text='Здати в оренду', state=NORMAL)
                Sell3House.config(text='Продати дім', state=NORMAL)
            else:
                messagebox.askokcancel('Помилка', 'У вас невистачає грошей для купівлі квартири')

def DefSettings3House():
    LabelHouse3.place_forget()
    LabelHouse2.place_forget()
    Buy2House.place_forget()
    Buy3House.place_forget()
    MicroLabel3House.place(x=110, y=30)
    Go3House.place(x=80, y=100)
    Maining3House.place(x=80, y=155)
    Orend3House.place(x=80, y=211)
    Sell3House.place(x=80, y=265)
    NextListRealEstate.place_forget()
    if Orend3HouseChange == False:
        Sell3House.config(state=NORMAL)
        Go3House.config(state=NORMAL)
    else:
        Sell3House.config(state=DISABLED)
        Go3House.config(state=DISABLED)
    if Have3House == False:
        Go3House.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend3House.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell3House.config(text='Це не баг, а фіча!', state=DISABLED)
        Maining3House.config(text='Це не баг, а фіча!', state=DISABLED)
def DefGo3House():
        MicroLabel3House.place_forget()
        Go3House.place_forget()
        LabelHouse3Interier1.place(x=0,y=80)
        BackMainMenu.place_forget()
        BackSettings3House.place(x=2, y=340)
        Maining3House.place_forget()
        Orend3House.place_forget()
        Sell3House.place_forget()
        NextListInterier3House.place(x=150, y=280)


def DefMaining3House():
    Go3House.place_forget()
    MicroLabel3House.place_forget()
    BackMainMenu.place_forget()
    BackSettings3House.place(x=2, y=340)
    Maining3House.place_forget()
    Orend3House.place_forget()
    Sell3House.place_forget()
    LabelMaining3House.place(x=-5,y=22)
    BuyVideoCard3House.place(x=2, y=180)
    BuyFrameForMining3House.place(x=2, y=220)
    BuyMiner3House.place(x=2, y=260)
    BuyMainingSetUp3House.place(x=2, y=300)
    if VideoCard3House:
        BuyVideoCard3House.place_forget()
    if FrameForMining3House:
        BuyFrameForMining3House.place_forget()
    if MainingIn3House:
        BuyMiner3House.place_forget()
    if MainingSetUp3House:
        BuyMainingSetUp3House.place_forget()
    if VideoCard3House and FrameForMining3House and MainingIn3House and MainingSetUp3House:
        btnCanGoTOBasement3House.place(x=2,y=240)


def DefBackSettings3House():
    global b
    #NextListMiningFarm2House.place_forget()
    LabelBeforeOrend3House.place_forget()
    BackSettings3House.place_forget()
    LabelHouse3Interier1.place_forget()
    LabelHouse3Interier2.place_forget()
    MicroLabel3House.place(x=110, y=30)
    BackMainMenu.place(x=2, y=340)
    btnStartOrend3House.place_forget()
    btnStopTaimerOrend3House.place_forget()
    LabelMaining3House.place_forget()
    LabelOrend3House.place_forget()
    BuyVideoCard3House.place_forget()
    BuyFrameForMining3House.place_forget()
    BuyMiner3House.place_forget()
    BuyMainingSetUp3House.place_forget()
    Go3House.place(x=80, y=100)
    Maining3House.place(x=80, y=155)
    Orend3House.place(x=80, y=211)
    Sell3House.place(x=80, y=265)
    LabelMainingFarm1.place_forget()
    LabelMainingFarm2.place_forget()
    LabelMainingFarm3.place_forget()
    LabelMainingFarm4.place_forget()
    LabelMainingFarm5.place_forget()
    btnStartMining3House.place_forget()
    LabelTaimerMaining3House.place_forget()
    btnCanGoTOBasement3House.place_forget()
    btnStopTaimerMaining3House.place_forget()
    LabelMainingFarm6.place_forget()
    LabelMainingFarm7.place_forget()
    LabelHalfMainingFarm1.place_forget()
    NextListMaining3House.place_forget()
    LabelHouse3Interier2.place_forget()
    LabelHouse3Interier1.place_forget()
    NextListInterier3House.place_forget()
    #NextListInterier3House.config(command=DefNextListInterier3House, text='>>>>')
    NextListMaining3House.place_forget()
    BackListMaining3House.place_forget()
    b = 0
    if Orend3HouseChange == False:
        Sell3House.config(state=NORMAL)
        Go3House.config(state=NORMAL)
    else:
        Sell3House.config(state=DISABLED)
        Go3House.config(state=DISABLED)
    if Have3House == False:
        Go3House.config(text='Це не баг, а фіча!', state=DISABLED)
        Orend3House.config(text='Це не баг, а фіча!', state=DISABLED)
        Sell3House.config(text='Це не баг, а фіча!', state=DISABLED)

def DefOrend3House():
    LabelBeforeOrend3House.place(x=-10, y=20)
    MicroLabel3House.place_forget()
    Go3House.place_forget()
    BackMainMenu.place_forget()
    BackSettings3House.place(x=2, y=340)
    Maining3House.place(x=800, y=1750)
    Orend3House.place(x=80, y=2100)
    Sell3House.place(x=80, y=2650)
    LabelOrend3House.place(x=0, y=240)
    if Orend3HouseChange == False:
        btnStartOrend3House.place(x=55,y=280)
    else:
        btnStopTaimerOrend3House.place(x=40,y=288)


def DefSell3House():
    global money, VideoCard3House, CanGoToBasement3Home, MainingSetUp3House, MainingIn3House,FrameForMining3House,Have3House,Taxes3House,AllTaxes
    if messagebox.askokcancel('Продаж квартири', 'За продаж квартири ви отримуєте 70% її ціни. В цьому випадку вам дадуть 7.000.000 гривень. Ви зходні?'):
        if Maining3HouseChange:
            messagebox.askokcancel('Помилка', 'Щоб продати дім зупиніть майнінг ферму')
        else:
            money=money+7000000
            VideoCard3House = False
            CanGoToBasement3Home = False
            MainingIn3House = False
            MainingSetUp3House = False
            FrameForMining3House = False
            MicroLabel3House.place_forget()
            BackMainMenu.place_forget()
            Maining3House.place_forget()
            Orend3House.place_forget()
            Sell3House.place_forget()
            Go3House.place_forget()
            Label1Room.place(x=-5, y=20)
            Label2Room.place(x=150, y=20)
            Label3Room.place(x=-5, y=190)
            LabelHouse1.place(x=150, y=190)
            BackMainMenu.place(x=2, y=340)
            NextListRealEstate.place(x=0, y=330)
            Buy3House.config(text='Купити хай-тег дім \n будинок', command=DefBuy3House)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            Buy1Room.place(x=0, y=122)
            Buy2Room.place(x=150, y=122)
            Buy3Room.place(x=0, y=260)
            Buy1House.place(x=150, y=260)
            Have3House = False
            AllTaxes = AllTaxes - Taxes3House
            btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
            Taxes3House = 0
            btnPayTaxes3House.config(text='Оплатити податки за\nхай-тег будинок\n(' + str(Taxes3House) + ' гривень)')

def DeftickOrend3House():
    global TempOrend3House, AfterIdOrend3House, s3House
    AfterIdOrend3House = root.after(1000,DeftickOrend3House)
    FTempOrend3House = str(int(TempOrend3House/3600))+":"+str(int((TempOrend3House % 3600) / 60) ) + ":" + str(int(TempOrend3House % 60))
    LabelOrend3House.config(text=str(FTempOrend3House))
    TempOrend3House +=1
    s3House = TempOrend3House*200

def DefStartOrend3House():
    global Orend3HouseChange
    Orend3HouseChange = True
    btnStartOrend3House.place_forget()
    btnStopTaimerOrend3House.place(x=37,y=281)
    DeftickOrend3House()

def DefStopOrend3House(v):
    global temp, Orend3HouseChange, money, TempOrend3House
    Orend3HouseChange = False
    temp = 0
    LabelOrend3House.config(text='0:0:0')
    btnStopTaimerOrend3House.place(x=1000,y=1000)
    btnStartOrend3House.place(x=55,y=280)
    root.after_cancel(AfterIdOrend3House)
    if v!= 1:
        btnStartOrend3House.place(x=55,y=280)
    else:
        btnStartOrend3House.place_forget()
    z3House = s3House // 12000
    w3House = z3House * 12000
    money = money+w3House
    TempOrend3House = 0
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    
    messagebox.askokcancel('Підсумки здачі в оренду.','За '+str(z3House)+' хвилин здачі ви отримали '+str(w3House)+' гривень ( Промокод: _Stop_OrEnD_3_HOUSE_)')


def DefBuyVideoCard3House():
    global money, VideoCard3House, CanGoToBasement3Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 700000 грн на 50 відео карт?'):
        if money>=700000:
            money = money - 700000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            VideoCard3House = True
            BuyVideoCard3House.place_forget()
            if FrameForMining3House and MainingIn3House and MainingSetUp3House and VideoCard3House:
                CanGoToBasement3Home = True
                btnCanGoTOBasement3House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')

def DefBuyMainingSetUp3House():
    global money, MainingSetUp3House, CanGoToBasement3Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 2000 грн на налаштуванння цієї системи?'):
        if money>=2000:
            money = money - 2000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingSetUp3House = True
            BuyMainingSetUp3House.place_forget()
            if FrameForMining3House and MainingIn3House and MainingSetUp3House and VideoCard3House:
                CanGoToBasement3Home = True
                btnCanGoTOBasement3House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')

def DefBuyMiner3House():
    global money, MainingIn3House, CanGoToBasement3Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 30000 грн на майнер відео карт?'):
        if money>=30000:
            money = money - 30000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            MainingIn3House = True
            BuyMiner3House.place_forget()
            if FrameForMining3House and MainingIn3House and MainingSetUp3House and VideoCard3House:
                CanGoToBasement3Home = True
                btnCanGoTOBasement3House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')


def DefBuyFrameForMining3House():
    global money,FrameForMining3House, CanGoToBasement3Home
    if messagebox.askokcancel('Підтвердження', 'Ви точно хочете витратити 26000 грн на каркас для відео карт'):
        if money>=26000:
            money = money - 26000
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            FrameForMining3House = True
            BuyFrameForMining3House.place_forget()
            if FrameForMining3House and MainingIn3House and MainingSetUp3House and VideoCard3House:
                CanGoToBasement3Home = True
                btnCanGoTOBasement3House.place(x=2,y=240)
                messagebox.askokcancel('Ви готові майнити', 'Ви купили все, що вам потрібно тому ви можете почати майнити')
        else:
            messagebox.askokcancel('Помилка', 'У вас невистачає грошей, щоб купити це')


def DefCanGoToBasement3Home():
    LabelMaining3House.place_forget()
    btnCanGoTOBasement3House.place_forget()
    LabelMainingFarm1.place(x=-2,y=20)
    LabelMainingFarm2.place(x=148,y=20)
    LabelMainingFarm3.place(x=-2,y=95)
    LabelMainingFarm4.place(x=148,y=95)
    LabelMainingFarm5.place(x=-2,y=170)
    LabelMainingFarm6.place(x=148,y=170)
    NextListMaining3House.place(x=230, y=260)
    LabelTaimerMaining3House.place(x=10, y=260)
    if Maining3HouseChange:
        btnStopTaimerMaining3House.place(x=2, y=300)
    else:
        btnStartMining3House.place(x=2, y=300)


def DeftickMining3House():
    global TempMaining3House, AfterIdMaining3House, Crypto3House
    AfterIdMaining3House = root.after(1000,DeftickMining3House)
    FTempMining3House = str(int(TempMaining3House/3600))+":"+str(int((TempMaining3House % 3600) / 60) ) + ":" + str(int(TempMaining3House % 60))
    LabelTaimerMaining3House.config(text=str(FTempMining3House))
    TempMaining3House +=1
    Crypto3House = TempMaining3House*2.5

def DefStartMining3House():
    global Maining3HouseChange
    Maining3HouseChange = True
    btnStartMining3House.place(x=1000,y=1000)
    btnStopTaimerMaining3House.place(x=2,y=300)
    DeftickMining3House()

def DefStopMining3House(v):
    global temp, Maining3HouseChange, money, TempMaining3House, HaveShopCoins
    Maining3HouseChange = False
    temp = 0
    LabelTaimerMaining3House.config(text='0:0:0')
    btnStopTaimerMaining3House.place_forget()
    btnStartMining3House.place(x=2,y=300)
    root.after_cancel(AfterIdMaining3House)
    if v != 1:
        btnStartMining3House.place(x=2,y=300)
    else:
        btnStartMining3House.place_forget()
    TempMaining3House = 0
    messagebox.askokcancel('Підсумки майнингу','За час поки ви майнили ви отримали '+str(Crypto3House)+' ShopCoins')
    HaveShopCoins = HaveShopCoins + Crypto3House
    #print(AllCrypto)

def DefNextListMaining3House():
    global b
    b = b + 1
    if b == 2:
        LabelMainingFarm1.place_forget()
        LabelMainingFarm2.place_forget()
        LabelMainingFarm3.place_forget()
        LabelMainingFarm4.place_forget()
        LabelMainingFarm5.place_forget()
        LabelMainingFarm6.place_forget()
        NextListMaining3House.place_forget()
        LabelHalfMainingFarm1.place(x=-2,y=20)
    if b == 1:
        BackListMaining3House.place(x=0,y=260)

def DefBackListMaining3House():
    global b
    b = b - 1
    if b==0:
        LabelMainingFarm1.place(x=-2,y=20)
        LabelMainingFarm2.place(x=148,y=20)
        LabelMainingFarm3.place(x=-2,y=95)
        LabelMainingFarm4.place(x=148,y=95)
        LabelMainingFarm5.place(x=-2,y=170)
        LabelMainingFarm6.place(x=148,y=170)
        NextListMaining3House.place(x=230, y=260)
        LabelHalfMainingFarm1.place_forget()
        NextListMaining3House.place(x=230,y=260)
        BackListMaining3House.place_forget()
    if b == 1:
        LabelMainingFarm1.place(x=-2, y=20)
        LabelMainingFarm2.place(x=148, y=20)
        LabelMainingFarm3.place(x=-2, y=95)
        LabelMainingFarm4.place(x=148, y=95)
        LabelMainingFarm5.place(x=-2, y=170)
        LabelMainingFarm6.place(x=148, y=170)
        NextListMaining3House.place(x=230, y=260)
        LabelHalfMainingFarm1.place_forget()
        NextListMaining3House.place(x=230, y=260)
        BackListMaining3House.place(x=0,y=260)

def DefNextListInterier3House():
    LabelHouse3Interier2.place(x=0,y=80)
    NextListInterier3House.place(x=0, y=280)
    NextListInterier3House.config(text='<<<<', command=DefBackInterier3House)

def DefBackInterier3House():
    LabelHouse3Interier1.place(x=0,y=80)
    NextListInterier3House.config(text='>>>>', command=DefNextListInterier3House)
    LabelHouse3Interier2.place_forget()
    NextListInterier3House.place(x=150, y=280)

def DefGoCharity():
    ExchangeCurrency.place(x=0, y=2200)
    Charity.place(x=160, y=2200)
    WhatUpdate.place(x=0, y=1000)
    PromoCode.place(x=160, y=1000)
    btnBank.place(x=0, y=1800)
    btnSaveSaves.place(x=160, y=1800)
    BackListMainMenu.place(x=0, y=2600)
    btnNextListMeinMenu3.place(x=160, y=2600)
    Reset.place(x=1000, y=1000)
    BackTo2ListMainMenu.place(x=2, y=340)
    LabelCharity.place(x=23,y=50)
    NextRateCharity.place(x=220,y=150)
    RateCharity.place(x=120,y=154)

def DefNextListMeinMenu():
    btnGoHome.place(x=0, y=2200)
    btnGoShop.place(x=160, y=2200)
    bthGoMarket.place(x=0, y=1000)
    btnGoCasino.place(x=160, y=1000)
    ListBuy.place(x=0, y=1800)
    LabelListCook.place(x=160, y=1800)
    Real_estate.place(x=0, y=2600)
    NextListMeinMenu.place(x=160, y=2600)
    ListCook.place(x=1000, y=1000)
    ExchangeCurrency.place(x=0, y=22)
    Charity.place(x=160, y=22)
    WhatUpdate.place(x=0, y=100)
    PromoCode.place(x=160, y=100)
    btnBank.place(x=0, y=180)
    btnSaveSaves.place(x=160, y=180)
    BackListMainMenu.place(x=0, y=260)
    btnNextListMeinMenu3.place(x=160, y=260)
    btnClicker.place_forget()
    BackListMainMenu.config(command=DefBackListMainMenu)
    btnWork.place_forget()
    btnBusiness.place_forget()
    btnCourses.place_forget()
    btnGoSeaBattle.place_forget()
    btnBackyard.place_forget()
    btnGardeningShop.place_forget()

def DefBackListMainMenu():
    ExchangeCurrency.place(x=0, y=2200)
    Charity.place(x=160, y=2200)
    WhatUpdate.place(x=0, y=1000)
    PromoCode.place(x=160, y=1000)
    btnBank.place(x=0, y=1800)
    btnSaveSaves.place(x=160, y=1800)
    BackListMainMenu.place(x=0, y=2600)
    btnNextListMeinMenu3.place(x=160, y=2600)
    btnGoHome.place(x=0, y=22)
    btnGoShop.place(x=160, y=22)
    bthGoMarket.place(x=0, y=100)
    btnGoCasino.place(x=160, y=100)
    ListBuy.place(x=0, y=180)
    ListCook.place(x=160, y=180)
    Real_estate.place(x=0, y=260)
    NextListMeinMenu.place(x=160, y=260)


def GoExchangeCenter():
    ExchangeCurrency.place(x=0, y=2200)
    Charity.place(x=160, y=2200)
    WhatUpdate.place(x=0, y=1000)
    PromoCode.place(x=160, y=1000)
    btnBank.place(x=0, y=1800)
    btnSaveSaves.place(x=160, y=1800)
    BackListMainMenu.place(x=0, y=2600)
    btnNextListMeinMenu3.place(x=160, y=2600)
    Reset.place(x=1000,y=1000)
    LabelShopCoin.place(x=0,y=22)
    LabelDollar.place(x=150, y=22)
    BackTo2ListMainMenu.place(x=2, y=340)
    CourseCurrency.place(x=0,y=118)
    CourseCurrencyDollar.place(x=0,y=180)
    SellDollar.place(x=190, y=164)
    BuyDollar.place(x=190,y=192)
    btnSellStarCoin.place(x=190, y=224)
    btnBuyStarCoin.place(x=190,y=251)
    Lines1.place(x=0, y=90)
    Lines2.place(x=0,y=150)
    Lines3.place(x=0, y=210)
    Lines4.place(x=0,y=270)
    EntryHaveShopCoin.config(state='normal')
    EntryHaveDolar.config(state='normal')
    EntryHaveStarCoin.config(state='normal')
    EntryHaveShopCoin.insert(0,str(HaveShopCoins))
    EntryHaveDolar.insert(0,str(HaveDollar))
    EntryHaveStarCoin.insert(0,format(HaveStarCoin,'.2f'))
    EntryHaveShopCoin.config(state='disabled')
    EntryHaveDolar.config(state='disabled')
    EntryHaveStarCoin.config(state='disabled')
    SellShopCoins.place(x=190,y=105)
    BuyShopCoins.place(x=190,y=132)
    EntryHaveShopCoin.place(x=74,y=53)
    EntryHaveDolar.place(x=225,y=53)
    EntryHaveStarCoin.place(x=60,y=300)
    LabelCoursStarCoin.place(x=0,y=242)
    CourseCurrency.config(text='1 ShopCoin - ' + str(CoursShopCoins) + ' грн')
    CourseCurrencyDollar.config(text='1 Доллар - ' + format(CoursDollar, '.2f') + ' грн')
    LabelCoursStarCoin.config(text='StarCoin - ' + format(CoursStarCoin, '.2f')+' грн', bg='white')
    LabelImgStarCoin.place(x=-5,y=280)


def DefBackTo2ListMainMenu():
    global ReadyCharity
    CourseCurrency.place(x=0, y=1050)
    Lines1.place(x=0, y=900)
    Lines2.place(x=0, y=1200)
    Lines3.place_forget()
    Lines4.place_forget()
    LabelShopCoin.place(x=0, y=2000)
    BackTo2ListMainMenu.place(x=1000,y=1000)
    EntryHaveShopCoin.place(x=70, y=4500)
    ExchangeCurrency.place(x=0, y=22)
    Charity.place(x=160, y=22)
    WhatUpdate.place(x=0, y=100)
    PromoCode.place(x=160, y=100)
    btnBank.place(x=0, y=180)
    btnSaveSaves.place(x=160, y=180)
    BackListMainMenu.place(x=0, y=260)
    btnNextListMeinMenu3.place(x=160, y=260)
    Reset.place(x=5, y=337)
    HowWantSellShopCoins.place_forget()
    LabelHowWantSellShopCoins.place_forget()
    EnterForSellShopCoins.place_forget()
    BuyShopCoins.place_forget()
    SellShopCoins.place_forget()
    HowWantBuyShopCoins.place_forget()
    LabelHowWantBuyShopCoins.place_forget()
    EnterForBuyShopCoins.place_forget()
    LabelCharity.place_forget()
    RateCharity.place_forget()
    NextRateCharity.place_forget()
    BackRateCharity.place_forget()
    ReadyCharity = 0
    RateCharity.config(text='0')
    ButtonForGiveCharity.place_forget()
    LabelDollar.place_forget()
    HowWantSellDollar.place_forget()
    LabelHowWantSellDollar.place_forget()
    EnterForSellDollar.place_forget()
    BuyDollar.place_forget()
    SellDollar.place_forget()
    HowWantBuyDollar.place_forget()
    LabelHowWantBuyDollar.place_forget()
    EnterForBuyDollar.place_forget()
    CourseCurrencyDollar.place_forget()
    EntryHaveDolar.place_forget()
    LabelPromoCode.place_forget()
    EntryPromoCode.place_forget()
    EnterPromoCode.place_forget()
    btnBankCard.place_forget()
    LabelInBank.place_forget()
    btnDeposit.place_forget()
    btnTaxes.place_forget()
    btnAddSave.place_forget()
    LabelSave1.place_forget()
    btnSaveIn1File.place_forget()
    btnUploadFrom1File.place_forget()
    btnDeleat1File.place_forget()
    LabelSave2.place_forget()
    btnSaveIn2File.place_forget()
    btnUploadFrom2File.place_forget()
    btnDeleat2File.place_forget()
    LabelSave3.place_forget()
    btnSaveIn3File.place_forget()
    btnUploadFrom3File.place_forget()
    btnDeleat3File.place_forget()
    LabelSave4.place_forget()
    btnSaveIn4File.place_forget()
    btnUploadFrom4File.place_forget()
    btnDeleat4File.place_forget()
    EntryHaveDolar.config(state='normal')
    EntryHaveDolar.delete(0,END)
    EntryHaveShopCoin.config(state='normal')
    EntryHaveShopCoin.delete(0,END)
    EntryHaveStarCoin.config(state='normal')
    EntryHaveStarCoin.delete(0,END)
    btnSellStarCoin.place_forget()
    btnBuyStarCoin.place_forget()
    LabelCoursStarCoin.place_forget()
    EntryHaveStarCoin.place_forget()
    LabelImgStarCoin.place_forget()
    EnterForBuyStarCoin.place_forget()
    EnterForSellStarCoin.place_forget()
    HowWantBuyStarCoin.place_forget()
    HowWantSellStarCoin.place_forget()
    LabelHowWantBuyStarCoin.place_forget()
    LabelHowWantSellStarCoin.place_forget()
    btnWork.place_forget()
    btnBusiness.place_forget()
    btnCourses.place_forget()
    btnGoSeaBattle.place_forget()
    btnBackyard.place_forget()
    btnGardeningShop.place_forget()

def DefSellShopCoins():
    SellShopCoins.place_forget()
    BuyShopCoins.place_forget()
    HowWantSellShopCoins.place(x=155,y=140)
    LabelHowWantSellShopCoins.place(x=140,y=105)
    EnterForSellShopCoins.place(x=255,y=135)


def DefBuyShopCoins():
    SellShopCoins.place_forget()
    BuyShopCoins.place_forget()
    HowWantBuyShopCoins.place(x=155, y=140)
    LabelHowWantBuyShopCoins.place(x=140, y=105)
    EnterForBuyShopCoins.place(x=255, y=135)


#КРИПТОВАЛЮТА



def DefEnterForBuyShopCoins():
    global money, WantBuyShopCoins, SumBuyShopCoins, HaveShopCoins, MoneyOnBankCard
    if PayInExchangeCenter =='Money':
        strWantBuyShopCoins = HowWantBuyShopCoins.get()
        WantBuyShopCoins = int(strWantBuyShopCoins)
        SumBuyShopCoins = WantBuyShopCoins*CoursShopCoins
        if SumBuyShopCoins <= money and WantBuyShopCoins>0:
            money = money - SumBuyShopCoins
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            SellShopCoins.place(x=190, y=105)
            BuyShopCoins.place(x=190, y=132)
            HaveShopCoins = HaveShopCoins + WantBuyShopCoins
            EntryHaveShopCoin.config(state='normal')
            EntryHaveShopCoin.delete(0, END)
            EntryHaveShopCoin.insert(0, str(HaveShopCoins))
            EntryHaveShopCoin.config(state='disabled')
            EnterForBuyShopCoins.place_forget()
            LabelHowWantBuyShopCoins.place_forget()
            HowWantBuyShopCoins.place_forget()
        else:
            messagebox.askokcancel('Сталася помилка','Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі ShopCoins')
    if PayInExchangeCenter == 'BankCard' and ProofPinCode == PinCode:
        strWantBuyShopCoins = HowWantBuyShopCoins.get()
        WantBuyShopCoins = int(strWantBuyShopCoins)
        SumBuyShopCoins = WantBuyShopCoins * CoursShopCoins
        if SumBuyShopCoins <= MoneyOnBankCard and WantBuyShopCoins > 0:
            MoneyOnBankCard = MoneyOnBankCard - SumBuyShopCoins
            SellShopCoins.place(x=190, y=105)
            BuyShopCoins.place(x=190, y=132)
            HaveShopCoins = HaveShopCoins + WantBuyShopCoins
            EntryHaveShopCoin.config(state='normal')
            EntryHaveShopCoin.delete(0, END)
            EntryHaveShopCoin.insert(0, str(HaveShopCoins))
            EntryHaveShopCoin.config(state='disabled')
            EnterForBuyShopCoins.place_forget()
            LabelHowWantBuyShopCoins.place_forget()
            HowWantBuyShopCoins.place_forget()
        else:
            messagebox.askokcancel('Сталася помилка',
                                   'Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі ShopCoins')

def DefEnterForSellShopCoins():
    global ReadySellShopCoins, money, HaveShopCoins, MoneyOnBankCard
    if PayInExchangeCenter =='Money':
        StrReadySellShopCoins = HowWantSellShopCoins.get()
        ReadySellShopCoins = int(StrReadySellShopCoins)
        if ReadySellShopCoins>0 and ReadySellShopCoins <= HaveShopCoins:
            money = money + (ReadySellShopCoins*CoursShopCoins)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.askokcancel('Підсумок','За ' + StrReadySellShopCoins + ' ShopCoins ви отримали '+ str(ReadySellShopCoins*CoursShopCoins) + ' гривень')
            HaveShopCoins = HaveShopCoins - ReadySellShopCoins
            EntryHaveShopCoin.config(state='normal')
            EntryHaveShopCoin.delete(0, END)
            EntryHaveShopCoin.insert(0, str(HaveShopCoins))
            EntryHaveShopCoin.config(state='disabled')
            HowWantSellShopCoins.place_forget()
            LabelHowWantSellShopCoins.place_forget()
            EnterForSellShopCoins.place_forget()
            SellShopCoins.place(x=190, y=105)
            BuyShopCoins.place(x=190, y=132)
        else:
            messagebox.askokcancel('Помилка', 'Сталася помилка, або у вас немає стільки монет або ви ввели некоректну кількість монет')
            HowWantSellShopCoins.place_forget()
            LabelHowWantSellShopCoins.place_forget()
            EnterForSellShopCoins.place_forget()
            SellShopCoins.place(x=190, y=105)
            BuyShopCoins.place(x=190, y=132)
    if PayInExchangeCenter =='BankCard' and ProofPinCode==PinCode:
        StrReadySellShopCoins = HowWantSellShopCoins.get()
        ReadySellShopCoins = int(StrReadySellShopCoins)
        if ReadySellShopCoins > 0 and ReadySellShopCoins <= HaveShopCoins:
            MoneyOnBankCard = MoneyOnBankCard + (ReadySellShopCoins * CoursShopCoins)
            messagebox.askokcancel('Підсумок', 'За ' + StrReadySellShopCoins + ' ShopCoins ви отримали ' + str(ReadySellShopCoins * CoursShopCoins) + ' гривень')
            HaveShopCoins = HaveShopCoins - ReadySellShopCoins
            EntryHaveShopCoin.config(state='normal')
            EntryHaveShopCoin.delete(0, END)
            EntryHaveShopCoin.insert(0, str(HaveShopCoins))
            EntryHaveShopCoin.config(state='disabled')
            HowWantSellShopCoins.place_forget()
            LabelHowWantSellShopCoins.place_forget()
            EnterForSellShopCoins.place_forget()
            SellShopCoins.place(x=190, y=105)
            BuyShopCoins.place(x=190, y=132)


def DefNextRateCharity():
    global ReadyCharity
    ReadyCharity = ReadyCharity + 100
    RateCharity.config(text=ReadyCharity)
    if ReadyCharity >= 100:
        BackRateCharity.place(x=0,y=150)
        ButtonForGiveCharity.place(x=40,y=200)

def DefBackRateCharity():
    global ReadyCharity
    ReadyCharity = ReadyCharity - 100
    RateCharity.config(text=ReadyCharity)
    if ReadyCharity == 0:
        BackRateCharity.place_forget()
        ButtonForGiveCharity.place_forget()

def DefCharityMoney():
    global money, MoneyOnBankCard
    if ReadyCharity <= money:
        if PayInCharity=='Money':
            FirstLeters = random.choice(Liters)
            money = money - ReadyCharity
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            for i in range(100):
                x = random.choice(Liters)
                FirstLeters = str(FirstLeters) + str(x)
                x = None
            messagebox.askokcancel('Таємне послання Промокод: Secret_Charity_SUS', FirstLeters)
            return
    else:
        messagebox.askokcancel('Сталася помилка', 'У вас нема стільки грошей :(')
    if ReadyCharity<=MoneyOnBankCard and ProofPinCode==PinCode and PayInCharity=='BankCard':
        FirstLeters = random.choice(Liters)
        MoneyOnBankCard = MoneyOnBankCard - ReadyCharity
        for i in range(100):
            x = random.choice(Liters)
            FirstLeters = str(FirstLeters) + str(x)
            x = None
        messagebox.askokcancel('Таємне послання Промокод: Secret_Charity_SUS', FirstLeters)
    else:
        messagebox.askokcancel('Сталася помилка', 'У вас нема стільки грошей або ви не підтвердили Pin-code:(')

def DefWhatUpdate():
    os.startfile('Txt_Shop\\Update.txt')
    #WhatUpdateLabel.place(x=0,y=20)

def BtnBuyMoreProduct_And_HideAllBtnShop():
    Sausage.place_forget()
    Cheese.place_forget()
    Than.place_forget()
    Flour.place_forget()
    Chocolate.place_forget()
    Cola.place_forget()
    Cucumber.place_forget()
    Bread.place_forget()
    BuyTomato.place_forget()
    BuySalat.place_forget()
    BuySalt.place_forget()
    BuyBowl.place_forget()
    BuyOil.place_forget()
    NextListShop.place_forget()
    CookButerbrod.place_forget()
    CookSalat.place_forget()
    CutSausage.place_forget()
    CutCheese.place_forget()
    CutThan.place_forget()
    CutFlour.place_forget()
    CutChocolate.place_forget()
    CutCola.place_forget()
    CutBread.place_forget()
    CutOil.place_forget()
    CutBowl.place_forget()
    CutSalt.place_forget()
    CutSalat.place_forget()
    CutTomato.place_forget()
    CutCucumber.place_forget()
    btnCut.place_forget()
    SellButerbrod.place_forget()
    SellSalat.place_forget()
    NextListCut.place_forget()
    btnInformationAboutWhatInTheBedsideTable.place_forget()
    btnPutInTheBedsideTable.place_forget()
    btnTakeFromBedsideTable.place_forget()
    LabelInfoBedsideTable.place_forget()
    BuyMoreProduct0.place(x=55, y=270)
    BuyMoreProduct1.place(x=55, y=110)
    BuyMoreProduct2.place(x=120, y=110)
    BuyMoreProduct3.place(x=185, y=110)
    BuyMoreProduct4.place(x=55, y=150)
    BuyMoreProduct5.place(x=120, y=150)
    BuyMoreProduct6.place(x=185, y=150)
    BuyMoreProduct7.place(x=55, y=190)
    BuyMoreProduct8.place(x=120, y=190)
    BuyMoreProduct9.place(x=185, y=190)
    BuyMoreProductEntr1.place(x=55, y=230)
    BuyMoreProductClear1.place(x=150, y=230)
    BuyMoreProductEntry.place(x=62, y=90)
    BuyMoreProductEntry.config(state='normal')
    BuyMoreProductEntry.delete(0, END)
    BuyMoreProductEntry.config(state='readonly')
    btnBuySpaghetti.place_forget()
    btnBuyStuff.place_forget()
    btnFry.place_forget()
    btnBoil.place_forget()
    btnCookSpaghettiWithCutlet.place_forget()
    btnSellSpaghettiWithCutlet.place_forget()
    btnCookIngredient.place_forget()
def DefHideMoreProduct():
    BuyMoreProduct0.place_forget()
    BuyMoreProduct1.place_forget()
    BuyMoreProduct2.place_forget()
    BuyMoreProduct3.place_forget()
    BuyMoreProduct4.place_forget()
    BuyMoreProduct5.place_forget()
    BuyMoreProduct6.place_forget()
    BuyMoreProduct7.place_forget()
    BuyMoreProduct8.place_forget()
    BuyMoreProduct9.place_forget()
    BuyMoreProductEntr1.place_forget()
    BuyMoreProductClear1.place_forget()
    BuyMoreProductEntry.place_forget()
    EntryPinCodeBankCard.place_forget()

def DefSellDollar():
    SellDollar.place_forget()
    BuyDollar.place_forget()
    HowWantSellDollar.place(x=155, y=200)
    LabelHowWantSellDollar.place(x=153, y=168)
    EnterForSellDollar.place(x=255, y=195)

def DefEnterForSellDollar():
    global ReadySellDollar, money, HaveDollar, MoneyOnBankCard, PayInExchangeCenter
    if PayInExchangeCenter =='Money':
        StrReadySellDollar = HowWantSellDollar.get()
        ReadySellDollar = int(StrReadySellDollar)
        if ReadySellDollar > 0 and ReadySellDollar <= HaveDollar:
            money = money + (ReadySellDollar * CoursDollar)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.askokcancel('Підсумок', 'За ' + StrReadySellDollar + ' доларів ви отримали ' + str(
                ReadySellDollar * CoursDollar) + ' гривень')
            HaveDollar = HaveDollar - ReadySellDollar
            EntryHaveDolar.config(state='normal')
            EntryHaveDolar.delete(0, END)
            EntryHaveDolar.insert(0, str(HaveDollar))
            EntryHaveDolar.config(state='disabled')
            HowWantSellDollar.place_forget()
            LabelHowWantSellDollar.place_forget()
            EnterForSellDollar.place_forget()
            SellDollar.place(x=190, y=164)
            BuyDollar.place(x=190, y=192)
            HowWantSellDollar.delete(0, END)
        else:
            messagebox.askokcancel('Помилка',
                               'Сталася помилка, або у вас немає стільки доларів або ви ввели некоректну кількість доларів')
    if PayInExchangeCenter =='BankCard' and ProofPinCode == PinCode:
        StrReadySellDollar = HowWantSellDollar.get()
        ReadySellDollar = int(StrReadySellDollar)
        if ReadySellDollar > 0 and ReadySellDollar <= HaveDollar:
            MoneyOnBankCard = MoneyOnBankCard + (ReadySellDollar * CoursDollar)
            messagebox.askokcancel('Підсумок', 'За ' + StrReadySellDollar + ' доларів ви отримали ' + str(
                ReadySellDollar * CoursDollar) + ' гривень')
            HaveDollar = HaveDollar - ReadySellDollar
            EntryHaveDolar.config(state='normal')
            EntryHaveDolar.delete(0, END)
            EntryHaveDolar.insert(0, str(HaveDollar))
            EntryHaveDolar.config(state='disabled')
            HowWantSellDollar.place_forget()
            LabelHowWantSellDollar.place_forget()
            EnterForSellDollar.place_forget()
            SellDollar.place(x=190, y=164)
            BuyDollar.place(x=190, y=192)
            HowWantSellDollar.delete(0, END)
        else:
            messagebox.askokcancel('Помилка',
                                   'Сталася помилка, або у вас немає стільки доларів або ви ввели некоректну кількість доларів')

def DefEnterForBuyDollar():
    global money, WantBuyDollar, SumBuyDollar, HaveDollar, MoneyOnBankCard
    if PayInExchangeCenter =='Money':
        strWantBuyDollar = HowWantBuyDollar.get()
        WantBuyDollar = int(strWantBuyDollar)
        SumBuyDollar = WantBuyDollar*CoursDollar
        if SumBuyDollar <= money and WantBuyDollar>0:
            money = money - SumBuyDollar
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            SellDollar.place(x=190, y=164)
            BuyDollar.place(x=190, y=192)
            HaveDollar = HaveDollar+ WantBuyDollar
            EntryHaveDolar.config(state='normal')
            EntryHaveDolar.delete(0, END)
            EntryHaveDolar.insert(0, str(HaveDollar))
            EntryHaveDolar.config(state='disabled')
            EnterForBuyDollar.place_forget()
            LabelHowWantBuyDollar.place_forget()
            HowWantBuyDollar.place_forget()
            HowWantBuyDollar.delete(0, END)
        else:
            messagebox.askokcancel('Сталася помилка','Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі доларів')
    if PayInExchangeCenter =='BankCard' and ProofPinCode==PinCode:
        strWantBuyDollar = HowWantBuyDollar.get()
        WantBuyDollar = int(strWantBuyDollar)
        SumBuyDollar = WantBuyDollar*CoursDollar
        if SumBuyDollar <= MoneyOnBankCard and WantBuyDollar>0:
            MoneyOnBankCard = MoneyOnBankCard - SumBuyDollar
            SellDollar.place(x=190, y=164)
            BuyDollar.place(x=190, y=192)
            HaveDollar = HaveDollar+ WantBuyDollar
            EntryHaveDolar.config(state='normal')
            EntryHaveDolar.delete(0,END)
            EntryHaveDolar.insert(0, str(HaveDollar))
            EntryHaveDolar.config(state='disabled')
            EnterForBuyDollar.place_forget()
            LabelHowWantBuyDollar.place_forget()
            HowWantBuyDollar.place_forget()
            HowWantBuyDollar.delete(0,END)
        else:
            messagebox.askokcancel('Сталася помилка','Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі доларів')





def DefBuyDollar():
    SellDollar.place_forget()
    BuyDollar.place_forget()
    HowWantBuyDollar.place(x=155, y=200)
    LabelHowWantBuyDollar.place(x=153, y=168)
    EnterForBuyDollar.place(x=255, y=195)


def DefPromoCode():
    ExchangeCurrency.place_forget()
    WhatUpdate.place_forget()
    PromoCode.place_forget()
    Charity.place_forget()
    btnBank.place_forget()
    btnSaveSaves.place_forget()
    btnNextListMeinMenu3.place_forget()
    BackListMainMenu.place_forget()
    Reset.place_forget()
    BackTo2ListMainMenu.place(x=2, y=340)
    EntryPromoCode.place(x=60,y=100)
    LabelPromoCode.place(x=-5,y=35)
    EnterPromoCode.place(x=59, y=120)



def DefEnterPromoCode():
    global  money, HaveShopCoins,HaveDollar, PromoCodeAmogus,PromoCodeUpdate_dowN_BlockNot,PromoCodeSecret_Charity_SUS, PromoCodeStooopOrend_One_Room
    global PromoCodeAmogus2024,PromoCodeFrog,PromoCodeAbyba,PromoCodeShop, PromoCodeMining_1House_lox_, PromoCodeStop_Orend_3_House
    global HaveMoneyInBedsideTable, HaveDollarInBedsideTable, MemeBedsideTable, PromoDontHaveMoneyShop
    if EntryPromoCode.get() == 'amogus' and PromoCodeAmogus == False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:500 грн')
        money = money+500
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        PromoCodeAmogus = True
        return
    if EntryPromoCode.get() == 'Update_dowN_BlockNot' and PromoCodeUpdate_dowN_BlockNot==False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:900 грн')
        money = money+900
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        PromoCodeUpdate_dowN_BlockNot = True
        return
    if EntryPromoCode.get() == 'Secret_Charity_SUS' and PromoCodeSecret_Charity_SUS==False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:7 Shop Coins')
        HaveShopCoins = HaveShopCoins+7
        PromoCodeSecret_Charity_SUS = True
        return
    if EntryPromoCode.get() == 'amogus2024' and PromoCodeAmogus2024==False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:666 грн')
        money = money+666
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        PromoCodeAmogus2024 = True
        return
    if EntryPromoCode.get() == 'frog' and PromoCodeFrog==False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:30 доларів')
        HaveDollar = HaveDollar+30
        PromoCodeFrog = True
        return
    if EntryPromoCode.get() == 'abyba' and PromoCodeAbyba == False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:10 Shop Coins')
        HaveShopCoins =HaveShopCoins+10
        PromoCodeAbyba = True
        return
    if EntryPromoCode.get() == 'Shop' and PromoCodeShop == False:
        messagebox.askokcancel('Промоко активовано','Промокод активовано. Винагорода:35 доларів')
        HaveDollar = HaveDollar+35
        PromoCodeShop = True
        return
    if EntryPromoCode.get() == '_Stop_OrEnD_3_HOUSE_' and PromoCodeStop_Orend_3_House == False:
        messagebox.askokcancel('Промоко активовано', 'Промокод активовано. Винагорода:1234 гривень')
        money = money + 1234
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        PromoCodeStop_Orend_3_House = True
        return
    if EntryPromoCode.get() == 'Mining_1HOUSE_lox_' and PromoCodeMining_1House_lox_ == False:
        messagebox.askokcancel('Промоко активовано', 'Промокод активовано. Винагорода:12 ShopCoins')
        HaveShopCoins=HaveShopCoins+12
        PromoCodeMining_1House_lox_ = True
        return
    if EntryPromoCode.get() == 'StooopOrend_One-Room' and PromoCodeStooopOrend_One_Room == False:
        messagebox.askokcancel('Промоко активовано', 'Промокод активовано. Винагорода:40 доларів')
        HaveDollar = HaveDollar + 40
        PromoCodeStooopOrend_One_Room = True
        return
    if EntryPromoCode.get() == 'meme_Infility_Money_AnD_Dollar_In_BedsideTable_2014_Yanycovich' and MemeBedsideTable == False :
        messagebox.askokcancel('Промоко активовано', 'Як ти знайшов цей промокод? Щоб зрозуміти,що він дає треба знати мем)')
        HaveMoneyInBedsideTable = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        HaveDollarInBedsideTable = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        MemeBedsideTable = False
        return
    if EntryPromoCode.get() == 'DontHaveMoneyShop' and PromoDontHaveMoneyShop == False :
        messagebox.askokcancel('Промоко активовано', 'Бідося( тримай 300 гривень - купи собі поїсти')
        money=money+300
        MemeBedsideTable = False
        return
    else:
        messagebox.askokcancel('Помилка','Такого промокоду не існіє або ви його вже активували')


def DefBedsideTable():
    if HaveBedSideTable:
        btnGoHome.place(x=80, y=330)
        DoInHome.place_forget()
        GoCook.place_forget()
        btnBedsideTable.place_forget()
        GoSleep.place_forget()
        BackMainMenu.place_forget()
        btnPutInTheBedsideTable.place(x=75, y=100)
        btnTakeFromBedsideTable.place(x=75, y=160)
        btnInformationAboutWhatInTheBedsideTable.place(x=75, y=220)
        LabelInfoBedsideTable.place(x=0,y=50)
        LabelPutInBedsideTableDollar.place_forget()
        LabelPutInBedsideTable.place_forget()
        LabelTakeInBedsideTable.place_forget()
        LabelTakeInBedsideTableDollar.place_forget()


def DefPutInBedsideTable():
    BtnBuyMoreProduct_And_HideAllBtnShop()
    if (messagebox.askyesno(title="Запит", message="Що будете класти долари чи гривні?(так-долари,ні-гривні)")):
        LabelPutInBedsideTableDollar.place(x=25,y=40)
        BuyMoreProductEntr1.config(command=DefPutDollarInBedsideTable)
    else:
        LabelPutInBedsideTable.place(x=25, y=40)
        BuyMoreProductEntr1.config(command=DefPutValutInBedsideTable)


def DefPutDollarInBedsideTable():
    global HaveDollar,HaveDollarInBedsideTable
    if HaveDollar>=int(BuyMoreProductEntry.get()):
        HaveDollarInBedsideTable = HaveDollarInBedsideTable + int(BuyMoreProductEntry.get())
        messagebox.askokcancel('Успіх!','Ви поклали '+BuyMoreProductEntry.get()+' доларів в тумбочку')
        HaveDollar = HaveDollar - int(BuyMoreProductEntry.get())
        DefHideMoreProduct()
        DefBedsideTable()
    else:
        messagebox.askokcancel('Помилка','Сталася помилка. Мабуть у вас немає стільки долларів')
def DefPutValutInBedsideTable():
    global money,HaveMoneyInBedsideTable
    if money>=int(BuyMoreProductEntry.get()):
        HaveMoneyInBedsideTable = HaveMoneyInBedsideTable + int(BuyMoreProductEntry.get())
        messagebox.askokcancel('Успіх!','Ви поклали '+BuyMoreProductEntry.get()+' гривень в тумбочку')
        money = money - int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        DefHideMoreProduct()
        DefBedsideTable()
    else:
        messagebox.askokcancel('Помилка','Сталася помилка. Мабуть у вас немає стільки гривень')


def DefInfoWhatInBedsideTable():
    LabelInfoBedsideTable.place_forget()
    btnPutInTheBedsideTable.place_forget()
    btnTakeFromBedsideTable.place_forget()
    btnInformationAboutWhatInTheBedsideTable.place_forget()
    EntryInfoMoneyInBedsideTable.place(x=5, y=60)
    EntryInfoMoneyInBedsideTable.insert(0,'Гривень: '+ str(HaveMoneyInBedsideTable))
    EntryInfoMoneyInBedsideTable.config(state='readonly')
    EntryInfoDollarInBedsideTable.place(x=155,y=60)
    EntryInfoDollarInBedsideTable.insert(0,'Доларів: '+ str(HaveDollarInBedsideTable))
    EntryInfoDollarInBedsideTable.config(state='readonly')
    LabelInfoWhatInBedsideTable.place(x=100,y=25)


def DefTakeInBedsideTable():
    BtnBuyMoreProduct_And_HideAllBtnShop()
    if (messagebox.askyesno(title="Запит", message="Що будете класти долари чи гривні?(так-долари,ні-гривні)")):
        LabelTakeInBedsideTableDollar.place(x=25,y=40)
        BuyMoreProductEntr1.config(command=DefTakeDollarInBedsideTable)
    else:
        LabelTakeInBedsideTable.place(x=25, y=40)
        BuyMoreProductEntr1.config(command=DefTakeValutInBedsideTable)


def DefTakeDollarInBedsideTable():
    global HaveDollar,HaveDollarInBedsideTable
    if HaveDollarInBedsideTable>=int(BuyMoreProductEntry.get()):
        HaveDollar = HaveDollar + int(BuyMoreProductEntry.get())
        messagebox.askokcancel('Успіх!','Ви дістали '+BuyMoreProductEntry.get()+' доларів з тумбочки')
        HaveDollarInBedsideTable = HaveDollarInBedsideTable - int(BuyMoreProductEntry.get())
        DefHideMoreProduct()
        DefBedsideTable()
    else:
        messagebox.askokcancel('Помилка','Сталася помилка. Мабуть у вас немає стільки долларів в тумбочці')

def DefTakeValutInBedsideTable():
    global money,HaveMoneyInBedsideTable
    if HaveMoneyInBedsideTable>=int(BuyMoreProductEntry.get()):
        HaveMoneyInBedsideTable = HaveMoneyInBedsideTable - int(BuyMoreProductEntry.get())
        messagebox.askokcancel('Успіх!','Ви дістали '+BuyMoreProductEntry.get()+' гривень з тумбочки')
        money = money + int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        DefHideMoreProduct()
        DefBedsideTable()
    else:
        messagebox.askokcancel('Помилка','Сталася помилка. Мабуть у вас немає стільки гривень в тумбочці')


def DefBuyBedsideTable():
    global money, HaveBedSideTable
    if messagebox.askokcancel('Покупка тумбочки','Тумбочка коштує 5000 грн. Будете купувати?'):
        if money>=5000:
            money=money-5000
            format(money)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.askokcancel('Успішна покупка!','Ви купили тумбочку за 5000 гривень! Дякую вам!')
            btnBedsideTable.config(text='Тумбочка',command=DefBedsideTable)
            HaveBedSideTable = True
        else:
            messagebox.askokcancel('Помилка', 'Сталася помилка. Мабуть у вас немає стільки гривень')


def DefGoBank():
    ExchangeCurrency.place_forget()
    WhatUpdate.place_forget()
    PromoCode.place_forget()
    Charity.place_forget()
    btnBank.place_forget()
    btnSaveSaves.place_forget()
    btnNextListMeinMenu3.place_forget()
    BackListMainMenu.place_forget()
    Reset.place_forget()
    btnPutOnBankCard.place_forget()
    btnTakeTheBankCard.place_forget()
    btnFindPinCode.place_forget()
    btnInfoPayAndGetBankCard.place_forget()
    BackTo2ListMainMenu.place(x=2, y=340)
    btnBankCard.place(x=75, y=100)
    LabelInBank.place(x=20,y=44)
    LabelBankCard.place_forget()
    DefHideMoreProduct()
    EntryPinCodeBankCard.delete(0,END)
    EntryHowMoneyOnBankCard.place_forget()
    EntryHowMoneyOnBankCard.config(state='normal')
    EntryHowMoneyOnBankCard.delete(0,END)
    LabelPayInExchangeCenter.place_forget()
    btnPayInExchangeCenterMoney.place_forget()
    btnPayInExchangeCenterCard.place_forget()
    LabelProofPinCode.place_forget()
    EntryProofPinCode.place_forget()
    btnEnterProofPinCode.place_forget()
    EntryProofPinCode.delete(0,END)
    LabelPayInShop.place_forget()
    btnPayInShopCard.place_forget()
    btnPayInShopMoney.place_forget()
    LabelPayInMarket.place_forget()
    btnPayInMarketCard.place_forget()
    btnPayInMarketMoney.place_forget()
    LabelPayInCasino.place_forget()
    btnPayInCasinoCard.place_forget()
    btnPayInCasinoMoney.place_forget()
    LabelPayInCharity.place_forget()
    btnPayInCharityCard.place_forget()
    btnPayInCharityMoney.place_forget()
    btnDeposit.place(x=75, y=160)
    LabelInDeposit.place_forget()
    btnPutOnDeposit.place_forget()
    btnTakeFromDeposit.place_forget()
    btnInfoAboutDeposit.place_forget()
    LabelPutInDeposite.place_forget()
    LabelTakeFromDeposite.place_forget()
    EntryHowMoneyOnDeposit.place_forget()
    EntryHowMoneyOnDeposit.config(state='normal')
    LabelInfoAboutDeposite.place_forget()
    btnTaxes.place(x=75, y=220)
    LabelInfoAboutTaxes.place_forget()
    btnPayAllTaxes.place_forget()
    btnPayTaxes.place_forget()
    btnPayTaxes1Room.place_forget()
    btnPayTaxes2Room.place_forget()
    btnPayTaxes3Room.place_forget()
    btnPayTaxes1House.place_forget()
    btnPayTaxes2House.place_forget()
    btnPayTaxes3House.place_forget()
    LabelPayTaxes.place_forget()
    btnPayTaxesCard.place_forget()
    btnPayTaxesMoney.place_forget()
    if HaveBankCard:
        btnBankCard.config(command=DefCard)

def DefGetBankCard():
    global money, PinCode,HaveBankCard
    if messagebox.askokcancel('Оформлення картки','Щоб оформити картку вам треба заплатити 2.000 гривень. Вам треба це зробити бо вона крута :)') and money>=2000:
        money = money-2000
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        PinCode = random.randint(1000,9999)
        btnBankCard.config(command=DefCard)
        HaveBankCard = True
        messagebox.askokcancel('Успіх!','Ви оформили картку ваш пін код ' +str(PinCode)+ '. Запишіть його десь, він буде потрібен для оплат')
    else:
        messagebox.askokcancel('Помилка','У вас немає стільки грошей або ви нехочете оформити картку :(')

def DefCard():
    btnBankCard.place_forget()
    btnPutOnBankCard.place(x=75, y=80)
    btnTakeTheBankCard.place(x=75, y=140)
    btnFindPinCode.place(x=75, y=200)
    btnInfoPayAndGetBankCard.place(x=75,y=260)
    BackTo2ListMainMenu.place_forget()
    LabelInBank.place_forget()
    LabelBankCard.place(x=15,y=33)
    btnBank.place(x=75, y=330)
    btnDeposit.place_forget()
    btnTaxes.place_forget()


def DefPutOnBankCard():
    LabelBankCard.place_forget()
    btnPutOnBankCard.place_forget()
    btnTakeTheBankCard.place_forget()
    btnFindPinCode.place_forget()
    btnInfoPayAndGetBankCard.place_forget()
    BtnBuyMoreProduct_And_HideAllBtnShop()
    EntryPinCodeBankCard.place(x=62, y=70)
    messagebox.askokcancel('Інструкція','В верхнє поле введіть пін-код,а в нижнє скільки хочете покласти грошей')
    BuyMoreProductEntr1.config(command=DefEnterPutOnBankCard)



def DefEnterPutOnBankCard():
    global PinCode,money, MoneyOnBankCard
    try:
        if int(EntryPinCodeBankCard.get()) == PinCode and money>=int(BuyMoreProductEntry.get()):
            money = money - int(BuyMoreProductEntry.get())
            MoneyOnBankCard = MoneyOnBankCard + int(BuyMoreProductEntry.get())
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.askokcancel('Успіх!','Ви успішно поклали '+BuyMoreProductEntry.get()+' гривень на рахунок карти. Тепер у вас на карті '+str(MoneyOnBankCard)+' гривень')
        else:
            messagebox.askokcancel('Помилка!','У вас немає стільки грошей або ви ввели неправильний пін-код')
    except:
        messagebox.askokcancel('Помилка!', 'У вас немає стільки грошей або ви ввели неправильний пін-код')



def DefTakeTheBankCard():
    LabelBankCard.place_forget()
    btnPutOnBankCard.place_forget()
    btnTakeTheBankCard.place_forget()
    btnFindPinCode.place_forget()
    btnInfoPayAndGetBankCard.place_forget()
    BtnBuyMoreProduct_And_HideAllBtnShop()
    EntryPinCodeBankCard.place(x=62, y=70)
    messagebox.askokcancel('Інструкція','В верхнє поле введіть пін-код,а в нижнє скільки хочете зняти грошей')
    BuyMoreProductEntr1.config(command=DefEnterTakeTheBankCard)


def DefEnterTakeTheBankCard():
    global PinCode,money, MoneyOnBankCard
    try:
        if int(EntryPinCodeBankCard.get()) == PinCode and MoneyOnBankCard>=int(BuyMoreProductEntry.get()):
            money = money + int(BuyMoreProductEntry.get())
            MoneyOnBankCard = MoneyOnBankCard - int(BuyMoreProductEntry.get())
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.askokcancel('Успіх!','Ви успішно взяли '+BuyMoreProductEntry.get()+' гривень з рахунку карти. Тепер у вас на карті '+str(MoneyOnBankCard)+' гривень')
        else:
            messagebox.askokcancel('Помилка!','У вас немає стільки грошей на карті або ви ввели неправильний пін-код')
    except:
        messagebox.askokcancel('Помилка!', 'У вас немає стільки грошей на карті або ви ввели неправильний пін-код')


def DefFindePinCode():
    global money
    if messagebox.askokcancel('Підтвердження','Якщо ви забули пін-код ви можете побачити його за 10.000 гривень. Згодні?') and money>=10000:
        money = money-10000
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        messagebox.askokcancel('Ваш пін-код','Ваш пін-код: '+str(PinCode)+'. Запишіть його кудись, щоб не забути')
    else:
        messagebox.askokcancel('Помилка','Ви не хочете побачити пін-код, або у вас немає 10.000 гривень')

def DefInfoPayAndGetBankCard():
    LabelBankCard.place_forget()
    btnPutOnBankCard.place_forget()
    btnTakeTheBankCard.place_forget()
    btnFindPinCode.place_forget()
    btnInfoPayAndGetBankCard.place_forget()
    EntryHowMoneyOnBankCard.insert(0,'Баланс карти: '+format(MoneyOnBankCard,'.2f'))
    EntryHowMoneyOnBankCard.config(state='readonly')
    EntryHowMoneyOnBankCard.place(x=10,y=33)
    LabelPayInExchangeCenter.place(x=5,y=82)
    btnPayInExchangeCenterCard.place(x=181,y=80)
    btnPayInExchangeCenterMoney.place(x=240,y=80)
    LabelProofPinCode.place(x=5,y=60)
    EntryProofPinCode.place(x=200,y=60)
    btnEnterProofPinCode.place(x=160,y=55)
    LabelPayInShop.place(x=5, y=112)
    btnPayInShopCard.place(x=181, y=110)
    btnPayInShopMoney.place(x=240, y=110)
    LabelPayInMarket.place(x=5,y=140)
    btnPayInMarketCard.place(x=181,y=140)
    btnPayInMarketMoney.place(x=240,y=140)
    LabelPayInCasino.place(x=5,y=170)
    btnPayInCasinoCard.place(x=181,y=170)
    btnPayInCasinoMoney.place(x=240,y=170)
    LabelPayInCharity.place(x=5,y=200)
    btnPayInCharityCard.place(x=181,y=200)
    btnPayInCharityMoney.place(x=240,y=200)
    LabelPayTaxes.place(x=5,y=230)
    btnPayTaxesCard.place(x=181,y=230)
    btnPayTaxesMoney.place(x=240,y=230)
def DefPayCardInExchangeCenter():
    global PayInExchangeCenter
    btnPayInExchangeCenterCard.config(state='normal',bg='green',fg='black')
    btnPayInExchangeCenterMoney.config(state='normal',bg='white',fg='black')
    PayInExchangeCenter = 'BankCard'
    messagebox.askokcancel('Нагадування!','Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                          ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                          'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                          '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                          'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayMoneyInExchangeCenter():
    global PayInExchangeCenter
    btnPayInExchangeCenterCard.config(state='normal',bg='white',fg='black')
    btnPayInExchangeCenterMoney.config(state='normal',bg='green',fg='black')
    PayInExchangeCenter = 'Money'



def DefProofPinCode():
    global ProofPinCode
    ProofPinCode = int(EntryProofPinCode.get())
    EntryProofPinCode.config(state="readonly")
    btnEnterProofPinCode.config(text='C', command=DefClearProofPinCode)


def DefClearProofPinCode():
    global ProofPinCode
    ProofPinCode = 0
    EntryProofPinCode.config(state='normal')
    EntryProofPinCode.delete(0,END)
    btnEnterProofPinCode.config(text='enter', command=DefProofPinCode)

def DefPayCardInShop():
    global PayInShop
    btnPayInShopCard.config(state='normal',bg='green',fg='black')
    btnPayInShopMoney.config(state='normal',bg='white',fg='black')
    PayInShop = 'BankCard'
    messagebox.askokcancel('Нагадування!','Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                          ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                          'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                          '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                          'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayMoneyInShop ():
    global PayInShop
    btnPayInShopCard.config(state='normal',bg='white',fg='black')
    btnPayInShopMoney.config(state='normal',bg='green',fg='black')
    PayInShop = 'Money'


def DefPayCardInMarket():
    global PayInMarket
    btnPayInMarketCard.config(state='normal',bg='green')
    btnPayInMarketMoney.config(state='normal',bg='white')
    PayInMarket = 'BankCard'
    messagebox.askokcancel('Нагадування!','Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                          ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                          'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                          '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                          'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayMoneyInMarket():
    global PayInMarket
    btnPayInMarketCard.config(state='normal',bg='white')
    btnPayInMarketMoney.config(state='normal',bg='green')
    PayInMarket = 'Money'


def DefPayCardInCasino():
    global PayInCasino
    btnPayInCasinoCard.config(state='normal',bg='green')
    btnPayInCasinoMoney.config(state='normal',bg='white')
    PayInCasino = 'BankCard'
    messagebox.askokcancel('Нагадування!','Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                          ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                          'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                          '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                          'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayMoneyInCasino():
    global PayInCasino
    btnPayInCasinoCard.config(state='normal',bg='white')
    btnPayInCasinoMoney.config(state='normal',bg='green')
    PayInCasino = 'Money'


def DefPayCardInCharity():
    global PayInCharity
    btnPayInCharityCard.config(state='normal',bg='green')
    btnPayInCharityMoney.config(state='normal',bg='white')
    PayInCharity = 'BankCard'
    messagebox.askokcancel('Нагадування!','Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                          ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                          'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                          '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                          'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayMoneyInCharity():
    global PayInCharity
    btnPayInCharityCard.config(state='normal',bg='white')
    btnPayInCharityMoney.config(state='normal',bg='green')
    PayInCharity = 'Money'



def DefDeposit():
    btnDeposit.place_forget()
    btnBankCard.place_forget()
    LabelInBank.place_forget()
    btnBank.place(x=75, y=330)
    BackTo2ListMainMenu.place_forget()
    btnPutOnDeposit.place(x=75, y=80)
    btnTakeFromDeposit.place(x=75, y=140)
    btnInfoAboutDeposit.place(x=75, y=200)
    LabelInDeposit.place(x=5,y=33)
    btnTaxes.place_forget()




def DefPutOnDeposit():
    global  TempDeposit
    btnPutOnDeposit.place_forget()
    btnTakeFromDeposit.place_forget()
    btnInfoAboutDeposit.place_forget()
    BtnBuyMoreProduct_And_HideAllBtnShop()
    LabelInDeposit.place_forget()
    BuyMoreProductEntr1.config(command=DefEnterPutOnDeposit)
    StopDeposit()
    TempDeposit = 0
    LabelPutInDeposite.place(x=15,y=40)


def DefEnterPutOnDeposit():
    global MoneyOnDeposit, money
    if int(BuyMoreProductEntry.get())<= money:
        MoneyOnDeposit = MoneyOnDeposit+int(BuyMoreProductEntry.get())
        money=money-int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        tickDeposit()
        print(MoneyOnDeposit)
        messagebox.askokcancel('Успішно','Ви успішно поклали '+BuyMoreProductEntry.get()+' гривень на депозит')
    else:
        messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
def DefTakeFromDeposit():
    global TempDeposit
    btnPutOnDeposit.place_forget()
    btnTakeFromDeposit.place_forget()
    btnInfoAboutDeposit.place_forget()
    BtnBuyMoreProduct_And_HideAllBtnShop()
    LabelInDeposit.place_forget()
    BuyMoreProductEntr1.config(command=DefEnterTakeFromDeposit)
    StopDeposit()
    TempDeposit = 0
    LabelTakeFromDeposite.place(x=15, y=40)

def DefEnterTakeFromDeposit():
    global MoneyOnDeposit, money
    if int(BuyMoreProductEntry.get())<= MoneyOnDeposit:
        MoneyOnDeposit = MoneyOnDeposit-int(BuyMoreProductEntry.get())
        money=money+int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        tickDeposit()
        print(MoneyOnDeposit)
        messagebox.askokcancel('Успішно','Ви успішно зняли '+BuyMoreProductEntry.get()+' гривень з депозиту')
    else:
        messagebox.askokcancel('Помилка','У вас немає стільки грошей на депозиті(')

def DefInfoAboutDeposit():
    btnPutOnDeposit.place_forget()
    btnTakeFromDeposit.place_forget()
    btnInfoAboutDeposit.place_forget()
    LabelInDeposit.place_forget()
    EntryHowMoneyOnDeposit.delete(0, END)
    EntryHowMoneyOnDeposit.insert(0, 'На депозиті: ' + format(MoneyOnDeposit, '.2f'))
    EntryHowMoneyOnDeposit.config(state='readonly')
    EntryHowMoneyOnDeposit.place(x=10, y=33)
    LabelInfoAboutDeposite.place(x=10,y=60)


def tickDeposit():
    global TempDeposit, AfterIdDeposit,MoneyOnDeposit
    AfterIdDeposit = root.after(1000, tickDeposit)
    FTempDeposit = str(int(TempDeposit / 3600)) + ":" + str(int((TempDeposit % 3600) / 60)) + ":" + str(int(TempDeposit % 60))
    TempDeposit = TempDeposit + 1
    if TempDeposit == 60:
        MoneyOnDeposit = MoneyOnDeposit + (MoneyOnDeposit//1000)
        EntryHowMoneyOnDeposit.config(state='normal')
        EntryHowMoneyOnDeposit.delete(0,END)
        EntryHowMoneyOnDeposit.insert(0, 'На депозиті: ' + format(MoneyOnDeposit, '.2f'))
        EntryHowMoneyOnDeposit.config(state='readonly')
        #print(MoneyOnDeposit)
        TempDeposit = 0


def StopDeposit():
    global TempDeposit,AfterIdDeposit, temp
    TempDeposit = 0
    temp = 0
    root.after_cancel(AfterIdDeposit)



def DefTaxes():
    LabelInBank.place_forget()
    btnBankCard.place_forget()
    btnDeposit.place_forget()
    btnTaxes.place_forget()
    btnBank.place(x=75, y=330)
    BackTo2ListMainMenu.place_forget()
    btnPayTaxes.place(x=75,y=145)
    LabelInfoAboutTaxes.place(x=0,y=20)
    btnPayAllTaxes.place(x=75,y=205)
    btnPayTaxes1Room.config(text='Оплатити податки за\nоднокімнатну квартиру\n(' + str(Taxes1Room) + ' гривень)')
    btnPayTaxes2Room.config(text='Оплатити податки за\nдвокімнатну квартиру\n(' + str(Taxes2Room) + ' гривень)')
    btnPayTaxes3Room.config(text='Оплатити податки за\nтрьохкімнатну квартиру\n(' + str(Taxes3Room) + ' гривень)')
    btnPayTaxes1House.config(text='Оплатити податки за\nодноповерховий будинок\n(' + str(Taxes1House) + ' гривень)')
    btnPayTaxes2House.config(text='Оплатити податки за\nдвоповерховий будинок\n(' + str(Taxes2House) + ' гривень)')
    btnPayTaxes3House.config(text='Оплатити податки за\nхай-тег будинок\n(' + str(Taxes3House) + ' гривень)')
    btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')

tickDeposit()



def tickTaxes():
    global TempTaxes, AfterIdTaxes,Taxes1Room,Taxes2Room,Taxes3Room,Taxes1House,Taxes2House,Taxes3House,AllTaxes
    global Have1Room,Have2Room,Have3Room,Have1House,Have2House,Have3House
    AfterIdTaxes = root.after(1000, tickTaxes)
    FTempTaxes = str(int(TempTaxes / 3600)) + ":" + str(int((TempTaxes % 3600) / 60)) + ":" + str(int(TempTaxes % 60))
    TempTaxes = TempTaxes + 1
    if TempTaxes >= 120:
        if Have1Room:
            Taxes1Room = Taxes1Room + 500
            btnPayTaxes1Room.config(text='Оплатити податки за\nоднокімнатну квартиру\n('+str(Taxes1Room)+' гривень)')
            if Taxes1Room>=250000:
                Have1Room = False
                Buy1Room.config(command=DefBuy1Room,text='Купити однокімнатну\nквартиру')
                Go1Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend1Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell1Room.config(text='Це не баг, а фіча!', state=DISABLED)
                try:
                    DefStopOrend1Room(1)
                except:
                    pass
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати вашу '
                'однокімнатну квартиру.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        if Have2Room:
            Taxes2Room = Taxes2Room+750
            btnPayTaxes2Room.config(text='Оплатити податки за\nдвокімнатну квартиру\n('+str(Taxes2Room)+' гривень)')
            if Taxes2Room>=375000:#37500
                Have2Room = False
                Buy2Room.config(command=DefBuy2Room,text='Купити двокімнатну \n квартиру')
                Go2Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend2Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell2Room.config(text='Це не баг, а фіча!', state=DISABLED)
                try:
                    DefStopOrend2Room(1)
                except:
                    pass
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати вашу '
                'двокімнатну квартиру.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        if Have3Room:
            Taxes3Room = Taxes3Room+1000
            btnPayTaxes3Room.config(text='Оплатити податки за\nтрьохкімнатну квартиру\n('+str(Taxes3Room)+' гривень)')
            if Taxes3Room>=500000:#50000
                Have3Room = False
                Buy3Room.config(text='Купити трьохкімнатну\nквартиру',command=DefBuy3Room)
                Go3Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend3Room.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell3Room.config(text='Це не баг, а фіча!', state=DISABLED)
                try:
                    DefStopOrend3Room(1)
                except:
                    pass
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати вашу '
                'трьохкімнатну квартиру.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        if Have1House:
            Taxes1House = Taxes1House+2500
            btnPayTaxes1House.config(text='Оплатити податки за\nодноповерховий будинок\n('+str(Taxes1House)+' гривень)')
            if Taxes1House>=1250000:#125000
                Have1House=False
                Buy1House.config(text='Купити одноповерховий\nбудинок',command=DefBuy1House)
                Go1House.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend1House.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell1House.config(text='Це не баг, а фіча!', state=DISABLED)
                Maining1House.config(text='Це не баг, а фіча!', state=DISABLED)
                DefNotPayTaxes1House()
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати ваш'
                'одноповерховий будинок.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        if Have2House:
            Taxes2House = Taxes2House+3750
            btnPayTaxes2House.config(text='Оплатити податки за\nдвоповерховий будинок\n('+str(Taxes2House)+' гривень)')
            if Taxes2House>=1875000:#187500
                Have2House = False
                Buy2House.config(text='Купити двоповерховий\nбудинок',command=DefBuy2House)
                Go2House.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend2House.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell2House.config(text='Це не баг, а фіча!', state=DISABLED)
                Maining2House.config(text='Це не баг, а фіча!', state=DISABLED)
                DefNotPayTaxes2House()
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати ваш'
                'двоповерховий будинок.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        if Have3House:
            Taxes3House = Taxes3House+5000
            btnPayTaxes3House.config(text='Оплатити податки за\nхай-тег будинок\n('+str(Taxes3House)+' гривень)')
            if Taxes3House>=2500000:#250000
                Have3House = False
                Buy3House.config(text='Купити хай-тег дім будинок',command=DefBuy3House)
                Go3House.config(text='Це не баг, а фіча!', state=DISABLED)
                Orend3House.config(text='Це не баг, а фіча!', state=DISABLED)
                Sell3House.config(text='Це не баг, а фіча!', state=DISABLED)
                Maining3House.config(text='Це не баг, а фіча!', state=DISABLED)
                DefNotPayTaxes3House()
                messagebox.askokcancel('Упс, ви не оплатили податки','Нажаль, через несплату податків ми мусимо забрати ваш'
                'одноповерховий будинок.Щоб такого більше не повторювалося не забувайте оплачувати податки.')
        print('True Taxes')
        AllTaxes = 0
        AllTaxes= Taxes1Room+Taxes2Room+Taxes3Room+Taxes1House+Taxes2House+Taxes3House
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
        TempTaxes=0

tickTaxes()


def DefPayTaxesMenu():
    btnPayTaxes.place_forget()
    btnPayAllTaxes.place_forget()
    LabelInfoAboutTaxes.place_forget()
    if Have1Room:
        btnPayTaxes1Room.config(state='normal')
    else:
        btnPayTaxes1Room.config(state='disabled')
    if Have2Room:
        btnPayTaxes2Room.config(state='normal')
    else:
        btnPayTaxes2Room.config(state='disabled')
    if Have3Room:
        btnPayTaxes3Room.config(state='normal')
    else:
        btnPayTaxes3Room.config(state='disabled')
    if Have1House:
        btnPayTaxes1House.config(state='normal')
    else:
        btnPayTaxes1House.config(state='disabled')
    if Have2House:
        btnPayTaxes2House.config(state='normal')
    else:
        btnPayTaxes2House.config(state='disabled')
    if Have3House:
        btnPayTaxes3House.config(state='normal')
    else:
        btnPayTaxes3House.config(state='disabled')
    btnPayTaxes1Room.place(x=2,y=23)
    btnPayTaxes2Room.place(x=153,y=23)
    btnPayTaxes3Room.place(x=2,y=83)
    btnPayTaxes1House.place(x=153,y=83)
    btnPayTaxes2House.place(x=2,y=143)
    btnPayTaxes3House.place(x=153,y=143)


def DefNotPayTaxes1House():
    global VideoCard1House,MainingIn1House,MainingSetUp1House,Have1House
    global FrameForMining1House,CanGoToBasement1Home,Maining1HouseChange
    VideoCard1House = False
    MainingIn1House = False
    MainingSetUp1House = False
    FrameForMining1House = False
    CanGoToBasement1Home = False
    Maining1HouseChange = False
    Buy1House.config(text='Купити одноповерховий \n будинок', command=DefBuy1House)
    try:
        DefStopMining1House(1)
    except:
        pass
    try:
        DefStopOrend1House(1)
    except:
        pass
    Have1House=False


def DefNotPayTaxes2House():
    global VideoCard2House,FrameForMining2House,MainingIn2House,Have2House
    global MainingSetUp2House,Orend2HouseChange,Maining2HouseChange
    VideoCard2House = False
    MainingIn2House = False
    MainingSetUp2House = False
    FrameForMining2House = False
    Maining2HouseChange = False
    Buy2House.config(text='Купити двоповерховий \n будинок', command=DefBuy2House)
    try:
        DefStopMining2House(1)
    except:
        pass
    try:
        DefStopOrend2House(1)
    except:
        pass
    Have2House = False

def DefNotPayTaxes3House():
    global Orend3HouseChange, VideoCard3House, FrameForMining3House
    global MainingIn3House, MainingSetUp3House, Maining3HouseChange,Have3House
    VideoCard3House = False
    MainingIn3House = False
    MainingSetUp3House = False
    FrameForMining3House = False
    Maining3HouseChange = False
    Buy3House.config(text='Купити триповерховий \n будинок', command=DefBuy2House)
    try:
        DefStopMining3House(1)
    except:
        pass
    try:
        DefStopOrend3House(1)
    except:
        pass
    Have3House = False

def DefPayTaxes1Room():
    global money,MoneyOnBankCard,Taxes1Room,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes1Room)+' гривень податку за однокімнатну квартиру?'):
        if PayTaxes=='Money':
            if money>=Taxes1Room:
                money=money-Taxes1Room
                AllTaxes = AllTaxes - Taxes1Room
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes1Room=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if ProofPinCode==PinCode:
                if MoneyOnBankCard>=Taxes1Room:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes1Room
                    AllTaxes = AllTaxes - Taxes1Room
                    Taxes1Room=0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-code, або підтвердили неправильно')
        btnPayTaxes1Room.config(text='Оплатити податки за\nоднокімнатну квартиру\n(' + str(Taxes1Room) + ' гривень)')
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')

def DefPayTaxes2Room():
    global money,MoneyOnBankCard,Taxes2Room,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes2Room)+' гривень податку за двокімнатну квартиру?'):
        if PayTaxes=='Money':
            if money>=Taxes2Room:
                money=money-Taxes2Room
                AllTaxes = AllTaxes - Taxes2Room
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes2Room=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=Taxes2Room:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes2Room
                    AllTaxes = AllTaxes - Taxes2Room
                    Taxes2Room=0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-code, або підтвердили неправильно')
        btnPayTaxes2Room.config(text='Оплатити податки за\nдвокімнатну квартиру\n(' + str(Taxes2Room) + ' гривень)')
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')


def DefPayTaxes3Room():
    global money,MoneyOnBankCard,Taxes3Room,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes3Room)+' гривень податку за трьохкімнатну квартиру?'):
        if PayTaxes=='Money':
            if money>=Taxes3Room:
                money=money-Taxes3Room
                AllTaxes = AllTaxes - Taxes3Room
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes3Room=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=Taxes3Room:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes3Room
                    AllTaxes = AllTaxes - Taxes3Room
                    Taxes3Room=0
                else:
                    messagebox.askokcancel('Помилка', 'У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка', 'Ви не підтвердили Pin-code, або підтвердили неправильно')
            btnPayTaxes3Room.config(text='Оплатити податки за\nтрьохкімнатну квартиру\n(' + str(Taxes3Room) + ' гривень)')
            btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
def DefPayTaxes1House():
    global money,MoneyOnBankCard,Taxes1House,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes1House)+' гривень податку за одноповерховий будинок?'):
        if PayTaxes=='Money':
            if money>=Taxes1House:
                money=money-Taxes1House
                AllTaxes = AllTaxes - Taxes1House
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes1House=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=Taxes1House:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes1House
                    AllTaxes = AllTaxes - Taxes1House
                    Taxes1House=0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-code, або підтвердили неправильно')
        btnPayTaxes1House.config(text='Оплатити податки за\nодноповерховий будинок\n(' + str(Taxes1House) + ' гривень)')
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')

def DefPayTaxes2House():
    global money,MoneyOnBankCard,Taxes2House,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes2House)+' гривень податку за двоповерховий будинок?'):
        if PayTaxes=='Money':
            if money>=Taxes2House:
                money=money-Taxes2House
                AllTaxes = AllTaxes - Taxes2House
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes2House=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=Taxes2House:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes2House
                    AllTaxes = AllTaxes - Taxes2House
                    Taxes2House=0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-code, або підтвердили неправильно')
        btnPayTaxes2House.config(text='Оплатити податки за\nдвоповерховий будинок\n(' + str(Taxes2House) + ' гривень)')
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')


def DefPayTaxes3House():
    global money,MoneyOnBankCard,Taxes3House,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити '+str(Taxes3House)+' гривень податку за хай-тег будинок?'):
        if PayTaxes=='Money':
            if money>=Taxes3House:
                money=money-Taxes3House
                AllTaxes = AllTaxes - Taxes3House
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                Taxes3House=0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=Taxes3House:
                    MoneyOnBankCard=MoneyOnBankCard-Taxes3House
                    AllTaxes = AllTaxes - Taxes3House
                    Taxes3House=0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на карті(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-code, або підтвердили неправильно')
        btnPayTaxes3House.config(text='Оплатити податки за\nхай-тег будинок\n(' + str(Taxes3House) + ' гривень)')
        btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')

def DefPayMoneyTaxes():
    global PayTaxes
    btnPayTaxesCard.config(state='normal',bg='white')
    btnPayTaxesMoney.config(state='normal',bg='green')
    PayTaxes='Money'


def DefPayBankCardTaxes():
    global PayTaxes
    btnPayTaxesMoney.config(state='normal',bg='white')
    btnPayTaxesCard.config(state='normal',bg='green')
    PayTaxes = 'BankCard'
    messagebox.askokcancel('Нагадування!', 'Якщо ви не підтвердили пінкод, то покупки, продажі на біржі, в казино і'
                                           ' на продажі їжі ви не зможете оплачувати/отримувати гроші на картку.'
                                           'Щоб підтвердити Pin-code просто введіть його в поле біля тексту '
                                           '"Підтвердити Pin-code" і натисніть enter. Якщо ви випадкова'
                                           'ввели не той пінкод просто натисніть на С і введіть по новому')


def DefPayAllTaxes():
    global money,MoneyOnBankCard,Taxes1Room,Taxes2Room,Taxes3Room,Taxes1House,Taxes2House,Taxes3House,AllTaxes
    if messagebox.askokcancel('Підтвердження','Ви точно хочете оплатити податки за всі будівлі('+str(AllTaxes)+'гривень)?'):
        if PayTaxes=='Money':
            if money>=AllTaxes:
                money=money-AllTaxes
                LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                AllTaxes=0
                btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
                Taxes1Room = 0
                Taxes2Room = 0
                Taxes3Room = 0
                Taxes1House = 0
                Taxes2House = 0
                Taxes3House = 0
            else:
                messagebox.askokcancel('Помилка','У вас немає стільки грошей(')
        if PayTaxes=='BankCard':
            if PinCode==ProofPinCode:
                if MoneyOnBankCard>=AllTaxes:
                    MoneyOnBankCard = MoneyOnBankCard - AllTaxes
                    AllTaxes = 0
                    btnPayAllTaxes.config(text='Оплатити всі податки\n(' + str(AllTaxes) + ' грн)')
                    Taxes1Room = 0
                    Taxes2Room = 0
                    Taxes3Room = 0
                    Taxes1House = 0
                    Taxes2House = 0
                    Taxes3House = 0
                else:
                    messagebox.askokcancel('Помилка','У вас немає стільки грошей на картці(')
            else:
                messagebox.askokcancel('Помилка','Ви не підтвердили Pin-Code, або підтвердили неправильно')
        btnPayTaxes1Room.config(text='Оплатити податки за\nоднокімнатну квартиру\n(' + str(Taxes1Room) + ' гривень)')
        btnPayTaxes2Room.config(text='Оплатити податки за\nдвокімнатну квартиру\n(' + str(Taxes2Room) + ' гривень)')
        btnPayTaxes3Room.config(text='Оплатити податки за\nтрьохкімнатну квартиру\n(' + str(Taxes3Room) + ' гривень)')
        btnPayTaxes1House.config(text='Оплатити податки за\nодноповерховий будинок\n(' + str(Taxes1House) + ' гривень)')
        btnPayTaxes2House.config(text='Оплатити податки за\nдвоповерховий будинок\n(' + str(Taxes2House) + ' гривень)')
        btnPayTaxes3House.config(text='Оплатити податки за\nхай-тег будинок\n(' + str(Taxes3House) + ' гривень)')



def DefGoSaveMenu():
    ExchangeCurrency.place_forget()
    Charity.place_forget()
    btnBank.place_forget()
    btnSave.place_forget()
    BackListMainMenu.place_forget()
    btnNextListMeinMenu3.place_forget()
    WhatUpdate.place_forget()
    PromoCode.place_forget()
    Reset.place_forget()
    LabelBeforeEnter.place_forget()
    BackTo2ListMainMenu.place(x=2, y=340)
    BackTo2ListMainMenu.config(command=Start)
    if HaveSave ==0:
        btnAddSave.place(x=230,y=30)
    if HaveSave >= 1:
        btnAddSave.place(x=230,y=110)
        LabelSave1.place(x=2, y=50)
        btnUploadFrom1File.place(x=225, y=47)
        btnDeleat1File.place(x=225, y=72)
    if HaveSave >= 2:
        btnAddSave.place(x=230,y=190)
        LabelSave2.place(x=2, y=130)
        btnUploadFrom2File.place(x=225, y=127)
        btnDeleat2File.place(x=225, y=152)
    if HaveSave >= 3:
        btnAddSave.place(x=230,y=270)
        LabelSave3.place(x=2, y=210)
        btnUploadFrom3File.place(x=225, y=207)
        btnDeleat3File.place(x=225, y=232)
    if HaveSave >= 4:
        btnAddSave.place_forget()
        LabelSave4.place(x=2, y=290)
        btnUploadFrom4File.place(x=225, y=287)
        btnDeleat4File.place(x=225, y=312)
    Lines1.place(x=0,y=90)
    Lines2.place(x=0,y=170)
    Lines3.place(x=0,y=250)

def DefAddSave():
    global NameSave1,NameSave2,NameSave3,NameSave4,HaveSave
    if HaveSave==0:
        btnAddSave.place_forget()
        EntryNameSave.place(x=70,y=60)
        LabelHowNammetSave.place(x=40,y=30)
        EnterNameSave.place(x=192,y=60)
    if HaveSave==1:
        btnAddSave.place_forget()
        EntryNameSave.place(x=70, y=140)
        LabelHowNammetSave.place(x=40, y=110)
        EnterNameSave.place(x=192, y=140)
    if HaveSave==2:
        btnAddSave.place_forget()
        EntryNameSave.place(x=70, y=220)
        LabelHowNammetSave.place(x=40, y=190)
        EnterNameSave.place(x=192, y=220)
    if HaveSave==3:
        btnAddSave.place_forget()
        EntryNameSave.place(x=70, y=300)
        LabelHowNammetSave.place(x=40, y=270)
        EnterNameSave.place(x=192, y=300)
    if HaveSave==4:
        btnAddSave.place_forget()
        EntryNameSave.place(x=70, y=380)
        LabelHowNammetSave.place(x=40, y=350)
        EnterNameSave.place(x=192, y=380)
def DefEnterNameSave():
    global NameSave1,NameSave2,NameSave3,NameSave4,HaveSave
    if HaveSave == 0:
        NameSave1 = EntryNameSave.get()
        EntryNameSave.delete(0,END)
        HaveSave= 1
        btnAddSave.place(x=230, y=110)
        EntryNameSave.place_forget()
        LabelHowNammetSave.place_forget()
        EnterNameSave.place_forget()
        LabelSave1.config(text='Збереження:'+NameSave1)
        LabelSave1.place(x=2,y=50)
        btnUploadFrom1File.place(x=225,y=47)
        btnDeleat1File.place(x=225,y=72)
        Save_saves = open('Txt_Shop/save/save_saves_name.txt', 'r+')
        Save_saves.writelines(NameSave1 + '\n' + NameSave2 + '\n' + NameSave3 + '\n' + NameSave4 + '\n' + str(HaveSave))
        Save_saves.close()
        return
    if HaveSave == 1:
        NameSave2 = EntryNameSave.get()
        EntryNameSave.delete(0,END)
        HaveSave= 2
        btnAddSave.place(x=230, y=190)
        EntryNameSave.place_forget()
        LabelHowNammetSave.place_forget()
        EnterNameSave.place_forget()
        LabelSave2.config(text='Збереження:' + NameSave2)
        LabelSave2.place(x=2,y=130)
        btnUploadFrom2File.place(x=225,y=127)
        btnDeleat2File.place(x=225,y=152)
        Save_saves = open('Txt_Shop/save/save_saves_name.txt', 'r+')
        Save_saves.writelines(NameSave1 + '\n' + NameSave2 + '\n' + NameSave3 + '\n' + NameSave4 + '\n' + str(HaveSave))
        Save_saves.close()
        return
    if HaveSave == 2:
        NameSave3 = EntryNameSave.get()
        EntryNameSave.delete(0,END)
        HaveSave= 3
        btnAddSave.place(x=230, y=270)
        EntryNameSave.place_forget()
        LabelHowNammetSave.place_forget()
        EnterNameSave.place_forget()
        LabelSave3.config(text='Збереження:' + NameSave3)
        LabelSave3.place(x=2,y=210)
        btnUploadFrom3File.place(x=225,y=207)
        btnDeleat3File.place(x=225,y=232)
        Save_saves = open('Txt_Shop/save/save_saves_name.txt', 'r+')
        Save_saves.writelines(NameSave1 + '\n' + NameSave2 + '\n' + NameSave3 + '\n' + NameSave4 + '\n' + str(HaveSave))
        Save_saves.close()
        return
    if HaveSave == 3:
        NameSave4 = EntryNameSave.get()
        EntryNameSave.delete(0,END)
        HaveSave= 4
        btnAddSave.place_forget()
        EntryNameSave.place_forget()
        LabelHowNammetSave.place_forget()
        EnterNameSave.place_forget()
        LabelSave4.config(text='Збереження:' + NameSave4)
        LabelSave4.place(x=2,y=290)
        btnUploadFrom4File.place(x=225,y=287)
        btnDeleat4File.place(x=225,y=312)
        Save_saves = open('Txt_Shop/save/save_saves_name.txt', 'r+')
        Save_saves.writelines(NameSave1 + '\n' + NameSave2 + '\n' + NameSave3 + '\n' + NameSave4 + '\n' + str(HaveSave))
        Save_saves.close()
        return



def DefSave1Save(v):
    Save1 = open('Txt_Shop/save/save_'+str(v)+'.txt','w')
    Save1.write('')
    Save1.close()
    Save1 = open('Txt_Shop/save/save_'+str(v)+'.txt', 'r+')
    Save1.writelines(str(money)+'\n'+str(TempOrend1Room)+'\n'+AfterIdOrend1Room+'\n'+str(Orend1RoomChange)+
                     '\n'+str(TempOrend2Room)+'\n'+AfterIdOrend2Room+'\n'+str(Orend2RoomChange)+'\n'+str(Orend3RoomChange)+
                     '\n'+str(TempOrend3Room)+'\n'+AfterIdOrend3Room+'\n'+str(Orend1HouseChange)+'\n'+str(TempOrend1House)+'\n'+AfterIdOrend1House+
                     '\n'+str(VideoCard1House)+'\n'+str(MainingIn1House)+'\n'+str(MainingSetUp1House)+'\n'+str(FrameForMining1House)+'\n'+
                     str(CanGoToBasement1Home)+'\n'+str(TempMaining1House)+'\n'+AfterIdMaining1House+'\n'+str(Crypto1House)+'\n'+
                     str(Maining1HouseChange)+'\n'+str(VideoCard2House)+'\n'+str(FrameForMining2House)+'\n'+str(MainingIn2House)+'\n'+
                     str(MainingSetUp2House)+'\n'+str(Orend2HouseChange)+'\n'+str(TempOrend2House)+'\n'+AfterIdOrend2House+'\n'+
                     str(Maining2HouseChange)+'\n'+str(TempMaining2House)+'\n'+str(Crypto2House)+'\n'+str(Orend3HouseChange)+
                     '\n'+str(VideoCard3House)+'\n'+str(FrameForMining3House)+'\n'+str(MainingIn3House)+'\n'+str(MainingSetUp3House)+
                     '\n'+str(Maining3HouseChange)+'\n'+str(TempOrend3House)+'\n'+AfterIdOrend3House+'\n'+str(Crypto3House)+
                     '\n'+str(TempMaining3House)+'\n'+AfterIdMaining3House+'\n'+str(TempCourseChangeShopCoins)+'\n'+
                     AfterIdCourseChangeShopCoins+'\n'+str(CoursShopCoins)+'\n'+str(HaveShopCoins)+'\n'+str(HaveDollar)+'\n'+
                     str(TempCourseChangeDollar)+'\n'+AfterIdCourseChangeDollar+'\n'+str(CoursDollar)+'\n'+str(HaveSausage)+'\n'+
                     str(HaveCheese)+'\n'+str(HaveThan)+'\n'+str(HaveFlour)+'\n'+str(HaveChocolate)+'\n'+str(HaveCola)+
                     '\n'+str(HaveBread)+'\n'+str(HaveOil)+'\n'+str(HaveBowl)+'\n'+str(HaveSalt)+'\n'+str(HaveSalad)+'\n'+
                     str(HaveTomato)+'\n'+str(HaveCucumber)+'\n'+str(HaveCutSausage)+'\n'+str(HaveCutCheese)+'\n'
                     +str(HaveCutChocolate)+'\n'+str(HaveCutBread)+'\n'+str(HaveCutSalad)+'\n'+str(HaveCutTomato)+'\n'
                     +str(HaveCutCucumber)+'\n'+str(HaveSalat)+'\n'+str(HaveButerbrod)+'\n'+str(PromoCodeAmogus)+'\n'+str(PromoCodeUpdate_dowN_BlockNot)
                     +'\n'+str(PromoCodeSecret_Charity_SUS)+'\n'+str(PromoCodeAmogus2024)+'\n'+str(PromoCodeFrog)+'\n'
                     +str(PromoCodeAbyba)+'\n'+str(PromoCodeShop)+'\n'+str(HaveDollarInBedsideTable)+'\n'+str(HaveMoneyInBedsideTable)
                     +'\n'+str(PromoCodeStop_Orend_3_House)+'\n'+str(PromoCodeMining_1House_lox_)+'\n'+str(PromoCodeStooopOrend_One_Room)
                     +'\n'+str(MemeBedsideTable)+'\n'+str(PinCode)+'\n'+str(MoneyOnBankCard)+'\n'+str(PromoDontHaveMoneyShop)+'\n'
                     +str(MoneyOnDeposit)+'\n'+str(TempDeposit)+'\n'+AfterIdDeposit+'\n'+str(AllTaxes)+'\n'+str(TempTaxes)
                     +'\n'+AfterIdTaxes+'\n'+str(Taxes1Room)+'\n'+str(Taxes2Room)+'\n'+str(Taxes3Room)+'\n'+str(Taxes1House)
                     +'\n'+str(Taxes2House)+'\n'+str(Taxes3House)+'\n'+str(Have1Room)+'\n'+str(Have2Room)+'\n'+str(Have3Room)
                     +'\n'+str(Have1House)+'\n'+str(Have2House)+'\n'+str(Have3House)+'\n'+str(HaveBedSideTable)+'\n'+str(HaveBankCard)+'\n'+
                     str(HaveStuffing)+'\n'+str(HaveSpaghetti)+'\n'+str(HaveCookSpaghetti)+'\n'+str(HaveCutlet)+'\n'+str(HaveSpaghettiWithCutlet))
    Save1.close()
    messagebox.askokcancel('Успіх!','Ваш прогрес успішно зберігся!')
    #  = 120000000
    # TempOrend1Room = 0
    # AfterIdOrend1Room = ''
    # Orend1RoomChange = False
    # TempOrend2Room = 0
    # AfterIdOrend2Room = ''
    # Orend2RoomChange = False
    # Orend3RoomChange = False
    # TempOrend3Room = 0
    # AfterIdOrend3Room = ''
    # Orend1HouseChange = False
    # TempOrend1House = 0
    # AfterIdOrend1House = ''
    # VideoCard1House = False
    # MainingIn1House = False
    # MainingSetUp1House = False
    # FrameForMining1House = False
    # CanGoToBasement1Home = False
    # TempMaining1House = 0
    # AfterIdMaining1House = ''
    # Crypto1House = 0
    # Maining1HouseChange = False
    # VideoCard2House = False
    # FrameForMining2House = False
    # MainingIn2House = False
    # MainingSetUp2House = False
    # Orend2HouseChange = False
    # TempOrend2House = 0
    # AfterIdOrend2House = ''
    # Maining2HouseChange = False
    # TempMaining2House = 0
    # Crypto2House = 0
    # Orend3HouseChange = False
    # VideoCard3House = False
    # FrameForMining3House = False
    # MainingIn3House = False
    # MainingSetUp3House = False
    # Maining3HouseChange = False
    # TempOrend3House = 0
    # AfterIdOrend3House = ''
    # Crypto3House = 0
    # TempMaining3House = 0
    # AfterIdMaining3House = ''
    # TempCourseChangeShopCoins = 0
    # AfterIdCourseChangeShopCoins = ''
    # CoursShopCoins = 100
    # HaveShopCoins = 0
    # HaveDollar = 0
    # TempCourseChangeDollar = 0
    # AfterIdCourseChangeDollar = ''
    # CoursDollar = 30
    # HaveSausage = 0
    # HaveCheese = 0
    # HaveThan = 0
    # HaveFlour = 0
    # HaveChocolate = 0
    # HaveCola = 0
    # HaveBread = 0
    # HaveOil = 0
    # HaveBowl = 0
    # HaveSalt = 0
    # HaveSalad = 0
    # HaveTomato = 0
    # HaveCucumber = 0
    # HaveCutSausage = 0
    # HaveCutCheese = 0
    # HaveCutChocolate = 0
    # HaveCutBread = 0
    # HaveCutSalad = 0
    # HaveCutTomato = 0
    # HaveCutCucumber = 0
    # HaveSalat = 0
    # HaveButerbrod = 0
    # PromoCodeAmogus = False
    # PromoCodeUpdate_dowN_BlockNot = False
    # PromoCodeSecret_Charity_SUS = False
    # PromoCodeAmogus2024 = False
    # PromoCodeFrog = False
    # PromoCodeAbyba = False
    # PromoCodeShop = False
    # HaveDollarInBedsideTable = 0
    # HaveMoneyInBedsideTable = 0
    # PromoCodeStop_Orend_3_House = False
    # PromoCodeMining_1House_lox_ = False
    # PromoCodeStooopOrend_One_Room = False
    # MemeBedsideTable = False
    # PinCode = 0
    # MoneyOnBankCard = 0
    # PromoDontHaveMoneyShop = False
    # MoneyOnDeposit = 0
    # TempDeposit = 0
    # AfterIdDeposit = ''
    # AllTaxes = 0
    # TempTaxes = 0
    # AfterIdTaxes = ''
    # Taxes1Room = 0
    # Taxes2Room = 0
    # Taxes3Room = 0
    # Taxes1House = 0
    # Taxes2House = 0
    # Taxes3House = 0
    # Have1Room = False
    # Have2Room = False
    # Have3Room = False
    # Have1House = False
    # Have2House = False
    # Have3House = False
    # HaveBedSideTable = False
    # HaveStuffing = 0
    # HaveSpaghetti = 0
    # HaveCookSpaghetti = 0
    # HaveCutlet = 0
    # HaveSpaghettiWithCutlet = 0

def DefUpload1File(v):
    global money,temp,after_id,TempOrend1Room,AfterIdOrend1Room,Orend1RoomChange,TempOrend2Room
    global AfterIdOrend2Room,Orend2RoomChange,Orend3RoomChange,TempOrend3Room,AfterIdOrend3Room,Orend1HouseChange
    global TempOrend1House,AfterIdOrend1House,VideoCard1House ,MainingIn1House,MainingSetUp1House,FrameForMining1House
    global CanGoToBasement1Home,TempMaining1House,AfterIdMaining1House,Crypto1House,Maining1HouseChange,VideoCard2House
    global FrameForMining2House,MainingIn2House,MainingSetUp2House,Orend2HouseChange,TempOrend2House,AfterIdOrend2House
    global Maining2HouseChange,TempMaining2House,Crypto2House,Orend3HouseChange,VideoCard3House,FrameForMining3House
    global MainingIn3House,MainingSetUp3House,Maining3HouseChange,TempOrend3House,AfterIdOrend3House,Crypto3House
    global TempMaining3House,AfterIdMaining3House,TempCourseChangeShopCoins,AfterIdCourseChangeShopCoins,CoursShopCoins
    global HaveShopCoins,HaveDollar,TempCourseChangeDollar,AfterIdCourseChangeDollar,CoursDollar,HaveSausage,HaveCheese
    global HaveThan,HaveFlour,HaveChocolate,HaveCola,HaveBread,HaveOil,HaveBowl,HaveSalt,HaveSalad,HaveTomato,HaveCucumber
    global HaveCutSausage,HaveCutCheese,HaveCutChocolate,HaveCutBread,HaveCutSalad,HaveCutTomato,HaveCutCucumber,HaveSalat
    global HaveButerbrod,PromoCodeAmogus,PromoCodeUpdate_dowN_BlockNot,PromoCodeSecret_Charity_SUS,PromoCodeAmogus2024
    global PromoCodeFrog,PromoCodeAbyba,PromoCodeShop,HaveDollarInBedsideTable,HaveMoneyInBedsideTable,PromoCodeStop_Orend_3_House
    global PromoCodeMining_1House_lox_,PromoCodeStooopOrend_One_Room,MemeBedsideTable,PinCode,MoneyOnBankCard,PromoDontHaveMoneyShop
    global MoneyOnDeposit,TempDeposit,AfterIdDeposit,AllTaxes,TempTaxes,AfterIdTaxes,Taxes1Room,Taxes2Room,Taxes3Room
    global Taxes1House,Taxes2House,Taxes3House,Have1Room,Have2Room,Have3Room,Have1House,Have2House,Have3House,HaveBedSideTable,HaveBankCard
    global HaveStuffing,HaveSpaghetti,HaveCookSpaghetti,HaveCutlet,HaveSpaghettiWithCutlet,NowSave
    with open('Txt_Shop/save/save_'+str(v)+'.txt','r') as file:
        try:
            money = float((file.readline()).replace('\n',''))
            TempOrend1Room = int((file.readline()).replace('\n', ''))
            AfterIdOrend1Room= str((file.readline()).replace('\n', ''))
            Orend1RoomChange= (file.readline()).replace('\n', '') == 'True'
            TempOrend2Room = int((file.readline()).replace('\n', ''))
            AfterIdOrend2Room = str((file.readline()).replace('\n', ''))
            Orend2RoomChange =(file.readline()).replace('\n', '') == 'True'
            Orend3RoomChange =(file.readline()).replace('\n', '') == 'True'
            TempOrend3Room = int((file.readline()).replace('\n', ''))
            AfterIdOrend3Room = str((file.readline()).replace('\n', ''))
            Orend1HouseChange =(file.readline()).replace('\n', '') == 'True'
            TempOrend1House = int((file.readline()).replace('\n', ''))
            AfterIdOrend1House = (file.readline()).replace('\n', '')
            VideoCard1House = (file.readline()).replace('\n', '') == 'True'
            MainingIn1House = (file.readline()).replace('\n', '') == 'True'
            MainingSetUp1House = (file.readline()).replace('\n', '') == 'True'
            FrameForMining1House = (file.readline()).replace('\n', '') == 'True'
            CanGoToBasement1Home = (file.readline()).replace('\n', '') == 'True'
            TempMaining1House = int((file.readline()).replace('\n', ''))
            AfterIdMaining1House = (file.readline()).replace('\n', '')
            Crypto1House = float((file.readline()).replace('\n', ''))
            Maining1HouseChange = (file.readline()).replace('\n', '') == 'True'
            VideoCard2House = (file.readline()).replace('\n', '') == 'True'
            FrameForMining2House = (file.readline()).replace('\n', '') == 'True'
            MainingIn2House = (file.readline()).replace('\n', '') == 'True'
            MainingSetUp2House = (file.readline()).replace('\n', '') == 'True'
            Orend2HouseChange = (file.readline()).replace('\n', '') == 'True'
            TempOrend2House = int((file.readline()).replace('\n', ''))
            AfterIdOrend2House = (file.readline()).replace('\n', '')
            Maining2HouseChange = (file.readline()).replace('\n', '') == 'True'
            TempMaining2House = int((file.readline()).replace('\n', ''))
            Crypto2House = float((file.readline()).replace('\n', ''))
            Orend3HouseChange = (file.readline()).replace('\n', '') == 'True'
            VideoCard3House = (file.readline()).replace('\n', '') == 'True'
            FrameForMining3House = (file.readline()).replace('\n', '') == 'True'
            MainingIn3House = (file.readline()).replace('\n', '') == 'True'
            MainingSetUp3House = (file.readline()).replace('\n', '') == 'True'
            Maining3HouseChange = (file.readline()).replace('\n', '') == 'True'
            TempOrend3House = int((file.readline()).replace('\n', ''))
            AfterIdOrend3House = (file.readline()).replace('\n', '')
            Crypto3House = float((file.readline()).replace('\n', ''))
            TempMaining3House = int((file.readline()).replace('\n', ''))
            AfterIdMaining3House = (file.readline()).replace('\n', '')
            TempCourseChangeShopCoins = int((file.readline()).replace('\n', ''))
            AfterIdCourseChangeShopCoins = (file.readline()).replace('\n', '')
            CoursShopCoins = int((file.readline()).replace('\n', ''))
            HaveShopCoins = float((file.readline()).replace('\n', ''))
            HaveDollar = float((file.readline()).replace('\n', ''))
            TempCourseChangeDollar = int((file.readline()).replace('\n', ''))
            AfterIdCourseChangeDollar = str((file.readline()).replace('\n', ''))
            CoursDollar = float((file.readline()).replace('\n', ''))
            HaveSausage = int((file.readline()).replace('\n', ''))
            HaveCheese = int((file.readline()).replace('\n', ''))
            HaveThan = int((file.readline()).replace('\n', ''))
            HaveFlour = int((file.readline()).replace('\n', ''))
            HaveChocolate = int((file.readline()).replace('\n', ''))
            HaveCola = int((file.readline()).replace('\n', ''))
            HaveBread = int((file.readline()).replace('\n', ''))
            HaveOil = int((file.readline()).replace('\n', ''))
            HaveBowl = int((file.readline()).replace('\n', ''))
            HaveSalt = int((file.readline()).replace('\n', ''))
            HaveSalad = int((file.readline()).replace('\n', ''))
            HaveTomato = int((file.readline()).replace('\n', ''))
            HaveCucumber = int((file.readline()).replace('\n', ''))
            HaveCutSausage = int((file.readline()).replace('\n', ''))
            HaveCutCheese = int((file.readline()).replace('\n', ''))
            HaveCutChocolate = int((file.readline()).replace('\n', ''))
            HaveCutBread = int((file.readline()).replace('\n', ''))
            HaveCutSalad = int((file.readline()).replace('\n', ''))
            HaveCutTomato = int((file.readline()).replace('\n', ''))
            HaveCutCucumber = int((file.readline()).replace('\n', ''))
            HaveSalat = int((file.readline()).replace('\n', ''))
            HaveButerbrod = int((file.readline()).replace('\n', ''))
            PromoCodeAmogus = (file.readline()).replace('\n', '') == 'True'
            PromoCodeUpdate_dowN_BlockNot = (file.readline()).replace('\n', '') == 'True'
            PromoCodeSecret_Charity_SUS = (file.readline()).replace('\n', '') == 'True'
            PromoCodeAmogus2024 = (file.readline()).replace('\n', '') == 'True'
            PromoCodeFrog = (file.readline()).replace('\n', '') == 'True'
            PromoCodeAbyba = (file.readline()).replace('\n', '') == 'True'
            PromoCodeShop = (file.readline()).replace('\n', '') == 'True'
            HaveDollarInBedsideTable = int((file.readline()).replace('\n', ''))
            HaveMoneyInBedsideTable = int((file.readline()).replace('\n', ''))
            PromoCodeStop_Orend_3_House = (file.readline()).replace('\n', '') == 'True'
            PromoCodeMining_1House_lox_ = (file.readline()).replace('\n', '') == 'True'
            PromoCodeStooopOrend_One_Room =(file.readline()).replace('\n', '') == 'True'
            MemeBedsideTable = (file.readline()).replace('\n', '') == 'True'
            PinCode = int((file.readline()).replace('\n', ''))
            MoneyOnBankCard = float((file.readline()).replace('\n', ''))
            PromoDontHaveMoneyShop = (file.readline()).replace('\n', '') == 'True'
            MoneyOnDeposit = float((file.readline()).replace('\n', ''))
            TempDeposit = int((file.readline()).replace('\n', ''))
            AfterIdDeposit = (file.readline()).replace('\n', '')
            AllTaxes = int((file.readline()).replace('\n', ''))
            TempTaxes = int((file.readline()).replace('\n', ''))
            AfterIdTaxes = (file.readline()).replace('\n', '')
            Taxes1Room = int((file.readline()).replace('\n', ''))
            Taxes2Room = int((file.readline()).replace('\n', ''))
            Taxes3Room = int((file.readline()).replace('\n', ''))
            Taxes1House = int((file.readline()).replace('\n', ''))
            Taxes2House = int((file.readline()).replace('\n', ''))
            Taxes3House = int((file.readline()).replace('\n', ''))
            Have1Room = (file.readline()).replace('\n', '') == 'True'
            Have2Room = (file.readline()).replace('\n', '') == 'True'
            Have3Room = (file.readline()).replace('\n', '') == 'True'
            Have1House =(file.readline()).replace('\n', '') == 'True'
            Have2House =(file.readline()).replace('\n', '') == 'True'
            Have3House =(file.readline()).replace('\n', '') == 'True'
            HaveBedSideTable =(file.readline()).replace('\n', '') == 'True'
            HaveBankCard =(file.readline()).replace('\n','')=='True'
            HaveStuffing = int((file.readline()).replace('\n', ''))
            HaveSpaghetti= int((file.readline()).replace('\n', ''))
            HaveCookSpaghetti= int((file.readline()).replace('\n', ''))
            HaveCutlet= int((file.readline()).replace('\n', ''))
            HaveSpaghettiWithCutlet= int((file.readline()).replace('\n', ''))
        except Exception as inst:
            pass
            # print(type(inst))    # the exception type
            # print(inst.args)     # arguments stored in .args
            # print(inst)
            # print('Eror Upload Save')
    # Save1 = open('Txt_Shop/save/save_'+str(v)+'.txt', 'w')
    # Save1.write('')
    # Save1.close()
    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
    if Orend1RoomChange:
        DeftickOrend1Room()
    if Orend2RoomChange:
        DeftickOrend2Room()
    if Orend3RoomChange:
        DeftickOrend3Room()
    if Orend1HouseChange:
        DeftickOrend1House()
    if Orend2HouseChange:
        DeftickOrend2House()
    if Orend3HouseChange:
        DeftickOrend3House()
    if FrameForMining1House and MainingIn1House and MainingSetUp1House and VideoCard1House:
        DeftickMining1House()
    if FrameForMining2House and MainingIn2House and MainingSetUp2House and VideoCard2House:
        DeftickMining2House()
    if FrameForMining3House and MainingIn3House and MainingSetUp3House and VideoCard3House:
        DeftickMining3House()
    btnAddSave.place_forget()
    LabelSave1.place_forget()
    btnSaveIn1File.place_forget()
    btnUploadFrom1File.place_forget()
    btnDeleat1File.place_forget()
    LabelSave2.place_forget()
    btnSaveIn2File.place_forget()
    btnUploadFrom2File.place_forget()
    btnDeleat2File.place_forget()
    LabelSave3.place_forget()
    btnSaveIn3File.place_forget()
    btnUploadFrom3File.place_forget()
    btnDeleat3File.place_forget()
    LabelSave4.place_forget()
    btnSaveIn4File.place_forget()
    btnUploadFrom4File.place_forget()
    btnDeleat4File.place_forget()
    Lines1.place_forget()
    Lines2.place_forget()
    Lines3.place_forget()
    Enter()
    NowSave=v
    print(NowSave)
    messagebox.askokcancel('Успішно','Ви успішно завантажили своє збереження, але в тому файлі більше нема його, тому не забудьте зберегтися!')


def DelSave(v):
    if messagebox.askokcancel('Підтвердження','Ви точно хочете видалити це збереження? Цю дію неможна скасувати в майбутньому'):
        Save = open('Txt_Shop/save/save_'+str(v)+'.txt', 'w')
        Save.write('')
        Save.close()
        messagebox.askokcancel('Успішно!','Файл з данними успішно почищенний!')


def DefListHowCookIngredient():
    CookButerbrod.place_forget()
    CookSalat.place_forget()
    btnCookIngredient.place_forget()
    btnCut.place(x=0,y=22)
    btnBoil.place(x=155,y=22)
    btnFry.place(x=0,y=100)
    btnCookSpaghettiWithCutlet.place_forget()


def FryStuffing():
    global HaveCutlet, HaveStuffing
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreFryStuffing)
    else:
        if HaveStuffing >= 1 and HaveBowl>=1:
            HaveCutlet = HaveCutlet +1
            HaveStuffing = HaveStuffing - 1
            messagebox.askokcancel("Дія виконана", "До ваших страв додана котлета")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару, або немає миски')


def DefEnterMoreFryStuffing():
    global HaveStuffing, HaveCutlet
    if int(BuyMoreProductEntry.get()) <= HaveStuffing:
        HaveStuffing = HaveStuffing - int(BuyMoreProductEntry.get())
        HaveCutlet = HaveCutlet+int(BuyMoreProductEntry.get())
        BuyMoreProduct0.place_forget()
        BuyMoreProduct1.place_forget()
        BuyMoreProduct2.place_forget()
        BuyMoreProduct3.place_forget()
        BuyMoreProduct4.place_forget()
        BuyMoreProduct5.place_forget()
        BuyMoreProduct6.place_forget()
        BuyMoreProduct7.place_forget()
        BuyMoreProduct8.place_forget()
        BuyMoreProduct9.place_forget()
        BuyMoreProductEntr1.place_forget()
        BuyMoreProductClear1.place_forget()
        BuyMoreProductEntry.place_forget()
        btnCut.place(x=0, y=22)
        btnBoil.place(x=155, y=22)
        btnFry.place(x=0, y=100)
        btnGoHome.place(x=80, y=330)
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви посмажили ' + BuyMoreProductEntry.get() + ' пачок фаршу і отримали ' +
                                   BuyMoreProductEntry.get() + ' котлет')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає пачок фаршу. Щоб вона з'явилися купіть їх в магазині.")


def BoilSpaghetti():
    global HaveCookSpaghetti, HaveSpaghetti
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете порізати 1 продукт чи декілка(Так-1 продукт Ні-декілька продуктів)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreBoilSpaghetti)
    else:
        if HaveSpaghetti >= 1 and HaveBowl>=1:
            HaveCookSpaghetti = HaveCookSpaghetti +1
            HaveSpaghetti = HaveSpaghetti - 1
            messagebox.askokcancel("Дія виконана", "До ваших страв додані спагетті")
        else:
            messagebox.askokcancel("Ой, сталася помилка.", 'У вас немає цього товару, або немає миски')


def DefEnterMoreBoilSpaghetti():
    global HaveSpaghetti, HaveCookSpaghetti
    if int(BuyMoreProductEntry.get()) <= HaveSpaghetti:
        HaveSpaghetti = HaveSpaghetti - int(BuyMoreProductEntry.get())
        HaveCookSpaghetti = HaveCookSpaghetti+int(BuyMoreProductEntry.get())
        BuyMoreProduct0.place_forget()
        BuyMoreProduct1.place_forget()
        BuyMoreProduct2.place_forget()
        BuyMoreProduct3.place_forget()
        BuyMoreProduct4.place_forget()
        BuyMoreProduct5.place_forget()
        BuyMoreProduct6.place_forget()
        BuyMoreProduct7.place_forget()
        BuyMoreProduct8.place_forget()
        BuyMoreProduct9.place_forget()
        BuyMoreProductEntr1.place_forget()
        BuyMoreProductClear1.place_forget()
        BuyMoreProductEntry.place_forget()
        btnCut.place(x=0, y=22)
        btnBoil.place(x=155, y=22)
        btnFry.place(x=0, y=100)
        btnGoHome.place(x=80, y=330)
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви зварили ' + BuyMoreProductEntry.get() + ' пачок спагеті і отримали ' +
                                   BuyMoreProductEntry.get() + ' порцій спагетті')
        return
    else:
        messagebox.askokcancel("Ой, сталася помилка.",
                               "Мабуть у вас невистачає пачок фаршу. Щоб вона з'явилися купіть їх в магазині.")



def DefCookSpaghettiWithCutlet():
    global HaveCutCheese, HaveCookSpaghetti, HaveCutlet,HaveSpaghettiWithCutlet
    #if HaveCutSausage >= 2 and HaveCutBread >= 1 and HaveCutCheese>=2:
    if (messagebox.askyesno(title="Скільки приготувати",
                            message="Ви хочете приготувати 1 страву чи декілка(Так-1 страву Ні-декілька страв)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSpaghettiWithCutlet)
    else:
        if HaveCutlet >= 1 and HaveCookSpaghetti >= 1:
            HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet + 1
            HaveCutlet = HaveCutlet - 1
            HaveCookSpaghetti = HaveCookSpaghetti - 1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на спагеті з котлетою"
                                                          " вам потрібен 1 котлета і 1 порція спагеті)")




def DefEnterMoreSpaghettiWithCutlet():
        global HaveCutlet,HaveCookSpaghetti, HaveSpaghettiWithCutlet
        if HaveCutlet >= int(BuyMoreProductEntry.get())  and HaveCookSpaghetti >= int(BuyMoreProductEntry.get()):
            HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet + int(BuyMoreProductEntry.get())
            HaveCutlet = HaveCutlet - int(BuyMoreProductEntry.get())
            HaveCookSpaghetti = HaveCookSpaghetti - int(BuyMoreProductEntry.get())
            DefHideMoreProduct()
            GoHome()
            messagebox.askokcancel('Операція пройша успішно',
                                   'Ви приготували ' + BuyMoreProductEntry.get() + ' спагеті з котлетою ')
            return
        else:
            messagebox.askokcancel("Ой, сталася помилка.",
                                   "Мабуть у вас немає продуктів. Щоб вони з'явилися сходіть в магазин та купіть їх.(на бутерброд вам потрібен 2 шматка ковбаси, 2 шматка сира і 1 шматок хліба)")



def DefSpaghettiWithCutletSell():
    global money, HaveSpaghettiWithCutlet, MoneyOnBankCard
    if (messagebox.askyesno(title="Скільки продуктів",
                            message="Ви хочете продати 1 бутерброд чи декілка(Так-1, Ні-декілька)")) == False:
        BtnBuyMoreProduct_And_HideAllBtnShop()
        BuyMoreProductEntr1.config(command=DefEnterMoreSpaghettiWithCutletSell)
    else:
        if PayInMarket =='Money':
            if HaveSpaghettiWithCutlet >= 1:
                if messagebox.askokcancel("Підтвердження", "Ви можете продати спагетті з котлетою. Ви цього хочете?"):
                    money = int(money) + 280
                    HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet -1
                    LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
                    return
        if PayInMarket=='BankCard' and ProofPinCode==PinCode:
            if HaveSpaghettiWithCutlet >= 1:
                if messagebox.askokcancel("Підтвердження", "Ви можете продати спагетті з котлетою. Ви цього хочете?"):
                    MoneyOnBankCard = int(MoneyOnBankCard) + 280
                    HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet -1
        else:
            messagebox.askokcancel("Ой, сталася помилка.","У вас немає спагетті з котлетою або ви не підтвердили Pin-Code")
def DefEnterMoreSpaghettiWithCutletSell():
    global money, HaveSpaghettiWithCutlet, MoneyOnBankCard
    if HaveSpaghettiWithCutlet >= int(BuyMoreProductEntry.get()) and PayInMarket=='Money':
        money = money + (int(BuyMoreProductEntry.get()) * 280)
        HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet - int(BuyMoreProductEntry.get())
        LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' спагет з котлетами ' + str(
                                   int(BuyMoreProductEntry.get()) * 280) + ' грн')
        return
    else:
        messagebox.askokcancel('Помилка', 'У вас немає стільки товару(((')
    if HaveSpaghettiWithCutlet>=int(BuyMoreProductEntry.get()) and PayInMarket=='BankCard' and ProofPinCode==PinCode:
        MoneyOnBankCard = MoneyOnBankCard + (int(BuyMoreProductEntry.get()) * 280)
        HaveSpaghettiWithCutlet = HaveSpaghettiWithCutlet - int(BuyMoreProductEntry.get())
        GoMarket()
        DefHideMoreProduct()
        messagebox.askokcancel('Операція пройша успішно',
                               'Ви продали ' + BuyMoreProductEntry.get() + ' спагет з котлетами ' + str(
                                   int(BuyMoreProductEntry.get()) * 280) + ' грн')
    else:
        messagebox.askokcancel('Помилка','У вас немає стільки товару, або ви не підтвердили Pin-code')




def DefNextListMainMenu3():
    ExchangeCurrency.place_forget()
    PromoCode.place_forget()
    WhatUpdate.place_forget()
    Charity.place_forget()
    btnBank.place_forget()
    btnSaveSaves.place_forget()
    btnNextListMeinMenu3.place_forget()
    btnWorkCourses.place_forget()
    btnBusinessCourses.place_forget()
    BackListMainMenu.config(command=DefNextListMeinMenu)
    btnClicker.place(x=0, y=22)
    btnWork.place(x=160, y=22)
    btnBusiness.place(x=0, y=100)
    btnCourses.place(x=160, y=100)
    btnGoSeaBattle.place(x=0, y=180)
    btnBackyard.place(x=160, y=180)
    btnGardeningShop.place(x=160, y=260)
    # btnNextListMeinMenu3.place(x=0, y=260)



def GoClicker():
    btnClicker.place_forget()
    BackListMainMenu.place_forget()
    Reset.place_forget()
    btnStarCoinTap.place(x=90,y=100)
    BackTo3ListMainMenu.place(x=2, y=340)
    LabelStarCoinInApp.place(x=80,y=50)
    btnWithdrawStarCoin.place(x=73,y=255)
    btnWork.place_forget()
    btnBusiness.place_forget()
    btnCourses.place_forget()
    btnGoSeaBattle.place_forget()
    btnBackyard.place_forget()
    btnGardeningShop.place_forget()
    if UpgradeStarCoin!=0.1:
        btnUpgradeStarCoin.place(x=70,y=280)
    else:
        btnUpgradeStarCoin.place_forget()

def DefBackTo3ListMainMenu():
    btnClicker.place(x=0, y=22)
    BackListMainMenu.place(x=0, y=260)
    btnStarCoinTap.place_forget()
    LabelStarCoinInApp.place_forget()
    BackTo3ListMainMenu.place_forget()
    Reset.place(x=2, y=340)
    btnUpgradeStarCoin.place_forget()
    btnWithdrawStarCoin.place_forget()
    btnBusinessCourses.place_forget()
    btnWorkCourses.place_forget()
    btnGoSeaBattle.place(x=0, y=180)
    btnWork.place(x=160, y=22)
    btnBusiness.place(x=0, y=100)
    btnCourses.place(x=160, y=100)
    btnBackyard.place(x=160, y=180)
    btnGardeningShop.place(x=160, y=260)
    
def ClickedStarCoin():
    global HaveStarCoinInApp
    HaveStarCoinInApp+=UpgradeStarCoin
    LabelStarCoinInApp.config(text="StarCoin's:"+format(HaveStarCoinInApp, '.2f'))


def UpgradeStarCoin1():
    global HaveStarCoinInApp, UpgradeStarCoin, btnUpgradeStarCoin
    if HaveStarCoinInApp>=9.99:
        UpgradeStarCoin = 0.02
        btnUpgradeStarCoin.config(text='Прокачати монету, щоб \n вона давала 0.03 за клік\nціна:30 StarCoin-ів в додатку',command=UpgradeStarCoin2)
        HaveStarCoinInApp = HaveStarCoinInApp-10
        LabelStarCoinInApp.config(text="StarCoin's:" + format(HaveStarCoinInApp, '.2f'))
        messagebox.showinfo("Повідомлення", "Ви успішно купили це покращення")
    else:
        messagebox.showerror("Помилка", "У вас немає стільки StarCoin-ів")



def UpgradeStarCoin2():
    global HaveStarCoinInApp, UpgradeStarCoin, btnUpgradeStarCoin
    if HaveStarCoinInApp>=29.99:
        UpgradeStarCoin = 0.03
        btnUpgradeStarCoin.config(text='Прокачати монету, щоб \n вона давала 0.05 за клік\nціна:70 StarCoin-ів в додатку',command=UpgradeStarCoin3)
        HaveStarCoinInApp = HaveStarCoinInApp-30
        LabelStarCoinInApp.config(text="StarCoin's:" + format(HaveStarCoinInApp, '.2f'))
        messagebox.showinfo("Повідомлення", "Ви успішно купили це покращення")
    else:
        messagebox.showerror("Помилка", "У вас немає стільки StarCoin-ів")


def UpgradeStarCoin3():
    global HaveStarCoinInApp, UpgradeStarCoin, btnUpgradeStarCoin
    if HaveStarCoinInApp>=70:
        UpgradeStarCoin = 0.05
        btnUpgradeStarCoin.config(text='Прокачати монету, щоб \n вона давала 0.1 за клік\nціна:300 StarCoin-ів в додатку',command=UpgradeStarCoin4)
        HaveStarCoinInApp = HaveStarCoinInApp-70
        LabelStarCoinInApp.config(text="StarCoin's:" + format(HaveStarCoinInApp, '.2f'))
        messagebox.showinfo("Повідомлення", "Ви успішно купили це покращення")
    else:
        messagebox.showerror("Помилка", "У вас немає стільки StarCoin-ів")


def UpgradeStarCoin4():
    global HaveStarCoinInApp, UpgradeStarCoin, btnUpgradeStarCoin
    if HaveStarCoinInApp>=300:
        UpgradeStarCoin = 0.1
        btnUpgradeStarCoin.place_forget()
        HaveStarCoinInApp = HaveStarCoinInApp-300
        LabelStarCoinInApp.config(text="StarCoin's:" + format(HaveStarCoinInApp, '.2f'))
        messagebox.showinfo("Повідомлення", "Ви успішно купили це покращення")
    else:
        messagebox.showerror("Помилка", "У вас немає стільки StarCoin-ів")



def tickCourseChangeStarCoin():
    global TempCourseChangeStarCoin, AfterIdCourseChangeStarCoin, sCourseChangeStarCoin, CoursStarCoin, UpOrDown, MovementStarCoin
    AfterIdCourseChangeStarCoin = root.after(45454,tickCourseChangeStarCoin)
    TempCourseChangeStarCoin +=1
    if TempCourseChangeStarCoin == 2:
        #print('aboba')
        TempCourseChangeStarCoin = 1
        UpOrDown = random.randint(1,2) # Якщо 1 то -      #Якщо 2 то +
        #print(UpOrDown)
        MovementStarCoin = random.randint(1,50)
        #print(MovementShopCoins)
        if UpOrDown == 1:
            CoursStarCoin = CoursStarCoin - (MovementStarCoin/100)
        else:
            CoursStarCoin = CoursStarCoin + (MovementStarCoin/100)
        if CoursStarCoin<=3:
            CoursStarCoin = CoursStarCoin + (MovementStarCoin/100)
        LabelCoursStarCoin.config(text='StarCoin - ' + format(CoursStarCoin, '.2f')+' грн', bg='white')



def DefSellStarCoin():
    btnSellStarCoin.place_forget()
    btnBuyStarCoin.place_forget()
    HowWantSellStarCoin.place(x=155, y=250)
    LabelHowWantSellStarCoin.place(x=120, y=230)
    EnterForSellStarCoin.place(x=255, y=245)


def DefBuyStarCoin():
    btnSellStarCoin.place_forget()
    btnBuyStarCoin.place_forget()
    HowWantBuyStarCoin.place(x=155, y=250)
    LabelHowWantBuyStarCoin.place(x=120, y=230)
    EnterForBuyStarCoin.place(x=255, y=245)


def DefEnterForBuyStarCoin():
    global money, WantBuyStarCoin, SumBuyStarCoin, HaveStarCoin, MoneyOnBankCard
    if PayInExchangeCenter =='Money':
        strWantBuyStarCoin = HowWantBuyStarCoin.get()
        WantBuyStarCoin = int(strWantBuyStarCoin)
        SumBuyStarCoin = WantBuyStarCoin*CoursStarCoin
        if SumBuyStarCoin <= money and WantBuyStarCoin>0:
            money = money - SumBuyStarCoin
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            btnSellStarCoin.place(x=190, y=224)
            btnBuyStarCoin.place(x=190, y=251)
            HaveStarCoin = HaveStarCoin + WantBuyStarCoin
            EntryHaveStarCoin.config(state='normal')
            EntryHaveStarCoin.delete(0, END)
            EntryHaveStarCoin.insert(0, str(HaveStarCoin))
            EntryHaveStarCoin.config(state='disabled')
            EnterForBuyStarCoin.place_forget()
            LabelHowWantBuyStarCoin.place_forget()
            HowWantBuyStarCoin.place_forget()
        else:
            messagebox.showerror('Сталася помилка','Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі StarCoins')
    if PayInExchangeCenter == 'BankCard' and ProofPinCode == PinCode:
        strWantBuyStarCoin = HowWantBuyStarCoin.get()
        WantBuyStarCoin = int(strWantBuyStarCoin)
        SumBuyStarCoin = WantBuyStarCoin * CoursStarCoin
        if SumBuyStarCoin <= MoneyOnBankCard and WantBuyStarCoin > 0:
            MoneyOnBankCard = MoneyOnBankCard - SumBuyStarCoin
            btnSellStarCoin.place(x=190, y=224)
            btnBuyStarCoin.place(x=190, y=251)
            HaveStarCoin = HaveStarCoin + WantBuyStarCoin
            EntryHaveStarCoin.config(state='normal')
            EntryHaveStarCoin.delete(0, END)
            EntryHaveStarCoin.insert(0, str(HaveStarCoin))
            EntryHaveStarCoin.config(state='disabled')
            EnterForBuyStarCoin.place_forget()
            LabelHowWantBuyStarCoin.place_forget()
            HowWantBuyStarCoin.place_forget()
        else:
            messagebox.showerror('Сталася помилка',
                                   'Ой, сталася помилка. Або у вас невистача грошей або ви ввели некоректну сумму купівлі StarCoins')

def DefEnterForSellStarCoin():
    global ReadySellStarCoin, money, HaveStarCoin, MoneyOnBankCard
    if PayInExchangeCenter =='Money':
        StrReadySellStarCoin = HowWantSellStarCoin.get()
        ReadySellStarCoin = int(StrReadySellStarCoin)
        if (ReadySellStarCoin>0) and (ReadySellStarCoin <= HaveStarCoin):
            money = money + (ReadySellStarCoin*CoursStarCoin)
            LeyblMoney['text'] = 'У тебе ' + format(money, '.2f') + ' гривень'
            messagebox.showinfo('Підсумок','За ' + StrReadySellStarCoin + ' StarCoins ви отримали '+ str(ReadySellStarCoin*CoursStarCoin) + ' гривень')
            HaveStarCoin = HaveStarCoin - ReadySellStarCoin
            EntryHaveStarCoin.config(state='normal')
            EntryHaveStarCoin.delete(0, END)
            EntryHaveStarCoin.insert(0, str(HaveStarCoin))
            EntryHaveStarCoin.config(state='disabled')
            HowWantSellStarCoin.place_forget()
            LabelHowWantSellStarCoin.place_forget()
            EnterForSellStarCoin.place_forget()
            btnSellStarCoin.place(x=190, y=224)
            btnBuyStarCoin.place(x=190, y=251)
        else:
            messagebox.showerror('Помилка', 'Сталася помилка, або у вас немає стільки монет або ви ввели некоректну кількість монет')
            HowWantSellStarCoin.place_forget()
            LabelHowWantSellStarCoin.place_forget()
            EnterForSellStarCoin.place_forget()
            btnSellStarCoin.place(x=190, y=224)
            btnBuyStarCoin.place(x=190, y=251)
    if PayInExchangeCenter =='BankCard' and ProofPinCode==PinCode:
        StrReadyStarCoin = HowWantSellStarCoin.get()
        ReadySellStarCoin = int(StrReadySellStarCoin)
        if ReadySellStarCoin > 0 and ReadySellStarCoin <= HaveStarCoin:
            MoneyOnBankCard = MoneyOnBankCard + (ReadySellStarCoin * CoursStarCoin)
            messagebox.showinfo('Підсумок', 'За ' + StrReadySellStarCoin + ' ShopCoins ви отримали ' + str(ReadySellStarCoin * CoursStarCoin) + ' гривень')
            HaveStarCoin = HaveStarCoin - ReadySellStarCoin
            EntryHaveStarCoin.config(state='normal')
            EntryHaveStarCoin.delete(0, END)
            EntryHaveStarCoin.insert(0, str(HaveShopCoins))
            EntryHaveStarCoin.config(state='disabled')
            HowWantSellStarCoin.place_forget()
            LabelHowWantSellStarCoin.place_forget()
            EnterForSellStarCoin.place_forget()
            btnSellStarCoin.place(x=190, y=105)
            btnBuyStarCoin.place(x=190, y=132)
    print(HaveStarCoin)


def WithdrawStarCoin():
    global HaveStarCoin, HaveStarCoinInApp
    HaveStarCoin += HaveStarCoinInApp
    HaveStarCoinInApp = 0
    LabelStarCoinInApp.config(text="StarCoin's:" + format(HaveStarCoinInApp, '.2f'))
    messagebox.showinfo('Успішно','Ваші StarCoin-и успішно виведенні на біржу')



def GoCourses():
    btnWork.place_forget()
    btnBusiness.place_forget()
    btnCourses.place_forget()
    btnClicker.place_forget()
    BackListMainMenu.place_forget()
    Reset.place_forget()
    btnGoSeaBattle.place_forget()
    BackTo3ListMainMenu.place(x=2, y=340)
    btnWorkCourses.place(x=80,y=105)
    btnBusinessCourses.place(x=80, y=175)
    btnBackyard.place_forget()
    btnGardeningShop.place_forget()


def defStartSeaBattle():
    os.startfile('E:\PycharmProjects\pythonProject\pythonProject1\output\Sea_Battle\SeaBattle.exe')



#Канвас - дозволяє малювати на екрані
canvas = Canvas(root, height=300, width=250)
canvas.pack()


#Фрейм - Полотно програми
frame = Frame(root, bg='white')
frame.place(relheight=1, relwidth=1)

tickTaxes()

#Текст
#Текст який розтагований на початку програми

LeyblMoney = Label(text='', width=42, bg='gray', font='Arial 10')
LeyblMoney.place(x=-5, y=0)

WelcomeTitle = Label(frame, text='Привіт!\nЦе гра магазин. Щоб почати натисни на\n кнопку Start щоб подивитися подробиці\n'
                                 ' натисни на кнопку Help',  height=15, width=40, font='April 11',bg='white')
WelcomeTitle.place(x=-35, y=20)
#А цей з'являється коли натискаєщ на кнопку Help
HelpLabel = Label(frame, text="Це гра магазин, тут ти можеш:\nходити до магазину де ти можеш\nкупити ковбасу,сир і т.д. "
                              "З хліба,\nковбаси і сира ти зможеш\nприготувати бутерброд і продати\n або з'їсти його. "
                              "Також тут є\nінші способи заробляти гроші.\nНаприклад: ти можеш майніти\nбіткоін, розводити"
                              " господарство,\nпокупати товар дешевше і продавати\nдороще і ще багато іншого. \n "
                              "Готов почати свій шлях?\n(Деяких предметів нема але\nвони обов'язково будуть)",
                  height=15, width=40, font='April 13',bg='white')
HelpLabel.place(x=440, y=20)
#Початок гри
QuestionMoney = Label(frame, text='Скільки у тебе грошей?', height=10, width=30, font='April 15', bg='white')
QuestionMoney.place(x=100, y=1000)
#Що будеш робити вдома
DoInHome = Label(frame, text='Що будеш робити вдома?', height=10, width=30, font='April 15', bg='white')
#Лейбл для сну
LabelSleep = Label(frame, width=10, font=('Comic Sans MS', 25), text='00:00', bg = 'white')
#Ви проспали
TimeSleep = Label(frame, text='Ви проспали:', height=3, width=10, font='April 15', bg='white')
#Вивід списку покупок
LabelBuy = Label(frame,text='Ваші продукти:', height=3, width=18, font=('Comic Sans MS', 15), bg='white')
#Поле з твоїми продуктами
#############
LabelListCook = Label(frame, text='----',bg='white', font='Arial 15')
##################
LabelCook = Label(frame, text='Ваші страви:', height=1, width=18, font=('Comic Sans MS', 15), bg='white')
#####################
LabelBeforeEnter = Label(frame, text='Привіт, це фінальний текст \n перед початком гри. З самого \n початку у тебе буде '
                                     '1000 гривень.\n З цієї 1000 ти повинен зробити \n мільйони!!!! Вдачі :)',
                         height=15, width=40, font='April 11',bg='white')
##################
ScoreOponent = Label(frame, text='Супротивник', height=10, width=18, font='April 15', bg='white' )
##################
ScoreYou = Label(frame, text='У вас:', height=1, width=15, font='April 15', bg='white' )
ScoreYou.place(x=650, y=2100)
Rate = Label(frame, text='Зробіть ставку', height=10, width=18, font='April 15', bg='white' )
###########################
LabelOrend = Label(frame,width=18, font='April 20', bg='white',text='0:0:0',height=1)
###################################
LabelBeforeOrend = Label(frame,width=40,height=14, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити(ви і до\n цього не могли, попуски) і \n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 1200 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди"\n і за кожну хвилину яка пройшла')
###############################################
LabelOrend2Room = Label(frame,width=18, font='April 20', bg='white',text='0:0:0',height=1)
###################################
LabelBeforeOrend2Room = Label(frame,width=40,height=14, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити(ви і до\n цього не могли, попуски) і \n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 1800 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди"\n і за кожну хвилину яка пройшла.')

LabelOrend3Room = Label(frame,width=18, font='April 20', bg='white',text='0:0:0', height=1)
###################################
LabelBeforeOrend3Room = Label(frame,width=40,height=14, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити(ви і до\n цього не могли, попуски) і \n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 2400 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди"\n і за кожну хвилину яка пройшла.')
####################################
LabelOrend1House = Label(frame,width=18, font='April 20', bg='white',text='0:0:0')
###################################
LabelBeforeOrend1House = Label(frame,width=40,height=13, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити але не зможете\n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 6000 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди".')
##################################
LabelMaining1House = Label(text='Ви ще можете заробляти гроші за допомогою \n майнингу. Щоб почати вам треба купити\n'
' відеокарти((20 штук.) за 280.000 грн), \n місце для цих карт (4 каркаси по \n 2.000 штука = 8.000 грн), Miner(30.000 грн) \n і '
' налаштувати 2.000 грн. Коли \n ви все купите ви зможете запустити ферму', height=10, width=40, font='April 10', bg='white')
LabelTaimerMaining1House = Label(frame,width=18, font='April 20', bg='white',text='0:0:0')
#LabelYourShopCoins = Label(frame, text='---', font='April 20', bg='white')
Lines1 = Label(text='------------------------------------------------------------', bg='white')
Lines2 = Label(text='------------------------------------------------------------', bg='white')
Lines3 = Label(text='------------------------------------------------------------', bg='white')
Lines4 = Label(text='------------------------------------------------------------', bg='white')
CourseCurrency = Label(text='1 ShopCoin - ' + str(CoursShopCoins) + ' грн', bg='white')
LabelHowWantSellShopCoins = Label(frame, text='Скільки хочете\nпродати ShopCoins?', bg='white')
LabelHowWantSellDollar = Label(frame, text='Скільки хочете\nпродати доларів?', bg='white')
LabelHowWantBuyDollar = Label(frame, text='Скільки хочете\nкупити доларів?', bg='white')
LabelMaining2House = Label(text='Ви ще можете заробляти гроші за допомогою \n майнингу. Щоб почати вам треба купити\n'
' відеокарти((30 штук.) за 420.000 грн), \n місце для цих карт (8 каркасів по \n 2.000 штука = 16.000 грн), Miner(30.000 грн) \n і '
' налаштувати 2.000 грн. Коли \n ви все купите ви зможете запустити ферму', height=10, width=40, font='April 10', bg='white')
LabelTaimerMaining2House = Label(frame,width=18, font='April 20', bg='white',text='00:00')

LabelOrend2House = Label(frame,width=18, font='April 20', bg='white',text='0:0:0')
###################################
LabelBeforeOrend2House = Label(frame,width=40,height=13, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити але не зможете \n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 9000 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди".')
##########################################################
LabelTaimerMaining3House = Label(frame,width=18, font='April 20', bg='white',text='0:0:0')

LabelOrend3House = Label(frame,width=18, font='April 20', bg='white',text='0:0:0')
###################################
LabelBeforeOrend3House = Label(frame,width=40,height=13, font='April 10', bg='white', text='Якщо у вас невистачає грошей ви'
' можете \n здати свою квартиру в оренду. Під час \n здачі ви зможете майнити але не зможете\n заходити '
'до самого дому.\n За кожну хвилину здачі ви будете \n отримувати 12000 гривень. Оплата буде \n приходити коли ви натисните \n кнопку'
' "завершити здачу оренди".')
LabelMaining3House = Label(text='Ви ще можете заробляти гроші за допомогою \n майнингу. Щоб почати вам треба купити\n'
' відеокарти((50 штук.) за 700.000 грн), \n місце для цих карт (13 каркасів по \n 2.000 штука = 26.000 грн), Miner(30.000 грн) \n і '
' налаштувати 2.000 грн. Коли \n ви все купите ви зможете запустити ферму', height=10, width=40, font='April 10', bg='white')
LabelHowWantBuyShopCoins = Label(frame, text='Скільки хочете\nкупити ShopCoins?', bg='white')
LabelCharity = Label(frame, text='Скільки хочете віддати\nна благодійність?', bg='white', font='Arial 17')
RateCharity = Label(frame, text='0', bg='white', font='Arial 15')
LabelPromoCode = Label(frame,text='Введіть промокод\n(його треба знайти або підібрати)', bg='white', font='Arial 15')
CourseCurrencyDollar = Label(text='1 Доллар - ' + str(CoursDollar) + ' грн', bg='white')
LabelInfoBedsideTable = Label(frame, text='Що будеш робити з тумбочкою?', font='April 15', bg='white')
LabelPutInBedsideTableDollar = Label(frame,text='Скільки покладете доларів?', font='April 15', bg='white')
LabelPutInBedsideTable = Label(frame,text='Скільки покладете гривень?', font='April 15', bg='white')
LabelInfoWhatInBedsideTable = Label(frame, text='В тумбочці:', bg='white',font='Aprill 15')
LabelTakeInBedsideTableDollar = Label(frame,text='Скільки візьмете доларів?', font='April 15', bg='white')
LabelTakeInBedsideTable = Label(frame,text='Скільки візьмете гривень?', font='April 15', bg='white')
LabelInBank = Label(frame,text='Що будете робити в банку?', font='April 15', bg='white')
LabelBankCard = Label(frame, text='Що будете робите з карткою?', font='April 15', bg='white')
LabelPayInExchangeCenter = Label(frame,text='Оплата на біржі:',font='April 11', bg='white')
LabelProofPinCode = Label(frame,text='Підтвердити Pin-code: ',font='April 11', bg='white')
LabelPayInShop = Label(frame,text='Оплата в магазині:',font='April 11', bg='white')
LabelPayInMarket = Label(frame,text='Отримання грошей на ринку:',font='April 9', bg='white')
LabelPayInCasino = Label(frame,text='Оплата в казино:',font='April 11', bg='white')
LabelPayInCharity = Label(frame,text='Оплата в благодійності:',font='April 11', bg='white')
LabelInDeposit = Label(frame,text='Що будете робити з депозитом?', font='April 14', bg='white')
LabelPutInDeposite = Label(frame,text='Скільки покладете на депозит?', font='April 14', bg='white')
LabelTakeFromDeposite = Label(frame,text='Скільки знімете з депозиту?', font='April 14', bg='white')
LabelInfoAboutDeposite = Label(frame,text='Якщо у вас є гроші і ви хочете їх кудись\nвкласти - покладіть на депозит. Кожну\n '
'хвилину вам на рахунок\n депозиту буде приходити 0.1% (6%\n за годину) від тієї суми яка у вас\n на депозиті. Мені,здається,'
'це вигідно', font='April 11', bg='white')
LabelInfoAboutTaxes = Label(text='Якщо у вас є нерухомість то вам\nавтоматично будуть нараховуватися\nподатки. Якщо сума '
'податків буде більше\nніж 25% ціни нерухомості - в вас її заберуть,\nтому не забувайте оплачувати податки!\n(за 1 хв нара'
'ховується 0,05% від\nвартості квартири/дому)', font='April 11', bg='white')
LabelPayTaxes = Label(frame, text='Оплата податків:',font='April 11', bg='white')
LabelHowNammetSave=Label(frame,text='Як назвете збереження?', font='April 14', bg='white')
LabelSave1 = Label(frame,text='Збереження:'+NameSave1, bg='white',font='April 11')
LabelSave2 = Label(frame,text='Збереження:'+NameSave2, bg='white',font='April 11')
LabelSave3 = Label(frame,text='Збереження:'+NameSave3, bg='white',font='April 11')
LabelSave4 = Label(frame,text='Збереження:'+NameSave4, bg='white',font='April 11')
LabelSave1.config(text='Збереження:'+NameSave1)
LabelSave2.config(text='Збереження:' + NameSave2)
LabelSave3.config(text='Збереження:' + NameSave3)
LabelSave4.config(text='Збереження:' + NameSave4)
LabelStarCoinInApp = Label(text="StarCoin's:"+str(HaveStarCoinInApp), bg='white',font='April 15')
LabelCoursStarCoin = Label(text='StarCoin - 30 грн', bg='white')
LabelHowWantSellStarCoin = Label(frame, text='Скільки хочете продати StarCoins?', bg='white')
LabelHowWantBuyStarCoin = Label(frame, text='Скільки хочете купити StarCoins?', bg='white')








#Кнопки
#Натискаєш на цю кнопку і повертаєшся в меню з кнопками Start і Help
ButtonBack = Button(root, text='Повернутися назад',command = ReturnToStart ,width=20, height=4 , font='April 10')
ButtonBack.place(x=350,y=350)
#При натисканні на кнопку гра починається
btnStart = Button(root, text='Start', width=16, height=4, command = Start, font='April 10')
btnStart.place(x=160, y=320)
#При натисканні на кнопку відправляє в меню допомоги
btnHelp = Button(root, text='Help', width=16, height=4, command = Help, font='April 10')
btnHelp.place(x=3, y=320)
#Кнопки для вводду скільки у тебе грошей
# btnmoney0 = Button(text='0', width=27, height=2, command = Zero)
# btnmoney1 = Button(text='1', width=8, height=2, command = One)
# btnmoney1.place(x= 1000, y= 1000)
# btnmoney2 = Button(text='2', width=8, height=2, command = Two)
# btnmoney2.place(x= 1000, y= 1000)
# btnmoney3 = Button(text='3', width=8, height=2, command = Thre)
# btnmoney3.place(x= 1000, y= 1000)
# btnmoney4 = Button(text='4', width=8, height=2, command = Four)
# btnmoney4.place(x= 1000, y= 1000)
# btnmoney5 = Button(text='5', width=8, height=2, command = Five)
# btnmoney5.place(x= 1000, y= 1000)
# btnmoney6 = Button(text='6', width=8, height=2, command = Six)
# btnmoney6.place(x=1000, y=1000)
# btnmoney7 = Button(text='7', width=8, height=2, command = Seven)
# btnmoney7.place(x= 1000, y= 1000)
# btnmoney8 = Button(text='8', width=8, height=2, command = Eight)
# btnmoney8.place(x= 1000, y= 1000)
# btnmoney9 = Button(text='9', width=8, height=2, command = Nine)
# btnmoney9.place(x= 1000, y= 1000)
# btnmoneyClear = Button(text='C', width=13, height=2, command = Clear)
# btnmoneyClear.place(x= 1000, y= 1000)
#Кнопка - вход до магазину
btnGoShop = Button(text='Вхід до магазину', width=17, height=4, command = GoShop, font='April 10')
btnGoShop.place(x=1000, y=1000)
#Кнопка - приход до дому
btnGoHome = Button(text='Додому', width=17, height=4, command = GoHome, font='April 10')
btnGoHome.place(x=1000, y=1000)
#Кнопка - піти на ринок
bthGoMarket = Button(text='На ринок', width=17, height=4, command = GoMarket, font='April 10')
bthGoMarket.place(x=1000, y=1000)
#Кнопка - дорого в казино
btnGoCasino = Button(text='В казино', width=17, height=4, command = GoKasino, font='April 10')
btnGoCasino.place(x=1000, y=1000)
#Кнопка почати все спочатку
Reset = Button(text='Розпочати все з початку(Нічого не збережиться\nі все пропаде якшо ви натиснете на цю кнопку)', fg='red', width=35, height=3, command =Back , font='April 10')
#Кнопка я не придумав
ListBuy = Button(text='Ваші товари', width=17, command = ListBuy ,height=4, font='April 10')
#Кнопка я не придумав
ListCook = Button(text='Ваші страви', width=17, height=4, command=ListCook,font='April 10')
#Кнопка я не придумав
Real_estate = Button(text='Нерухомість', width=17, height=4, font='April 10', command=RealEstate)
#Кнопка я не придумав
NextListMeinMenu = Button(text='Наступна сторінка', width=17, height=4, font='April 10', command=DefNextListMeinMenu)
#Кнопки для покупки їжі в магазині
Sausage = Button(text='Купити ковбасу - 200', width=17,height=4, command= BuySausage , font='April 10')
Than = Button(text='Купити ніж - 150', width=17, height=4, command= BuyThan, font='April 10')
Cheese = Button(text='Купити сир - 120', width=17, height=4,command=BuyCheese, font='April 10')
Flour = Button(text='Купити борошно - 80', width=17, height=4, command= BuyFlour , font='April 10')
Chocolate = Button(text='Купити шоколадку - 70', width=17, height=4, command= BuyChocolate, font='April 10')
Cola = Button(text='Купити колу - 35', width=17, height=4, command= BuyCola , font='April 10')
Cucumber = Button(text='Купити огірок - 20', width=17, height=4,  command= BuyCucumber ,font='April 10')
Bread = Button(text='Купити хліб - 10',width=17, height=4,  command= BuyBread ,font='April 10' )
#Кнопка - повернутися назад
BackMainMenu = Button(text='На головний екран', width=36, height=3, command=DefBackMainMenu, font='April 10')
#Кнопка - на наступний лист з їжею
NextListShop = Button(text='На наступний лист', width=17, height=4, command=NextListShop,font='April 10')
#Кнопка - піти відпочити
GoSleep = Button(text='Піду посплю',width=17, height=3, command=Gosleep , font='April 10')
#Кнопка - піти поготувати
GoCook = Button(text='Піду поготую',width=17, height=3, command=DefGoCook,font='April 10')
#Кнопки для таймеру
btnStartTaimer = Button(text='Заснути', font=('Comic Sans MS', 20), width=15, command=start_tick)
btnStopTaimer = Button(text='Прокинутися', font=('Comic Sans MS', 20), width=15, command=stop_tick)
btnContinuetTaimer = Button(text='Знов заснути', font=('Comic Sans MS', 20), width=15, command=continue_tick)
#Багато кнопок для готування
CookButerbrod = Button(text='Приготувати Бутерброд', width=17,height=4, command= cookButerbrot , font='April 10')
#####################
SellButerbrod = Button(text='Продати бутерброд\nза 120', width=17, height=4, command = SellButterbrod, font='April 10')
######################
btnCut = Button(text = 'Порізати їжу\n(потрібен ніж)',width=17,height=4, command= Cut,font='April 10')
CutSausage = Button(text='Порізати ковбасу', width=17,height=4, command= CutSausage , font='April 10')
CutThan = Button(text='Порізати ніж', width=17, height=4, command= CutThan, font='April 10')
CutCheese = Button(text='Порізати сир', width=17, height=4,command=CutCheese, font='April 10')
CutFlour = Button(text='Порізати борошно', width=17, height=4, command= CutFlour , font='April 10')
CutChocolate = Button(text='Порізати шоколадку ', width=17, height=4, command= CutChocolate, font='April 10')
CutCola = Button(text='Порізати колу', width=17, height=4, command= CutCola , font='April 10')
CutCucumber = Button(text='Порізати огірок', width=17, height=4,  command= CutCucumber ,font='April 10')
CutBread = Button(text='Порізати хліб',width=17, height=4,  command= CutBread ,font='April 10' )
BuyTomato = Button(text='Купити помідор - 20', width=17,height=4, command=BuyTomato ,font='April 10')
BuySalat = Button(text='Купити салат - 30', width=17,height=4, command=BuySalat ,font='April 10')
BuySalt = Button(text='Купити сіль - 20', width=17,height=4, command=BuySalt,font='April 10')
BuyBowl = Button(text='Купити миску - 50', width=17,height=4, command=BuyBowl ,font='April 10')
BuyOil = Button(text='Купити Масло - 30', width=17,height=4, command=BuyOil,font='April 10')
NextListCut = Button(text='Наступний лист', width=17,height=4, command=NextListCut ,font='April 10')
CutTomato = Button(text='Порізати помідор', width=17,height=4, command=CutTomato ,font='April 10')
CutSalat = Button(text='Порізати салат ', width=17,height=4, command=CutSalad ,font='April 10')
CutSalt = Button(text='Порізати сіль', width=17,height=4, command=CutSalt,font='April 10')
CutBowl = Button(text='Порізати миску', width=17,height=4, command=CutBowl ,font='April 10')
CutOil = Button(text='Порізати Масло', width=17,height=4, command=CutOil,font='April 10')
CookSalat = Button(text='Приготувати Салат', width=17,height=4, command=CookSalat,font='April 10')
SellSalat = Button(text='Продати Салат\nза 340', width=17, height=4, command = SellSalat, font='April 10')
######################
btnmoney10 = Button(text='0', width=27, height=2, command = lambda: OneDigit('0'))
btnmoney11 = Button(text='1', width=8, height=2, command = lambda: OneDigit('1'))
btnmoney11.place(x= 1000, y= 1000)
btnmoney12 = Button(text='2', width=8, height=2, command = lambda: OneDigit('2'))
btnmoney12.place(x= 1000, y= 1000)
btnmoney13 = Button(text='3', width=8, height=2, command = lambda: OneDigit('3'))
btnmoney13.place(x= 1000, y= 1000)
btnmoney14 = Button(text='4', width=8, height=2, command = lambda: OneDigit('4'))
btnmoney14.place(x= 1000, y= 1000)
btnmoney15 = Button(text='5', width=8, height=2, command = lambda: OneDigit('5'))
btnmoney15.place(x= 1000, y= 1000)
btnmoney16 = Button(text='6', width=8, height=2, command = lambda: OneDigit('6'))
btnmoney16.place(x=1000, y=1000)
btnmoney17 = Button(text='7', width=8, height=2, command = lambda: OneDigit('7'))
btnmoney17.place(x= 1000, y= 1000)
btnmoney18 = Button(text='8', width=8, height=2, command = lambda: OneDigit('8'))
btnmoney18.place(x= 1000, y= 1000)
btnmoney19 = Button(text='9', width=8, height=2, command = lambda: OneDigit('9'))
btnmoney19.place(x= 1000, y= 1000)
btnmoneyEntr1 = Button(text='Enter', width=13, height=2, command= Enter1)
btnmoneyEntr1.place(x= 1000, y= 1000)
btnmoneyClear1 = Button(text='C', width=13, height=2,command = Clear1)
btnmoneyClear1.place(x= 1000, y= 1000, )
GetCard = Button(text='Взяти карту', width=20, height=4, command= GetCard)
StopKasino = Button(text='Зупинитися', width=20, height=4, command=StopKasino)
NextListRealEstate = Button(text='На наступну сторінку', width=38,height=1, command=DefNextListRealEstate ,font='April 10')
Buy1Room = Button(text='Купити однокімнату \n квартиру', width=20, height=4, command=DefBuy1Room)
Go1Room = Button(text='Увійти в дім', width=20, height=3, command=DefGo1Room)
BackSettings1Room =  Button(text='Назад', width=36, height=3, command=DefBackSettings1Room, font='April 10')
Maining1Room = Button(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
Orend1Room = Button(text='Здати в оренду', width=20, height=3, command=DefOrend1Room)
Sell1Room = Button(text='Продати квартиру', width=20, height=3, command=DefSell1Room)
##############################
btnStartOrend1Room = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend1Room)
btnStopTaimerOrend1Room = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend1Room(2))

Buy2Room = Button(text='Купити двокімнатну \n квартиру', width=20, height=4, command=DefBuy2Room)
Go2Room = Button(text='Увійти в дім', width=20, height=3, command=DefGo2Room)
BackSettings2Room =  Button(text='Назад', width=36, height=3, command=DefBackSettings2Room, font='April 10')
Maining2Room = Button(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
Orend2Room = Button(text='Здати в оренду', width=20, height=3, command=DefOrend2Room)
Sell2Room = Button(text='Продати квартиру', width=20, height=3, command=DefSell2Room)
##############################
btnStartOrend2Room = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend2Room)
btnStopTaimerOrend2Room = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend2Room(2))
############################
NextInterier = Button(text='>>>>', width=20, height=4, command=DefNextListInterier1)
BackInterier = Button(text='<<<<', width=20, height=4, command=DefBackListInterier1)
############################
Buy3Room = Button(text='Купити трьохкімнатну \n квартиру', width=20, height=4, command=DefBuy3Room)


Go3Room = Button(text='Увійти в дім', width=20, height=3, command= lambda : Go3RoomCommand(
    [
    'images_shop/Квартири/3 квартира/Interior/modulna-spalna-sona-new-svit-mebliv-83784-product.jpg',
    'images_shop/Квартири/3 квартира/Interior/spalnya-selena-eko.jpg',
    'images_shop/Квартири/3 квартира/Interior/Дизайн-квартиры-Запорожье-гостиная-дизайн-проект.jpg',
    'images_shop/Квартири/3 квартира/Interior/4515wdeg7trn1iu6plxiw0gd2d73g.webp'
    ]
    ))


BackSettings3Room =  Button(text='Назад', width=36, height=3, command=DefBackSettings3Room, font='April 10')
Maining3Room = Button(text='Майніти криптовалюту', width=20, height=3, state=DISABLED)
Orend3Room = Button(text='Здати в оренду', width=20, height=3, command=DefOrend3Room)
Sell3Room = Button(text='Продати квартиру', width=20, height=3, command=DefSell3Room)
##############################
btnStartOrend3Room = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend3Room)
btnStopTaimerOrend3Room = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend3Room(2))
#############################
Buy1House = Button(text='Купити одноповерховий \n будинок', width=20, height=4, command=DefBuy1House)
Go1House = Button(text='Увійти в дім', width=20, height=3, command=DefGo1House)
BackSettings1House =  Button(text='Назад', width=36, height=3, command=DefBackSettings1House, font='April 10')
Maining1House = Button(text='Майніти криптовалюту', width=20, height=3, command=DefMaining1House)
Orend1House = Button(text='Здати в оренду', width=20, height=3, command=DefOrend1House)
Sell1House = Button(text='Продати дім', width=20, height=3, command=DefSell1House)
##############################
btnStartOrend1House = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend1House)
btnStopTaimerOrend1House = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend1House(2))
##############################
BuyVideoCard1House = Button(text='Купити 20 відеокарт за 280.000 грн', height=2,width=42, command=DefBuyVideoCard1House)
BuyFrameForMining1House = Button(text='Купити  5 каркасів по 2000 грн = 10000 грн', height=2,width=42, command=DefBuyFrameForMining1House)
BuyMiner1House = Button(text='Купити майнер - 30000 грн', height=2,width=42, command=DefBuyMiner1House)
BuyMainingSetUp1House = Button(text='Найняти майстера, щоб він все налаштував', height=2,width=42, command=DefBuyMainingSetUp1House)
btnCanGoTOBasement1House = Button(text='Увійти в підвал', height=2,width=42, command=DefCanGoToBasement1Home)
############################
btnStartMining1House = Button(text='Запустити ферму', width=36, height=2, font='April 10', command=DefStartMining1House )
btnStopTaimerMaining1House = Button(text='Зупинити ферму', width=36, height=2, font='April 10', command=lambda: DefStopMining1House(2))
#############################
ExchangeCurrency = Button(text='Біржа', width=17, height=4, font='April 10', command=GoExchangeCenter)
Charity = Button(text='Благодійність', width=17, height=4, font='April 10', command=DefGoCharity)
WhatUpdate= Button(text='Що додали?', width=17, height=4, font='April 10', command=DefWhatUpdate)
PromoCode = Button(text='Промокод', width=17, height=4, font='April 10', command=DefPromoCode)
btnBank = Button(text='Банк', width=17, height=4, font='April 10', command=DefGoBank)
btnSave = Button(text='Збереження', width=17, height=4, font='April 10', command=DefGoSaveMenu)
btnNextListMeinMenu3 = Button(text='Наступна сторінка', width=17, height=4, font='April 10', command=DefNextListMainMenu3)
BackListMainMenu = Button(text='Попередня сторінка', width=17, height=4, font='April 10', command=DefBackListMainMenu)
BackTo2ListMainMenu = Button(text='Назад', width=36, height=3, command=DefBackTo2ListMainMenu, font='April 10')
BackTo3ListMainMenu = Button(text='Назад', width=36, height=3, command=DefBackTo3ListMainMenu, font='April 10')
SellShopCoins = Button(text='Продати ShopCoin', bg='Green', command=DefSellShopCoins)
BuyShopCoins = Button(text='Купити ShopCoin', bg='Red', width=15, command=DefBuyShopCoins)
EnterForSellShopCoins = Button(text='Ввести', command=DefEnterForSellShopCoins)
##########################################################
Buy2House = Button(text='Купити двоповерховий \n будинок', width=20, height=4, command=DefBuy2House)
Go2House = Button(text='Увійти в дім', width=20, height=3, command=DefGo2House)
BackSettings2House =  Button(text='Назад', width=36, height=3, command=DefBackSettings2House, font='April 10')
Maining2House = Button(text='Майніти криптовалюту', width=20, height=3, command=DefMaining2House)
Orend2House = Button(text='Здати в оренду', width=20, height=3, command=DefOrend2House)
Sell2House = Button(text='Продати дім', width=20, height=3, command=DefSell2House)
##############################
btnStartOrend2House = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend2House)
btnStopTaimerOrend2House = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend2House(2))
##############################
BuyVideoCard2House = Button(text='Купити 20 відеокарт за 420.000 грн', height=2,width=42, command=DefBuyVideoCard2House)
BuyFrameForMining2House = Button(text='Купити  8 каркасів по 2000 грн = 16000 грн', height=2,width=42, command=DefBuyFrameForMining2House)
BuyMiner2House = Button(text='Купити майнер - 30000 грн', height=2,width=42, command=DefBuyMiner2House)
BuyMainingSetUp2House = Button(text='Найняти майстера, щоб він все налаштував', height=2,width=42, command=DefBuyMainingSetUp2House)
btnCanGoTOBasement2House = Button(text='Увійти в підвал', height=2,width=42, command=DefCanGoToBasement2Home)
btnStartMining2House = Button(text='Запустити ферму', width=36, height=2, font='April 10', command=DefStartMining2House )
btnStopTaimerMaining2House = Button(text='Зупинити ферму', width=36, height=2, font='April 10', command=lambda: DefStopMining2House(2))
NextListMaining2House = Button(text='>>>>', width=10,height=2, command=DefNextListMaining2House)
NextListInterier2House = Button(text='>>>>', width=20, height=4, command=DefNextListInterier2House)
###########################################
Buy3House = Button(text='Купити хай-тег \n будинок', width=20, height=4, command=DefBuy3House)
Go3House = Button(text='Увійти в дім', width=20, height=3, command=DefGo3House)
BackSettings3House =  Button(text='Назад', width=36, height=3, command=DefBackSettings3House, font='April 10')
Maining3House = Button(text='Майніти криптовалюту', width=20, height=3, command=DefMaining3House)
Orend3House = Button(text='Здати в оренду', width=20, height=3, command=DefOrend3House)
Sell3House = Button(text='Продати дім', width=20, height=3, command=DefSell3House)
##############################
btnStartOrend3House = Button(text='Здати в оренду', font=('Comic Sans MS', 15), width=15, command=DefStartOrend3House)
btnStopTaimerOrend3House = Button(text='зупинити здачу в оренду', font=('Comic Sans MS', 15), width=20, command=lambda: DefStopOrend3House(2))
##############################
BuyVideoCard3House = Button(text='Купити 50 відеокарт за 700.000 грн', height=2,width=42, command=DefBuyVideoCard3House)
BuyFrameForMining3House = Button(text='Купити  13 каркасів по 2000 грн = 26000 грн', height=2,width=42, command=DefBuyFrameForMining3House)
BuyMiner3House = Button(text='Купити майнер - 30000 грн', height=2,width=42, command=DefBuyMiner3House)
BuyMainingSetUp3House = Button(text='Найняти майстера, щоб він все налаштував', height=2,width=42, command=DefBuyMainingSetUp3House)
btnCanGoTOBasement3House = Button(text='Увійти в підвал', height=2,width=42, command=DefCanGoToBasement3Home)
btnStartMining3House = Button(text='Запустити ферму', width=36, height=2, font='April 10', command=DefStartMining3House)
btnStopTaimerMaining3House = Button(text='Зупинити ферму', width=36, height=2, font='April 10', command=lambda: DefStopMining3House(2))
NextListMaining3House = Button(text='>>>>', width=10,height=2, command=DefNextListMaining3House)
NextListInterier3House = Button(text='>>>>', width=20, height=4, command=DefNextListInterier3House)
BackListMaining3House = Button(text='<<<<', width=10,height=2, command=DefBackListMaining3House)
EnterForBuyShopCoins = Button(text='Ввести', command=DefEnterForBuyShopCoins)
EnterForBuyDollar = Button(text='Ввести', command=DefEnterForBuyDollar)
NextRateCharity = Button(text='>>>>', height=2,width=10, command=DefNextRateCharity)
BackRateCharity = Button(text='<<<<', height=2,width=10, command=DefBackRateCharity)
ButtonForGiveCharity = Button(text='Пожертвувати', height=2,width=30, command=DefCharityMoney)
############################
BuyMoreProduct0 = Button(text='0', width=27, height=2, command = lambda: DefBuyMoreProduct('0'))
BuyMoreProduct1 = Button(text='1', width=8, height=2, command = lambda: DefBuyMoreProduct('1'))
BuyMoreProduct2 = Button(text='2', width=8, height=2, command = lambda: DefBuyMoreProduct('2'))
BuyMoreProduct3 = Button(text='3', width=8, height=2, command = lambda: DefBuyMoreProduct('3'))
BuyMoreProduct4 = Button(text='4', width=8, height=2, command = lambda: DefBuyMoreProduct('4'))
BuyMoreProduct5 = Button(text='5', width=8, height=2, command = lambda: DefBuyMoreProduct('5'))
BuyMoreProduct6 = Button(text='6', width=8, height=2, command = lambda: DefBuyMoreProduct('6'))
BuyMoreProduct7 = Button(text='7', width=8, height=2, command = lambda: DefBuyMoreProduct('7'))
BuyMoreProduct8 = Button(text='8', width=8, height=2, command = lambda: DefBuyMoreProduct('8'))
BuyMoreProduct9 = Button(text='9', width=8, height=2, command = lambda: DefBuyMoreProduct('9'))
BuyMoreProductEntr1 = Button(text='Entr', width=13, height=2)
BuyMoreProductClear1 = Button(text='C', width=13, height=2, command = ClearMoreProduct)

btnBedsideTable = Button(text='Купити тумбочку',width=17, height=3,font='April 10', command=DefBuyBedsideTable)
SellDollar = Button(text='Продати долари', bg='Green', width=15,command=DefSellDollar)
BuyDollar = Button(text='Купити долари', bg='Red', width=15,command=DefBuyDollar)
EnterForSellDollar = Button(text='Ввести', command=DefEnterForSellDollar)

EnterPromoCode = Button(text='Enter', bg='white', width=25,command=DefEnterPromoCode)

btnTakeFromBedsideTable = Button(text='Дістати з тумбочки',width=17, height=3,font='April 10', command=DefTakeInBedsideTable)
btnPutInTheBedsideTable = Button(text='Покласти в тумбочку',width=17, height=3,font='April 10', command=DefPutInBedsideTable)
btnInformationAboutWhatInTheBedsideTable = Button(text='Інформація про речі\nв тумбочці',width=17, height=3,font='April 10', command=DefInfoWhatInBedsideTable)
btnBankCard = Button(text='Банківська картка',width=17, height=3,font='April 10', command=DefGetBankCard)
btnPutOnBankCard = Button(text='Покласти на карту',width=17, height=3,font='April 10', command=DefPutOnBankCard)
btnTakeTheBankCard = Button(text='Зняти з карти',width=17, height=3,font='April 10', command=DefTakeTheBankCard)
btnFindPinCode = Button(text='Дізнатися пін-код:\n10.000 грн',width=17, height=3,font='April 10', command=DefFindePinCode)
btnInfoPayAndGetBankCard = Button(text='Інформація про\nкартку, оплати',width=17, height=3,font='April 10', command=DefInfoPayAndGetBankCard)
btnPayInExchangeCenterCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayCardInExchangeCenter,bg='green')
btnPayInExchangeCenterMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyInExchangeCenter )
btnEnterProofPinCode = Button(text='Enter', height=1, command=DefProofPinCode)
btnPayInShopCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayCardInShop,bg='green')
btnPayInShopMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyInShop)
btnPayInMarketCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayCardInMarket,bg='green')
btnPayInMarketMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyInMarket)
btnPayInCasinoCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayCardInCasino,bg='green')
btnPayInCasinoMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyInCasino)
btnPayInCharityCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayCardInCharity,bg='green')
btnPayInCharityMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyInCharity)
btnDeposit = Button(text='Депозит',width=17, height=3,font='April 10', command=DefDeposit)
btnPutOnDeposit = Button(text='Покласти на депозит',width=17, height=3,font='April 10', command=DefPutOnDeposit)
btnTakeFromDeposit = Button(text='Зняти з депозиту',width=17, height=3,font='April 10', command=DefTakeFromDeposit)
btnInfoAboutDeposit = Button(text='Інформація про\nдепозит',width=17, height=3,font='April 10', command=DefInfoAboutDeposit)
btnTaxes = Button(text='Податки',width=17, height=3,font='April 10',command=DefTaxes)
btnPayTaxes = Button(text='Оплатити податки',width=17, height=3,font='April 10',command=DefPayTaxesMenu)
btnPayAllTaxes = Button(text='Оплатити всі податки\n('+str(AllTaxes)+' грн)',width=17, height=3,font='April 10',command=DefPayAllTaxes)
btnPayTaxes1Room = Button(text='Оплатити податки за\nоднокімнатну квартиру\n('+str(Taxes1Room)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes1Room)
btnPayTaxes2Room = Button(text='Оплатити податки за\nдвокімнатну квартиру\n('+str(Taxes2Room)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes2Room)
btnPayTaxes3Room = Button(text='Оплатити податки за\nтрьохкімнатну квартиру\n('+str(Taxes3Room)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes3Room)
btnPayTaxes1House = Button(text='Оплатити податки за\nодноповерховий будинок\n('+str(Taxes1House)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes1House)
btnPayTaxes2House = Button(text='Оплатити податки за\nдвоповерховий будинок\n('+str(Taxes2House)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes2House)
btnPayTaxes3House = Button(text='Оплатити податки за\nдвокімнатну квартиру\n('+str(Taxes3House)+' гривень)',width=17, height=3,font='April 10',command=DefPayTaxes3House)
btnPayTaxesCard = Button(text='Карткою', width=6,height=1,font='April 10', command=DefPayBankCardTaxes,bg='green')
btnPayTaxesMoney = Button(text='Готівкою', width=6,height=1,font='April 10', command=DefPayMoneyTaxes)
btnAddSave = Button(text='+',width=6,height=2,bg='green',font='April 15', command=DefAddSave)
btnSaveIn1File = Button(text='Зберегти',bg='green', width=10,height=1,command=lambda: DefSave1Save(1))
btnSaveIn2File = Button(text='Зберегти',bg='green', width=10,height=1,command=lambda: DefSave1Save(2))
btnSaveIn3File = Button(text='Зберегти',bg='green', width=10,height=1,command=lambda: DefSave1Save(3))
btnSaveIn4File = Button(text='Зберегти',bg='green', width=10,height=1,command=lambda: DefSave1Save(4))
btnUploadFrom1File = Button(text='Завантажити',bg='green', width=10,height=1,command=lambda: DefUpload1File(1))
btnUploadFrom2File = Button(text='Завантажити',bg='green', width=10,height=1,command=lambda: DefUpload1File(2))
btnUploadFrom3File = Button(text='Завантажити',bg='green', width=10,height=1,command=lambda: DefUpload1File(3))
btnUploadFrom4File = Button(text='Завантажити',bg='green', width=10,height=1,command=lambda: DefUpload1File(4))
btnDeleat1File = Button(text='Видалити',bg='red', width=10,height=1,command=lambda: DelSave(1))
btnDeleat2File = Button(text='Видалити',bg='red', width=10,height=1,command=lambda: DelSave(2))
btnDeleat3File = Button(text='Видалити',bg='red', width=10,height=1,command=lambda: DelSave(3))
btnDeleat4File = Button(text='Видалити',bg='red', width=10,height=1,command=lambda: DelSave(4))
EnterNameSave = Button(text='enter',command=DefEnterNameSave)
btnBuyStuff = Button(text='Купити фарш-100', width=17,height=4,font='April 10',command=DefBuyStuffing)
btnBuySpaghetti = Button(text='Купити спагеті-40', width=17,height=4,font='April 10',command=DefBuySpaghetti)
btnCookIngredient = Button(text='Готувати інгредієнти',width=36, height=3,font='April 10',command=DefListHowCookIngredient)
btnBoil = Button(text='Зварити спагетті\n(потрібна миска)',width=17,height=4,font='April 10',command=BoilSpaghetti)
btnFry = Button(text="Посмажити м'ясо і\nзробити котлети\n(потрібна миска)",width=17,height=4,font='April 10',command=FryStuffing)
btnCookSpaghettiWithCutlet = Button(text='Приготувати спагеті\nз котлетою' ,width=17,height=4, command=DefCookSpaghettiWithCutlet,font='April 10')
btnSellSpaghettiWithCutlet = Button(text='Продами спагетті з\nкотлетою\nза 280', width=17, height=4, command = DefSpaghettiWithCutletSell, font='April 10')
btnSaveSaves = Button(text='Зберегтися', width=17, height=4, font='April 10', command=lambda: DefSave1Save(NowSave) )
btnClicker = Button(text='Клікер',width=17, height=4,font='April 10', command=GoClicker)
btnUpgradeStarCoin = Button(text='Прокачати монету, щоб \n вона давала 0.02 за клік\nціна:10 StarCoin-ів в додатку',command=UpgradeStarCoin1)
btnWithdrawStarCoin = Button(text='Вивести StarCoin на біржу', command=WithdrawStarCoin)
btnSellStarCoin = Button(text='Продати StarCoin', bg='Green', width=15,command=DefSellStarCoin)
btnBuyStarCoin = Button(text='Купити StarCoin', bg='Red', width=15,command=DefBuyStarCoin)
EnterForSellStarCoin = Button(text='Ввести', command=DefEnterForSellStarCoin)
EnterForBuyStarCoin = Button(text='Ввести', command=DefEnterForBuyStarCoin)
btnWork = Button(text='Робота',width=17, height=4,font='April 10')
btnBusiness = Button(text='Бізнеси',width=17, height=4,font='April 10')
btnCourses = Button(text='Курси',width=17, height=4,font='April 10', command=GoCourses)
btnWorkCourses = Button(text='Курси по\nроботам',width=17, height=4,font='April 10')
btnBusinessCourses = Button(text='Курси по\nбізнесу',width=17, height=4,font='April 10')
btnGoSeaBattle = Button(text='Пограти в морській\nбій',width=17, height=4,font='April 10',command=defStartSeaBattle)
btnBackyard = Button(text='Город',width=17, height=4,font='April 10')
btnGardeningShop = Button(text='Магазин\n"Все для городу"',width=17, height=4,font='April 10')

#Поля вводу
#Запитує скільки у тебе грошей
EntryPromoCode = Entry(root, width=30, state='normal')
Howmuchmoney = Entry(root, width=30, state="readonly")
Howmuchmoney.place(x=1000, y=200)
RateKasino = Entry(root, width=30, state="readonly")
HowWantSellShopCoins = Entry(root, width=15,state='normal')
HowWantBuyShopCoins = Entry(root, width=15,state='normal')
HowWantSellDollar = Entry(root, width=15,state='normal')
HowWantBuyDollar = Entry(root, width=15,state='normal')
HowWantBuyStarCoin = Entry(root,width=15,state='normal')
HowWantSellStarCoin = Entry(root,width=15,state='normal')
YourBuy =  Entry(root, width=23,state='normal')
YourBuy2 =  Entry(root, width=23,state='normal')
YourBuy3 =  Entry(root, width=23,state='normal')
YourBuy4 =  Entry(root, width=23,state='normal')
YourBuy5 =  Entry(root, width=23,state='normal')
YourBuy6 =  Entry(root, width=23,state='normal')
YourBuy7 =  Entry(root, width=23,state='normal')
YourBuy8 =  Entry(root, width=23,state='normal')
YourBuy9 =  Entry(root, width=23,state='normal')
YourBuy10 =  Entry(root, width=23,state='normal')
YourBuy11 =  Entry(root, width=23,state='normal')
YourBuy12 =  Entry(root, width=23,state='normal')
YourBuy13 =  Entry(root, width=23,state='normal')
YourBuy14 =  Entry(root, width=23,state='normal')
YourBuy15 =  Entry(root, width=23,state='normal')
YourBuy16 =  Entry(root, width=23,state='normal')
YourBuy17 =  Entry(root, width=23,state='normal')
YourBuy18 =  Entry(root, width=23,state='normal')
YourBuy19 =  Entry(root, width=23,state='normal')
YourBuy20 = Entry(root, width=23,state='normal')
YourBuy21 =  Entry(root, width=23,state='normal')
YourBuy22 = Entry(root, width=23,state='normal')
YourCook = Entry(root, width=23,state='normal')
YourCook2 = Entry(root, width=23,state='normal')
YourCook3 = Entry(root, width=23,state='normal')
YourCook4 = Entry(root, width=23,state='normal')
YourCook5 = Entry(root, width=48,state='normal')
BuyMoreProductEntry = Entry(root, width=30, state="readonly")
EntryInfoMoneyInBedsideTable = Entry(root, width=23,state='normal')
EntryInfoDollarInBedsideTable = Entry(root, width=23,state='normal')
EntryPinCodeBankCard = Entry(root,width=30, show='*')
EntryHowMoneyOnBankCard = Entry(root,width=46,state='normal')
EntryProofPinCode = Entry(root,width=15,state='normal', show='*')
EntryHowMoneyOnDeposit = Entry(root,width=46,state='normal')
EntryNameSave = Entry(root,width=20,state='normal')
EntryHaveShopCoin = Entry(root,width=12,state='normal')
EntryHaveDolar = Entry(root,width=12,state='normal')
EntryHaveStarCoin = Entry(root,width=20,state='normal')




#Фотографії
ImgStarCoin = Image.open('images_shop/icons/StarCoin.jpg')
ImgStarCoin = ImgStarCoin.resize((100,100))
ImgStarCoinLabel = ImgStarCoin.resize((60,60))
ImgStarCoin = ImageTk.PhotoImage(ImgStarCoin)
ImgStarCoinLabel = ImageTk.PhotoImage(ImgStarCoinLabel)
btnStarCoinTap = Button(image=ImgStarCoin,command=ClickedStarCoin)
LabelImgStarCoin = Label(image= ImgStarCoinLabel)
LabelImgStarCoin.image = ImgStarCoinLabel
####################################
Image1Room = Image.open('images_shop/Квартири/1 квартира/Building/budinok-scaled.jpg')
Image1Room = Image1Room.resize((150,100))
Image1Room = ImageTk.PhotoImage(Image1Room)
Label1Room = Label(image = Image1Room)
Label1Room.image = Image1Room
################################
MicroImage1Room = Image.open('images_shop/Квартири/1 квартира/Building/budinok-scaled.jpg')
MicroImage1Room = MicroImage1Room.resize((80, 50))
MicroImage1Room = ImageTk.PhotoImage(MicroImage1Room)
MicroLabel1Room = Label(image=MicroImage1Room)
MicroLabel1Room.image = MicroImage1Room
##################################
Image1RoomInterior = Image.open('images_shop/Квартири/1 квартира/Interior/Remont-odnokomnatnoj-kvartiry-dlya-molodoy-semyi_800x800-equal.jpg')
Image1RoomInterior = Image1RoomInterior.resize((300,200))
Image1RoomInterior = ImageTk.PhotoImage(Image1RoomInterior)
Label1RoomInterior = Label(image = Image1RoomInterior)
Label1RoomInterior.image = Image1RoomInterior
#################################################################################
Image2Room = Image.open('images_shop/Квартири/2 квартира/Building/мун.буд 1.jpg')
Image2Room = Image2Room.resize((150,100))
Image2Room = ImageTk.PhotoImage(Image2Room)
Label2Room = Label(image = Image2Room)
Label2Room.image = Image2Room
#################################
MicroImage2Room = Image.open('images_shop/Квартири/2 квартира/Building/мун.буд 1.jpg')
MicroImage2Room = MicroImage2Room.resize((80, 50))
MicroImage2Room = ImageTk.PhotoImage(MicroImage2Room)
MicroLabel2Room = Label(image=MicroImage2Room)
MicroLabel2Room.image = MicroImage2Room
###################################
Image2RoomInterior = Image.open('images_shop/Квартири/2 квартира/Interior/61c78c87-51a2-4a58-a20e-4805eab5364b.webp')
Image2RoomInterior = Image2RoomInterior.resize((300,200))
Image2RoomInterior = ImageTk.PhotoImage(Image2RoomInterior)
Label2RoomInterior = Label(image = Image2RoomInterior)
Label2RoomInterior.image = Image2RoomInterior
###################################
Image2RoomInterior2 = Image.open('images_shop/Квартири/2 квартира/Interior/3dsmax-view01.jpg')
Image2RoomInterior2 = Image2RoomInterior2.resize((300,200))
Image2RoomInterior2 = ImageTk.PhotoImage(Image2RoomInterior2)
Label2RoomInterior2 = Label(image = Image2RoomInterior2)
Label2RoomInterior2.image = Image2RoomInterior2
###################################
Image2RoomInterior3 = Image.open('images_shop/Квартири/2 квартира/Interior/Frame-6190-1.png.webp')
Image2RoomInterior3 = Image2RoomInterior3.resize((300,200))
Image2RoomInterior3 = ImageTk.PhotoImage(Image2RoomInterior3)
Label2RoomInterior3 = Label(image = Image2RoomInterior3)
Label2RoomInterior3.image = Image2RoomInterior3
####################################################################################
Image3Room = Image.open('images_shop/Квартири/3 квартира/Building/images (2).jfif')
Image3Room = Image3Room.resize((150,90))
Image3Room = ImageTk.PhotoImage(Image3Room)
Label3Room = Label(image = Image3Room)
Label3Room.image = Image3Room
###################################
MicroImage3Room = Image.open('images_shop/Квартири/3 квартира/Building/images (2).jfif')
MicroImage3Room = MicroImage3Room.resize((80, 50))
MicroImage3Room = ImageTk.PhotoImage(MicroImage3Room)
MicroLabel3Room = Label(image=MicroImage3Room)
MicroLabel3Room.image = MicroImage3Room
##################################

# ImageSlider
CurrentSlide = Label()
NextSlide = Button(text='>>>>', width=20, height=4)
BackSlide = Button(text='<<<<', width=20, height=4)

####################################################################################
ImageHouse1 = Image.open('images_shop/Будинки/1 будинок/Building/proekt_1_etazh_doma_104m2_k1104780_1.jpg')
ImageHouse1 = ImageHouse1.resize((150,90))
ImageHouse1 = ImageTk.PhotoImage(ImageHouse1)
LabelHouse1 = Label(image = ImageHouse1)
LabelHouse1.image = ImageHouse1
#########################################
MicroImage1House = Image.open('images_shop/Будинки/1 будинок/Building/proekt_1_etazh_doma_104m2_k1104780_1.jpg')
MicroImage1House = MicroImage1House.resize((80, 50))
MicroImage1House = ImageTk.PhotoImage(MicroImage1House)
MicroLabel1House = Label(image=MicroImage1House)
MicroLabel1House.image = MicroImage1House
##########################################
Image1HouseInterior = Image.open('images_shop/Будинки/1 будинок/Interior/a8dznacojkymonvn29ju.jpg')
Image1HouseInterior = Image1HouseInterior.resize((300,200))
Image1HouseInterior = ImageTk.PhotoImage(Image1HouseInterior)
Label1HouseInterior = Label(image = Image1HouseInterior)
Label1HouseInterior.image = Image1HouseInterior
####################################################################################
ImageHouse2 = Image.open('images_shop/Будинки/2 будинок/Building/images.jfif')
ImageHouse2 = ImageHouse2.resize((150,90))
ImageHouse2 = ImageTk.PhotoImage(ImageHouse2)
LabelHouse2 = Label(image = ImageHouse2)
LabelHouse2.image = ImageHouse2
###########################################
MicroImage2House = Image.open('images_shop/Будинки/2 будинок/Building/images.jfif')
MicroImage2House = MicroImage2House.resize((80, 50))
MicroImage2House = ImageTk.PhotoImage(MicroImage2House)
MicroLabel2House = Label(image=MicroImage2House)
MicroLabel2House.image = MicroImage2House
##########################################
ImageHouse2Interier1 = Image.open('images_shop/Будинки/2 будинок/Interior/images.jfif')
ImageHouse2Interier1 = ImageHouse2Interier1.resize((300,200))
ImageHouse2Interier1 = ImageTk.PhotoImage(ImageHouse2Interier1)
LabelHouse2Interier1 = Label(image = ImageHouse2Interier1)
LabelHouse2Interier1.image = ImageHouse2Interier1
##########################################
ImageHouse2Interier2 = Image.open('images_shop/Будинки/2 будинок/Interior/png-transparent-floor-plan-house-plan-interior-design-services-interior-design-plan-furniture-building-apartment.png')
ImageHouse2Interier2 = ImageHouse2Interier2.resize((300,200))
ImageHouse2Interier2 = ImageTk.PhotoImage(ImageHouse2Interier2)
LabelHouse2Interier2 = Label(image = ImageHouse2Interier2)
LabelHouse2Interier2.image = ImageHouse2Interier2
###################################################################################
ImageHouse3 = Image.open( 'images_shop/Будинки/3 будинок/Building/1407942551_1-800x467.jpg')
ImageHouse3 = ImageHouse3.resize((150,90))
ImageHouse3 = ImageTk.PhotoImage(ImageHouse3)
LabelHouse3 = Label(image = ImageHouse3)
LabelHouse3.image = ImageHouse3
######################################
ImageHouse3Interier1 = Image.open( 'images_shop/Будинки/3 будинок/Interior/4b8306c2.png')
ImageHouse3Interier1 = ImageHouse3Interier1.resize((300,200))
ImageHouse3Interier1 = ImageTk.PhotoImage(ImageHouse3Interier1)
LabelHouse3Interier1= Label(image = ImageHouse3Interier1)
LabelHouse3Interier1.image = ImageHouse3Interier1
######################################
ImageHouse3Interier2 = Image.open( 'images_shop/Будинки/3 будинок/Interior/planirovka-doma-1.jpg')
ImageHouse3Interier2 = ImageHouse3Interier2.resize((300,200))
ImageHouse3Interier2 = ImageTk.PhotoImage(ImageHouse3Interier2)
LabelHouse3Interier2= Label(image = ImageHouse3Interier2)
LabelHouse3Interier2.image = ImageHouse3Interier2
###########################################################################
ImageMainingFarm = Image.open('images_shop/Будинки//Mining farm/photo_2023-12-27_13-21-31.jpg')
ImageMainingFarm = ImageMainingFarm.resize((150,75))
ImageMainingFarm = ImageTk.PhotoImage(ImageMainingFarm)
LabelMainingFarm1 = Label(image= ImageMainingFarm)
LabelMainingFarm1.image = ImageMainingFarm

LabelMainingFarm2 = Label(image= ImageMainingFarm)
LabelMainingFarm2.image = ImageMainingFarm

LabelMainingFarm3 = Label(image= ImageMainingFarm)
LabelMainingFarm3.image = ImageMainingFarm

LabelMainingFarm4 = Label(image= ImageMainingFarm)
LabelMainingFarm4.image = ImageMainingFarm

LabelMainingFarm5 = Label(image= ImageMainingFarm)
LabelMainingFarm5.image = ImageMainingFarm

LabelMainingFarm6 = Label(image=ImageMainingFarm)
LabelMainingFarm6.image = ImageMainingFarm

LabelMainingFarm7 = Label(image=ImageMainingFarm)
LabelMainingFarm7.image = ImageMainingFarm

ImagesShopCoin = Image.open('images_shop/icons/photo_2023-12-27_23-33-42.jpg')
ImagesShopCoin = ImagesShopCoin.resize((70,70))
ImagesShopCoin = ImageTk.PhotoImage(ImagesShopCoin)
LabelShopCoin = Label(image= ImagesShopCoin)
LabelShopCoin.image = ImagesShopCoin

ImageHalfMainingFarm = Image.open('images_shop/Будинки/Mining farm/Майнинг ферми.png')
ImageHalfMainingFarm = ImageHalfMainingFarm.resize((150,75))
ImageHalfMainingFarm = ImageTk.PhotoImage(ImageHalfMainingFarm)
LabelHalfMainingFarm1 = Label(image= ImageHalfMainingFarm)
LabelHalfMainingFarm1.image = ImageHalfMainingFarm

MicroImage3House = Image.open( 'images_shop/Будинки/3 будинок/Building/1407942551_1-800x467.jpg')
MicroImage3House = MicroImage3House.resize((80,50))
MicroImage3House = ImageTk.PhotoImage(MicroImage3House)
MicroLabel3House = Label(image = MicroImage3House)
MicroLabel3House.image = MicroImage3House


ImagesDollar = Image.open('images_shop/icons/pngtree-green-dollars-png-image_9011319.png')
ImagesDollar = ImagesDollar.resize((70,70))
ImagesDollar = ImageTk.PhotoImage(ImagesDollar)
LabelDollar = Label(image= ImagesDollar)
LabelDollar.image = ImagesDollar
#Запускає всю програму

root.mainloop()