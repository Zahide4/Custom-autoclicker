import pyautogui,time, keyboard
import sys
import tkinter

sys.setrecursionlimit(10**8)

startkey = '`'
endkey = '1'

root = Tk()
root.geometry(500, 600)
root.title("Autoclicker By Zahid :>")

welcome_Text1 = Label(root, text = "Autoclicker")
welcome_Text1.place(20, 30)

def autoclickerOn():
    while True:
        try:
            if keyboard.is_pressed(startkey):
                print('[Started] the clicking started ')
                while True:
                    position = pyautogui.position()
                    pyautogui.click(position)
                    pyautogui.PAUSE = 0.02
                    if keyboard.is_pressed(endkey):
                        print('[Ended] the clicking ended ')
                        autoclickerOn()


            elif keyboard.is_pressed(endkey):
                autoclickerOn()

        except KeyboardInterrupt:
                print('\nDone Reading input. Keyboard Interupt.')
                break
    
    
autoclickerOn()
