import pyautogui
import time

def main():
    for i in ['skip.png', 'skip2.png']:
        o = .8 if i == 'skip.png' else .5
        cordinates = pyautogui.locateCenterOnScreen(i, confidence= o)
        if cordinates:
            pyautogui.click(cordinates)
            break
        else:
            pass


while True:
    try:
        main()
        # time.sleep to prevent double clicking
        time.sleep(.2)
    except:
        continue #was pass, neeeds to be continue
    
    time.sleep(5) #You can do whatever but running for lots of time with small wait can affect speed of computer, but only a little
