import pyautogui, time, keyboard
import sys
from tkinter import *

sys.setrecursionlimit(10**8)

def autoclickerOn():
    inpstart = startkey1.get()
    inpend = endkey1.get()
    while True:
        try:
            if keyboard.is_pressed(inpstart):
                print('[Started] the clicking started ')
                while True:
                    position = pyautogui.position()
                    pyautogui.click(position)
                    pyautogui.PAUSE = 0.02
                    if keyboard.is_pressed(inpend):
                        print('[Ended] the clicking ended ')
                        autoclickerOn()


            elif keyboard.is_pressed(inpend):
                autoclickerOn()

        except KeyboardInterrupt:
                print('\nDone Reading input. Keyboard Interupt.')
                break
    
root = Tk()
root.geometry('230x170')
root.title("Autoclicker by Zahid :>")

welcome_Text1 = Label(root, text = "Autoclicker")
welcome_Text1.place(x=80, y=10)

startText = Label(root, text="START KEY: ")
startText.place(x= 30, y =40)

startkey1 = Text(root)
startkey1.place(x = 100, y = 40)
startkey1.insert(END, 'k')

endText = Label(root, text="END KEY: ")
endText.place(x = 30, y = 70)

endkey1 = Text(root)
endkey1.place(x = 100, y = 70)
endkey1.insert(END, 'l')

btn = Button(root, text = 'SAVE', command=autoclickerOn)
btn.place(x=80, y = 90)

# autoclickerOn()


