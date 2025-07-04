import pyautogui
import time

def d():
    for i in ['skip.png', 'skip2.png', 'skip3.png']:
        center_coords = pyautogui.locateCenterOnScreen(i, confidence=0.85)
        if center_coords:
            pyautogui.click(center_coords)
        else:
            pass

while True:
    try:
        d()
        time.sleep(.2)
    except:
        continue
    time.wait(5)
