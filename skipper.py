#Imports the needed modules
import pyautogui
import time

#function to dectect the skip button, if it can see it, if it can then it clicks the button
def d():
    for i in ['skip.png', 'skip2.png', 'skip3.png']:
        center_coords = pyautogui.locateCenterOnScreen(i, confidence=0.85)
        if center_coords:
            pyautogui.click(center_coords)
        else:
            pass

#main code
while True:
    try:
        d()
        #time.sleep() to prevent from double clicking
        time.sleep(.2)
    except:
        continue
    #This is to Prevent Using To Much processing power, because we dont want it to constantly check when 99% of the time you wouldn't get an ad.
    time.wait(5)
