from colorama import init
from colorama import Fore, Back, Style
import random
init()
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)

while True:

    choise = input('Що будет робити? y-продовжу грати, n-показати пароль')
    if choise == 'y':
        a1 = input()
        b1 = input()
        c1 = input()
        d1 = input()
        if int(a) == int(a1) and int(b) == int(b1) and int(c) == int(c1) and int(d) == int(d1):
            print(Fore.LIGHTGREEN_EX, a,b,c,d)
            print("Ти переміг")
            break
        else:
            #Три числа?
            if int(a) == int(a1) and int(b) == int(b1) and int(c) == int(c1):
                print(Fore.LIGHTGREEN_EX, a1, b1, c1, Fore.LIGHTWHITE_EX,d1, Fore.LIGHTWHITE_EX)
                continue

            if int(a) == int(a1) and int(b) == int(b1) and int(d) == int(d1):
                print(Fore.LIGHTGREEN_EX, a1, b1,Fore.LIGHTWHITE_EX ,c1, Fore.LIGHTGREEN_EX, d1, Fore.LIGHTWHITE_EX)
                continue

            if int(c) == int(c1) and int(b) == int(b1) and int(d) == int(d1):
                print(Fore.LIGHTWHITE_EX, a1, Fore.LIGHTGREEN_EX,b1, c1, d1, Fore.LIGHTWHITE_EX)
                continue

            if int(c) == int(c1) and int(a) == int(a1) and int(d) == int(d1):
                print(Fore.LIGHTGREEN_EX, a1, Fore.LIGHTWHITE_EX,b1,Fore.LIGHTGREEN_EX ,c1, d1, Fore.LIGHTWHITE_EX)
                continue

            #Два числа

            if int(a) == int(a1) and int(b) == int(b1):
                print(Fore.LIGHTGREEN_EX, a1, b1, Fore.LIGHTWHITE_EX, c1, d1, Fore.LIGHTWHITE_EX)
                continue

            if int(a) == int(a1) and int(c) == int(c1):
                print(Fore.LIGHTGREEN_EX, a1, Fore.LIGHTWHITE_EX ,b1, Fore.LIGHTGREEN_EX ,c1, Fore.LIGHTWHITE_EX ,d1, Fore.LIGHTWHITE_EX)
                continue

            if int(a) == int(a1) and int(d) == int(d1):
                print(Fore.LIGHTGREEN_EX, a1, Fore.LIGHTWHITE_EX ,b1, c1, Fore.LIGHTGREEN_EX ,d1, Fore.LIGHTWHITE_EX)
                continue

            if int(b) == int(b1) and int(c) == int(c1):
                print(Fore.LIGHTWHITE_EX,a1, Fore.LIGHTGREEN_EX ,b1, c1, Fore.LIGHTWHITE_EX ,d1, Fore.LIGHTWHITE_EX)
                continue

            if int(b) == int(b1) and int(d) == int(d1):
                print(Fore.LIGHTWHITE_EX,a1, Fore.LIGHTGREEN_EX ,b1,Fore.LIGHTWHITE_EX,c1,Fore.LIGHTGREEN_EX,d1, Fore.LIGHTWHITE_EX)
                continue

            if int(c) == int(c1) and int(d) == int(d1):
                print(Fore.LIGHTWHITE_EX,a1, b1, Fore.LIGHTGREEN_EX, c1, d1, Fore.LIGHTWHITE_EX)
                continue


            #Одна цифра

            if int(a) == int(a1):
                print(Fore.LIGHTGREEN_EX,a1,Fore.LIGHTWHITE_EX,b1,c1,d1, Fore.LIGHTWHITE_EX)
                continue
            #else:
                #if a1 == b or c or d:
                    #print(Fore.LIGHTYELLOW_EX,a1,Fore.LIGHTWHITE_EX,b1,c1,d1)
                    #continue

            if int(b) == int(b1):
                print(Fore.LIGHTWHITE_EX,a1,Fore.LIGHTGREEN_EX,b1,Fore.LIGHTWHITE_EX,c1,d1, Fore.LIGHTWHITE_EX)
                continue
            #else:
                #if b1 == a or c or d:
                    #print(Fore.LIGHTWHITE_EX,a1,Fore.LIGHTYELLOW_EX,b1,Fore.LIGHTWHITE_EX,c1,d1)
                    #continue

            if int(c) == int(c1):
                print(Fore.LIGHTWHITE_EX,a1,b1,Fore.LIGHTGREEN_EX,c1, Fore.LIGHTWHITE_EX ,d1, Fore.LIGHTWHITE_EX)
                continue
            #else:
                #if a1 == b or c or d:
                    #print(Fore.LIGHTWHITE_EX,a1,Fore.LIGHTYELLOW_EX,b1,Fore.LIGHTWHITE_EX,c1,d1)
                    #continue

            if int(d) == int(d1):
                print(Fore.LIGHTWHITE_EX,a1,b1,c1,Fore.LIGHTGREEN_EX ,b1, Fore.LIGHTWHITE_EX, Fore.LIGHTWHITE_EX)
                continue
            else:
                print(a1,b1,c1,d1)
    elif choise == 'n':
        print('Код - ',a,b,c,d)
        break
input()