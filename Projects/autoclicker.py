import pyautogui,time, keyboard
import sys

sys.setrecursionlimit(10**8)

startkey = input("START KEY: ")
endkey = input('END KEY: ')


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
