import keyboard
import mouse
import time

IsStopClick = False
IsClicking = False
IsClick = False
a = 5000


def set_clicker():
    global IsClicking
    IsClicking = not IsClicking
keyboard.add_hotkey('Alt + Z', set_clicker)

def set_clicker2():
    global IsClick
    IsClick = not IsClick
keyboard.add_hotkey('Alt + X', set_clicker2)

def set_clicker_stop():
    global IsStopClick
    IsStopClick = not IsStopClick
keyboard.add_hotkey('Alt + C', set_clicker_stop)


while True:
    #a = input('Скільки натискань')
    if IsClicking:
        #a = input('Скільки натискань')
        for i in range(0,a):
            mouse.click(button='left')
            time.sleep(0.01)
        IsClicking = False
    if IsClick:
        b = a + 10
        for v in range(0,b):
            mouse.click(button='left')
            time.sleep(0.007)
            keyboard.press('Enter')
            time.sleep(0.007)
        IsClick = False
    if IsStopClick:
        break